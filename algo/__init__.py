def get_closest_car(cars, ride):
    min_distance = 1000000000
    min_car_id = -1
    bonus = False
    for i in range(len(cars)):
        res = cars[i].is_free(ride)
        dist = res[0]
        is_bonus = res[1]
        if bonus == is_bonus:
            if dist != -1 and dist < min_distance:
                min_car_id = i
                min_distance = dist
        elif is_bonus is True:
            if dist != -1 and dist < min_distance:
                min_car_id = i
                min_distance = dist
    if min_car_id == -1:
        return None
    return cars[min_car_id]
