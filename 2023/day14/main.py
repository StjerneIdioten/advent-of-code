from pathlib import Path

start_rock_map = list(map(list, zip(*[line.rstrip('\n') for line in open(Path(__file__).parent / "test").readlines()])))

def roll(rock_map):
    for row_idx, row in enumerate(rock_map):
        roll_spot = 0
        for col_idx, col in enumerate(row):
            if col == 'O':
                rock_map[row_idx][col_idx] = '.'
                rock_map[row_idx][roll_spot] = 'O'
                roll_spot += 1
            elif col == '#':
                roll_spot = col_idx + 1
    return rock_map


def print_matrix(matrix):
    for row in matrix:
        print(row)


def cycle(rock_map):
    north = roll(rock_map)
    

rocks_rolled_north = roll(start_rock_map)
total_sum = 0
for rock_lane in rocks_rolled_north:
    for tile_idx, tile in enumerate(rock_lane):
        if tile == 'O':
            total_sum += len(rock_lane) - tile_idx
print(total_sum)
cycle(start_rock_map)