# Filename: main.py
# Course: CS450 - Data Networks
# Assignment: Week 1 Program
# Author: Matt Hartigan
# Date: 2-Nov-2019
# Description: Main file for executing first programming assignment.

from tollgate import TollGate

if __name__ == '__main__':

	# Define variables
	total_transit_time = 0    # hours
	dist_between_gates = 0    # assume all gates are equally spaced along route
	gate_list = []    # list of each TollGate class instance

	# Greet user
	print("Welcome to CS450 - Assignment #1!")
	print("Please enter the requested information as prompted.")

	# Get input
	try:
		route_distance = float(input("Input total distance traveled on route (mi): "))
		speed_limit = float(input("Input universal highway speed limit (mph): "))
		num_cars = int(input("Input number of cars in the caravan: "))
		num_gates = int(input("Input number of toll gates on route: "))
		for i in range(0, num_gates):
			delay = float(input("Input processing delay (min) for gate #" + str(i+1) + ": "))
			gate_list.append(TollGate(i+1, delay))
	except:
		print("There was an error in the user's input.  Please restart.")
		exit(1)

	# Calculate answers
	dist_between_gates = route_distance / (num_gates - 1)
	for i in range(0, num_gates-1):    # time between gates
		gate_list[i].calcTimeToNextGate(speed_limit, dist_between_gates)
	for gate in gate_list:    # compute sum
		total_transit_time = total_transit_time + (gate.process_time/60)*num_cars + gate.time_to_next_gate

	# Output answers
	# Echo input data
	print()
	print()
	print("INPUT DATA SUMMARY")
	print("Total route distance = " + str(route_distance) + " miles")
	print("Highway speed limit = " + str(speed_limit) + " mph")
	print("Number of cars in caravan = " + str(num_cars))
	print("Number of toll gates = " + str(num_gates))
	print("Distance between gates = " + str(dist_between_gates))

	# Output total time to complete journey
	print()
	print()
	print("TOTAL TRAVEL TIME: " + str(round(total_transit_time, 2)) + " hours.")