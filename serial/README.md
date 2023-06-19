I don't exactly remember specifically why I was supposed to use pyserial but
since there's going to be a lot of connecting and communicating back and forth
to a device over serial port in order to test it, it'll probably be used more
later. For now, i was just told to get familiar with how it worked and the
pyserial.py script just connects and either auto logs in or prompts for login
and then allows a user to communicate with the device as you would through ssh
or minicom.


notes:
- pyserial.py has not been tested much at the moment. It works for file navigating
and some other simple command line commands. It's able to take cmd line input
and reads back the output but certain things may confuse it atm.
- pretty sure that pyserial gets pissy if minicom is open at the same time

