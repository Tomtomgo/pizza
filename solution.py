

def distance(start, end):
    (a, b) = start
    (x, y) = end
    return abs(b - y) + abs(a - x)


def simulate_ride(current_time, car, start, end, timerange):
    (time_start, time_end) = timerange
    to_start_point = distance(car, start)
    ride_time = distance(start, end)
    arrival_to_start_time = current_time + to_start_point
    arrival_to_end_time = max(arrival_to_start_time, time_start) + ride_time
    can_make_it = arrival_to_end_time < time_end
    wait = time_start - arrival_to_start_time
    return {
        'possible': can_make_it,
        'bonus': wait == 0,
        'wait': max(0, wait),
        'position': end,
        'time': arrival_to_end_time
    }

if __name__ == '__main__':
    car = (0, 0)
    start = (1, 2)
    finish = (1, 4)
    time = (5, 8)
    current_time = 0
    print(simulate_ride(current_time, car, start, finish, time))
