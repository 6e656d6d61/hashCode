class Car:
    def __init__(self):
        self.rides = []
        self.x = 0
        self.y = 0
        self.t = 0

    def get_distance_between(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def time_of_last_ride(self):
        time = 0
        for ride in self.rides:
            time += self.get_distance_between(self.x, self.y, ride[0], ride[1])
            if time < ride[4]:
                time = ride[4]
            time += self.get_distance_between(ride[0], ride[1], ride[2], ride[3])
            self.x = ride[2]
            self.y = ride[3]
        return time 

    def is_free(self, new_ride):
        if len(self.rides) == 0:
            dist = self.get_distance_between(0, 0, new_ride[0], new_ride[1])
            if dist <= new_ride[4]:
                return [dist, True]
            else:
                return [dist, False]
        last_ride = self.rides[-1]
        dist = self.get_distance_between(last_ride[0], last_ride[1], new_ride[0], new_ride[1])
        time_on_starting_cell = dist + self.time_of_last_ride()
        if time_on_starting_cell <= new_ride[5] - self.get_distance_between(new_ride[0], new_ride[1], new_ride[2], new_ride[3]):
            if time_on_starting_cell <= new_ride[4]:
                return [dist + self.time_of_last_ride(), True]
            else:
                return [dist + self.time_of_last_ride(), False]
        return [-1, -1]

    def assign(self, ride):
        self.rides.append(ride)

    def export(self):
        ids = []
        for ride in self.rides:
            ids.append(str(ride[-1]))
        return [str(len(ids))] + ids

def create(n):
    cars = []
    for i in range(n):
        cars.append(Car())
    return cars

