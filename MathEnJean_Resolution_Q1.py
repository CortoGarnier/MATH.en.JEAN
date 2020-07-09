from Module_MenJ import *

# A is the key
A = theorem_DF_HL()
print("\n")
print("brassage des cartes")
print("\n")
# if you don't want use comb_aleatoire() you could create a dictionary : {'Alice': [...], 'Bob': [...], 'Charlie':[...]}
B = comb_aleatoire()
C = B['Alice']
# The Alice's cards :
R1 = C[0]
R2 = C[1]
R3 = C[2]
# We adding the cards of Alice with the key
result = A + R1 + R2 + R3
print("\n")
print("Le resultat de l'addition des cartes d'Alice a la clé est:{0}".format(result))
print("\n")
Bob = result - A
D = BobCalcul(Bob, B['Bob'])
print("Les cartes d'Alice est :{0}".format(D))
