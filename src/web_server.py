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
        # Delete pass and write
        print('Delete this')
        pass

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        # Delete pass and write
        pass

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        # Read file off disk, to send
        # Store the content of the requested file in a temporary buffer
        # Delete pass and write
        pass

        # Send the HTTP response header line to the connection socket
        # Delete pass and write
        pass

        # Send the content of the requested file to the connection socket
        # Delete pass and write
        pass

    except IOError:
        # Send HTTP response message for file not found (404)
        # Delete pass and write
        pass

        # Open file, store the content of the requested file in a temporary buffer (variable).
        # Delete pass and write
        pass

        # Send the content of the requested file to the connection socket
        # Delete pass and write
        pass

    except:
        print("Bad request")
    finally:
        conn_socket.close()


def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_port = 6789

    # Bind the socket to server address and server port
    # Delete pass and write
    pass

    # Listen to at most 2 connection at a time
    # Server should be up and running and listening to the incoming connections
    # Delete pass and write
    pass

    threads = []
    try:
        while True:
            # Set up a new connection from the client
            # Delete pass and write
            pass

            # call handler here, start any threads needed
            # Delete pass and write
            pass

            # Just to keep track of threads
            threads.append(new_thread)
    except Exception as e:
        print("Exception occured (maybe you killed the server)")
        print(e)
    except:
        print("Exception occured (maybe you killed the server)")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
