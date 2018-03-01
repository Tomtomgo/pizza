#!/usr/bin/env python


IN = 'example.in'
OUT = 'example.out'


def split_as_int(line):
    return (int(x) for x in line.rstrip().split(' '))


with open(IN, 'r') as f:
    (rows, columns, num_vehicles, num_rides, bonus, steps,) = split_as_int(f.readline())
    rides = [None] * num_rides
    for i, line in enumerate(f):
        rides[i] = split_as_int(line)


vehicle_rides = [list() for i in range(0, num_vehicles)]

for ride, (startRow, startColumn, finishRow, finishColumn, earliestStart, latestFinish) in enumerate(rides):
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



