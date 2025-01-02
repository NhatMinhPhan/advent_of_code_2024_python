from typing import List
import copy

# For my test case, it's going to take 10 hours roughly. So, it's not effective.

class Guard:
    def __init__(self, orientation, x, y):
        assert orientation == 'left' or orientation == 'right' \
        or orientation == 'up' or orientation == 'down', 'orientation must be left, right, up or down'
        assert isinstance(x, int) and x >= 0, 'x is not a non-negative integer'
        assert isinstance(y, int) and y >= 0, 'y is not a non-negative integer'
        self.orientation = orientation
        self.x = x
        self.y = y
        self.turning_points = []

    def get_orientation(self):
        return self.orientation

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move_x(self, steps: int):
        """ Moves x-position by steps and returns the modified x-position """
        assert isinstance(steps, int), 'steps is not an integer'
        self.x += steps
        return self.x

    def move_y(self, steps: int):
        """ Moves y-position by steps and returns the modified y-position
        Positive steps mean up, and negative steps down """
        assert isinstance(steps, int), 'steps is not an integer'
        self.y -= steps
        return self.y

    def turn_right(self):
        match (self.orientation):
            case 'up':
                self.orientation = 'right'
            case 'right':
                self.orientation = 'down'
            case 'down':
                self.orientation = 'left'
            case 'left':
                self.orientation = 'up'
        self.turning_points.append((self.get_x(), self.get_y()))

    def is_in_loop(self):
        # If a sequence of the two most recent turning points has occurred in the
        # list of turning points before, the guard is in a loop.
        if len(self.turning_points) < 2:
            return False

        second_most_recent = self.turning_points[-2]
        most_recent = self.turning_points[-1]
        second_most_index = self.turning_points.index(second_most_recent)
        most_recent_index = self.turning_points.index(most_recent)
        return second_most_index < len(self.turning_points) - 2 and \
            most_recent_index < len(self.turning_points) - 1 and \
            second_most_index == most_recent_index - 1 and \
            second_most_recent != most_recent
    pass

class Map:
    def __init__(self, map: List[str]):
        self.map = copy.deepcopy(map)
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.guard = None
        for i in range(self.height):
            for j in range(self.width):
                if map[i][j] == '^':
                    self.guard = Guard('up', j, i)
                elif map[i][j] == '>':
                    self.guard = Guard('right', j, i)
                elif map[i][j] == 'v':
                    self.guard = Guard('down', j, i)
                elif map[i][j] == '<':
                    self.guard = Guard('left', j, i)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_guard(self):
        return self.guard

    def num_of_visited_positions(self):
        total = 0
        for row in self.map:
            for char in row:
                if char == 'X':
                    total += 1
        return total

    def update_map(self):
        new_map = [''] * self.height
        for i in range(self.height):
            for j in range(self.width):
                if self.guard.get_x() == j and self.guard.get_y() == i:
                    match (self.guard.get_orientation()):
                        case 'left':
                            new_map[i] += '<'
                        case 'right':
                            new_map[i] += '>'
                        case 'up':
                            new_map[i] += '^'
                        case 'down':
                            new_map[i] += 'v'
                elif self.map[i][j] == '<' or self.map[i][j] == '>' \
                     or self.map[i][j] == '^' or self.map[i][j] == 'v':
                    new_map[i] += 'X' # Since the guard's not here but used to be here
                else:
                    new_map[i] += self.map[i][j]
        self.map = new_map

    def guard_forward(self):
        match(self.guard.get_orientation()):
            case 'left':
                self.guard.move_x(-1)
            case 'right':
                self.guard.move_x(1)
            case 'up':
                self.guard.move_y(1)
            case 'down':
                self.guard.move_y(-1)

    def guard_right(self):
        self.guard.turn_right()

    def guard_move(self):
        x = self.guard.get_x()
        y = self.guard.get_y()
        match(self.guard.get_orientation()):
            case 'left':
                if (x - 1 >= 0 and self.map[y][x - 1] != '#') or x - 1 < 0:
                    self.guard_forward()
                else:
                    self.guard_right()
            case 'right':
                if (x + 1 < self.width and self.map[y][x + 1] != '#') or x + 1 >= self.width:
                    self.guard_forward()
                else:
                    self.guard_right()
            case 'up':
                if (y - 1 >= 0 and self.map[y - 1][x] != '#') or y - 1 < 0:
                    self.guard_forward()
                else:
                    self.guard_right()
            case 'down':
                if (y + 1 < self.height and self.map[y + 1][x] != '#') or y + 1 >= self.height:
                    self.guard_forward()
                else:
                    self.guard_right()
        self.update_map()

    def add_obstacle(self, x: int, y: int):
        assert isinstance(x, int) and 0 <= x < self.width, "x must be an integer and 0 <= x < map's width"
        assert isinstance(y, int) and 0 <= x < self.height, "y must be an integer and 0 <= y < map's height"
        self.map[y] = self.map[y][:x] + '#' + self.map[y][x + 1:]

    pass

with open('adventofcode_input.txt', 'r') as file:
    map_file = []
    for line in file:
        map_file.append(line.strip())
    map_obj = Map(map_file)
    guard = map_obj.get_guard()

    original_path = [] # To place obstacles

    while 0 <= guard.get_x() < map_obj.get_width() \
        and 0 <= guard.get_y() < map_obj.get_height():
        map_obj.guard_move()
        if 0 <= guard.get_x() < map_obj.get_width() \
        and 0 <= guard.get_y() < map_obj.get_height():
            original_path.append((guard.get_x(), guard.get_y()))

    # Remove all starting points from original path
    starting_point = original_path[0]
    original_path = original_path[1:]
    while starting_point in original_path:
        original_path.remove(starting_point)

    # Turn original_path into a set
    original_path = set(original_path)
    
    in_loop_count = 0
    print(f'Original path count: {len(original_path)}')
    counter = 1

    for point in original_path:
        test_map = Map(map_file)
        guard = test_map.get_guard()
        test_map.add_obstacle(point[0], point[1])
        while 0 <= guard.get_x() < test_map.get_width() \
                and 0 <= guard.get_y() < test_map.get_height() \
                and not guard.is_in_loop():
            test_map.guard_move()
            if guard.is_in_loop():
                in_loop_count += 1
        print(f'Point {counter} done! {in_loop_count} - {point}')
        counter += 1

    print(in_loop_count)
    pass