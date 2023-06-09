"""
Hello World example.
"""

ma_variable = 2
print(ma_variable)
fhgjk = "toto"

#%%
mon_complexe = 2 + 1j
mon_complexe + 2j

#%%
# fstrings
b = 12344355454
a = 234
#print(a + " " + b)
print(f"{a:>10} {b}")

liste_de_liste = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8],
]

import numpy as np
a = np.array([[1, 0],

              [0, 0]])

b = np.array([[4, 1],

              [2, 2]])

# multiplication matricielle
np.matmul(a, b)
a @ b

# multiplication termes à termes
a * b

# inversion
c = np.linalg.inv(b)
b @ c

#%%

# dans 99% des cas, la bonne façon de faire
for castor in castors_juniors:
    print(castor)
    
# le 1% des cas restant
for index in range(len(castors_juniors)):
    castor = castors_juniors[index]
    print(castor)


puissances = []
for i in range(10):
    puissances.append(2**i)
print(puissances)


age = 20
if age < 19:
    print("mineur")
elif age == 18:
    print("majeur cette année")
else: 
    print("majeur")
