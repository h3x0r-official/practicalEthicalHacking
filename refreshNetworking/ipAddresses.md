
# IP Addresses

> ifconfig (linux)

`Used to show up ip addresses info and interfaces connected to machine, using IP addresses we communicate on layer 3 (router)`.

Here we have main three things to note:

	- interface name
	- inet 192.168.1.1 (which is ipv4 address in decimal notaion:32bit)
	- inet6 (which is ipv6 address in hexadecimal notation:128bit)

> inet/ipv4

	- made up of 32 bit, means it have 2^32 = 4,294,967,296 possible IP's ~ 4 billion
	ipv4 is here since 1981. We use NAT to resolve IPs for 7 billion people.
	8bit + 8bit + 8bit + 8bit ==> 192.168.1.1
	8bit ==> 128 64 32 16 8 4 2 1
	           1  1  1  1 1 1 1 1 = 255
	________________________________________________
			   1  1  0  0 0 0 0 0 = 192
			   1  0  1  0 1 0 0 0 = 168
			   0  0  0  0 0 0 0 1 = 1
			   0  0  0  0 0 0 0 1 = 1

		- Private address

Network Class	  Network        	    Network Mask		 No. of Networks		   Number of Hosts 
CLASS A 			  10.0.0.0			        255.0.0.0			    126					           16,646,144
CLASS B 			  172.16.0.0 to	        255.255.0.0 		    16,383				            65,024
				-				172.31.0.0 															
CLASS C 			  192.168.0.0 to 	    255.255.255.0 		2,097,151			            354
				-		  192.168.255.255