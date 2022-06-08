# python3
import sys


def compute_min_refills(distance, tank, stops):
    tank_refills = 0
    tank_remaining = tank
    distance_remaining = distance
    stops = [0] + stops + [distance]

    for i in range(len(stops)):
        # print(f"\nAt stop {i+1}")
        if i == 0:
            distance_moved = 0
        else:
            distance_moved = stops[i] - stops[i - 1]

        if i == len(stops) - 1:
            next_stop_at = 0
        else:
            next_stop_at = stops[i + 1] - stops[i]

        distance_remaining -= distance_moved
        tank_remaining -= distance_moved
        # assert tank_remaining >= 0
        # print(f"Distnace remaining: {distance_remaining}")
        if distance_remaining <= 0:
            # print("Reached destination!")
            return tank_refills

        # print(f"Next stop at: {next_stop_at}")
        # print(f"Tank remaining: {tank_remaining}")
        if tank_remaining < 0:
            return -1
        if next_stop_at <= tank_remaining:
            # print("Can reach next stop!")
            continue
        else:
            # print("Cannot reach next stop! Fill tank!")
            tank_refills += 1
            tank_remaining = tank
    # print("Can not reach destination!".upper())
    return -1


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
