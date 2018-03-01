#!/usr/bin/env python

from objects import *

import time

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
    for car in cars:
        while car.time < steps:
            ride, score = car.choose_next_ride(rides, bonus)
            if ride is None:
                break
            car.complete(ride, score)

    vehicle_assigned_to_ride = [None] * num_rides
    for car in cars:
        for ride in car.completed_rides:
            if vehicle_assigned_to_ride[ride.i] is not None:
                raise Exception('Ride {} is assigned to both vehicle {} and {}'.format(ride.i, vehicle_assigned_to_ride[ride.i], car.i))
            vehicle_assigned_to_ride[ride.i] = car.i

    with open(input_file.replace('.in', '.out'), 'w') as f:
        for car in cars:
            f.write(' '.join([str(len(car.completed_rides))] + [str(ride.i) for ride in car.completed_rides]) + '\n')


for input_file in ('a_example.in', 'b_should_be_easy.in', 'c_no_hurry.in', 'd_metropolis.in', 'e_high_bonus.in'):
    print('Running ' + input_file)
    start = time.time()
    run(input_file)
    print('Finished in {} seconds'.format(time.time() - start))
