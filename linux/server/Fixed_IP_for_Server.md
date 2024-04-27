

sudo apt install net-tools


You can check if NetworkManager is installed using the following command:

dpkg -l | grep network-manager

If NetworkManager is not installed, you can install it using:

sudo apt install network-manager

If NetworkManager is installed but the service unit is missing, you might need to reinstall it:

sudo apt install --reinstall network-manager



> sudo nano /etc/netplan/01-network-manager-all.yaml

    network:
    version: 2
    renderer: NetworkManager
    ethernets:
        enp1s0:
        dhcp4: no
        addresses: [192.168.1.50/24]

>sudo chmod 600 /etc/netplan/01-network-manager-all.yaml

> sudo netplan try

> ifconfig -a

> sudo netplan apply