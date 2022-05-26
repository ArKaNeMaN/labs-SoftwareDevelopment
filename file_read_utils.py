def read_line(h_file, with_comments=1):
    line = h_file.readline().strip()
    if line == '':
        return None

    # Skip comments
    if with_comments and (
            (line[0] == ';')
            | (line[0] == '#')
            | (line[:2] == '//')
    ):
        return ''

    return line


def read_matrix(file, sep=' '):
    h_file = open(file, 'r')
    if not h_file.readable():
        return []

    size = -1
    mat = []
    while 1:
        line = read_line(h_file, 0)

        if line is None:
            break

        if line == '':
            continue

        row = []
        for item in line.split(sep):
            item = item.strip()
            if item != '':
                row.append(int(item))

        if size < 0:
            size = len(row)
        elif size != len(row):
            print(f"Invalid matrix row size {len(row)}, expected {size}.")
            return []

        mat.append(row)

    h_file.close()
    return mat


def write_matrix_as_csv(file, mat):
    h_file = open(file, 'w')
    if not h_file.writable():
        return 0

    for row in mat:
        for i in range(len(row)):
            row[i] = str(row[i])
        h_file.write(';'.join(row) + '\n')

    h_file.close()
    return 1


def parse_csv_line(line):
    return line.split(';')


def read_csv(file, with_header=1):
    h_file = open(file, 'r')
    if not h_file.readable():
        return []

    header = []
    rows = []
    while 1:
        line = read_line(h_file, 0)

        if line is None:
            break

        if line == '':
            continue

        cells = parse_csv_line(line)
        if with_header:
            if len(header) < 1:
                header = cells
            else:
                row = {}
                for i in range(len(header)):
                    row[header[i]] = cells[i]
                rows.append(row)
        else:
            rows.append(cells)

    h_file.close()

    return rows


def read_graph_as_list_to_matrix(file):
    h_file = open(file, 'r')
    if not h_file.readable():
        return []

    size = -1
    graph = []
    while 1:
        line = read_line(h_file, 1)

        if line is None:
            break

        if line == '':
            continue

        if size < 0:
            size = int(line)
            for x in range(size):
                row = []
                for y in range(size):
                    row.append(0)
                graph.append(row)
            continue

        cells = line.split(' ')
        x = int(cells[0].strip())
        y = int(cells[1].strip())
        if x >= size or y >= size:
            print("Invalid graph...")
            return []

        if len(cells) > 2:
            w = int(cells[2].strip())
        else:
            w = 1

        graph[x][y] = w

    h_file.close()
    return graph


if __name__ == '__main__':
    write_matrix_as_csv("./tests/mat.csv", read_matrix('./tests/mat.txt'))

    print("Matrix:")
    print(read_matrix('./tests/mat.txt'))
    print("")

    print("Matrix (from csv):")
    print(read_csv("./tests/mat.csv", 0))
    print("")

    print("Some data from CSV (with header):")
    print(read_csv("./tests/test.csv", 1))
    print("")

    print("Graph:")
    print(read_graph_as_list_to_matrix("./tests/graph.txt"))
    print("")
