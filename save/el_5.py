import numpy as np
import math 
ik = -5 -2j
e2 = -550 + 320j
e3 = 400 - 200j
e6 = 240 + 20j


z1 = -40j
z2 = 30j
z4 = 20 + 90j
z5 = 70 - 20j
z6 = -20j

"""i1 = -3 + 1j
i2 = -2 - 3j
i3 = -5
i4 = 3 - 3j
i5 = -2j"""

i1=3.2
i2=3.6
i3=5
i4=4.2
i5=-2
ik=5.4

"""i_3 = 4.995*np.exp(-0j)
i_2 = 3.597*np.exp(-56.31j)
i_5 = 1.995*np.exp(-89.86j)
i_1 = 3.157*np.exp(-18.43j)
i_4 = 4.238*np.exp(-44.93j)
"""

"""u_ik = 302.67*np.exp(-55.72j)
i_k = 5.374*np.exp(-201.79j)"""
# Рассчитываем s
s = (ik**2) * z1 + (i1**2) * z4 + (i2**2) * z6 + (i3**2) * z2 + (i4**2) * z5

u_ik = e3 + i1*z4 +ik*z1
print(f"u_ik = {u_ik:.3f}")



s_ik = ik * u_ik
print(f"s_ik = {s_ik:.3f}")
# Вывод результата
print(f"s_pr = {s:.3f}")

i_3 = 5
i_2 = 3.6
i_5 = 2

e_2 = 636.3
e_3 = 447.2
e_6 = 240.8

phi35 = -2.035
phi23 = -0.527
phi62 = -4.042


"""phi35 = 1.695
phi23 = -0.5
phi62 = 1.6"""
P_ist = e_3*i_5*np.cos(phi35) + e_2*i_3*np.cos(phi23) + e_6*i_2*np.cos(phi62) - 1350 
Q_ist = (e_3*i_5*np.sin(phi35) + e_2*i_3*np.sin(phi23) + e_6*i_2*np.sin(phi62) + 910)*1j

print(f"P_ist = {P_ist:.3f}")
print(f"Q_ist = {Q_ist:.3f}")

print(math.atan2(-3,-2))