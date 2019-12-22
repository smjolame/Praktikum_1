import matplotlib as plt
import numpy as np 


I_q=(0.01**4)/12    #Flaechentraegheit Quadtrat in Meter
I_r=(np.pi*0.01**4)/64  #Flaechentraegheit Kreis in Meter
m_ein=1.169+0.0406 #Masse bei einseitiger Einspannung in Kg
m_bei=0.0406+1.169+1.169+1.168+1.170 #Masse bei beidseitiger Einspannung in Kg
L=0.55 #Laenge des Stabes bei beidseitiger Einpannung in Meter

#ab hier alle x in cm und alle D in mm

x1,D_01,D_m1 =np.genfromtxt('ein_k.csv',delimiter=',', unpack=True)

D1=D_01-D_m1

D1_alles=np.append([x1],[D_01,D_m1,D1],axis=0)
D1_alles=D1_alles.T

np.savetxt('D_ein_k.txt',D1,fmt="%1.2f")
np.savetxt('D_ein_k_alles',D1_alles,fmt="%1.2f",delimiter=',')






x2,D_02,D_m2 =np.genfromtxt('ein_a.csv',delimiter=',', unpack=True)

D2=D_02-D_m2

D2_alles=np.append([x2],[D_02,D_m2,D2],axis=0)
D2_alles=D2_alles.T

np.savetxt('D_ein_a.txt',D2,fmt="%1.2f")
np.savetxt('D_ein_a_alles',D2_alles,fmt="%1.2f",delimiter=',')






x3,D_03_l,D_03_r =np.genfromtxt('bei_k_o.csv',delimiter=',', unpack=True)
x3,D_m3_l,D_m3_r =np.genfromtxt('bei_k_m.csv',delimiter=',', unpack=True)

x3_l=27.5-x3
x3_r=27.5+x3
x3_l_flip=np.flip(x3_l)

np.savetxt('x_bei_l.txt',x3_l_flip,fmt="%1.2f")
np.savetxt('x_bei_r.txt',x3_r,fmt="%1.2f")

D3_l=D_03_l-D_m3_l
D3_r=D_03_r-D_m3_r
D3_l_flip=np.flip(D3_l)

D_03_lr=np.append(np.flip(D_03_l),D_03_r)
D_m3_lr=np.append(np.flip(D_m3_l),D_m3_r)
D3_xlr=np.append(x3_l_flip,x3_r)
D3_lr=np.append(D3_l,D3_r)
D3_alles=np.append([D3_xlr],[D_03_lr,D_m3_lr,D3_lr],axis=0)
D3_alles=D3_alles.T

np.savetxt('D_bei_k_l.txt',D3_l_flip,fmt="%1.2f")
np.savetxt('D_bei_k_r.txt',D3_r,fmt="%1.2f")
np.savetxt('D_bei_k_alles',D3_alles,fmt="%1.2f",delimiter=',')





x4,D_04_l,D_04_r =np.genfromtxt('bei_a_o.csv',delimiter=',', unpack=True)
x4,D_m4_l,D_m4_r =np.genfromtxt('bei_a_m.csv',delimiter=',', unpack=True)

x4_l=27.5-x4
x4_r=27.5+x4
x4_l_flip=np.flip(x4_l)

D4_l=D_04_l-D_m4_l
D4_r=D_04_r-D_m4_r
D4_l_flip=np.flip(D4_l)

D_04_lr=np.append(np.flip(D_04_l),D_04_r)
D_m4_lr=np.append(np.flip(D_m4_l),D_m4_r)
D4_xlr=np.append(x4_l_flip,x4_r)
D4_lr=np.append(D4_l,D4_r)
D4_alles=np.append([D4_xlr],[D_04_lr,D_m4_lr,D4_lr],axis=0)
D4_alles=D4_alles.T



np.savetxt('D_bei_a_l.txt',D4_l_flip,fmt="%1.2f")
np.savetxt('D_bei_a_r.txt',D4_r,fmt="%1.2f")
np.savetxt('D_bei_a_alles',D4_alles,fmt="%1.2f",delimiter=',')
