import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()

fig = plt.figure() # まっさらな新しい描画領域を作る

パラパラ漫画の全て = [] # リストのリスト
X軸=range(10) # X軸は[0,1,2,3,4,5,6,7,8,9]

for i in range(50):
        # 0以上10未満の乱数を10個生成しリストにする
        乱数のリスト = np.random.randint(0,10,10)
        # 10個の乱数をグラフにする        
        パラパラ漫画の1枚分 = plt.bar(X軸,乱数のリスト,color='c')
        # グラフをパラパラ漫画に追加        
        パラパラ漫画の全て.append(パラパラ漫画の1枚分)

ani=animation.ArtistAnimation(fig, パラパラ漫画の全て, interval=500,repeat=False) 
#interval=500は0.5秒ごとに次のグラフに切り替えるという意味
#repeat=Falseは最後のグラフになったら止めるという意味
plt.show()



import matplotlib.animation as animation


#algorithm animation って呼ばれる

fig = plt.figure() # まっさらな新しい描画領域を作る

パラパラ漫画の全て = [] # ソート途中のリストを全てAppendしていく配列
X軸=range(10) # X軸は[0,1,2,3,4,5,6,7,8,9]

def バブルソート(リスト):
    # 見る範囲を1ずつ狭めていく
    for i in range(len(リスト)): 
        # リストの最後尾から開始位置まで1ずつ遡る
        for j in range(len(リスト)-1, i, -1): 
            # 後ろのほうが小さかったら
            if リスト[j] < リスト[j-1]: 
                # リスト[j]とリスト[j-1]を入れ替える
                一時的な値 = リスト[j]
                リスト[j] = リスト[j-1]
                リスト[j-1] = 一時的な値
            # ソート中のリストをグラフに                
            パラパラ漫画の1枚分 = plt.bar(X軸, リスト, color='c') 
            # グラフをパラパラ漫画に追加            
            パラパラ漫画の全て.append(パラパラ漫画の1枚分)
            print(リスト) # 並べ替える最中のリストを画面出力

バブルソート([31,53,69,12,74,88,46,92,21,5])

ani=animation.ArtistAnimation(fig,パラパラ漫画の全て,interval=500, repeat=False)
plt.show()