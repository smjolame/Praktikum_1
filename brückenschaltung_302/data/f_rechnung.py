import numpy as np 

Ubr=0.08
Ubr_eff=Ubr/(np.sqrt(2)*2)
U2=Ubr_eff*np.sqrt(45)
U1=2.5
k=U2/U1

print(k)
