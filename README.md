# cea-os Sensor Package
Driver package for controlled environment agriculture sensors

# Installation
1. Download Python 3 on Raspberry Pi (version >= 3.7)
2. Clone the cea-os-sensors repo onto the Raspberry Pi
    ```sh
    git clone https://github.com/mlab-upenn/cea-os-sensors.git
    ```
# Usage
1. Start containers for cea-os main package https://github.com/mlab-upenn/cea-os
2. Run the drivers for the sensors connected to the Raspberry Pi

    ```sh
    chmod 755 {launcher_name}.sh
    sh {launcher_name}.sh &
    ```
OR

2. Create a crontab that runs the launcher scripts on boot 
(example here: https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/)
