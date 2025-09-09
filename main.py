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

    def gen_vecteur_3d(self):

        point_a = [randint(0,self.size) for _ in range(3)] #genere un point dans le tenseur
        point_b = [randint(0,self.size) for _ in range(3)] #genere un point dans le tenseur
        print(f"point_a: {point_a}, point_b: {point_b}")
        vecteur_ab = [point_b[i]-point_a[i] for i in range(3)] #creer le vecteur AB
        dist_max = max(vecteur_ab)
        print(f"dist_max = {dist_max}")
        step_x = point_a[0] / dist_max
        step_y = point_a[1] / dist_max
        step_z = point_a[2] / dist_max

        for step in range(0,dist_max):
            self.tenseur[round(step*step_x)][round(step*step_y)][round(step*step_z)] = 1


monde = Tenseur(3)
monde.gen_vecteur_3d()
print(monde)


