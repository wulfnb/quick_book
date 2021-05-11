### Follow live of file
>tail -f /var/log/file.log


### Zero fill 
>sudo fdisk -l
>sudo shred -n 2 -z -v /dev/sdc1

### See all the boots
>journalctl --list-boots



### Hardrive analysis
>sudo apt-get update

>sudo apt-get install smartmontools

>sudo smartctl -x /dev/sdY #Replace "Y" appropriately for your system

### Disabling the recovery
/etc/default/grub
GRUB_DISABLE_RECOVERY="true"
GRUB_DISABLE_SUBMENU=y

#### list all the partitions
sudo fdisk -l

#### zerofill the drive
sudo shred -n 2 -z -v /dev/sda1


#### Create ssh key
ssh-keygen -t rsa -b 4096 -C "mail@gmail.com"


#### Rename .vm extension to .html
```for name in *.vm
do
    newname="$(echo "$name" | cut -f 1 -d '.')".html
    mv "$name" "$newname"
done
```