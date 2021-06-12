![alt tag](https://github.com/GoVanguard/legion/blob/master/images/LegionBanner.png)
[![Build Status](https://travis-ci.com/GoVanguard/legion.svg?branch=master)](https://travis-ci.com/GoVanguard/legion)
[![Known Vulnerabilities](https://snyk.io/test/github/GoVanguard/legion/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/GoVanguard/legion?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e33e52aab8f49cdcd02/maintainability)](https://codeclimate.com/github/GoVanguard/legion/maintainability)
![Linter](https://img.shields.io/badge/linter-flake8-brightgreen)
[![Analytics](https://ga-beacon-gvit.appspot.com/UA-126307374-3/legion/readme)](https://github.com/GoVanguard/legion)



## ABOUT
Legion, a fork of SECFORCE's Sparta, is an open source, easy-to-use, super-extensible and semi-automated network 
penetration testing framework that aids in discovery, reconnaissance and exploitation of information systems. 
[Legion](https://govanguard.com/legion) is developed and maintained by [GoVanguard](https://govanguard.com). 
More information about Legion, including the [roadmap](https://govanguard.com/legion), can be found on it's project 
page at [https://GoVanguard.com/legion](https://govanguard.com/legion).
If you are interested in contributing to Legion, join our [Legion Keybase Team](https://keybase.io/team/govanguard.dev.legion).

### FEATURES

* Automatic recon and scanning with NMAP, whataweb, nikto, Vulners, Hydra, SMBenum, dirbuster, sslyzer, webslayer 
and more (with almost 100 auto-scheduled scripts).
* Easy to use graphical interface with rich context menus and panels that allow pentesters to quickly find and 
exploit attack vectors on hosts.
* Modular functionality allows users to easily customize Legion and automatically call their own scripts/tools.
* Highly customizable stage scanning for ninja-like IPS evasion.
* Automatic detection of CPEs (Common Platform Enumeration) and CVEs (Common Vulnerabilities and Exposures).
* Ties CVEs to Exploits as detailed in Exploit-Database.
* Realtime autosaving of project results and tasks.

### NOTABLE CHANGES FROM SPARTA

* Refactored from Python 2.7 to Python 3.6 and the elimination of deprecated and unmaintained libraries.
* Upgraded to PyQT5, increased responsiveness, less buggy, more intuitive GUI that includes features like:
   * Task completion estimates
   * 1-Click scan lists of ips, hostnames and CIDR subnets
   * Ability to purge results, rescan hosts and delete hosts
   * Granular NMAP scanning options
* Support for hostname resolution and scanning of vhosts/sni hosts.
* Revise process queuing and execution routines for increased app reliability and performance.
* Simplification of installation with dependency resolution and installation routines.
* Realtime project autosaving so in the event some goes wrong, you will not lose any progress!
* Docker container deployment option.
* Supported by a highly active development team.

### GIF DEMO 
![](https://govanguard.com/wp-content/uploads/2019/02/LegionDemo.gif)

## INSTALLATION

It is preferable to use the docker image over a traditional installation. This is because of all the dependancy 
requirements and the complications that occur in environments which differ from a clean, non-default installation.

NOTE: Docker versions of Legion are *unlikely* to work when run as root or under a root X!

### Supported Distributions
#### Docker runIt script

RunIt supports Ubuntu 18, Fedora 30, Parrot and Kali at this time. It is possible to run the docker image on any 
Linux distribution, however, different distributions have different hoops to jump through to get a docker app to 
be able to connect to the X server. Everyone is welcome to try to figure those hoops out and create a PR for runIt. 

#### Traditional Install

We can only promise correct operation on Ubuntu 18 using the traditional installation at this time. While it should 
work on ParrotOS, Kali and others, until we have Legion packaged and placed into the repos for each of these distros, 
it's musical chairs with regards to platform updates changing and breaking dependencies.

### DOCKER METHOD
------

Linux with Local X11:

 - Assumes Docker and X11 are installed and setup (including running docker commands as a non-root user).
 - It is critical to follow all the instructions for running as a non-root user. Skipping any of them will result in 
 complications getting docker to communicate with the X server.
 - See detailed instructions to setup docker [here](#docker-setup) and enable running containers as non-root users 
 and granting docker group ssh rights [here](#docker-setup-non-root).

 - Within Terminal:
   ```
   git clone https://github.com/GoVanguard/legion.git
   cd legion/docker
   chmod +x runIt.sh
   ./runIt.sh
   ```

Linux with Remote X11:
 - Assumes Docker and X11 are installed and setup.
 - Replace X.X.X.X with the IP of the remote running X11.
 - Within Terminal:
   ```
   git clone https://github.com/GoVanguard/legion.git
   cd legion/docker
   chmod +x runIt.sh
   ./runIt.sh X.X.X.X
   ```

Windows under WSL using Xming and Docker Desktop:
 - Assumes Xming is installed in Windows.
 - Assumes Docker Desktop is installed in Windows, Docker Desktop is running in Linux containers mode and 
 Docker Desktop is connected to WSL.
 - See detailed instructions [here](#docker-setup-wsl)
 - Replace X.X.X.X with the IP with which Xming has registered itself.
   - Right click Xming in system tray -> View log and see IP next to "XdmcpRegisterConnection: newAddress"
 - Within Terminal:
   ```
   git clone https://github.com/GoVanguard/legion.git
   cd legion/docker
   sudo chmod +x runIt.sh
   sudo ./runIt.sh X.X.X.X
   ```

Windows using Xming and Docker Desktop without WSL:
 - Why? Don't do this. :)


OSX using XQuartz:
 - Not yet in runIt.sh script.
 - Possible to setup using socat. See instructions here: 
 https://kartoza.com/en/blog/how-to-run-a-linux-gui-application-on-osx-using-docker/


<a name="docker-setup"></a>
Setup Docker on Linux:
 - To install docker components typically needed and add setup the environment for docker, under a term, run:
   ```
   sudo apt-get update
   sudo apt-get install -y docker.io python3-pip -y
   sudo groupadd docker
   pip install --user docker-compose
   ```

<a name="docker-setup-non-root"></a>
Setup Docker to allow non-root users:
 - To enable non-root users to run docker commands, under a term, run:
   ```
   sudo usermod -aG docker $USER
   sudo chmod 666 /var/run/docker.sock
   sudo xhost +local:docker
   ```

<a name="docker-setup-wsl"></a>
Setup Hyper-V, Docker Desktop, Xming and WSL:
 - The order is important for port reservation reasons. If you have WSL, HyperV or Docker Desktop installed then 
 please uninstall those features before proceeding.
 - Cortana / Search -> cmd -> Right click -> Run as Administrator
 - To reserve the docker port, under CMD, run:
   ```
   netsh int ipv4 add excludedportrange protocol=tcp startport=2375 numberofports=1
   ```
   - This will likely fail if you have Hyper-V already enabled or Docker Desktop installed
 - To install Hyper-V, under CMD, run:
   ```
   dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
   ```
 - Reboot
 - Cortana / Search -> cmd -> Right click -> Run as Administrator
 - To install WSL, under CMD, run:
   ```
   dism.exe /Online /Enable-Feature /FeatureName:Microsoft-Windows-Subsystem-Linux
   ```
 - Reboot
 - Download from https://hub.docker.com/editions/community/docker-ce-desktop-windows (Free account required)
 - Run installer
 - Optionally input your docker hub login
 - Right click Docker Desktop in system tray -> Switch to Linux containers
   - If it says Switch to Windows containers then skip this step, it's already using Linux containers
 - Right click Docker Desktop in system tray -> Settings
 - General -> Expose on localhost without TLS
 - Download https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download
 - Run installer and select multi window mode
 - Open Microsoft Store
 - Install Kali, Ubuntu or one of the other WSL Linux Distributions
 - Open the distribution, let it bootstrap and fill in the user creation details
 - To install docker components typically needed and add setup the environment for docker redirection, 
 under the WSL window, run:
   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   sudo apt-get update
   sudo apt-get install -y docker-ce python-pip -y
   sudo apt autoremove
   sudo usermod -aG docker $USER
   pip install --user docker-compose
   echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc && source ~/.bashrc
   ```
 - Test docker is reachable with:
   ```
   docker images
   ```

### TRADITIONAL METHOD
 - Please use the docker image where possible! It's becoming very difficult to support all the various platforms 
 and their own quirks.
 - Assumes Ubuntu, Kali or Parrot Linux is being used with Python 3.6 installed.
 - Within Terminal:
   ```
   git clone https://github.com/GoVanguard/legion.git
   cd legion
   sudo chmod +x startLegion.sh
   sudo ./startLegion.sh
   ```

## Development

### Executing test cases

To run all test cases, execute the following in root directory:

```bash
python -m unittest
```

## LICENSE

Legion is licensed under the GNU General Public License v3.0. Take a look at the 
[LICENSE](https://github.com/GoVanguard/legion/blob/master/LICENSE) for more information.

## ATTRIBUTION
* Refactored Python 3.6+ codebase, added feature set and ongoing development of Legion is credited to [GoVanguard](https://govanguard.com)
* The initial Sparta Python 2.7 codebase and application design is credited SECFORCE.
* Several additional PortActions, PortTerminalActions and SchedulerSettings are credited to batmancrew.
* The nmap XML output parsing engine was largely based on code by yunshu, modified by ketchup and modified SECFORCE.
* ms08-067_check script used by smbenum.sh is credited to Bernardo Damele A.G.
* Legion relies heavily on nmap, hydra, python, PyQt, SQLAlchemy and many other tools and technologies so we 
would like to thank all of the people involved in the creation of those.
* Special thanks to Dmitriy Dubson for his continued contributions to the project!

# Legion
