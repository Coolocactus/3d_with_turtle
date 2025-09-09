import math
from random import randint

class tenseur:
    def __init__(self,size) -> None:
        self.size = size
        self.tenseur = self.gen_tenseur()


    def __str__(self) -> str:
        return self.tenseur

    def gen_tenseur(self):
        tenseur = [[[0 for i in range(self.size)] for i in range(self.size)] for i in range(self.size)]
        return tenseur

    def gen_vecteur_3d(self):

        point_a = [randint(0,size) for _ in range(3)] #genere un point dans le tenseur
        point_b = [randint(0,size) for _ in range(3)] #genere un point dans le tenseur

        vecteur_AB = [point_b[i]-point_a[i] for i in range(3)] #creer le vecteur AB
        dist_max = max(vecteur_AB)
        for step in range(0,dist_max):
            step_x = point_a[]/dist_max
            step_y =
            step_z =
            


