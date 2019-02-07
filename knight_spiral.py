##  Knight on an infinite chess board problem - seen on Numberphile



class Spiral_Board:

	#def __init__(self):


	def calculate_spiral_number(self, position):
		if position in self.already_visited:
			return "already visited"
		else:
			already_visited.append(position)
			pass # this is the hard bit
			# need to work out how to calculate the number based on the 2d coordinates


	def possible_moves(self, position):
		coord_changes = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2)]

		pos_moves = [tuple(map(sum, zip(change, position))) for change in coord_changes]

		return pos_moves


	def move_right(self, pos):
		(x, y) = pos
		return (x+1, y)

	def move_up(self, pos):
		(x, y) = pos
		return (x, y+1)

	def move_left(self, pos):
		(x, y) = pos
		return (x-1, y)

	def move_down(self, pos):
		(x, y) = pos
		return (x, y-1)




	def make_spiral_board(self, num_range):
		spiral_positions = {
		(0, 0): 1
		}

		moves = ["right", "up", "left", "down"]
		position = (0, 0)
		move_until = 1
		counter_move_twice = 1
		counter_until = 1
		for i in range(2, num_range):

			if moves[0] == "right":
				position = self.move_right(position)
			if moves[0] == "up":
				position = self.move_up(position)
			if moves[0] == "left":
				position = self.move_left(position)
			if moves[0] == "down":			
				position = self.move_down(position)

			

			spiral_positions[position] = i


			if counter_until == move_until:
				counter_until = 1
				moves = moves[1:] + [moves[0]]
				if counter_move_twice == 2:
					counter_move_twice = 1
					move_until += 1
				else:
					counter_move_twice += 1
				
			else:
				counter_until += 1


		return spiral_positions






print(Spiral_Board().make_spiral_board(10))