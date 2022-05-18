# 捷運(基底)
class MRT:
    def __init__(self):
        self.country = []
        self.city = []
        self.line = []
        self.station = []
        self.staff = []


class country:
    def __init__(self, name):
        self.name = name
        self.city = []


class city:
    def __init__(self, name):
        self.name = name
        self.line = []


class line:
    def __init__(self, name):
        self.name = name
        self.station = []


class station:
    def __init__(self, name):
        self.name = name
        self.staff = []


class staff:
    def __init__(self, security_guard, clean, serve):
        self.security_guard = security_guard
        self.clean = clean
        self.serve = serve


mrt = MRT()

country_list = ['Taiwan', 'Japan', 'USA']
for i in range(len(country_list)):
    mrt.country.append(country(country_list[i]))


city_list = ['Taipei', 'Taoyuan', 'Taichung', 'Kaohsiung']
for i in range(len(city_list)):
    mrt.country[0].city.append(city(city_list[i]))


color_list = ['red', 'green', 'blue', 'orange', 'brown', 'yellow']
for i in range(len(color_list)):
    mrt.country[0].city[0].line.append(line(color_list))

station_list = ['北車', '淡水站', '象山站']
for i in range(len(station_list)):
    mrt.country[0].city[0].line[0].station.append(station(station_list))

for i in range(5):
    mrt.country[0].city[0].line[0].station[0].staff.append(staff(3, 6, 9))


print(mrt.country[0].city[0].line[0].station[0].staff[0].clean)
