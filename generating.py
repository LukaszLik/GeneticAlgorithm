import vpython as vp
import numpy as np
from chair import Chair, print_chairs
import random


class Genotype:
    # [0] siedzenie
    # [1] nogi
    # [2] opparcie
    # [3] podłokiet
    counter = 0

    def __init__(self, gen0=None, gen1=None, gen2=None):
        self.genotype = [[0 for x in range(8)] for y in range(4)]

        if (gen0 is None and gen1 is None and gen2 is None):
            self.initialize()

        else:
            self.genotype[0] = list(gen0)
            self.genotype[1] = list(gen1)
            self.genotype[2] = list(gen2)

    def print_array(self):
        for i in self.genotype:
            print(i),
            # self.genotype[i][6] = i
            # print ("[{}]   ".format(i) + str(self.genotype[i]))

    def initialize(self, seed=0):
        self.seat_init()
        self.legs_init()
        self.back_init()
        self.armrest_init()

    def seat_init(self, seed=0):
        seat = self.get_seat()
        # [0] ilosc, [1] pozycja ???, [2] dlugosc, [3] wysokosc, [4] szerokosc, [5] - kolor, [6] - ???, [7] - styl
        seat[0] = random.randint(0, 4)
        seat[1] = (0, 0, 0)
        seat[2] = random.randint(1, 25)
        seat[3] = random.randint(1, 2)
        seat[4] = random.randint(1, 25)
        seat[5] = (random.random(), random.random(), random.random())
        seat[6] = 'seat'
        seat[7] = 'styl'

    def legs_init(self, seed=0):
        legs = self.get_legs()
        legs[0] = random.randint(0, 4)
        legs[1] = (0, 0, 0)
        legs[2] = random.randint(2, 3)
        legs[3] = random.randint(2, 30)
        legs[4] = random.randint(1, 2)
        legs[5] = (random.random(), random.random(), random.random())
        legs[6] = 'legs'
        legs[7] = random.randint(1, 3)

    #     1 - kwadratowe, 2 - elipsoidalne, 3 - cylinder

    def back_init(self, seed=0):
        back = self.get_back()
        back[0] = random.randint(2, 5)
        back[1] = (0, 0, 0)
        back[2] = random.randint(2, 3)  # len
        back[3] = random.randint(2, 30)  # height
        back[4] = random.randint(1, 2)  # width
        back[5] = (random.random(), random.random(), random.random())
        back[6] = 'back'
        back[7] = 1  # random.randint(1,2)

    def armrest_init(self, seed=0):
        pass

    def get_seat(self):
        return self.genotype[0]

    def get_legs(self):
        return self.genotype[1]

    def get_back(self):
        return self.genotype[2]

    def getArray(self):
        return self.genotype
        # seat fit value


def sort_chairs(e):
    return e.fit_value()


def crossover(parent_a, parent_b):
    # choosing parents' genes
    gen0 = parent_a.genotype[0]
    gen1 = parent_b.genotype[1]
    gen2 = parent_a.genotype[2]

    kid = Genotype(gen0, gen1, gen2)
    # print ("CROSS HEX")
    # print(str(hex(id(parent_a.genotype[0]))) + " " + str(hex(id(parent_a.genotype[1]))) + " " + str(hex(id(parent_a.genotype[2]))))
    # print(str(hex(id(kid.genotype[0]))) + " " + str(hex(id(kid.genotype[1]))) + " " + str(hex(id(kid.genotype[2]))))
    return kid


scene = vp.canvas(title='Example of chairs', width=1800, height=900, center=vp.vector(0, 0, 30),
                  background=vp.color.white)


# scene.camera.pos(vp.vector(0, 0, 100))

# mybox1 = vp.box(pos=vp.vector(0, 0, 0), length=10, height=10, width=1, color=vp.color.black)


def first_population_roulette(genotypes):
    f_sum = 0
    wheel = list()
    mating_pool = list()

    for gene in genotypes:
        f_sum += gene.fit_value()

    for gene in genotypes:
        wheel.append((gene.fit_value() * 100) / f_sum)

    roulette = np.add.accumulate(wheel)

    print(roulette)
    # creating mating pool
    for j in range(20):
        p = np.random.uniform(0, 100)
        # print("Chance = " + str(p))
        k = 0

        for x in roulette:
            if (p <= x):
                mating_pool.append(Chair(Genotype(genotypes[k].genotype[0], genotypes[k].genotype[1], genotypes[k].genotype[2])))
                # print("Dodano krzesło nr " + str(k + 1))
                break
            else:
                k += 1

    return mating_pool


chair_list = list()
for i in range(1, 50):
    chair_list.append(Chair(Genotype()))
    print("Chair [" + str(i) + "] fit: \t" + str(chair_list[i - 1].fit_value()))

sorted_chairs = list()
# pool = list()

chair_list.sort(reverse=True, key=sort_chairs)

for i in range(1, 21):
    # chair_list.append(Chair(Genotype()))
    print("Chair [" + str(i) + "] fit: \t" + str(chair_list[i - 1].fit_value()))

print(sorted_chairs)
# print("pepega")

print_chairs(chair_list, scene.width, 20)



def mating_pool(b):
    print("Generate stuff", b.text)
    pool = first_population_roulette(getattr(b, "pool"))

    # print("Mating pool:\n")
    # pool.sort(reverse=True, key=sort_chairs)

    if (getattr(b, "print")):
        for chair in pool:
            print(str(chair.fit_value()) + " [" + str(chair.ID) + "]")

    # scene2 = vp.canvas(title='Example of chairs', width=1800, height=900, center=vp.vector(0, 0, 30), background=vp.color.white)

    # getting rid of trash
    for x in scene.objects:
        x.visible = False

    if (getattr(b, "print")):
        print_chairs(pool, scene.width)
    # scene.select(scene2)
    setattr(b, "pool", pool)

    update_pool(b1, b2, b3, b4, b5, pool)


def cross(b):
    setattr(b, "pool", getattr(b1, "pool"))
    # print("Generate stuff", b.text)
    # print(getattr(b, "pool"))

    chairs = getattr(b, "pool")
    crossed_pool = list()

    for i in range (int(len(chairs)/2)):
        # for j in range (int(len(chairs)/2), len(chairs)):
        # print(str(i) + "  " + str(i+1))

        # 1 /2 /1
        # 2/ 1 /2
        crossed_pool.append(Chair(crossover(chairs[i], chairs[i+1])))
        crossed_pool.append(Chair(crossover(chairs[i+1], chairs[i])))

    for x in scene.objects:
        x.visible = False

    if (getattr(b, "print")):
        print_chairs(crossed_pool, scene.width)

    setattr(b, "pool", crossed_pool)
    print("end")
    update_pool(b1, b2, b3, b4, b5, crossed_pool)


def evolve(b):
    n = 0

    if (not getattr(b, "used")):
        setattr(b, "pool", getattr(b2, "pool"))

    if (getattr(b, "id") == 4):
        n = 10

    elif (getattr(b, "id") == 5):
        n = 100

    for i in range(n):
        print ("evolve[" + str(i) + "]")
        mating_pool(b)
        cross(b)
        mutate(b)

    for x in scene.objects:
        x.visible = False

    print_chairs(getattr(b, "pool"), scene.width)

    pool = getattr(b, "pool")
    print(pool)

    # for chair in pool:
        # print(str(hex(id(chair.genotype[0]))) + " " + str(hex(id(chair.genotype[1]))) + " " + str(hex(id(chair.genotype[2]))))

    setattr(b1, "pool", getattr(b, "pool"))
    setattr(b2, "pool", getattr(b, "pool"))
    update_pool(b1, b2, b3, b4, b5, pool)


def mutate(b):
    # if (getattr(b, "id") != 4):
    pool = getattr(b1, "pool")
        # setattr(b, "pool", getattr(b2, "pool"))

    for chair in pool:
        chance = np.random.uniform(0, 1)

        if (chance < 0.05):
            chance2 = np.random.uniform(0, 1)

            # [0] ilosc, [1] pozycja ???, [2] dlugosc,
            # [3] wysokosc, [4] szerokosc, [5] - kolor

            # seat[0]
            # seat[2] = random.randint(1, 25)
            # seat[3] = random.randint(1, 2)
            # seat[4] = random.randint(1, 25)
            # seat[5] = (random.random(), random.random(), random.random())
            if (chance2 < 0.33):
                chance3 = np.random.uniform(0, 1)
                # len
                if (chance3 < 0.25):
                    chair.genotype[0][2] = random.randint(1, 25)
                # hei
                elif (chance3 < 0.5):
                    chair.genotype[0][3] = random.randint(1, 2)
                #wid
                elif (chance3 < 0.75):
                    chair.genotype[0][4] = random.randint(1, 25)

                #color
                else:
                    chair.genotype[0][5] = (random.random(), random.random(), random.random())

            # legs[1]
            # legs[2] = random.randint(2, 3)
            # legs[3] = random.randint(2, 30)
            # legs[4] = random.randint(1, 2)
            elif (chance2 < 0.66):
                chance3 = np.random.uniform(0, 1)
                # len
                if (chance3 < 0.25):
                    chair.genotype[1][2] = random.randint(2, 3)
                    # hei
                elif (chance3 < 0.5):
                    chair.genotype[1][3] = random.randint(2, 30)
                    #wid
                elif (chance3 < 0.75):
                    chair.genotype[1][4] = random.randint(1, 2)

                    #color
                else:
                    chair.genotype[1][5] = (random.random(), random.random(), random.random())

            # back [2]
            # back[2] = random.randint(2, 3)  # len
            # back[3] = random.randint(2, 30)  # height
            # back[4] = random.randint(1, 2)  # width
            else:
                chance3 = np.random.uniform(0, 1)
                # len
            if (chance3 < 0.25):
                chair.genotype[2][2] = random.randint(2, 3)
                # hei
            elif (chance3 < 0.5):
                chair.genotype[2][3] = random.randint(2, 30)
                #wid
            elif (chance3 < 0.75):
                chair.genotype[2][4] = random.randint(1, 2)

                #color
            else:
                chair.genotype[2][5] = (random.random(), random.random(), random.random())

    update_pool(b1, b2, b3, b4, b5, pool)


def update_pool(b1, b2, b3, b4, b5, pool=None):
    setattr(b1, "pool", pool)
    setattr(b2, "pool", pool)
    setattr(b3, "pool", pool)
    setattr(b4, "pool", pool)
    setattr(b5, "pool", pool)


b1 = vp.button(bind=mating_pool, text='Create mating pool')
b2 = vp.button(bind=cross, text='Crossover')
b3 = vp.button(bind=mutate, text="Mutate")
b4 = vp.button(bind=evolve, text='10 iterations')
b5 = vp.button(bind=evolve, text='100 iterations')

setattr(b1, "pool", chair_list)
setattr(b1, "print", True)
setattr(b1, "id", 1)

setattr(b2, "pool", list())
setattr(b2, "print", True)
setattr(b2, "crossed_pool", list())
setattr(b2, "id", 2)

setattr(b3, "pool", list())
setattr(b3, "print", True)
setattr(b3, "id", 3)

setattr(b4, "pool", list())
setattr(b4, "print", False)
setattr(b4, "used", False)
setattr(b4, "id", 4)

setattr(b5, "pool", list())
setattr(b5, "print", False)
setattr(b5, "used", False)
setattr(b5, "id", 5)

scene.append_to_caption('\n\n')

update_pool(b1,b2,b3,b4,b5, chair_list)






