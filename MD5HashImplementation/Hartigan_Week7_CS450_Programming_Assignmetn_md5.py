###############################################################################
# Course: CS 450
# Assignment: Week 7 Programming Assignment - MD5 Hash Algorithm
# Author: Matt Hartigan
# Date: 15-December-2019
# Description: A python implementation of a MD5 hash algorithm.
###############################################################################

##### TEST MESSAGES #####
key1 = 'THE QUICK BROWN FOX JUST CAME OVER TO SEE THE LAZY POODLE'   # encryption key
key2 = 'FOUR SCORE AND SEVEN YEARS AGO'
key3 = 'Hi'

##### FUNCTION DEFINITIONS #####
def append_message(padded_message, message):
	""" Function that appends a 64-bit representation of the message. """
	# Get 64-bit representation of original message
	binary_message = bin(int.from_bytes(message.encode(), 'big'))
	binary_message = format(binary_message[2:], '>066')
	print(binary_message)
	full_message = padded_message + binary_message
	return full_message


def pad_message(message):
	""" Function to pad input message to the desired length. """
	# Convert to binary
	temp_message = 0
	for char in message:
		temp = ord(char)
		temp_message = (temp_message << len(bin(temp)[2:])) + temp

	# Pad message
	padded_message = ''
	if len(bin(temp_message)[2:]) < 448:
		padded_message = bin(temp_message) + '1'
		while len(padded_message[2:]) < 448:
			padded_message = padded_message + '0'
	elif len(bin(temp_message)[2:1]) > 448:
		print("FIXME: Input message too long for demo case. Exiting now.")
		exit(1)

	return padded_message[2:]


def main():
	""" Main function. """
	print("Welcome to the CS450 MD5 Hashing Algorithm Demo!")

	# Step 1 - Pad message
	print("Step 1 - Pad message")
	print("Input message: " + key3)
	# Convert message to binary
	message = key3.replace(' ', '')    # strip spaces
	print(message)
	padded_message = pad_message(message)
	print(padded_message)
	print("Length of the above padded message = " + str(len(padded_message)))
	print()

	# Step 2 - Append message
	print("Step 2 - Append message")
	appended_message = append_message(padded_message, message)
	print(appended_message[2:])
	print(len(appended_message[2:]))
	print()

	# Step 3 - Initialize MD Buffer
	print("Step 3 - Initialize MD buffer")
	word_A = [0x01, 0x23, 0x45, 0x67]
	word_B = [0x89, 0xab, 0xcd, 0xef]
	word_C = [0xfe, 0xdc, 0xba, 0x98]
	word_D = [0x76, 0x54, 0x32, 0x10]
	print("Complete.")
	print()

	# Step 4 - Process Message in 16-Word Blocks
	print("Step 4 - Process message in 16-word blocks")
	print("FIXME")
	print()

	# Step 5 - Output (hex format)
	print("Step 5 - Output (hex format)")
	print("FIXME")
	print()


if __name__ == '__main__':
	main()
