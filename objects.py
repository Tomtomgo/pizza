class Car:
    def __init__(self, location, time, points):
        self.location = location
        self.time = time
        self.points = points

class Ride:
    def __init__(self, start_location, stop_location, start_time, end_time):
        self.start_location = start_location
        self.stop_location = stop_location
        self.start_time = start_time
        self.end_time = end_time

class Location:
    def __init__(self, row, column):
        self.row = row
        self.column = column
