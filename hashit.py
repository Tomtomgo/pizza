#!/usr/bin/env python

from objects import *
import time
import math

def sq(a):
    return a * a

def space_time(r):
    return math.sqrt(
        sq(r.end_time - r.start_time) +
        sq(r.stop_location.column - r.start_location.column) +
        sq(r.stop_location.row - r.start_location.row))

def run(input_file):
    def split_as_int(line):
        return (int(x) for x in line.rstrip().split(' '))

    with open(input_file, 'r') as f:
        (rows, columns, num_vehicles, num_rides, bonus, steps,) = split_as_int(f.readline())
        rides = [None] * num_rides
        for i, line in enumerate(f):
            (start_row, start_column, finish_row, finish_column, earliest_start, latest_finish) = split_as_int(line)
            rides[i] = Ride(i, Location(start_row, start_column), Location(finish_row, finish_column), earliest_start, latest_finish)

    cars = [Car(i) for i in range(0, num_vehicles)]


    for ride in sorted(rides, key=space_time):
        ride.assign_car(cars, bonus)
    # for car in cars:
    #     while car.time < steps:
    #         ride, points = car.choose_next_ride(rides, bonus)
    #         if ride is None:
    #             break
    #         car.complete(ride, points)

    vehicle_assigned_to_ride = [None] * num_rides
    for car in cars:
        for ride in car.completed_rides:
            if vehicle_assigned_to_ride[ride.i] is not None:
                raise Exception('Ride {} is assigned to both vehicle {} and {}'.format(ride.i, vehicle_assigned_to_ride[ride.i], car.i))
            vehicle_assigned_to_ride[ride.i] = car.i

    points = 0
    with open(input_file.replace('.in', '.out'), 'w') as f:
        for car in cars:
            points += car.points
            f.write(' '.join([str(len(car.completed_rides))] + [str(ride.i) for ride in car.completed_rides]) + '\n')

    print('Scored {}'.format(points))

level = 'b'
for input_file in ('b_should_be_easy.in', 'c_no_hurry.in', 'd_metropolis.in', 'e_high_bonus.in'):
    if input_file[0] > level:
        continue

    print('Running ' + input_file)
    start = time.time()
    run(input_file)
    print('Finished in {} seconds'.format(time.time() - start))
