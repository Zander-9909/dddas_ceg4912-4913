# Drowsy (and) Distracted Driving Avoidance System (CEG4912/CEG4913 Capstone Project)
The DDDAS will be able to monitor and track biometrics of the driver. It will alert the driver by
vibrating the steering wheel and playing a notification sound. The DDDAS will be connected to an
eLog tablet through USB tether to have further access to functions that will be used to detect a
crash, such as inertial sensor, a GPS with access to google maps, and a microphone.

In the case of all 3 detecting, it will automatically call emergency services, however when only 1
or 2 go off, it will ask the driver if it will be necessary through sound and vibrating the steering
wheel in intervals, and will call if there is no response from the driver
## Group Members and Roles
+ Griffin Taylor (Scrum Master)
+ Ali Jafri
+ Jessica Cai
+ Ryan Tong
+ Kenneth Chen
+ Leonardo Saavedra Morales
#
![alt text](https://github.com/Zander-9909/dddas_ceg4912-4913/blob/main/assets/diagrams/hardware-architecture.png "Initial Architecture")

NOTE: If you are running this on a raspberry pi or similar ARM processor, it is highly recommended to compile dlib and OpenCV with Neon instruction, OpenBLAS, and VFPv3 support. This will significantly increase performance

To clone project, do ```git clone --recurse-submodules https://github.com/Zander-9909/dddas_ceg4912-4913.git```
This will also clone and update the submodule dlib used within the project.
