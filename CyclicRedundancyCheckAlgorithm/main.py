###############################################################################
# Course: CS 450
# Assignment: Week 6 Programming Assignment - Cyclic Redundancy Check Algorithm
# Author: Matt Hartigan
# Date: 7-December-2019
# Description: A python implementation of a cyclic redundancy check algorithm.
###############################################################################


##### CONSTANTS
POLYNOMIAL = '111111111111111111111111111111111'    # must be 33 bits for it to be CRC-32


##### FUNCTION DEFINITIONS
def xor(dividend, divisor, original_dividend_length):
	""" Returns remainder of XOR operation performed on the inputs. """

	j = 0
	while j < original_dividend_length - 1:
		# Convert to strings, strip preceding zeroes
		initial_length = len(dividend)
		dividend = lst_to_str(dividend).lstrip('0')
		final_length = len(dividend)
		num_stripped = initial_length - final_length
		divisor = lst_to_str(divisor).lstrip('0')

		# Convert back to lists
		dividend = str_to_lst(dividend)
		divisor = str_to_lst(divisor)

		# Perform XOR
		result = []
		i = 0
		k = len(dividend)
		while k < len(divisor):
			dividend.append("x")
			k = k + 1
		while i < min(len(dividend), len(divisor)):
			if dividend[i] == "x":
				result.append(divisor[i])
			elif dividend[i] == '1' and divisor[i] == '1':
				result.append('0')
			elif dividend[i] == '0' and divisor[i] == '0':
				result.append('0')
			else:
				result.append('1')
			i = i + 1

		dividend = result
		j = j + num_stripped

	return dividend


def lst_to_str(input_list):
	""" Returns contents of input list in string format. """
	str = ""
	for element in input_list:
		str += element
	return str


def str_to_lst(input_string):
	""" Returns contents of input string in list format. """
	i = 0
	list = []
	while i<len(input_string):
		list.append(input_string[i])
		i = i + 1
	return list


def main():
	""" Main function. """
	# Greet user, prompt for input message
	print("Welcome to the CS450 Cyclic Redundancy Check Algorithm!")
	original_input = input("Enter your message (binary, <128 chars): ")
	#FIXME: test case
	# original_input = "11000010"
	#FIXME: 128-bit sample data stream
	# original_input = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"
	crc_message = original_input
	if len(crc_message) > 128:
		print("Input message too long!  Exiting now.")
		exit(1)


	# Append POLYNOMIAL
	i = 0
	original_length = len(original_input)
	while i < (len(POLYNOMIAL) - 1):
		crc_message = crc_message + '0'
		i = i + 1

	# Calculate remainder
	crc_message_list = str_to_lst(crc_message)
	polynomial_list = str_to_lst(POLYNOMIAL)
	remainder = xor(crc_message_list, polynomial_list, original_length)

	# Output results in hex format
	print("Remainder in binary: ", remainder)
	print("Input data stream (in hex): ", hex(int(original_input, 2)))
	print("Calculated CRC-32 remainder  (in hex): ", hex(int(lst_to_str(remainder), 2)))


if __name__ == '__main__':
	main()
