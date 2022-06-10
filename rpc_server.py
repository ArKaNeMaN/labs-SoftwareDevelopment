from xmlrpc.server import SimpleXMLRPCServer
import file_read_utils

if __name__ == '__main__':

    server = SimpleXMLRPCServer(("localhost", 80))
    print("Started RPC server on http://localhost:80...")

    server.register_function(file_read_utils.read_matrix, "read_matrix")
    server.register_function(file_read_utils.read_csv, "read_csv")
    server.register_function(file_read_utils.read_int_list, "read_int_list")
    server.register_function(file_read_utils.write_matrix_as_csv, "write_matrix_as_csv")

    server.serve_forever()
