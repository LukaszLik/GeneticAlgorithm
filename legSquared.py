import vpython as vp


class LegSquared:
    def __init__(self, genotype, x, y, z):
        self.genotype = genotype.getArray()
        self.X = x
        self.Y = y
        self.Z = z

    def draw(self, x, y, z):
        seat_x = self.genotype[0][2]
        seat_z = self.genotype[0][4]

        relative_x = seat_x / 2
        relative_z = seat_z / 2
        relative_y = self.genotype[1][3] / 2

        off_x = self.genotype[1][2] / 2
        off_y = self.genotype[0][3] / 2
        off_z = self.genotype[1][4] / 2

        r = float(self.genotype[1][5][0])
        g = float(self.genotype[1][5][1])
        b = float(self.genotype[1][5][2])

        leg1 = vp.box(pos=vp.vector(relative_x - off_x + x,
                                    -relative_y - off_y + y,
                                    relative_z - off_z + z),
                      length=self.genotype[1][2], height=self.genotype[1][3],
                      width=self.genotype[1][4], color=vp.vector(r, g, b))

        leg2 = vp.box(pos=vp.vector(-relative_x + off_x + x,
                                    -relative_y - off_y + y,
                                    relative_z - off_z + z),
                      length=self.genotype[1][2], height=self.genotype[1][3],
                      width=self.genotype[1][4], color=vp.vector(r, g, b))

        leg3 = vp.box(pos=vp.vector(relative_x - off_x + x,
                                    -relative_y - off_y + y,
                                    -relative_z + off_z + z),
                      length=self.genotype[1][2], height=self.genotype[1][3],
                      width=self.genotype[1][4], color=vp.vector(r, g, b))

        leg4 = vp.box(pos=vp.vector(-relative_x + off_x + x,
                                    -relative_y - off_y + y,
                                    -relative_z + off_z + z),
                      length=self.genotype[1][2], height=self.genotype[1][3],
                      width=self.genotype[1][4], color=vp.vector(r, g, b))
