# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_stops = 0
    remaining_distance = distance
    current_dist = 0
    for i, dist in enumerate(stops[:-1]):
        # Changing Distances
        current_dist += dist
        remaining_distance -= dist
        # Checking whether car has reached its destination
        reached = remaining_distance <= 0

        # If yes, return num_stops
        if reached:
            # print("Reached!")
            return num_stops
        # print("Distance Remaiming", remaining_distance)

        # Check whether the car can reach the next stop
        next_stop_dist = current_dist + stops[i + 1]
        # print("Next stop at", next_stop_dist)
        # print("While tank is", tank)
        if next_stop_dist <= tank:
            # If yes, continue
            # print("Distnace on meter,", current_dist, "Can continue")
            continue
        else:
            # Else fill the tank
            # print("Fill the tank")
            num_stops += 1
            current_dist = 0
    return -1


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
