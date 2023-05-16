import numpy as np

A = (55, 100, 195, 245, 420, 500, 600, 801)

MAX_DISTANCE = 202


def get_penalties(arr):
    penalties = np.ones((len(arr), len(arr)+1))*np.inf
    penalties[:, 0] = 0
    for end in range(penalties.shape[1]):
        for start in range(end):
            end_loc = arr[end-1]
            start_loc = 0 if start == 0 else arr[start-1]
            if end_loc - start_loc <= MAX_DISTANCE:
                penalties[start][end] = (MAX_DISTANCE - (end_loc - start_loc))**2 + np.min(penalties[:, start])
    return penalties


def get_hotel_stops(arr):
    penalty_matrix = get_penalties(arr)
    loc = len(arr)
    stops = [loc]
    while loc > 0:
        if np.all(penalty_matrix[:, loc] == np.inf):
            return "Destination Not Reachable"
        loc = np.argmin(penalty_matrix[:, loc])
        stops.insert(0, loc)
    return stops, np.min(penalty_matrix[:, -1])


print(get_hotel_stops(A))
