# Class: CS450
# Assignment: Week 3 Programming Assignment
# Student: Matt Hartigan
# Description:  Implement a sending state machine using python.

def call_zero():
	"""Function defining Call 0 state behavior."""
	print("[CURRENT STATE = Call 0] 0 = simulate receiving packets. 1 = simulate sending data.")

	# Process user input
	user_input = input("[CURRENT STATE = Call 0] User input: ")
	if int(user_input) == 0:
		print("Packets received.  Throwing packets away.")
		print("Re-entering Call 0 state.")
		call_zero()
	elif int(user_input) == 1:
		print("Sending data....")
		print("_snd_packet = make_pkt(0, data, checksum)")
		print("_udt_send(_snd_packet)")
		print("start_timer")
		print("Transitioning to Wait 0 state")
		print()
		wait_zero()
	else:
		print("There was an error with user's input. Exiting program.")
		exit(999)

def wait_zero():
	"""Function defining Wait 0 state behavior."""
	print("[CURRENT STATE = Wait 0] 0 = simulate timeout. 1 = simulate corrupt packet. 2 = simulate clean packet and ACK receipt.")

	# Process user input
	user_input = input("[CURRENT STATE = Wait 0] User input: ")
	if int(user_input) == 0:
		print("Time out error...")
		print("_udt_sent(_snd_packet)")
		print("start_timer")
		print("Re-entering Wait 0 state.")
		wait_zero()
	elif int(user_input) == 1:
		print("Corrupt packet received....")
		print("Re-entering Wait 0 state.")
		wait_zero()
	elif int(user_input) == 2:
		print("Received a clean packet and ACK...")
		print("stop_timer")
		print("Transitioning to Call 1 state")
		print()
		call_one()
	else:
		print("There was an error with user's input. Exiting program.")
		exit(999)

def call_one():
	"""Function defining Call 1 state behavior."""
	print("[CURRENT STATE = Call 1] 0 = simulate receiving packets. 1 = simulate sending data.")

	# Process user input
	user_input = input("[CURRENT STATE = Call 1] User input: ")
	if int(user_input) == 0:
		print("Packets received.  Throwing packets away.")
		print("Re-entering Call 1 state.")
		call_one()
	elif int(user_input) == 1:
		print("Sending data....")
		print("_snd_packet = make_pkt(1, data, checksum)")
		print("_udt_send(_snd_packet)")
		print("start_timer")
		print("Transitioning to Wait 1 state")
		print()
		wait_one()
	else:
		print("There was an error with user's input. Exiting program.")
		exit(999)


def wait_one():
	"""Function defining Wait 1 state behavior."""
	print("[CURRENT STATE = Wait 1] 0 = simulate timeout. 1 = simulate corrupt packet. 2 = simulate clean packet and ACK receipt.")

	# Process user input
	user_input = input("[CURRENT STATE = Wait 1] User input: ")
	if int(user_input) == 0:
		print("Time out error...")
		print("_udt_sent(_snd_packet)")
		print("start_timer")
		print("Re-entering Wait 1 state.")
		wait_one()
	elif int(user_input) == 1:
		print("Corrupt packet received....")
		print("Re-entering Wait 1 state.")
		wait_one()
	elif int(user_input) == 2:
		print("Received a clean packet and ACK...")
		print("stop_timer")
		print("Transitioning to Call 0 state")
		print()
		call_zero()
	else:
		print("There was an error with user's input. Exiting program.")
		exit(999)

# MAIN FUNCTION (START HERE)
print("Welcome to the Week 3 Programming Assingment!")
print("You (the user) will be prompted to interact with a sending state machine.")
print("We will start in the Call 0 state.")
print("To exit, type an integer that does NOT correspond to a prompted response.")
print("Here we go!")
print()
call_zero()
