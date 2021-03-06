import itertools
import time
from ctypes import *


def line_is_comment(line):
    return (line[0] == ';') | (line[0] == '#') | (line[:2] == '//')


def file_foreach_line(filename, callback, with_comments=False):
    with open(filename, 'r') as h_file:
        return list(filter(
            lambda line: not (line is None),
            map(
                lambda line: None if ((with_comments and line_is_comment(line)) or line == '') else callback(line),
                h_file
            )
        ))


def read_csv(file):
    return file_foreach_line(file, lambda line: line.split(';'), False)


def write_matrix_as_csv(file, mat):
    with open(file, 'w') as h_file:
        [h_file.write(';'.join([str(cell) for cell in row]) + '\n') for row in mat]
    return 0


def read_matrix(file):
    return file_foreach_line(
        file,
        lambda line: list(filter(
            lambda cell: not (cell is None),
            map(lambda cell: None if cell.strip() == '' else int(cell.strip()), line.split(' '))
        ))
    )


def merge_lists(lists):
    return list(itertools.chain.from_iterable(lists))


def read_int_list(file):
    return merge_lists(read_matrix(file))


def read_int_list_c(file):
    dll = cdll.LoadLibrary("liblab_SoftwareDevelopment_dll.dll")

    print("\n")
    dll.hello()
    print(dll.sum(2, 5))

    dll.read_int_list.restype = c_int64
    dll.read_int_list.argtypes = [c_char_p]

    res = dll.read_int_list(file.encode('utf-8'))

    size = c_int64.from_address(res).value
    print('size = ', size)
    res += 8

    lst = []
    for i in range(size):
        lst.append(c_int64.from_address(res + (8 * i)).value)

    return lst


if __name__ == '__main__':
    st_time = time.perf_counter()
    read_int_list_c('tests/big-test.txt')
    print('С++:', time.perf_counter() - st_time)

    st_time = time.perf_counter()
    read_int_list('tests/big-test.txt')
    print('Python:', time.perf_counter() - st_time)

    # write_matrix_as_csv("./tests/mat.csv", read_matrix('./tests/mat.txt'))
    #
    # print("Matrix:")
    # print(read_matrix('./tests/mat.txt'))
    # print("")
    #
    # print("Matrix (from csv):")
    # print(read_csv("./tests/mat.csv"))
    # print("")
    #
    # print("Some data from CSV:")
    # print(read_csv("./tests/test.csv"))
    # print("")
    #
    # print("Matrix (int list):")
    # print(read_int_list("./tests/mat.txt"))
    # print("")
