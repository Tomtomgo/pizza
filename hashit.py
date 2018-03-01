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
        rides[i] = Ride(i, Location(start_row, start_column), Location(finish_row, finish_column), earliest_start, latest_finish)


cars = [Car(i) for i in range(0, num_vehicles)]
for car in cars:
    print(f'Simulating {car}')
    while car.time < steps:
        print(f'at {car.time}...')
        ride, score = car.choose_next_ride(rides, bonus)
        print(f'Found {ride} with {score}')
        if ride is None:
            break
        car.complete(ride, score)
    print(f'Done with the {car}')


vehicle_assigned_to_ride = [None] * num_rides
for car in cars:
    for ride in car.completed_rides:
        if vehicle_assigned_to_ride[ride.i] is not None:
            raise Exception('Ride {} is assigned to both vehicle {} and {}'.format(ride.i, vehicle_assigned_to_ride[ride.i], car.i))
        vehicle_assigned_to_ride[ride.i] = car.i


with open(OUT, 'w') as f:
    for car in cars:
        f.write(' '.join([str(len(car.completed_rides))] + [str(ride.i) for ride in car.completed_rides]) + '\n')
