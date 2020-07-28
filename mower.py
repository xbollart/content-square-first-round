from enum import Enum

class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4
    UNKNOWN = 5

class Mower:
    def __init__(self,id, x, y, size_x, size_y, direction, moves):
        self.id = str(id)
        self.pos_x = int(x)
        self.pos_y = int(y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.direction = self.str_to_direction(direction)
        self.moves = moves

    def str_to_direction(self,input):
        switcher = {
            'n': Direction.NORTH,
            'w': Direction.WEST,
            's': Direction.SOUTH,
            'e': Direction.EAST
        }
        return switcher.get(input.lower(),Direction.UNKNOWN)

    def direction_to_str(self):
        switcher= {
                    Direction.NORTH: 'N',
                    Direction.WEST: 'W',
                    Direction.SOUTH: 'S',
                    Direction.EAST: 'E'
                    }
        return switcher.get(self.direction,'')


    def move_forward(self):
        if self.direction == Direction.NORTH:
            if self.pos_y + 1 <= self.size_y:
                self.pos_y += 1
            else:
                print('mower '+self.id+': North side of the loan reached')
        elif self.direction == Direction.SOUTH:
            if self.pos_y -1 >= 0:
                self.pos_y -= 1
            else:
                print('mower '+self.id+': South side of the loan reached')
        elif self.direction == Direction.WEST:
            if self.pos_x - 1 >= 0:
                self.pos_x -= 1
            else:
                print('mower '+self.id+': West side of the loan reached')    
        elif self.direction == Direction.EAST:
            if self.pos_x + 1 <= self.size_x:
                self.pos_x += 1
            else:
                print('mower '+self.id+': East side of the loan reached')

    def rotate_left(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.NORTH
        else:
            print('error rotate_left: unknow direction') 

    def rotate_right(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.NORTH
        else:
            print('error rotate_right: unknow direction')

    def show_my_position(self):
        return str(self.pos_x) + ' ' + str(self.pos_y) + ' ' +self.direction_to_str()+'\n'


    def mow(self):
        for move in self.moves:
            if move == 'L':
                self.rotate_left()
            elif move == 'R':
                self.rotate_right()
            elif move == 'F':
                self.move_forward()
            else:
                print('unknown move')