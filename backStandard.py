import vpython as vp

class BackStandard():
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
        relative_y = self.genotype[2][3] / 2

        off_x = self.genotype[2][2] / 2
        off_y = self.genotype[0][3] / 2
        off_z = self.genotype[2][4] / 2

        r = float(self.genotype[2][5][0])
        g = float(self.genotype[2][5][1])
        b = float(self.genotype[2][5][2])

        offset = seat_x / (self.genotype[2][0] * self.genotype[2][2])

        # for i in range(self.gen
        # otype[2][0]):
        #     back1 = vp.box(pos=vp.vector((-relative_x + off_x)*(-i -1) + (offset)*i,
        #                                    relative_y + off_y, -relative_z + off_z),
        #                    length=self.genotype[2][2], height=self.genotype[2][3],
        #                    width=self.genotype[2][4], color=vp.vector(r, g, b))

        if (self.genotype[2][0] >= 2):
            back1 = vp.box(pos=vp.vector(-relative_x + off_x + x,
                                         relative_y + off_y + y,
                                         -relative_z + off_z + z),
                           length=self.genotype[2][2], height=self.genotype[2][3], width=self.genotype[2][4],
                           color=vp.vector(r, g, b))

            back2 = vp.box(pos=vp.vector(relative_x - off_x + x,
                                         relative_y + off_y + y,
                                         -relative_z + off_z + z),
                           length=self.genotype[2][2], height=self.genotype[2][3], width=self.genotype[2][4],
                           color=vp.vector(r, g, b))

            space_left = 0
            if (self.genotype[2][0] > 0):
                space_left = (self.genotype[0][2] - 2 * self.genotype[2][2]) / (self.genotype[2][0] - 1)

            new_zero = (-relative_x + off_x)

            off = (self.genotype[0][2] - self.genotype[2][2]) / self.genotype[2][0]

            prev_back = None

            for i in range(self.genotype[2][0] - 2):
                # if (prev_back is None):
                back = vp.box(pos=vp.vector(new_zero + space_left * (i + 1) + off_x + x,
                                            relative_y + off_y + y,
                                            -relative_z + off_z + z),
                                length=self.genotype[2][2], height=self.genotype[2][3], width=self.genotype[2][4],
                                color=vp.vector(r, g, b))

                    # prev_back = back

                # else:
                #     back = vp.box(pos=vp.vector(new_zero + space_left * (i + 1) + off_x + x,
                #                                 relative_y + off_y + y,
                #                                 -relative_z + off_z + z),
                #                   length=self.genotype[2][2], height=self.genotype[2][3], width=self.genotype[2][4],
                #                   color=vp.vector(r, g, b))

                # back = back1.clone(pos=vp.vector(new_zero + space_left * (i + 1) + off_x + x,
                #                                  relative_y + off_y + y,
                #                                  -relative_z + off_z + z))

        # if ()

        post = vp.box(pos=vp.vector(0 + x, self.genotype[2][3] + y, -relative_z + off_z + z),
                      length=self.genotype[0][2], height=1, width=1, color=vp.vector(r, g, b))
