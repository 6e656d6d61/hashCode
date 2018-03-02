#! /usr/bin/python3

from threading import Thread
import exporting
import parsing
import fleet
import algo
import sort


def my_try_run(rides, cars):
    # Process data
    nb_ride_failed = 0
    for ride in rides:
        car = algo.get_closest_car(cars, ride)
        if car is not None:
            car.assign(ride)
        else:
            nb_ride_failed += 1

    print("Number of ride failed :", nb_ride_failed)
    return nb_ride_failed


def run(input_file_name, output_file_name):
    # Load data set
    input_file = parsing.CSV().from_file(input_file_name)
    header = input_file.read_line(sep=" ")
    for i in range(len(header)):
        header[i] = int(header[i])

    rides = input_file.read_n_line(int(header[3]), " ")
    for i in range(len(rides)):
        rides[i].append(i)
    for i in range(len(rides)):
        for j in range(len(rides[0])):
            rides[i][j] = int(rides[i][j])
    rides = sort.by_time_lastest(rides, header[3])

    # Create fleet
    cars_1 = fleet.create(header[2])
    cars_2 = fleet.create(header[2])

    rides_2 = rides
    nb_ride_failed_1 = my_try_run(rides, cars_1)
    rides_2.reverse()
    nb_ride_failed_2 = my_try_run(rides_2, cars_2)


    # Export
    output_file = exporting.CSV().from_file(output_file_name)
    if nb_ride_failed_1 < nb_ride_failed_2:
        for car in cars_1:
            output_file.write_line(car.export(), sep=" ")
    else:
        for car in cars_2:
            output_file.write_line(car.export(), sep=" ")

    print("End of", input_file_name)


thread_a = Thread(target=run, args=("./data/a_example.in", "out/a.out"))
thread_b = Thread(target=run, args=("./data/b_should_be_easy.in", "out/b.out"))
thread_c = Thread(target=run, args=("./data/c_no_hurry.in", "out/c.out"))
thread_d = Thread(target=run, args=("./data/d_metropolis.in", "out/d.out"))
thread_e = Thread(target=run, args=("./data/e_high_bonus.in", "out/e.out"))

thread_a.start()
thread_b.start()
thread_c.start()
thread_d.start()
thread_e.start()

thread_a.join()
thread_b.join()
thread_c.join()
thread_d.join()
thread_e.join()

print("Done !")
