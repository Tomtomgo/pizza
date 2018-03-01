NEGATIVE_INFINITY = -1e12
NO_RIDE = -NEGATIVE_INFINITY, 0

class Location:
    def __init__(self, row=0, column=0):
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
        self._length = self.start_location.distance_to(self.stop_location)

    def length(self):
        return self._length

    def score_points(self, pickup_time, bonus):
        if pickup_time + self._length >= self.end_time:
            return 0
        return self._length + (bonus if pickup_time == self.start_time else 0)

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

    def choose_next_ride(self, rides, bonus, max_length):
        best = None
        best_score = NEGATIVE_INFINITY
        best_points = 0
        for ride in rides:
            score, points = self.score_ride(ride, bonus, max_length)
            if score > best_score:
                best = ride
                best_score = score
                best_points = points
        return best, best_points

    def duration(self, ride: Ride):
        time_until_start = max(self.location.distance_to(ride.start_location), ride.start_time)
        return time_until_start + ride.length()

    def score_ride(self, ride: Ride, bonus, max_length):
        if self.time + self.duration(ride) >= ride.end_time:
            return NO_RIDE

        pickup_duration = self.location.distance_to(ride.start_location)
        arrival_time = self.time + pickup_duration
        wait = max(ride.start_time - arrival_time, 0)

        points = ride.score_points(arrival_time + wait, bonus)
        score = points - wait

        return score, points

    def complete(self, ride: Ride, points):
        self.location = ride.stop_location
        self.time += self.duration(ride)
        self.points += points
        self.completed_rides.append(ride)

    def __str__(self):
        return 'Car#{}[t={}; loc={}; b={}; cmp=[{}]]'.format(self.i,
                                                             self.time,
                                                             self.location,
                                                             self.points,
                                                             ','.join(map(str, self.completed_rides)))
