#!/usr/bin/env python

from objects import *
from rides_index import RidesIndex
import time
from multiprocessing import Pool


def run(input_file):
    def split_as_int(line):
        return (int(x) for x in line.rstrip().split(' '))

    with open(input_file, 'r') as f:
        (rows, columns, num_vehicles, num_rides, bonus, steps,) = split_as_int(f.readline())
        ride_bonus = bonus * 10 if input_file[0] == 'e' else bonus
        rides = [None] * num_rides
        max_length = float('-inf')
        for i, line in enumerate(f):
            (start_row, start_column, finish_row, finish_column, earliest_start, latest_finish) = split_as_int(line)
            rides[i] = Ride(i, Location(start_row, start_column), Location(finish_row, finish_column), earliest_start, latest_finish)
            l = rides[i].length()
            if (l > max_length):
                max_length = l
        print('Max ride-length for {}: {}'.format(input_file, max_length))
        rides_index = RidesIndex(rides, rows, columns, steps)

    cars = [Car(i) for i in range(0, num_vehicles)]
    for car in cars:
        while car.time < steps:
            smart_rides = rides_index.smart_ride_candidates(car, max_length)
            ride, points = car.choose_next_ride(smart_rides, ride_bonus, max_length)
            # fallback? ride, points = car.choose_next_ride(rides, bonus, max_length, rides)
            if ride is None:
                break
            rides_index.mark_as_complete(ride)
            # fallback? rides.remove(ride)
            car.complete(ride, points)

    points = 0
    vehicle_assigned_to_ride = [None] * num_rides
    for car in cars:
        time = 0
        location = Location()
        for ride in car.completed_rides:
            if vehicle_assigned_to_ride[ride.i] is not None:
                raise Exception('Ride {} is assigned to both vehicle {} and {}'.format(ride.i, vehicle_assigned_to_ride[ride.i], car.i))
            vehicle_assigned_to_ride[ride.i] = car.i

            time += location.distance_to(ride.start_location)
            if ride.start_time > time:
                time += ride.start_time - time
            points += ride.score_points(time, bonus)
            time += ride.length()
            location = ride.stop_location

    print('Scored {}'.format(points))

    with open(input_file.replace('.in', '.out'), 'w') as f:
        for car in cars:
            points += car.points
            f.write(' '.join([str(len(car.completed_rides))] + [str(ride.i) for ride in car.completed_rides]) + '\n')


def single_run(input_file):
    print(input_file + ' Running ' + input_file)
    start = time.time()
    run(input_file)
    print(input_file + ' Finished in {} seconds'.format(time.time() - start))


def main():
    level = 'c'
    levels = ['e_high_bonus.in']

    pool = Pool(len(levels))
    pool.map(single_run, levels)

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
