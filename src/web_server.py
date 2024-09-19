#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A simple Web server.
GET requests must name a specific file,
since it does not assume an index.html.
"""

import socket
import threading


def handler(conn_socket: socket.socket, address: tuple[str, int]) -> None:
    """
    Handles the part of the client work-flow that is client-dependent,
    and thus may be delayed by the user, blocking program flow.
    """
    try:
        # Receives the request message from the client
        request = conn_socket.recv(1024).decode()
        print(f"Received request from {address}:\n{request}")

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        request_line = request.splitlines()[0]  # First line is the request line
        filename = request_line.split()[1]  # Second part is the path

        # Because the extracted path of the HTTP request includes
        # a character '/', we read the path from the second character
        if filename == "/":
            filename = "/web_files/hello_world.html"  # Default to index.html if no specific file requested

        # Read file off disk, to send
        file_path = "." + filename  # Assuming the current directory holds files
        print(f"Serving file from path: {file_path}")
        with open(file_path, "rb") as f:
            response_body = f.read()

        # Send the HTTP response header line to the connection socket
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Type: text/html\r\n"
        response_header += f"Content-Length: {len(response_body)}\r\n\r\n"
        conn_socket.sendall(response_header.encode())

        # Send the content of the requested file to the connection socket
        conn_socket.sendall(response_body)

    except IOError:
        # Send HTTP response message for file not found (404)
        response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
        conn_socket.sendall(response_header.encode() + response_body)

    except Exception as e:
        print(f"Bad request from {address}: {e}")

    finally:
        conn_socket.close()


def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_port = 6789

    # Bind the socket to server address and server port
    server_socket.bind(("0.0.0.0", server_port))

    # Listen to at most 2 connection at a time
    # Server should be up and running and listening to the incoming connections
    server_socket.listen(2)
    print(f"Server started on port {server_port}, listening for connections...")

    threads = []
    try:
        while True:
            # Set up a new connection from the client
            conn_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # call handler here, start any threads needed
            new_thread = threading.Thread(
                target=handler, args=(conn_socket, client_address)
            )
            new_thread.start()

            # Just to keep track of threads
            threads.append(new_thread)
    except Exception as e:
        print("Exception occurred (maybe you killed the server)")
        print(e)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
