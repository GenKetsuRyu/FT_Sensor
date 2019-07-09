# FT300 Sensor

## Basic Specification

Device Name                   | FT-300 Sensor
------------------------------|:-------------------------------:| 
Input Voltage Range           | from 5 V to 24 V (DC)
Maximum Power Comsumption     | 2 W
Sensing Range                 | from -300 N to +300 N

## Testing FT300 Sensor on Ubuntu Linux environment

### Unzip the test Package

Copy FT-300_dev_package_SDP-1.0.1_20180328.rar from Robotiq's USB driver and unzip in your home folder.

### Envronment Setting

Open terminal in the folder **~/driver/** and use the following command to compile the application:

```bash
$ make linux
```
Access to the virtual serial port and add the username to the group dialout
(**superuser** mode is required before using this command )

```bash
$ sudo su
$ usermod -a -G dialout [your_username]
```
After all above commands have been done, it is required to **Logout and re-Login the session** in order to activate the group change

You can check the usermod status by using following comannd:

```bash
$ usermod -a -G dialout $[your_username]
```
### Testing 

Power on your sensor according to **Basic Specification** above, make sure your power supply is in the input voltage range. Then, connect your sensor to the PC using RS485-USB converter. You can check your connection by the following command:

```bash
$ ls -l /dev | grep ttyUSB
```

Open a terminal and go to the folder by **$ cd ~/driver/Linux/bin**, using the following comand to start the testing:

```bash
$ ./driverSensor
```


# reference :
 
 [1] offical ros package: https://github.com/ros-industrial/robotiq/tree/hydro-devel/robotiq_force_torque_sensor
