#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Run with the following command line parameters:
python3 client_browser.py <hostname> <port> <file>

Examples:
$ python3 client_browser.py info.cern.ch 80 "" # defaults to index.html
$ python3 client_browser.py localhost 6789 "hello_world.html"
"""

import sys
import socket

if len(sys.argv) != 4:
    server_hostname = "localhost"
    server_ip = "127.0.0.1"
    server_port = 6789
    file_name = "web_files/hello_world.html"
else:
    # Delete the pass and do your arg parsing here.
    # Hint, you may need to get an IP from a hostame.
    pass

try:
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # Delete the pass and make your GET request here
    pass

    # Delete the pass and parse the return data here.
    # Hint: a loop helps to make sure you got all the data.
    # Just print what's returned from the server.
    pass

except Exception as e:
    print("Exception was: ", e)

finally:
    client_socket.close()
