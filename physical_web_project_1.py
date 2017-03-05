def main():
	"""
	Takes the input of the user for the number of commands
	try/except conditions for each command input
	if string index is out of range in case '1'
	if the list is empty in case '2' or '3' 
	if the input is other than '1', '2' or '3'
	"""
	num_commands = raw_input() # Taking user's input for number of commands
	command_index = 0
	queue = [] # Initializing the queue
	queue_printed = [] # Initializing the queue list to be printed
	while command_index < int(num_commands):
		x = raw_input()
		if int(x[0]) == 1:
			try:
				queue.append(x[2:])
			except IndexError:
				print "Please correct your input"
			command_index += 1
		elif int(x[0]) == 2:
			try:
				queue[0] = queue[-1]
				queue.remove(queue[-1])
			except IndexError:
				print "List is empty"
			command_index += 1
		elif int(x[0]) == 3:
			try:
				queue_printed.append(queue[0])
			except IndexError:
				print "List is empty and no element can be printed"
			command_index += 1
		else:
			print "Please correct your input"
			command_index += 0
	for element in queue_printed:
		print element

