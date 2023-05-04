import vpython as vp
import numpy as np
import math

import legCylindrical, legElipse, legSquared, backStandard, backFancy


class Chair:
    # genotype = list()
    ID = 0

    def __init__(self, genotype):
        self.genotype = genotype.getArray()
        self.X = self.genotype[0][1][0]
        self.Y = self.genotype[0][1][1]
        self.Z = self.genotype[0][1][2]
        self.ID = Chair.ID
        Chair.ID += 1

        if (self.genotype[1][7] == 1):
            self.leg = legSquared.LegSquared(genotype, self.X, self.Y, self.Z)

        elif (self.genotype[1][7] == 2):
            self.leg = legElipse.LegElipse(genotype, self.X, self.Y, self.Z)

        elif (self.genotype[1][7] == 3):
            self.leg = legCylindrical.LegCylindrical(genotype, self.X, self.Y, self.Z)

        if (self.genotype[2][7] == 1):
            self.back = backStandard.BackStandard(genotype, self.X, self.Y, self.Z)

        elif (self.genotype[2][7] == 2):
            self.back = backFancy.BackFancy(genotype, self.X, self.Y, self.Z)

    def printChair(self, x=0, y=0, z=0):
        self.printSeat(x, y, z)
        self.printLegs(x, y, z)
        self.printBack(x, y, z)

    def changeXYZ(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def printSeat(self, x, y, z):
        r = float(self.genotype[0][5][0])
        g = float(self.genotype[0][5][1])
        b = float(self.genotype[0][5][2])
        box = vp.box(pos=vp.vector(x, y, z), length=self.genotype[0][2], height=self.genotype[0][3],
                     width=self.genotype[0][4], color=vp.vector(r, g, b))
        # box.rotate(angle=vp.radians(90), axis=vp.vector(1, 0, 0))

    def printLegs(self, x, y, z):
        self.leg.draw(x, y, z)

    def printBack(self, x, y, z):
        self.back.draw(x, y, z)

    def fit_value(self):
        leg_height = self.genotype[1][3]
        back_height = self.genotype[2][3] * 0.95
        fit = 0

        # legs / back fit value
        if (leg_height > back_height):
            fit += (back_height / leg_height) * 10
        else:
            fit += (leg_height / back_height) * 10

        seat_length = self.genotype[0][2] * 0.98
        seat_width = self.genotype[0][4]

        # seat_height = self.genotype[0][3]
        if (seat_length > seat_width):
            fit += (seat_width / seat_length) * 13
        else:
            fit += (seat_length / seat_width) * 13

        fit += self.genotype[2][0] #??????

        # r, g, b = self.genotype[0][5][0], self.genotype[0][5][1], self.genotype[0][5][2]

        normalisation_val = self.calculate_rgb_distance((0, 0, 0), (255, 255, 255))
        leg_seat_dist_norm = self.calculate_rgb_distance(self.genotype[0][5], self.genotype[1][5]) / normalisation_val
        leg_back_dist_norm = self.calculate_rgb_distance(self.genotype[0][5], self.genotype[2][5]) / normalisation_val

        fit += leg_seat_dist_norm * 7
        fit += leg_back_dist_norm * 7

        #kara za zbyt duze siedzenia?
        # if (leg_height < seat_length or leg_height < seat_width):
        #     fit -= 1

        # if (leg_height < seat_width or leg_height < seat_length):
        #     fit -= 5

        # if (back_height < seat_length or back_height < seat_width):
        #     fit -= 5

        # if (back)

        return fit

    def calculate_rgb_distance(self, c1, c2):
        return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)

def print_chairs(chairList, sceneWidth, numberPrinted = 20):
    # if (len(chairList) != 3):
    #     exit("Number of charis to print must be 5")

    if (numberPrinted > len(chairList)):
        exit ("Number of elements to be printed > len(list).")

    if (numberPrinted % 2 != 0):
        exit ("Number of elemts to be printed is an odd number.")

    # print(sceneWidth)

    leftX = -sceneWidth/8 + 10
    rightX = sceneWidth/8 - 10

    newZero = (-leftX + rightX) / ((numberPrinted / 2) - 1)
    offset = newZero / ((numberPrinted / 2) - 2)

    # print (str(leftX) + "   " + str(newZero) + "   " + str(rightX) + "   " + str(offset))

    x = 0
    y = 0
    z = 0

    for j in range(2):
        nbr = 0

        for i in range(int(numberPrinted / 2)):
            if (i == 0):
                # print ("First = " + str(i) + "   " + str(j))
                # chairList[i + (j * int(len(chairList)/2))].changeXYZ\
                x = leftX
                y = 25 - j*70
                z = 0

            elif (i == int(len(chairList) / 2) - 1):
                # print ("Last = " + str(i) + "   " + str(j))
                # chairList[i + (j * int(len(chairList)/2))].changeXYZ\
                x = rightX
                y = 25 - j*70
                z = 0

            else:
                # chairList[i + (j * int(len(chairList)/2))].changeXYZ\
                x = leftX + newZero * (nbr + 1)
                y = 25 - j * 70
                z = 0
                nbr += 1

            chairList[i + (j * int(len(chairList)/2))].printChair(x, y, z)
            # chairList[i + (j * int(len(chairList)/2))].changeXYZ(0, 0, 0)
