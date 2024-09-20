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
        request = conn_socket.recv(1024).decode()  # decode bytes to string
        print(f"Received request from {address}:\n{request}")

        # Extract the path of the requested object from the message
        filepath = request.split()[1]  # Second part is the path (requested file)

        # If the requested file is '/', return index.html by default
        if filepath == "/":
            filepath = "tests/web_files/index.html"

        # Read the requested file from the disk
        with open(filepath[1:], "rb") as f:  # open file in binary mode to get bytes
            response_body = f.read()  # read 404 page

        # Construct the response header
        response_header = "HTTP/1.1 200 OK\r\n\r\n"

        # Send the response header and body to the client
        conn_socket.sendall(response_header.encode())  # encode header to bytes
        conn_socket.sendall(response_body)  # response_body is already bytes

    except FileNotFoundError:
        # Handle file not found case (404)
        try:
            # Open 'not_found.html' in binary mode to return its content
            with open("tests/web_files/not_found.html", "rb") as file:
                response_body = file.read()  # content is bytes

            # Create a response header for 404 error
            response_header = "HTTP/1.1 404 Not Found\r\n\r\n"

            # Send the HTTP response header and body
            conn_socket.sendall(response_header.encode())  # header encoded to bytes
            conn_socket.sendall(response_body)  # response_body is already bytes

        except FileNotFoundError:
            # If the 'not_found.html' itself doesn't exist, send a basic 404 response
            response_body = (
                b"<html><body><h1>404 Not Found</h1></body></html>"  # bytes object
            )
            response_header = "HTTP/1.1 404 Not Found\r\n"
            conn_socket.sendall(response_header.encode())  # encode header to bytes
            conn_socket.sendall(response_body)  # response_body is already bytes

    except Exception as e:
        print(f"Bad request from {address}: {e}")

    finally:
        # Close the connection socket after sending the response
        conn_socket.close()


# Main function to start the server
def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # Reuse the socket
    server_port = 6789

    # Bind the socket to server address and server port
    server_socket.bind(("0.0.0.0", server_port))

    # Listen for up to 2 connections at a time
    server_socket.listen(2)
    print(f"Server started on port {server_port}, listening for connections...")

    threads = []
    try:
        while True:
            # Accept new client connections
            conn_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Start a new thread to handle the client
            new_thread = threading.Thread(
                target=handler, args=(conn_socket, client_address)
            )
            new_thread.start()

            # Keep track of threads
            threads.append(new_thread)

    except Exception as e:
        print("Exception occurred (maybe you killed the server)")
        print(e)
    finally:
        # Close the server socket when done
        server_socket.close()


# Run the server if this script is executed directly
if __name__ == "__main__":
    main()
