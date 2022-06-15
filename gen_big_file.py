if __name__ == '__main__':
    with open("tests/big-test.txt", 'w') as h_file:
        h_file.write("123 " * 1000000)
