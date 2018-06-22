# DriveSimulator
Driving simulator of a car with human input

## Requirements
+ Python (I use version 3.6.)
  - scipy
  - matplotlib
  - numpy
  - math
  - win32api
+ Windows (Win32 API, I use Windows 10.)

## Files
+ main.py: Execute it and the simulation would be start.
+ carImage.py: For displaying the position of the car
+ getkey.py: For obtaining an input from your keyboard
+ model.py: Description for dynamics of cars
+ virtualKey.py: Keymap. Great thanks to chriskiehl/Vitual keystroke example(https://gist.github.com/chriskiehl/2906125)

## How to use
1. Execute main.py, and command line and figure will be started.
2. Control the car.
+ Accelerate: u(fast), i, o, p, j, and k(slow)
+ Deccelerate: l(slow), ;, ,, ., /(fast)
+ Handling: a(left, fast), s(left, slow), d(right, slow), f(right, fast)
3. To stop the simulation, press 'G'
