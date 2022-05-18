# 組合
from turtle import color, st


class Person:
    def __init__(self):
        self.hd = None
        self.bd = None
        self.rh = None
        self.lh = None
        self.rl = None
        self.ll = None


class Head:
    def __init__(self, size):
        self.size = size


class Body:
    def __init__(self, capacity):
        self.capacity = capacity


class Hand:
    def __init__(self, length):
        self.length = length


class Leg:
    def __init__(self, width):
        self.width = width


handsome = Person()
handsome.hd = Head(50)
print(handsome.hd.size)

handsome.bd = Body(3000)
print(handsome.bd.capacity)

handsome.rh = Hand(80)
print(handsome.rh.length)

handsome.rh = Hand(80)
print(handsome.rh.length)

handsome.rl = Leg(100)
print(handsome.rl.width)

handsome.ll = Leg(100)
print(handsome.rl.width)


class Car:
    def __init__(self):
        self.cc = None
        self.FRtire = None
        self.FLtire = None
        self.BRtire = None
        self.FLtire = None


class CC:
    def __init__(self, engine):
        self.engine = engine


class Tire:
    def __init__(self, tire=200):  # tire=200 ->預設值
        self.tire = tire


bugatti = Car()
bugatti.cc = CC(5000)
bugatti.FRtire = Tire(20)
bugatti.FLtire = Tire(20)
bugatti.BRtire = Tire(30)
bugatti.BLtire = Tire(30)

print(bugatti.cc.engine)
print(bugatti.FRtire.tire)
print(bugatti.FLtire.tire)
print(bugatti.BRtire.tire)
print(bugatti.BLtire.tire)


class Car1:
    def __init__(self):
        self.eg = None
        self.wls = []


m2 = Car1()
m2.eg = CC(4000)
for i in range(8):
    m2.wls.append(Tire(100))  # 等等

print(m2.eg.engine)
for i in range(8):
    print(m2.wls[i].tire)


class classroom:
    def __init__(self):
        self.table = []
        self.chair = []
        self.computer = []
        self.light = []
        self.whiteBoard = None


class WB:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class TB:
    def __init__(self, length, width, hight):
        self.length = length
        self.width = width
        self.hight = hight


class CH:
    def __init__(self, size):
        self.size = size


class COM:
    def __init__(self, cpu):
        self.cpu = cpu


class LI:
    def __init__(self, onoff=False):
        self.onoff = onoff


ma218 = classroom()
ma218.whiteBoard = WB(400, 300)

for i in range(2):
    ma218.table.append(TB(70, 60, 100))
    ma218.chair.append(CH(30))
    ma218.computer.append(COM('i7-12500'))
    ma218.light.append(LI())

for i in range(2):
    print(ma218.table[i].length, ma218.table[i].width, ma218.table[i].hight)
    print(ma218.light[i].onoff)


# hw
class MRT:
    def __init__(self):
        self.city = []
        self.line = []
        self.train = []
        self.station = []
        self.driver = []
        self.station_staff = []


class City:
    def __init__(self, cityy):
        self.cityy = cityy


class Line:
    def __init__(self, color):
        self.color = color


class Train:
    def __init__(self, volume):
        self.volume = volume


class Station:
    def __init__(self, info_desk, toilet, ticket_mac, platform, ticket_gate, mrt_exit):
        self.info_desk = info_desk
        self.toilet = toilet
        self.ticket_mac = ticket_mac
        self.platform = platform
        self.ticket_gate = ticket_gate
        self.exit = mrt_exit


class Driver:
    def __init__(self, gender):
        self.gender = gender


class staff:
    def __init__(self, preservation, clean, serve):
        self.preservation = preservation
        self.clean = clean
        self.serve = serve


mrt = MRT()
city_list = ['Taipei', 'New_Taipei', 'Kaohsiung', 'Taoyuan', 'Taichung']
for i in range(5):
    mrt.city.append(City(city_list[i]))

color_list = ['red', 'green', 'blue', 'orange', 'brown', 'yellow']
for i in range(6):
    mrt.line.append(Line(color_list[i]))

volume_list = ['high', 'medium']
for i in range(2):
    mrt.train.append(Train(volume_list[i]))

for i in range(131):
    mrt.station.append(Station(1, 5, 8, 16, 2, 4))

for i in range(30):
    for j in range(2):
        mrt.driver.append(Driver(j))

for i in range(80):
    mrt.station_staff.append(staff(3, 5, 6))