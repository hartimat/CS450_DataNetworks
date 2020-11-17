# Filename: tollgate.py
# Course: CS450 - Data Networks
# Assignment: Week 1 Program
# Author: Matt Hartigan
# Date: 2-Nov-2019
# Description: Defines toll gate class for first programming assignment.


class TollGate:

	def __init__(self, gate_number, process_time):
		self.gate_number = gate_number
		self.process_time = process_time
		self.time_to_next_gate = 0

	def calcTimeToNextGate(self, speed, distance_to_next):
		self.time_to_next_gate = distance_to_next / speed