def by_time_lastest(rides, nb_rides):
    f = []
    for i in range(0, nb_rides):
        f.append(find_smallest(rides))
    return f

def find_smallest(rides):
    s = rides[0]
    for i in range(0, len(rides)):
        if s[4] > rides[i][4]:
            s = rides[i]
    for i in range(0, len(rides)):
        if s == rides[i]:
            rides.pop(i)
            break
    return s
