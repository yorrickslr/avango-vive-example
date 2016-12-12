# Vive Window Example for Avango

### Notes
This is an example on how to use the [Guacamole](https://github.com/vrsys/guacamole) Vive window in [Avango](https://github.com/vrsys/avango). In order to run this example, you will have to compile both Guacamole (with ViveWindow plugin) and Avango.

This example is currently working on Windows only owing to SteamVR not being ported to Linux already.

### Running the Application
 * plug in all Vive devices (e.g. power for lighthouses and headset)
 * start SteamVR from your Steam software library
 * check if all devices are conntected properly (green icons in SteamVR control panel; see [SteamVR helpdesk](https://support.steampowered.com/kb_article.php?ref=8566-SDZC-9326&l=german) for further assistance)
 * check if `set_environment.bat`contains the right Avango paths
 * check if `daemon.py` contains the right server IP and port
 * open first terminal in the application directory
   * start `set_environment.bat` to setup the avango environment
   * type `python daemon.py` to start the Avango daemon
 * start the [HMD device server](https://github.com/DreadNoize/HMD-Server)
 * open second terminal in the application directory
   * run `set_environment.bat` again
   * type `python main.py` to start the application

### Notes for usage in the VR-Lab
Avango and Guacamole are usually located in the `C:\data\repositories\` directory on Windows machines. The uploaded `set_environment.bat` will point to this location.

A Vive device server may be located in this directory, too. If not, you may take a look into the `\data\socialvr\` directory.

The daemon is currently configured to listen on Demeter [141.54.147.35:7770]. You should run the device server with this address...
