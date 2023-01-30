from tkinter import *
from random import randint


def turn( face, direction) :
        newFace = [["0" for i in range(3)] for j in range(3)]
        if direction == 1:
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = face[2-j][i]
        else :
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = face[j][2-i]
        return newFace

class RubiksCube :

    cube = [
        [[0 for j in range(3)] for i in range(3)], # White
        [[1 for j in range(3)] for i in range(3)], # Yellow
        [[2 for j in range(3)] for i in range(3)], # Blue
        [[3 for j in range(3)] for i in range(3)], # Red
        [[4 for j in range(3)] for i in range(3)], # Green
        [[5 for j in range(3)] for i in range(3)]  # Orange
    ]

    color = ["white", "yellow", "blue", "red", "green", "orange"]

    def printFace(self, face) :
        for i in range(3) :
            for j in range(3) :
                print(self.cube[face][i][j], end=' ')
            print()
        print()

    def printCube(self, longueur=1280, largeur=680, c=60) :
        root = Tk()
        root.title("Rubik's cube")
        canvas = Canvas(root, width=longueur, height=largeur)
        canvas.pack(fill="both", expand=True)
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+c*j+20, c*i+20, c*j+c+20+(longueur/2 - 1.5*c), c*i+c+20, fill=self.color[self.cube[1][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+c*j+20, c*i+60+6*c, c*j+c+20+(longueur/2 - 1.5*c), c*i+c+60+6*c, fill=self.color[self.cube[0][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+60+c*j-3*c, c*i+40+3*c, c*j-4*c+60+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube[5][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+80+c*j, c*i+40+3*c, c*j-c+80+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube[2][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+100+c*j+3*c, c*i+40+3*c, c*j-c+100+3*c+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube[3][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+120+c*j+6*c, c*i+40+3*c, c*j-c+120+6*c+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube[4][i][j]])
        root.mainloop()

    

    def D(self) :
        self.cube[0] = turn(self.cube[0], 1)
        nR, nG, nO, nB= self.cube[3][2], self.cube[4][2], self.cube[5][2], self.cube[2][2]
        self.cube[3][2], self.cube[4][2], self.cube[5][2], self.cube[2][2] = nB, nR, nG, nO

    def d(self) :
        self.cube[0] = turn(self.cube[0], -1)
        nR, nG, nO, nB= self.cube[3][2], self.cube[4][2], self.cube[5][2], self.cube[2][2]
        self.cube[3][2], self.cube[4][2], self.cube[5][2], self.cube[2][2] = nG, nO, nB, nR

    def U(self) :
        self.cube[1] = turn(self.cube[1], 1)
        nR, nG, nO, nB= self.cube[3][0], self.cube[4][0], self.cube[5][0], self.cube[2][0]
        self.cube[3][0], self.cube[4][0], self.cube[5][0], self.cube[2][0] = nG, nO, nB, nR

    def u(self) : 
        self.cube[1] = turn(self.cube[1], -1)
        nR, nG, nO, nB= self.cube[3][0], self.cube[4][0], self.cube[5][0], self.cube[2][0]
        self.cube[3][0], self.cube[4][0], self.cube[5][0], self.cube[2][0] = nB, nR, nG, nO

    def F(self) :
        self.cube[2] = turn(self.cube[2], 1)
        nY, nR, nW, nO = self.cube[1][2], [self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0]], self.cube[0][0], [self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2]]
        self.cube[1][2],self.cube[3][0][0],self.cube[3][1][0],self.cube[3][2][0],self.cube[0][0],self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2] = [nO[2],nO[1],nO[0]], nY[0],nY[1],nY[2], [nR[2],nR[1],nR[0]], nW[0],nW[1],nW[2]
            
    def f(self) :
        self.cube[2] = turn(self.cube[2], -1)
        nY, nR, nW, nO = self.cube[1][2], [self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0]], self.cube[0][0], [self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2]]
        self.cube[1][2], self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0], self.cube[0][0], self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2] = nR, nW[2], nW[1], nW[0], nO, nY[2], nY[1], nY[0]

    def B(self) :
        self.cube[4] = turn(self.cube[4], 1)
        nY, nR, nW, nO = self.cube[1][0], [self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2]], self.cube[0][2], [self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0]]
        self.cube[1][0], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[0][2], self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0] = nR, nW[2], nW[1], nW[0], nO, nY[2], nY[1], nY[0]

    def b(self) :
        self.cube[4] = turn(self.cube[4], -1)
        nY, nR, nW, nO = self.cube[1][0], [self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2]], self.cube[0][2], [self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0]]
        self.cube[1][0], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[0][2], self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0] = [nO[2], nO[1], nO[0]], nY[0], nY[1], nY[2], nR, nW[0], nW[1], nW[2]

    def R(self) :
        self.cube[3] = turn(self.cube[3], 1)
        nY, nG = [self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2]], [self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0]]
        nW, nB = [self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2]], [self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2]]
        self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2],self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0] = nB[0], nB[1], nB[2], nY[2], nY[1], nY[0]
        self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2],self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2] = nG[2], nG[1], nG[0], nW[0], nW[1], nW[2]

    def r(self) :
        self.cube[3] = turn(self.cube[3], -1)
        nY, nG = [self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2]], [self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0]]
        nW, nB = [self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2]], [self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2]]
        self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2],self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0] = nG[2], nG[1], nG[0], nW[2], nW[1], nW[0]
        self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2],self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2] = nB[0], nB[1], nB[2], nY[0], nY[1], nY[2]

    def L(self) :
        self.cube[5] = turn(self.cube[5], 1)
        nY, nG = [self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0]], [self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2]]
        nW, nB = [self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0]], [self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0]]
        self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0],self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2] = nG[2], nG[1], nG[0], nW[2], nW[1], nW[0]
        self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0],self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0] = nB[0], nB[1], nB[2], nY[0], nY[1], nY[2]
    
    def l(self) :
        self.cube[5] = turn(self.cube[5], -1)
        nY, nG = [self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0]], [self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2]]
        nW, nB = [self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0]], [self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0]]
        self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0],self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2] = nB[0], nB[1], nB[2], nY[0], nY[1], nY[2]
        self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0],self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0] = nG[2], nG[1], nG[0], nW[2], nW[1], nW[0] 

    def move(self, mot) :
        for movement in range(len(mot)) :
            if mot[movement] == "R" :
                self.R()
            elif mot[movement] == "r" :
                self.r()
            elif mot[movement] == "U" :
                self.U()
            elif mot[movement] == "u" :
                self.u()
            elif mot[movement] == "F" :
                self.F()
            elif mot[movement] == "f" :
                self.f()
            elif mot[movement] == "D" :
                self.D()
            elif mot[movement] == "d" :
                self.d()
            elif mot[movement] == "L" :
                self.L()
            elif mot[movement] == "l" :
                self.l()
            elif mot[movement] == "B" :
                self.B()
            elif mot[movement] == "b" :
                self.b()
            else :
                raise ValueError("movement does not exist")
            
    def randomCube(self) :
        movements = ["R","r","U","u","F","f","D","d","L","l","B","b"]
        mot = ""
        for i in range(randint(800, 1000)) :
            mot = mot + movements[randint(0, 11)]
        self.move(mot)

cube = RubiksCube()
cube.move("RUrurFRRuruRUrf")
cube.printCube()