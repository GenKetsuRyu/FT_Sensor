# FT300 Sensor

## Basic Specification

   Device Name                   | FT300 Sensor
   ------------------------------|:-------------------------------:| 
   Input Voltage Range           | from 5 V to 24 V (DC)
   Maximum Power Comsumption     | 2 W
   Sensing Range                 | from -300 N to +300 N

   *Warning: In order to avoid damaging the sensor, input voltage which over **26 V (DC)** is strictly prohibited.

## Testing FT300 Sensor on Ubuntu Linux environment

### Envronment Setting

1. Copy FT-300_dev_package_SDP-1.0.1_20180328.rar from Robotiq's USB driver and unzip in your home folder.

2. Open terminal in the folder **~/driver/** and use the following command to compile the application:

```bash
$ make linux
```
3. Access to the virtual serial port and add the username to the group dialout
(**superuser** mode is required before using this command )

```bash
$ sudo su
$ usermod -a -G dialout [your_username]
```
4. After all above commands have been done, it is required to **Logout and re-Login the session** in order to activate the group change

5. You can check the usermod status by using following comannd:

```bash
$ usermod -a -G dialout $[your_username]
```
### Testing

1. Power on your sensor according to **Basic Specification** above, make sure your power supply is in the input voltage range. Then, connect your sensor to the PC using RS485-USB converter. You can check your connection by the following command:

```bash
$ ls -l /dev | grep ttyUSB
```

2. Open a terminal and go to the folder by **$ cd ~/driver/Linux/bin**, using the following comand to start the testing:

```bash
$ ./driverSensor
```
## Calibration

1. Download the calibration software [**Visual Demo Software**](https://robotiq.com/support/archive/) on **Windows** environment

2. follow the Steps below to compelete your sensor calibration:

   Step 1: Open the Software

   Step 2: go to "**Calibration**" 

   Setp 3: Setup the FT Sensor on  your development environment (ex: manipulator) 

   Step 4: Press "Lock Image" buttom to start the calibration 

   Step 5: Point the direction X, Y and Z of sensor downward below and press the relative calibration buttoms respectively 

   Step 6: After finishng all the calibration procedure, go to "**Sensor Data**" and check your results

## ROS Package Setup


# reference :
 
 [1] officail ros package: https://github.com/ros-industrial/robotiq/tree/hydro-devel/robotiq_force_torque_sensor
 
 [2] official ip (Visual Demo Software): https://robotiq.com/support/archive
