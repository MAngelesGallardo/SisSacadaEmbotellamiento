Bottling system

It is an industrial control system simulator that adds real-world-like control logic to the basic PLC-like tag read / write feature. All software is written in Python and runs Modbus as its protocol. To make the bottling system work, initially a virtual machine (Kali Linux tool) was used since it is a tool that is frequently used for computer security, in a machine the entire operation of the bottling system will be simulated.

The program works by running the command ./start.sh in which the hmi.py and word.py scripts are called, where are the basic functionalities of the bottling system and the connection to the PLC which refers to a generic-modular model, that is, it allows the reading of signals from distributed sensors, allows communication with the different equipment, an interface that allows use and dialogue with the operators, receives and executes continuous orders for long periods of time and can control inputs and outputs distributed and outside the central cabinet of the PLC through a network cable. In addition, the system handles binary signals, which are encoded by means of a button or a switch.

The operation of the system consists of two windows, one that simulates the controls, HMI, run for starting and stop for stopping.

Install 
To install all the pip packages using our provided require.txt file:

pip install <requirements.txt
