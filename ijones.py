from collections import defaultdict


def get_paths_number(corridor: list, height: int, width: int) -> int:
    solutions_in_line = [0] * height
    endpoints = set()
    plates_visited_count = defaultdict(int)

    for i in (0, height - 1):
        endpoint_plate = corridor[i][width - 1]
        solutions_in_line[i] = 1
        endpoints.add(endpoint_plate)
        plates_visited_count[endpoint_plate] += 1

    for j in range(width - 2, -1, -1):
        current_column_paths_count = defaultdict(int)

        for i in range(height):
            plate = corridor[i][j]
            if plate not in endpoints and solutions_in_line[i] == 0:
                continue
            plate_solution_count = plates_visited_count[plate]

            if plate is not corridor[i][j + 1]:
                plate_solution_count += solutions_in_line[i]

            solutions_in_line[i] = plate_solution_count
            current_column_paths_count[plate] += plate_solution_count

        for plate_key in current_column_paths_count:
            endpoints.add(plate_key)
            plates_visited_count[plate_key] += current_column_paths_count[plate_key]

    return sum(solutions_in_line)


def main(IN_FILE, OUT_FILE) -> int:
    with open(IN_FILE, 'r') as in_file:
        in_data = in_file.readlines()
    width, height = map(int, in_data[0].split(' '))
    corridor = [in_data[line].rstrip('\n') for line in range(1, height + 1)]

    paths_number = get_paths_number(corridor, height, width)

    with open(OUT_FILE, 'w') as file:
        file.write(str(paths_number))

    print(paths_number)
    return paths_number


if __name__ == '__main__':
    main('ijones.in', 'ijones.out')
