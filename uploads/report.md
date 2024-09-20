1. This report documents the successful setup and testing of both container-to-host and container-to-container communication using Podman. A web server and web client were configured in separate containers, and the communication was verified through browser access (container-to-host) and internal container requests (container-to-container).

2. Container-to-Host Communication
In this part, a web server container was exposed to the host via port 6789, allowing access from the host machine’s browser.

Web Server: A Python-based web server was set up in a container using port 6789 inside the container and mapped to port 6789 on the host. The web server could be accessed using http://localhost:6789 on the host machine.
Screenshot:

3. Container-to-Container Communication
For container-to-container communication, a separate container running a Python web client was used to query the web server running in another container. Both containers were connected to the same Podman bridge network (my-container-network) to facilitate direct communication.

Web Client: The client was configured to send an HTTP GET request to the web server by using its container name (web-server) and port 80.
This demonstrated successful communication between the two containers, showing that the client was able to connect to and receive responses from the server.

4. Summary of Setup
Web Server: A Python web server was built using the official python:3.10-slim image. The server listens on port 80 inside the container and was made accessible to the host by mapping port 80 to port 8080. The server container was part of a custom network, my-container-network.

Web Client: A Python web client container was built similarly to the server. It sends HTTP requests to the web server container using its container name and port 80. The client container was also connected to my-container-network for internal communication.

Networking: A custom bridge network (my-container-network) was created to allow communication between the containers. This network ensured that the containers could resolve each other's names and communicate directly over port 80.

5. Compose File Summary
A compose.yaml file was created to manage both services (web server and web client) and define the custom network. The Compose file ensured that both services were connected to the same network and that the server was accessible from the host.

The web server was exposed to the host on port 8080, and the web client container depended on the web server to ensure it started first for successful container-to-container communication.
