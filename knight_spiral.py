##  Knight on an infinite chess board problem - seen on Numberphile
import sys



def move_right(pos):
    (x, y) = pos
    return (x+1, y)

def move_up(pos):
    (x, y) = pos
    return (x, y+1)

def move_left(pos):
    (x, y) = pos
    return (x-1, y)

def move_down(pos):
    (x, y) = pos
    return (x, y-1)





def make_spiral_board(num_range):
    print("make_spiral_board")
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
            position = move_right(position)
        if moves[0] == "up":
            position = move_up(position)
        if moves[0] == "left":
            position = move_left(position)
        if moves[0] == "down":          
            position = move_down(position)

        

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




class Spiral_Board:

    #def __init__(self, colour):
    #    self.colour = colour


    spiral_board_10000 = make_spiral_board(10000)


    def best_move(self, position):
        #print("best move")
        possible_moves = self.possible_moves(position)
        possible_moves = [(self.spiral_board_10000[pos_move], pos_move) for pos_move in possible_moves if type(self.spiral_board_10000[pos_move]) == int]
        #print("possible_moves: ", possible_moves)
        if possible_moves != []:
            best_move = min(possible_moves)
            return best_move # (smallest number, position of that number)
        else:
            print("There are no options remaining")
            print(f"The Knight made it to space {position}, which is number {self.spiral_board_10000[position]}")
            sys.exit(1)


    def move(self, position):
        #print(position, self.spiral_board_10000[position])
        (next_num, next_pos) = self.best_move(position)
        self.spiral_board_10000[position] = "visited"
        return next_pos




    def possible_moves(self, position):
        #print("possible_moves")
        coord_changes = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2)]

        pos_moves = [tuple(map(sum, zip(change, position))) for change in coord_changes]

        return pos_moves






    

inf_board = Spiral_Board()

pos = (0, 0)

while True:
    pos = inf_board.move(pos)

