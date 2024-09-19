#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A simple Web server.
GET requests must name a specific file,
since it does not assume an index.html.
"""

import socket
import threading
import os

# Handler function, which manages a single client's request. The function takes two arguments conn_socket and address
# conn_socket:the connection socket through which commuication with the client happens
# address: A tuple containing the IP adress and port of the client
def handler(conn_socket: socket.socket, address: tuple[str, int]) -> None:
    """
    Handles the part of the client work-flow that is client-dependent,
    and thus may be delayed by the user, blocking program flow.
    """
    """
    conn_socket.recv(1024).decode(): Recieves up to 1024 bytes from the client through the socket. Assume that the HTTP request will fit within this size.
    .decode()": Convets the recieved bytes into a string (assumed to be UTF-8 encoded
    print(f"Recevied request..."): Logs the recieved request along with the client address for debugging
    """

    try:
        # Receives the request message from the client
        request = conn_socket.recv(1024).decode()
        print(f"Received request from {address}:\n{request}")

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        """
        request.splitline()[0]: The HTTP request has multiple lines. This extracts the first line (called the request line), which contains the HTTP method, the requested file path an the HTTP method, the requested file path, and the HTTP version
        """
        request_line = request.splitlines()[0]  # First line is the request line
        filename = request_line.split()[1]  # Second part is the path

        # Handle root path by redirecting to a default file
        # if filename == "/":
        # filename = "/hello_world.html"  # Default file
        filename = filename.lstrip("/")
        # Determine file path to serve
        file_path = (
            "../tests/" + filename
        )  # Construct file path from current directory
        print(f"Serving file from path: {file_path}")
        print(f"Serving file from absolute path: {os.path.abspath(file_path)}")

        # Check for the file's MIME type (for the sake of this example, we'll handle HTML only)
        if filename.endswith(".html"):
            content_type = "text/html"
        else:
            content_type = "application/octet-stream"

        # Read file off disk, to send
        with open(file_path, "rb") as f:
            response_body = f.read()

        # Send the HTTP response header line to the connection socket
        response_header = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(response_body)}\r\n\r\n"
        conn_socket.sendall(response_header.encode())

        # Send the content of the requested file to the connection socket
        conn_socket.sendall(response_body)

    except IOError:
        # Send custom HTTP response message for file not found (404)
        response_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response_body = b"""
        <!DOCTYPE html>
        <html>
          <head>
            <title>Page not found!!</title>
          </head>
          <body>
            <h1>404 Page Not Found</h1>
            <p1>Sorry, the page you're looking for does not exist.</p>
          </body>
        </html>
        """
        conn_socket.sendall(response_header.encode() + response_body)

    except Exception as e:
        print(f"Bad request from {address}: {e}")

    finally:
        conn_socket.close()


def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

            # Call handler here, start any threads needed
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
