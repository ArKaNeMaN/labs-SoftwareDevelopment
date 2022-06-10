import xmlrpc.client

if __name__ == '__main__':
    proxy = xmlrpc.client.ServerProxy("http://localhost")

    matrix = proxy.read_matrix('./tests/mat.txt')
    proxy.write_matrix_as_csv("./tests/mat.csv", matrix)

    print("Matrix:")
    print(proxy.read_matrix('./tests/mat.txt'))
    print("")

    print("Matrix (from csv):")
    print(proxy.read_csv("./tests/mat.csv"))
    print("")

    print("Some data from CSV:")
    print(proxy.read_csv("./tests/test.csv"))
    print("")

    print("Matrix (int list):")
    print(proxy.read_int_list("./tests/mat.txt"))
    print("")
