from tkinter import *

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
        tkRoot = Tk()
        tkRoot.title("Rubik's cube")
        canvas = Canvas(tkRoot, width=longueur, height=largeur)
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
        tkRoot.mainloop()

    def turn(self, face, direction) :
        newFace = [[0 for i in range(3)] for j in range(3)]
        if direction > 0:
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = self.cube[face][2-j][i]
        
        elif direction < 0 :
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = self.cube[face][j][2-i]
        
        else : 
            raise ValueError("turn = 0")

        self.cube[face] = newFace


    
cube = RubiksCube()
cube.turn(2, 1)
cube.turn(2, 1)
cube.printCube()