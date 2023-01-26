from tkinter import *


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
        # Open tkinter window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        tkRoot = Tk()
        tkRoot.title("Rubik's cube")
        canvas = Canvas(tkRoot, width=self.windowWidth, height=self.windowHeight)
        canvas.pack(fill="both", expand=True)

        # Display the cube
        self.cubesDisplayIDs = [[] for i in range(6)]
        for i in range(3):
            self.cubesDisplayIDs[1].append([])
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) +
                    cubeDisplaySize * j + 20,
                    cubeDisplaySize * i + 20,
                    cubeDisplaySize * j + cubeDisplaySize + 20 +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + cubeDisplaySize + 20,
                    fill=self.color[self.cube[1][i][j]])
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) +
                    cubeDisplaySize * j + 20,
                    cubeDisplaySize * i + 60 + 6 * cubeDisplaySize,
                    cubeDisplaySize * j + cubeDisplaySize + 20 +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + cubeDisplaySize + 60 +
                    6 * cubeDisplaySize,
                    fill=self.color[self.cube[0][i][j]])
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 60 +
                    cubeDisplaySize * j - 3 * cubeDisplaySize,
                    cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                    cubeDisplaySize * j - 4 * cubeDisplaySize + 60 +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                    fill=self.color[self.cube[5][i][j]])
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 80 +
                    cubeDisplaySize * j,
                    cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                    cubeDisplaySize * j - cubeDisplaySize + 80 +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                    fill=self.color[self.cube[2][i][j]])
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 100 +
                    cubeDisplaySize * j + 3 * cubeDisplaySize,
                    cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                    cubeDisplaySize * j - cubeDisplaySize + 100 +
                    3 * cubeDisplaySize +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                    fill=self.color[self.cube[3][i][j]])
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize) + 120 +
                    cubeDisplaySize * j + 6 * cubeDisplaySize,
                    cubeDisplaySize * i + 40 + 3 * cubeDisplaySize,
                    cubeDisplaySize * j - cubeDisplaySize + 120 +
                    6 * cubeDisplaySize +
                    (self.windowWidth / 2 - 1.5 * cubeDisplaySize),
                    cubeDisplaySize * i + 40 + 4 * cubeDisplaySize,
                    fill=self.color[self.cube[4][i][j]])

    def printFace(self, face):
        for i in range(3):
            for j in range(3):
                print(self.cube[face][i][j], end=' ')
            print()
        print()

    def turnFace(self, face, direction):
        newFace = [[0 for i in range(3)] for j in range(3)]
        if direction > 0:
            for i in range(3):
                for j in range(3):
                    newFace[i][j] = self.cube[face][2 - j][i]

        elif direction < 0:
            for i in range(3):
                for j in range(3):
                    newFace[i][j] = self.cube[face][j][2 - i]

        else:
            raise ValueError("turn = 0")

        self.cube[face] = newFace


cube = RubiksCube()
cube.turnFace(2, 1)
cube.turnFace(2, 1)
