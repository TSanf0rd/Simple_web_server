# Easy development container
This repository offers an easy-to-use environment setup for programming assignments.
It can be used in conjunction with:

* https://github.com/redkyn/assigner
* https://git-classes.mst.edu (or any gitlab instance), and 
* https://gitlab.com/classroomcode/grade-sh/grade-sh

## Install Podman or Docker
Docker and Podman are two containerization suites that both support Open Container Initiative (OCI) containers.
Docker is more popular, but Podman is better engineered.
Virtually all their sub-commands are the same, so learning one will teach you the other.

### Linux/Unix
If you are on Linux/Unix, then you should likely use `podman` or `docker` in the host system repositories,
and not install based on the versions present on their websites.
For example, on Fedora do this:

```
sudo dnf install podman podman-compose
```

or: 

```
sudo dnf install docker docker-compose
```

### Mac
If you are on Mac, then see the instructions here:

https://podman.io/docs/installation

or:

https://docs.docker.com/get-docker/

### Windows
If you are on Windows, first install:
https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux

To do so, run Windows Powershell as administrator, and within it type this:
```
wsl --install
```
Then you can install containerization in one of three ways,
in order of your likely preference:

1. Within the WSL pseudo-Ubuntu install itself -- Install with: `sudo apt update && sudo apt install docker docker-compose podman*`.
2. Within a full Linux VM -- Use the commands as above for Linux install. While this could work, it will not be as fast or easy as WSL.
3. In your Windows host itself -- Download from the urls above listed for Mac install. While podman and docker will run this way, `git clone` on Windows host will break repositories by injecting Windows newlines into them...

## Test running a basic container works
After installing `podman` or `docker`, open a terminal, and then run:
```
podman run --interactive --tty --rm fedora
```
or: 
```
sudo docker run --interactive --tty --rm fedora
```

Confirm that it worked, and you're in a Fedora container:

`cat /etc/os-release`

Then, to leave the container, type:

`exit`

Note:
For all of the following command examples, depending on your machine,
you could replace `podman` with `sudo docker`, and the command should work identically.
I suggest `podman`, because it is better engineered, but you can choose either.

## Running the remote pre-built image
If you are on an x86-64 architecture,
you can just pull a pre-built image.
Run the following command from the root directory of your Git repository:

```
podman run --interactive --tty --rm --mount type=bind,source="$(pwd)"/,target=/your_code --workdir=/your_code git-docker-classes.mst.edu/containers/container fish
```

I suggest the `fish` shell, but you can run whichever shell you like,
by changing the last part of the command.

Your repository files are mounted inside the following directory:

`/your_code/`

## Building and running the image locally (optional)
If you are not on an x86-64 architecture,
or are curious, or are security-conscious,
you may want to build the image yourself.
From within the `container` repository directory 
(usually a Git sub-module of your assignment), execute:

```
podman build --tag container .
```

Then, you can run the image you built locally.
From the root directory of your assignment Git repository,
or any directory that you would like to mount in a container, execute:

```
podman run --interactive --tty --rm --mount type=bind,source="$(pwd)"/,target=/your_code --workdir=/your_code container fish
```

Your files will be mounted inside the container,
in the following directory:

`/your_code/`

## Campus Linux Machines (rootless container)
If you use `ssh` (via putty or otherwise) to access the campus Linux machines,
then you will need to run a rootless container option.
First type `cd` to head to your home directory, then type:

```
singularity shell docker://git-docker-classes.mst.edu/containers/container
```
or:
```
apptainer shell docker://git-docker-classes.mst.edu/containers/container
```

After that, your entire home directory should be accessible from the container.

## Networking containers
To expose a port, for example 6789:
```
podman run --interactive --tty --rm -p 6789 --mount type=bind,source="$(pwd)"/,target=/your_code --workdir=/your_code git-docker-classes.mst.edu/containers/container fish
```

Or, more verbosely using the long syntax format (which may not work on old versions of podman/docker), for example when exposing port 6789:
```
podman run --interactive --tty --publish target=6789,published=127.0.0.1:6789,protocol=tcp --mount type=bind,source="$(pwd)"/,target=/your_code --workdir=/your_code git-docker-classes.mst.edu/containers/container fish
```

This allows you to access network programs or services running within the container,
from your host.
For example, you could connect a web browser in the host,
to a web server in the container.

To get two containers connected together, you can create a network, and launch them both with it:
```
# If you don't see a podman network, then create it:
podman network ls 

# This part may already done by default on some platforms
podman create network -d bridge podman  

# Launch one or many containers on the same network:
podman run --interactive --tty --network=podman --mount type=bind,source="$(pwd)"/,target=/your_code --workdir=/your_code git-docker-classes.mst.edu/containers/container fish
```

Podman also offers pods, which allow containers to network together.

## Docker Compose
If you would like to launch your runtime configuration from a `compose.yaml` file, 
then run the following to enter a shell:
```
podman-compose run --rm programming`
```

If you would like the jupyter notebooks containerized for CS5700, then run:
```
podman-compose up --detach jupyter
```
Then, connect to the notebook at `http://localhost:8888`.
Be sure to modify the compose file to point towards your *sequence-informatics* folder.

Notes:
`sudo docker-compose` is the Docker alternative.
On some systems, `sudo docker-compose` may be `sudo docker compose`.

# Want to learn all about containers?
Only install code locally ;)
https://www.youtube.com/watch?v=J0NuOlA2xDc

## Containers broadly:
https://en.wikipedia.org/wiki/OS-level_virtualization

https://en.wikipedia.org/wiki/Open_Container_Initiative

## Learn Podman
Podman is a better-engineered containerization suite compatible with OCI containers and Docker.
It's commands are mostly the same as Docker's.

https://docs.podman.io/en/latest/

## Learn Docker
https://en.wikipedia.org/wiki/Docker_(software)

Read the following:
https://docs.docker.com/get-started/overview/

Do this tutorial:
https://www.docker.com/101-tutorial/

Read the networking sub-sections of the documentation:
https://docs.docker.com/network/

Skim the API reference:
https://docs.docker.com/engine/reference/

For example, Dockerfiles, which specify how to build a container:
https://docs.docker.com/engine/reference/builder/

Or, docker run, which runs containers:
https://docs.docker.com/reference/cli/docker/container/run/
https://docs.docker.com/engine/reference/run/

Or, compose files, which are kind of like Makefiles for running multiple docker containers:
https://docs.docker.com/compose/ 
and 
https://docs.docker.com/compose/compose-file/

## Learn Singularity
You may prefer singularity / apptainer if you need to do HPC work,
or you are working on the campus virtual Linux machines:

https://en.wikipedia.org/wiki/Singularity_(software)

https://apptainer.org/user-docs/master/introduction.html

## Maintenance
If you maintain or update this container:

### Adding this submodule to your repo
If you, as an assignment developer or repository owner,
want to add this submodule to your repo, then:

`git submodule add https://git-classes.mst.edu/containers/container/`

### Adding software
The container image is hosted on git-docker-classes.mst.edu.
You could host such an image at any container registry.
The software in the image can be changed or updated.
After you have created a token in the gitlab web interface,
which will be required to copy-paste as your password,
I push a new locally built container to the registry via:

```sh
podman login git-docker.mst.edu
podman build -t git-docker.mst.edu/os/container .
podman push git-docker.mst.edu/os/container
```

If you were to do the same for your own hosted image, 
then the url would differ.
