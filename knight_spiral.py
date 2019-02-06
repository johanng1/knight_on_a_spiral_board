##  Knight on an infinite chess board problem - seen on Numberphile



class Spiral_Board:

	#def __init__(self):

	spiral_positions = {
	(0,0): 1,
	}

	def calculate_spiral_number(self, position):
		if position in self.spiral_positions:
			return spiral_positions[position]
		else:
			pass # this is the hard bit
			# need to work out how to calculate the number based on the 2d coordinates


	def possible_moves(self, position):
		coord_changes = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2)]

		pos_moves = [tuple(map(sum, zip(change, position))) for change in coord_changes]

		return pos_moves


