* [ ] TODO delete general autograding stuff, pulling anything good to git_autograding.md

# Programming assignment 1 (pa01)
Welcome to the World Wide Web (HTTP)

![](ithinkthereforeiam.png)

## Deliverables
* `web_server.py`
* `iactuallytestedthis-containerserver-hostbrowser.png`
* `iactuallytestedthis-containerclient-containerserver.png`
* `client_browser.py`
* `report.md`

## Summary
* The first assignment should have been performed in full VMs.
This assignment should be performed in containers.
* Finish / fill in your python server `web_server.py`.
* Write the client `client_browser.py`.
* Test the code in networked containers.
* Include screenshots of you how you ran the code,
with your web browser and termials displaying the results in two containers.
* All source and text files should be utf-8 with Unix delimiters, written in Python3.

## Grading
In the container itself, run the grade script via:

`bash grade.sh`

The `grade.sh` script is not intended to be run WSL, Mac's zsh terminal, etc.,
but instead, only in actual Linux, like the Fedora container or VM.

Open it to see what commands we run,
and run them yourself manually!

Note:
The grade script is not intended to be run in WSL, Git-Bash, or a Mac host,
but instead in an actual Linux VM or container.

## Hints
* To debug your web server, open a browser, have it visit your server.
* To debug your web client, have it actually "visit" a real website.
* You can have Wireshark in your host watch ports in the container by publishing those ports.
* Only after debugging each with a known correct server/client,
should you test them against each other!
* Only after testing them against each other in a single container, 
should you test them between containers.
* Have fun!

If you want to test a browser in the container without a GUI, 
then you can either use `curl` or `wget`, 
or use another command line browser:
* https://daniel.haxx.se/docs/curl-vs-wget.html
* https://www.brow.sh/
* `lynx -vikeys`
* `w3m`
* `links`
* `elinks`

## Part 0: Containers

### Get a containerization suite running an configured, and learn it:
See the `containers/` directory in this repository.
It has scripts to install everything you need to run a container.
Read the README.md file in this sub-directory and follow the instructions!
There is a section on learning containerization.

This directory is a git sub-module:
https://git-scm.com/book/en/v2/Git-Tools-Submodules

When you do clone, please clone as follows:
`git clone --recurse-submodules <yourlink>`

## Part 1: You code a simple Web server
In this lab, you will learn the basics of socket programming for TCP connections in Python.
You will create a socket, bind it to a specific address and port, 
as well as send and receive HTTP packets.
You will also learn some basics of the HTTP header format.
You will develop a web server that handles client requests.
Your web server should:
* accept and parse the HTTP request, 
* get the requested file from the server's file system, 
* create an HTTP response message consisting of the requested file preceded by header lines, and then 
* send the response directly to the client.
* If the requested file is not present in the server, 
then the server should send an HTTP "404 Not Found" back to the client.

### Code
Read the skeleton code for the Web server in the repository.
Complete the skeleton code.
The places where you need to fill in code are marked with `pass`.
Each place may require one or more lines of code.

### Running the Server
There are some an HTML files in the `web_files/` directory,
e.g., `web_files/hello_world.html`.
Run the server program.
Observe it's funtionality in a web browser.
To do so, visit this in the web browser:

`http://localhost:6789/web_files/hello_world.html`

Or this (Windows host may not like this one):

`http://127.0.0.1:6789/web_files/hello_world.html`

Note also the use of the port number after the colon (:).
You need to replace this port number with whatever port you have used in the server code.
In the above example, we have used the port number 6789.
The real browser should then display the contents of `web_files/hello_world.html`.
If you omit ":6789", the browser will assume port 80,
and you will get the web page from the server,
only if your server is listening at port 80.
Then change the url to get a file that is not present at the server. 
You should get a "404 Not Found" message, 
and return the 404 file.

This first part will get you some points,
independent of whether you complete the next section!

## Part 2: Multi-thread the server
Use multithreading on your server,
so that is capable of serving multiple requests simultaneously.
Using threading, first create a main thread in which your modified server listens for clients at a fixed port.
When it receives a TCP connection request from a client,
it will set up the TCP connection to service the client request in a separate thread.
There will be a separate TCP connection in a separate thread for each request/response pair.

## Part 3: You code a simple Web browser
Instead of using a browser,
write your own HTTP client to test your server,
and query various websites.
Your client will connect to a server using a TCP connection,
send an HTTP request to a server,
and display the server response as an output.
You can assume that the HTTP request sent is a GET method.
The client should take command line arguments,
specifying the server IP address or host name,
the port at which the server is listening,
and the path at which the requested object is stored at the server.
The following is an input command format to run the client.

`client_browser.py server_host server_port filename`

It should be able to work with real http websites, on the actual internet too!

## Part 4: Test networking between containers
* Using a browser in your host, query the web-server while it is running in a container.
You will need to `--publish` ports in the container to do this.
This is your first screenshot.
* Using the web-server in one container, query it using the python web client you wrote in another container.
To do this, you should create a container-specific virtual network to allow each container to see each other. 
This is your second screenshot.

## Part 5: Compose file
Background: 
Actually read the reading on compose files in the container sub-repo.
See the `containers/` submodule for an example.

Deliverables:
One `compose.yaml` that has two services,
one for each of the above tasks (`container<->host` and `container<->container` networks), 
and specifies the network itself in the compose file.

## Part 6: Write up
Write a `report.md` which includes:
* Screenshots of the demonstration of the container-host and container-container communication.
* Summary of your setup.
