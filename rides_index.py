from typing import List
from objects import *

class RidesIndex:
    def __init__(self, rides: List[Ride], n_rows, n_columns, steps):
        self._completed_rides = set()
        self._row_index = [set()] * n_rows
        self._column_index = [set()] * n_columns
        self._start_time_index = [set()] * steps
        self._end_time_index = [set()] * steps
        for ride in rides:
            self._row_index[ride.start_location.row].add(ride)
            self._column_index[ride.start_location.column].add(ride)
            self._start_time_index[ride.start_time].add(ride)
            self._end_time_index[ride.end_time].add(ride)

    def smart_ride_candidates(self, car: Car, max_length):
        min_row = max(car.location.row - max_length, 0)
        row_candidates = set.union(*self._row_index[min_row:car.location.row + max_length])
        min_column = max(car.location.column - max_length, 0)
        column_candidates = set.union(*self._column_index[min_column:car.location.column + max_length])

        start_candidates = set.union(*self._start_time_index[car.time:car.time + 2 * max_length])
        end_candidates = set.union(*self._end_time_index[car.time:])

        return set.intersection(row_candidates, column_candidates, start_candidates, end_candidates) - self._completed_rides

    def mark_as_complete(self, ride):
        self._completed_rides.add(ride)
