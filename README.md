# FT300 Sensor 

## Testing FT300 Sensor on your Ubuntu Linux environment

1. Copy the FT-300_dev_package_SDP-1.0.1_20180328.rar from Robotiq USB drive and unzip in your home folder.

2. Open the terminal in the folder ~/driver/ and use the following command to compile the application:

```bash
$ make linux
```
3. Access to the virtual serial port. (Before running this command, you need to open the superuser mode)

```bash
$ sudo su
$ usermod -a -G dialout [your_username]
```
   After all, you can check your usermod status by following command:

```bash
$ usermod -a -G dialout $[your_username]
```

# reference :
 
 [1] offical ros package: https://github.com/ros-industrial/robotiq/tree/hydro-devel/robotiq_force_torque_sensor
