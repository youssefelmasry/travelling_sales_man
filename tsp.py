'''
first set the starting point
we will represent the distance as a weight between each others by calculating the sum of distances
get all possible combinations of the given distances by using permutation
then calculate the min weighted distance among them
'''

from itertools import permutations

def distance(p1, p2):
    '''
    Euclidean distance between two points P1 = (x1, y1) and P2 = (x2, y2) is:
    sqrt((x1 - x2)^2 + (y1 - y2)^2)
    '''
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def total_distance(points):
    list_len = len(points)
    return sum([distance(points[index], points[index+1]) for index in range(list_len-1)])

def solve_tsp(points, start = None):
    '''
    the permutations result is n!, we should to filter the combinations that with only the provided starting point
    so we have to put condition if perm[0] == start
    '''
    if start is None:
        start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key = total_distance)

# example
# print(solve_tsp(([[0,0],[6,0],[2,3],[3,7],[0.5,9],[3,5],[9,1]])))
# >>> ([0, 0], [6, 0], [9, 1], [2, 3], [3, 5], [3, 7], [0.5, 9])