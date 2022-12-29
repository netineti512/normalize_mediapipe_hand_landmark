---
title: 【MediaPipe】顔と手の座標データを正規化する(CSVファイル)
tags: MediaPipe CSV
author: netineti512
slide: false
---
>MediaPipeで取得した座標データの統一化

手の座標の見本です。
![aa.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2702119/71f06798-30b7-baef-2a11-b9d786e6fd4f.jpeg)

顔の座標データの見本です。
![A6E6F3D5-545A-4FE2-9596-8D4F5942D2F1.jpeg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2702119/40c316cf-f1d5-a6f8-6b74-b1b19ba32d16.jpeg)

2つのポイントを決定する。具体的にはP0(WRIST)を絶対動かない基準として設定する。それとP9(MIDDLE_FINGER_MCP)からP0までの距離が1になるように大きさを揃える。(P9以外でも大丈夫です。)
※z軸はあってもなくても大丈夫です。

必要な座標データです。
[・landmark_hand21_face4.csv](https://drive.google.com/drive/folders/10yytVY-0LR-fA7255X6oI5C1wO-Z05BV)

まず全体のソースコードです。
```python:standard_hand_face.py
import csv
import numpy as np
import math

with open("./result/landmark_hand21_face4.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",").ravel()
    #print(array)
    
x1 = array[::3]
y1 = array[1::3]
z1 = array[2::3]
    
x2 = []
y2 = []
z2 = []
for i in range(0,25):
    a = x1[i] - x1[0]
    x2.append(a)
    b = y1[i] - y1[0]
    y2.append(b)
    c = z1[i] - z1[0]
    z2.append(c)
#print(x2, y2, z2)

#k = math.sqrt((x2[1] - x2[0])**2 + (y2[1] - y2[0])**2)
k = math.sqrt((x2[1] - x2[0])**2 + (y2[1] - y2[0])**2 + (z2[1] - z2[0])**2)
print(k)

x = []
y = []
z = []
for i in range(24):
    d = x2[i] / k
    x.append(d)
    e = y2[i] / k
    y.append(e)
    f = z2[i] / k
    z.append(f)
#print(x, y, z)

"""
#xy = []
xy.extend(x)
xy.extend(y)
np.savetxt('./result/distance_hand_face.csv', xy, delimiter=',')
"""

xyz = [] 
xyz.extend(x)
xyz.extend(y)
xyz.extend(z)

np.savetxt('./result/distance_hand_face.csv', xyz, delimiter=',')
```

出力されたデータです。
72行あります。
[・distance_hand_face.csv](https://drive.google.com/drive/folders/10yytVY-0LR-fA7255X6oI5C1wO-Z05BV)
```distance_hand_face.csv
0
-0.75175872
..........
..........
-4.8186489
-4.467570984
```
>他の記事
・[MediaPipeで顔と手の座標データを出力する方法[CSV]](https://qiita.com/netineti512/items/cd642e130887a4636ec1)
・[[MediaPipe]手の座標データ(21個)と特定の顔の座標データ(4個)を結合させる。](https://qiita.com/netineti512/items/64bf47d5a61b474a55b5)
・[【MediaPipe】顔と手の座標データを正規化する(CSVファイル)](https://qiita.com/netineti512/items/34fb10a172588a71fe01)
