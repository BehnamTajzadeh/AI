points = [(2,9),(3,6),(4,2),(6,7),(8,4),(10,1)]
prediceted_points = [(2,2),(3,2.5),(4,3.5),(6,6.3),(8,7.7),(10,9.6)]

def least_square_error(_points,prd_point):
    minimum_least_square_fault = 0

    for i in _points:
        j = prd_point[_points.index(i)]
        z = (i[1]-j[1])**2
        minimum_least_square_fault += z
    return minimum_least_square_fault

print(least_square_error(points, prediceted_points))