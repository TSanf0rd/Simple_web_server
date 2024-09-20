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
    # shows the what is in use by the user and provies 3 arguments
    # Check if correct number of arguments is provided
    # if len(sys.argv) < 3:
    # print("Usage: python3 client_browser.py <hostname> <port> <file>")
    # sys.exit(1)

    # Extract command-line arguments
    # Extract the hostname and port fromt the command-line arguments(sys.argv)
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])

    # Default to requesting root ("/") if no filename is provided
    # check: Third argument (file name is provided) if not default to ("")
    file_name = sys.argv[3] if len(sys.argv) > 3 else ""

    # Convert hostname to IP address
    # Attempt to resolve the hostname to an IP address. If it fails, it prints an error and exits
    try:
        server_ip = socket.gethostbyname(server_hostname)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {server_hostname}")
        sys.exit(1)

    try:
        # Create a TCP socket and allows the client to connect to the server
        client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Client connects to the server using IP and port
        client_socket.connect((server_ip, server_port))
        # print(f"Connected to {server_hostname} ({server_ip}) on port {server_port}")

        # If file_name is empty, default to "/"
        if file_name == "":
            file_name = "/"

        # Ensure that the file name starts with a single slash
        if not file_name.startswith("/"):
            file_name = "/" + file_name

        # Construct the HTTP GET request for Debugging
        request_line = f"GET {file_name} HTTP/1.1\r\n"
        headers = f"Host: {server_hostname}\r\nConnection: close\r\n\r\n"
        http_request = request_line + headers

        # Send the HTTP GET request
        client_socket.sendall(http_request.encode())
        # print(f"Sent request:\n{http_request}")

        # client reads the server's response in chunks of 1024 bytes and appends it to response.
        # Continues until no more data is recieved.
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # Print the server's response
        # print("Response from server:")
        print(response.decode())

    except (
        Exception
    ) as e:  # Catch any execeptions during the conncectin or data transfer
        print("Exception occurred:", e)

    finally:
        # Close the socket after sending the request and receiving the response
        client_socket.close()


# Entry point to run the main function
if __name__ == "__main__":
    main()
