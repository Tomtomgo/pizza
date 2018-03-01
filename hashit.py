#!/usr/bin/env python

from objects import *

IN = 'b_should_be_easy.in'
OUT = IN.replace('.in', '.out')


def split_as_int(line):
    return (int(x) for x in line.rstrip().split(' '))


with open(IN, 'r') as f:
    (rows, columns, num_vehicles, num_rides, bonus, steps,) = split_as_int(f.readline())
    rides = [None] * num_rides
    for i, line in enumerate(f):
        (start_row, start_column, finish_row, finish_column, earliest_start, latest_finish) = split_as_int(line)
        rides[i] = Ride(Location(start_row, start_column), Location(finish_row, finish_column), earliest_start, latest_finish)


vehicle_rides = [list() for i in range(0, num_vehicles)]
for i, ride in enumerate(rides):
    pass


vehicle_assigned_to_ride = [None] * num_rides
for vehicle, dispatched in enumerate(vehicle_rides):
    for ride in dispatched:
        if vehicle_assigned_to_ride[ride] is not None:
            raise Exception('Ride {} is assigned to both vehicle {} and {}'.format(ride, vehicle_assigned_to_ride[ride], vehicle))
        vehicle_assigned_to_ride[ride] = vehicle


with open(OUT, 'w') as f:
    for dispatched in vehicle_rides:
        f.write(' '.join([str(len(dispatched))] + [str(x) for x in dispatched]) + '\n')
