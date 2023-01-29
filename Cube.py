from tkinter import *
import time
import copy


class RubiksCube:

    cube = [
        [[0 for j in range(3)] for i in range(3)],  # White
        [[1 for j in range(3)] for i in range(3)],  # Yellow
        [[2 for j in range(3)] for i in range(3)],  # Blue
        [[3 for j in range(3)] for i in range(3)],  # Red
        [[4 for j in range(3)] for i in range(3)],  # Green
        [[5 for j in range(3)] for i in range(3)]   # Orange
    ]

    color = ["white", "yellow", "blue", "red", "green", "orange"]

    def __init__(self, windowWidth=1280, windowHeight=680, cubeDisplaySize=60):
        # --- Create tkinter window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.tkRoot = Tk()
        self.tkRoot.title("Rubik's cube")
        self.canvas = Canvas(self.tkRoot,
                             width=self.windowWidth,
                             height=self.windowHeight)
        self.canvas.pack(fill="both", expand=True)

        # --- Create the cube display
        self.cubesDisplayIDs = [[] for i in range(6)] # List to save the cubes canvas IDs

        for i in range(3):
            self.cubesDisplayIDs[1].append([])
            for j in range(3):
                self.cubesDisplayIDs[1][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) +
                        cubeDisplaySize * j + 20,
                        cubeDisplaySize * i + 20,
                        cubeDisplaySize * j + cubeDisplaySize + 20 +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + cubeDisplaySize + 20,
                        fill=self.color[self.cube[1][i][j]]))
        for i in range(3):
            self.cubesDisplayIDs[0].append([])
            for j in range(3):
                self.cubesDisplayIDs[0][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) +
                        cubeDisplaySize * j + 20,
                        cubeDisplaySize * i + 60 + 6 * cubeDisplaySize,
                        cubeDisplaySize * j + cubeDisplaySize + 20 +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + cubeDisplaySize + 60 +
                        6 * cubeDisplaySize,
                        fill=self.color[self.cube[0][i][j]]))
        for i in range(3):
            self.cubesDisplayIDs[5].append([])
            for j in range(3):
                self.cubesDisplayIDs[5][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 60 +
                        cubeDisplaySize * j - 3 * cubeDisplaySize,
                        cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                        cubeDisplaySize * j - 4 * cubeDisplaySize + 60 +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                        fill=self.color[self.cube[5][i][j]]))
        for i in range(3):
            self.cubesDisplayIDs[2].append([])
            for j in range(3):
                self.cubesDisplayIDs[2][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 80 +
                        cubeDisplaySize * j,
                        cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                        cubeDisplaySize * j - cubeDisplaySize + 80 +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                        fill=self.color[self.cube[2][i][j]]))
        for i in range(3):
            self.cubesDisplayIDs[3].append([])
            for j in range(3):
                self.cubesDisplayIDs[3][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 100 +
                        cubeDisplaySize * j + 3 * cubeDisplaySize,
                        cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                        cubeDisplaySize * j - cubeDisplaySize + 100 +
                        3 * cubeDisplaySize +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                        fill=self.color[self.cube[3][i][j]]))
        for i in range(3):
            self.cubesDisplayIDs[4].append([])
            for j in range(3):
                self.cubesDisplayIDs[4][i].append(
                    self.canvas.create_rectangle(
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 120 +
                        cubeDisplaySize * j + 6 * cubeDisplaySize,
                        cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                        cubeDisplaySize * j - cubeDisplaySize + 120 +
                        6 * cubeDisplaySize +
                        (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                        cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                        fill=self.color[self.cube[4][i][j]]))

    def updateDisplay(self):
        # Updating tkinter window
        for face in range(6):
            for line in range(3):
                for cube in range(3):
                    self.canvas.itemconfig(
                        self.cubesDisplayIDs[face][line][cube],
                        fill=self.color[self.cube[face][line][cube]]
                    )

        self.tkRoot.update()
        self.tkRoot.update_idletasks()

    def printFace(self, face):
        for i in range(3):
            for j in range(3):
                print(self.cube[face][i][j], end=' ')
            print()
        print()

    def turnFace(self, face, direction):
        # List wich references the faces that is connected to each face of the cube in the clockwise order
        faceMoves = [
            [2, 3, 4, 5], # White
            [2, 5, 4, 3], # Yellow
            [0, 5, 1, 3], # Blue
            [0, 2, 1, 4], # Red
            [0, 3, 1, 5], # Green
            [0, 4, 1, 2]  # Orange
        ]

        for loop in range(abs(direction)):
            # Variable that will be aplied the changes
            newCube = copy.deepcopy(self.cube)

            if direction > 0:
                # --- Turning the only the selected face
                for i in range(3):
                    for j in range(3):
                        newCube[face][i][j] = self.cube[face][2 - j][i]

                # --- Turning connected faces
                newCube[faceMoves[face][0]][0] = [ 
                    self.cube[faceMoves[face][3]][0][0],
                    self.cube[faceMoves[face][3]][1][0],
                    self.cube[faceMoves[face][3]][2][0]
                ]

                newCube[faceMoves[face][1]][0][2], newCube[faceMoves[face][1]][1][2], newCube[faceMoves[face][1]][2][2] = \
                self.cube[faceMoves[face][0]][0]

                newCube[faceMoves[face][2]][2] = [
                    self.cube[faceMoves[face][1]][0][2],
                    self.cube[faceMoves[face][1]][1][2],
                    self.cube[faceMoves[face][1]][2][2] 
                ]

                newCube[faceMoves[face][3]][0][0], newCube[faceMoves[face][3]][1][0], newCube[faceMoves[face][3]][2][0] = \
                self.cube[faceMoves[face][2]][2]
            
            elif direction < 0:
                # --- Turning the only the selected face
                for i in range(3):
                    for j in range(3):
                        newCube[face][i][j] = self.cube[face][j][2 - i]

                # --- Turning connected faces
                newCube[faceMoves[face][0]][0] = [
                    self.cube[faceMoves[face][1]][0][2],
                    self.cube[faceMoves[face][1]][1][2],
                    self.cube[faceMoves[face][1]][2][2]
                ]

                newCube[faceMoves[face][1]][0][2], newCube[faceMoves[face][1]][1][2], newCube[faceMoves[face][1]][2][2] = \
                self.cube[faceMoves[face][2]][2]

                newCube[faceMoves[face][2]][2] = [
                    self.cube[faceMoves[face][3]][0][0],
                    self.cube[faceMoves[face][3]][1][0],
                    self.cube[faceMoves[face][3]][2][0]
                ]

                newCube[faceMoves[face][3]][0][0], newCube[faceMoves[face][3]][1][0], newCube[faceMoves[face][3]][2][0] = \
                self.cube[faceMoves[face][0]][0]
            
            else:
                raise ValueError("Please enter a valid value for direction")

            # Applying the changes
            self.cube = copy.deepcopy(newCube)


cube = RubiksCube()
cube.cube[2][0] = [0, 0, 0]
cube.updateDisplay()
time.sleep(2)
cube.turnFace(2, -1)
cube.updateDisplay()
time.sleep(10)
