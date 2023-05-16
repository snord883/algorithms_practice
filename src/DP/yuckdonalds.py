import numpy as np

# POSSIBLE_LOCATIONS = {
#     0: {'location': 14, 'profit': 5},
#     1: {'location': 25, 'profit': 91},
#     2: {'location': 33, 'profit': 82},
#     3: {'location': 37, 'profit': 71},
#     4: {'location': 43, 'profit': 21},
#     5: {'location': 44, 'profit': 30},
#     6: {'location': 49, 'profit': 29},
#     7: {'location': 55, 'profit': 90},
#     8: {'location': 56, 'profit': 74},
#     9: {'location': 71, 'profit': 15}
# }
LOCATIONS = np.array([14, 25, 33, 37, 43, 44, 49, 55, 56, 58])
PROFITS   = np.array([15, 91, 82, 71, 21, 30, 29, 90, 74, 15])
MIN_DISTANCE = 10


def get_optimal_locations():
    opt_locations = np.zeros((len(LOCATIONS), len(LOCATIONS)))
    prev_profits_loc_i_included = np.zeros(len(LOCATIONS))
    for i in range(len(LOCATIONS)):
        eligible_prev_profits_loc_i_included = prev_profits_loc_i_included[LOCATIONS <= LOCATIONS[i]-MIN_DISTANCE]
        if eligible_prev_profits_loc_i_included.shape[0] > 0:
            opt_prev_locations_to_include_i = np.argmax(eligible_prev_profits_loc_i_included)
            opt_locations[i] = opt_locations[opt_prev_locations_to_include_i, :]
        opt_locations[i, i] = 1
        prev_profits_loc_i_included[i] = np.sum(opt_locations[i] * PROFITS)
    return opt_locations[np.argmax(prev_profits_loc_i_included)]


locs = get_optimal_locations()
print(locs)
print(np.sum(locs*PROFITS))
