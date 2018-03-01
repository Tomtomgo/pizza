class Location:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def distance_to(self, other):
        return abs(self.column - other.column) + abs(self.row - other.row)

    def __str__(self):
        return 'Location[{}; {}]'.format(self.row, self.column)


class Ride:
    def __init__(self, i, start_location: Location, stop_location: Location, start_time, end_time):
        self.i = i
        self.start_location = start_location
        self.stop_location = stop_location
        self.start_time = start_time
        self.end_time = end_time

    def length(self):
        return self.start_location.distance_to(self.stop_location)

    def __str__(self):
        return 'Ride#{}[from={} to={}; ({}; {})]'.format(self.i,
                                                         self.start_location,
                                                         self.stop_location,
                                                         self.start_time,
                                                         self.end_time)


class Car:
    def __init__(self, i):
        self.i = i
        self.location = Location(0, 0)
        self.time = 0
        self.points = 0
        self.completed_rides = []

    def choose_next_ride(self, rides, bonus):
        best = None
        best_score = 0
        for ride in rides:
            score = self.score_ride(ride, bonus)
            if score > 0:
                best = ride
                best_score = score
        if best is not None:
            rides.remove(best)
        return best, best_score

    def duration(self, ride: Ride):
        time_until_start = max(self.location.distance_to(ride.start_location), ride.start_time)
        return time_until_start + ride.length()

    def score_ride(self, ride: Ride, bonus):
        if self.time + self.duration(ride) >= ride.end_time:
            return 0

        b = bonus if self.time + self.location.distance_to(ride.start_location) <= ride.start_time else 0
        return b + ride.length()

    def complete(self, ride: Ride, score):
        self.location = ride.stop_location
        self.time += self.duration(ride)
        self.points += score
        self.completed_rides.append(ride)

    def __str__(self):
        return 'Car#{}[t={}; loc={}; b={}; cmp=[{}]]'.format(self.i,
                                                             self.time,
                                                             self.location,
                                                             self.points,
                                                             ','.join(map(str, self.completed_rides)))
