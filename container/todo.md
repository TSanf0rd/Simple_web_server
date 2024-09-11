* [ ] test singularity / apptainer on new virtual RDP systems on the Mill again.
* [ ] How to clean up and reduce size of container?

* [ ] Include X11 forwarding or SSH-X (differs by platform?) 
    * https://rs1.es/tutorials/2021/10/29/x11-forwarding-docker.html
    * https://rs1.es/tutorials/2021/08/18/how-to-add-a-desktop.html
    * https://stackoverflow.com/questions/44429394/x11-forwarding-of-a-gui-app-running-in-docker
    * https://dzone.com/articles/docker-x11-client-via-ssh
    * https://www.howtogeek.com/devops/how-to-run-gui-applications-in-a-docker-container/
    * https://superuser.com/questions/1202611/forward-x11-over-an-ssh-connection-to-containers-host
    * https://unix.stackexchange.com/questions/403424/x11-forwarding-from-a-docker-container-in-remote-server
    * In host on Mac: `docker run -it -e DISPLAY=<localhost_ip>:0 -v /tmp/.X11-unix:/tmp/.X11-unix`
    * In container: `dnf install qt5-qtbase wireshark -y && wireshark`
