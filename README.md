# FT300 Sensor 

## Testing FT300 Sensor on your Ubuntu Linux environment

### Unzip the test Package

Copy the FT-300_dev_package_SDP-1.0.1_20180328.rar from Robotiq USB drive and unzip in your home folder.

### Envronment Setting

Open the terminal in the folder ~/driver/ and use the following command to compile the application:

```bash
$ make linux
```
Access to the virtual serial port and add the username to the group dialout
(**superuser** mode is required before using this command )

```bash
$ sudo su
$ usermod -a -G dialout [your_username]
```
Then, **Logout and re-Login the session** to activate your group change

Also, You can check the usermod status by using following comannd:

```bash
$ usermod -a -G dialout $[your_username]
```

# reference :
 
 [1] offical ros package: https://github.com/ros-industrial/robotiq/tree/hydro-devel/robotiq_force_torque_sensor
