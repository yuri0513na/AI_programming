import numpy as np
import matplotlib.pyplot as plt

plt.figure() #まっさらな新しい描画領域を作る

x=np.array([1,2,3,4,5])
y=np.array([100,200,300,400,500])
plt.bar(x,y) #棒グラフ



plt.figure()

x=np.array([0,1,2,3,4])
y=np.array([431,53,69,12,74])

plt.plot(x,y,color='r') #赤い線で折れ線グラフ




plt.figure()

x=range(20) #x軸は０から１９まで
y=np.random.randint(0,10,20) #0以上10未満の値をランダムに20個作る
plt.scatter(x,y,color='r') #赤い点で散布図




plt.figure()

x=np.linspace(-50,50,20) #ー５０から５０までの範囲で20個の数値を得る
y=x**2 #Xのすべての値を2乗してｙに代入
plt.plot(x,y,color='r') #折れ線グラフだけど曲線に見える




plt.figure()

x=np.linspace(-50,50,30) #30個の数値をー50から50の間で得る

y=x**2
y2=(x-10)**2

plt.plot(x,y,color='r')
plt.plot(x,y2,color='b')



plt.figure()

score_list = np.random.normal(50,10,500) #平均50、標準偏差１０の正規分布に従う乱数を５００個得る
plt.hist(score_list, bins=20) #便の数が２０


plt.show() #すべてのグラフを表示する