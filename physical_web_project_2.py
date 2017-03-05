def main():
	"""
	Takes the input of the user and calculates the running median
	"""
	num_inputs = raw_input()
	input_index = 0
	num_list = [] # Initializing the number list entered by the user
	median_list = [] # Initializing the running median list
	while input_index < int(num_inputs):
		number = raw_input()
		num_list.append(int(number))
		if len(num_list)%2 == 0:
			mid_index = (len(num_list)/2) - 1
			new_median = (float(num_list[mid_index]) + float(num_list[mid_index+1]))/2
			median_list.append(new_median)
			input_index += 1
		else:
			mid_index = ((len(num_list)+1)/2) - 1
			new_median = num_list[mid_index]
			median_list.append(new_median)
			input_index += 1

	for median in median_list:
		print float(median)