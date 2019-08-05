# FT-300 Sensor

## Basic Specification

   Device Name                   | FT-300 Sensor
   ------------------------------|:-------------------------------:| 
   Input Voltage Range           | from 5 V to 24 V (DC)
   Maximum Power Comsumption     | 2 W
   Sensing Range                 | from -300 N to +300 N

   ****Warning***: In order to avoid damaging the sensor, input voltage which over **26 V (DC)** is strictly prohibited.

## Testing FT-300 Sensor on Ubuntu Linux environment

### Envronment Setting (first time)

1. clone this repo 

2. setup driver
```bash

$ cd <ros_ws>/src/robotiq_force_torque_sensor/tools/FT_sensor/FT-300_dev_package_SDP-1.0.1_20180328/robotiq_ft_sensor_dev_v1.0.1/driver

$ make linux
```
3. Access to the virtual serial port and add the username to the group dialout  (**Superuser** mode is required before using this command )

```bash
$ sudo su

$ usermod -a -G dialout [your_username]
```

4. After all above commands have been done, it is required to **Logout and re-Login the session** in order to activate the group change

5. (optional) You can check the usermod status by using following comannd:

```bash
$ sudo su # Usermod must be opened by superuser mode.

$ usermod -a -G dialout $[your_username]

$ exit # Use "exit" to close superuser mode after your checks have done.
```

6. (optional) Test if env setting success or not
- the torque will display on terminal (value are without calibration)
- 1. Power on your sensor according to **Basic Specification** above, 
- 2. make sure your power supply is in the input voltage range. 
- 3. connect your sensor to the PC using RS485-USB converter. 
```bash
$ ls -l /dev | grep ttyUSB
```
- 4. Open a terminal and using the following comand to start the testing for check the connection:
```bash
$ cd <ros_ws>/src/robotiq_force_torque_sensor/tools/FT_sensor/FT-300_dev_package_SDP-1.0.1_20180328/robotiq_ft_sensor_dev_v1.0.1/driver/Linux/bin

$ ./driverSensor
```


## Setup ROS Package 

1. make package
```bash
$ cd <ros_ws>

$ . devel/setup.bash

$ catkin_make robotiq_force_torque_sensor_generate_messages

$ catkin_make
```

2. (optional) Make sure that you have already accessed to the virtual serial port:

```bash
$ sudo su

$ usermod -a -G dialout [your_username]
```

3. (optional) **Logout and re-Login** the session to activate your change

4. run ROS package:

```bash
$ roscore
```

6. Open a new Terminal by **ctrl+shift+T**, Starting your sensor on ROS:

```bash
$ . devel/setup.bash

$ rosrun robotiq_force_torque_sensor rq_sensor
```
- Check the led on sensor change to blue light

7. Get torque value (Open another Terminal by **ctrl+shift**)::

```bash
$ . devel/setup.bash

$ rosrun robotiq_force_torque_sensor rq_test_sensor
```
-  the calibration already complete when rosrun this node

****Warning***: Any node execution shoud use **". devel/setup.bash"** respectively in order to source the Catkin  workspace



## Calibration (for windows user)

1. Download the calibration software [**Visual Demo Software**](https://robotiq.com/support/archive/) on **Windows** environment

2. follow the Steps below to compelete your sensor calibration:

   Step 1: Open the Software

   Step 2: go to "**Calibration**" 

   Setp 3: Setup the FT Sensor on  your development environment (ex: manipulator) 

   Step 4: Press "Lock Image" buttom to start the calibration 

   Step 5: Point the direction X, Y and Z of sensor downward below and press the relative calibration buttoms respectively 

   Step 6: After finishng all the calibration procedure, go to "**Sensor Data**" and check your results

# reference :
 
 [1] officail ros package: https://github.com/ros-industrial/robotiq/tree/hydro-devel/robotiq_force_torque_sensor
 
 [2] official ip (Visual Demo Software): https://robotiq.com/support/archive
 
 [3] official document: https://assets.robotiq.com/website-assets/support_documents/document/FT_Sensor_Instruction_Manual_PDF_20181218.pdf
