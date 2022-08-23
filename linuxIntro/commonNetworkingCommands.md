
# Common Networking Commands


## ip a/ifconfig

> used to look for ip addresses of all interfaces.

	- ip addresses
	- MAC address
	- ipv6 address
	- broadcast address etc.

> same thing can be done with `ifconfig` but its old school, in some cases `ip a` might not be available and in some cases `ifconfig` might not be avaialable or you may require **sudo** privilages.


## iwconfig

> used for wireless interfaces information.


## ip n/arp -a

> used to see what MAC address is associated with what ip address.

## ping

> used to verify connection with destination.

```
ping localhost
```