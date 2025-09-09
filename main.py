import math
from random import randint

class Tenseur:
    def __init__(self,size) -> None:
        self.size = size
        self.tenseur = self.gen_tenseur()


    def __str__(self) -> str:
        return str(self.tenseur)

    def gen_tenseur(self):
        tenseur = [[[0 for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
        return tenseur

    def gen_random_point(self):
        return [randint(0,self.size-1) for _ in range(3)]
    def gen_vecteur_3d(self):

        point_a = self.gen_random_point() #genere un point dans le tenseur
        point_b = self.gen_random_point() #genere un point dans le tenseur
        while point_a == point_b:
            point_b = self.gen_random_point() #avoide division by 0

        print(f"point_a: {point_a}, point_b: {point_b}")
        
        vecteur_ab = [point_b[i]-point_a[i] for i in range(3)] #creer le vecteur AB
        dist_max = abs(max(vecteur_ab,key= lambda x: abs(x)))
        
        print(f"dist_max = {dist_max}")
        print(f"nombre de points 1 : {dist_max+1}")
        
        step_x = vecteur_ab[0] / dist_max
        step_y = vecteur_ab[1] / dist_max              # x est la profondeur , y la hauteur et z la longueur
        step_z = vecteur_ab[2] / dist_max

        for step in range(0,dist_max+1):
            self.tenseur[round(step*step_x + point_a[0])][round(step*step_y + point_a[1])][round(step*step_z + point_a[2])] = 1


monde = Tenseur(3)
monde.gen_vecteur_3d()
print(monde.tenseur)
print()
for i in range(0,3):
    print(monde.tenseur[i])


