# Pi Zero Waveshare 2.13" Touch E-paper Password Manager

This project uses the Waveshare 2.13" touch e-paper HAT (or the case that includes the HAT) as a portable password manager based on Keepass. It converts a Pi Zero W into a USB keyboard and network device. It uses a Keepass database on a CIFS shared drive with a numeric passcode as a source of passwords and allows the user to authenticate using the passcode and have the device automatically type the username and/or passwords from the database into the attached USB host.

## Limitations

There is currently no security on the network share. This means that someone who gets hold of the device can overwrite your password database without authentication. The plan is to have the app only enable the SMB share when the file is opened successfully.

The IP address of the USB ethernet interface is 10.0.0.1. You must manually set the hosts's IP on the interface to 10.0.0.2 and the netmask to 255.255.255.252 to connect. If this clashes with your LAN IP then you will need to modify assets/init_usb_gadget to use a different IP and CIDR.

The UI is a bit crap. The page-up and page-down buttons are replaced by Lock and Shutdown buttons when you are on the first/last page respectively.

## Pre-Requisites

The included Ansible playbook will set up the device and install all the required software. You must have already installed a recent version of Raspbian (preferably Raspbian lite) and enabled WiFi with passwordless SSH access to a user that has passwordless sudo (basically the standard pi user). You also must have Ansible installed on your host device.

You must have a version 3 Waveshare 2.13" touch e-paper HAT attached to the Pi.

## Procedure

* Connect the Pi to your PC. Make sure you connect to the USB port, not the power-only port
* Run ./install.sh _pi-username_ _pi-hostname_
* Wait for the playbook to complete
* Reboot the Pi
* Configure the "USB Multifunction Device" network interface with the IP details above
* Open the \\\\10.0.0.1\\passman shared folder and create (or copy) a Keepass database in there with the filename passman.kdbx with a numeric only password (and no other key material)

If all is successful you should be presented with a pin entry screen and when the correct passcode is entered you will see your password entries listed.

## Acknowledgments

Thanks to these repos/pages for some useful code to manage the touchscreen and E-Paper interfaces on the HAT as well as how to configure Pi Zero as a USB gadget:

* https://github.com/waveshare/Touch_e-Paper_HAT
* https://github.com/thewh1teagle/zero-hid
* https://www.isticktoit.net/?p=1383