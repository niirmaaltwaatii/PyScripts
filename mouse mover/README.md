#Mouse Mover

This script continuously moves the mouse cursor to random positions on the screen, simulating mouse clicks.


##Prerequisites

To run this script, you need to install the following Python packages:



_win32api_

_win32con_


You can install the packages using pip:


```
pip install pywin32
```
##Usage

To start the mouse mover script, simply run the following command:


```
python mouse_mover.py
```
##How it works

The click function is defined to move the cursor to the specified coordinates and simulate a left mouse button click at that position. The x and y parameters represent the coordinates where you want to click the mouse.


The script enters an infinite loop that continuously calls the click function with random x and y coordinates generated using random.randint(0, 100). After each click, the script waits for 1 second using time.sleep(1).


This script is often used for automation or testing purposes, where you want to simulate mouse clicks at random positions on the screen.

