import math
from tools.Tensor import Tenseur
monde = Tenseur(3)
monde.gen_vecteur_3d()
print(monde.tenseur)
print()
for i in range(0,3):
    for j in range(0,3):
        print(monde.tenseur[j][i],end=" ")
    print()



            


