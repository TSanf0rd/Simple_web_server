#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Run with the following command line parameters:
python3 client_browser.py <hostname> <port> <file>

Examples:
$ python3 client_browser.py info.cern.ch 80 ""  # defaults to index.html
$ python3 client_browser.py localhost 6789 "hello_world.html"
"""

import sys
import socket


def main() -> None:
    # Default values for hostname, port, and file if arguments are not provided
    if len(sys.argv) != 4:
        server_hostname = "localhost"
        server_ip = "127.0.0.1"
        server_port = 6789
        file_name = "web_files/hello_world.html"
    else:
        # Extract command-line arguments
        server_hostname = sys.argv[1]
        server_port = int(sys.argv[2])
        file_name = sys.argv[3]

        # Convert hostname to IP address
        try:
            server_ip = socket.gethostbyname(server_hostname)
        except socket.gaierror:
            print(f"Error: Unable to resolve hostname {server_hostname}")
            sys.exit(1)

    try:
        # Create a TCP socket
        client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Connect to the server using IP and port
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_hostname} ({server_ip}) on port {server_port}")

        # Construct the HTTP GET request
        request_line = f"GET /{file_name} HTTP/1.1\r\n"
        headers = f"Host: {server_hostname}\r\nConnection: close\r\n\r\n"
        http_request = request_line + headers

        # Send the HTTP GET request
        client_socket.sendall(http_request.encode())
        print(f"Sent request:\n{http_request}")

        # Receive the response from the server
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # Print the server's response
        print("Response from server:")
        print(response.decode())

    except Exception as e:
        print("Exception was:", e)

    finally:
        # Close the socket after sending the request and receiving the response
        client_socket.close()


# Entry point to run the main function
if __name__ == "__main__":
    main()
