from cmath import inf
import math
from statistics import multimode
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)

# Take a list of lat/lon coords and extract out the easting and northing vectors (in m)
# NOTE: For the purposes of this exercise we can ignore differing zone letters and numbers
def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)
    return total_distance

def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))


    multi_start = True

    #to try all locations as starting loc
    if multi_start == True:
        best_path_len = 1000000000000
        best_path = []

        #outer for loop simulates a mutliple restart algo, since no constraint governs startint location, all must be tried
        for k in range(len(indices)):
            curr = k
            path = [k]

            #simle NN greedy algorithm
            for i in (range(len(indices))):
                min = 1000000000000000000000
                if i != k:
                    for j in range(len(indices)):
                        if math.dist(coordinates_xy[curr], coordinates_xy[j]) < min and j not in path:
                            min = math.dist(coordinates_xy[curr], coordinates_xy[j])
                            min_ind = j

                    path.append(min_ind)
                    curr = min_ind


            if calc_total_distance(coordinates_xy, path) < best_path_len:
                print('foudn a best path')
                best_path_len = calc_total_distance(coordinates_xy, path)
                best_path = path
                print(best_path_len)

        return best_path
    else:
        curr = 0
        path = [0]
        #simle NN greedy algorithm
        for i in (range(len(indices)-1)):
            min = 1000000000000000000000
            for j in range(len(indices)):
                if math.dist(coordinates_xy[curr], coordinates_xy[j]) < min and j not in path:
                    min = math.dist(coordinates_xy[curr], coordinates_xy[j])
                    min_ind = j

            path.append(min_ind)
            curr = min_ind
    # TODO Devise an algorithm to optimise the order
        
        return path

