from tkinter import *

class RubiksCube :

    w = [[0 for j in range(3)] for i in range(3)]
    y = [[1 for j in range(3)] for i in range(3)]
    b = [[2 for j in range(3)] for i in range(3)]
    r = [[3 for j in range(3)] for i in range(3)]
    g = [[4 for j in range(3)] for i in range(3)]
    o = [[5 for j in range(3)] for i in range(3)]

    test = [[1,2,3],[8,0,4],[7,6,5]]

    cube = {"w" : w, "y" : y, "b" : b, "r" : r, "g" : g, "o" : o}
    color = ["white", "yellow", "blue", "red", "green", "orange"]

    def printFace(self, face) :
        for i in range(3) :
            for j in range(3) :
                print(self.cube[face][i][j], end=' ')
            print()

    def printCube(self, Cube=cube, longueur=1280, largeur=680, c=60) :
        root = Tk()
        root.title("Rubik's cube")
        canvas = Canvas(root, width=longueur, height=largeur)
        canvas.pack(fill="both", expand=True)
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+c*j+20, c*i+20, c*j+c+20+(longueur/2 - 1.5*c), c*i+c+20, fill=self.color[self.cube["y"][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+c*j+20, c*i+60+6*c, c*j+c+20+(longueur/2 - 1.5*c), c*i+c+60+6*c, fill=self.color[self.cube["w"][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+60+c*j-3*c, c*i+40+3*c, c*j-4*c+60+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube["o"][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+80+c*j, c*i+40+3*c, c*j-c+80+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube["b"][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+100+c*j+3*c, c*i+40+3*c, c*j-c+100+3*c+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube["r"][i][j]])
        for i in range(3) :
            for j in range(3) :
                canvas.create_rectangle((longueur/2 - 1.5*c)+120+c*j+6*c, c*i+40+3*c, c*j-c+120+6*c+(longueur/2 - 1.5*c), c*i+40+4*c, fill=self.color[self.cube["g"][i][j]])
        root.mainloop()

    def turn(self, face, direction) :
        newFace = [[0 for j in range(3)] for i in range(3)]
        if direction == 1:
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = face[2-j][i]
        else :
            for i in range(3) :
                for j in range(3) :
                    newFace[i][j] = face[j][2-i]
        return newFace

cube = RubiksCube()
cube.printCube()
    