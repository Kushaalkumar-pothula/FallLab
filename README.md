# FallLab
A simple Python code to simulate and analyze free fall kinematics and dynamics.

Features:
- Height vs time
- Potential energy (PE) vs time
- Kinetic energy (KE) vs time
- Velocity vs time
- KE/PE vs time
- KE vs height
- PE vs height

## 1.1 Installation
Requirements:
- Numpy
- Matplotlib

To install FallLab, run the following command in your terminal:
```bash
> git clone https://github.com/Kushaalkumar-pothula/FallLab.git
```
## 1.2 Usage
To run the simulation, you will have to run ```main.py``` with some parameters.
```bash
> python main.py [t] [h] [m] [g]
```
Where:
- ```t```: The time for which the simulation is to be run, in seconds. Required.
- ```h```: Height of the body above the surface, in meters. Required.
- ```m```: Mass of the smaller body, in kilograms. Required.
- ```-g``` or ```--acceleration```: Acceleration due to gravity in m/s^2. Optional, default value is 9.81 m/s^2.

The parameters can be displayed by using ```-h``` or ```--help```:
```bash
$ python main.py -h
usage: main.py [-h] [-g] t h m

positional arguments:
  t                     Time for which the simulation is ran, in seconds.
  h                     Height of the body from the surface, in meters.
  m                     Mass of the body, in kilograms.

optional arguments:
  -h, --help            show this help message and exit
  -g, --acceleration    Acceleration due to gravity
```
