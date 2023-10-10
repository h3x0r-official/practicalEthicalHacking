# Scripting with bash

## ping sweep

### ping
if we use `ping <ip-address>`
This command pings the ip address by sending multiple packets.

```
$ ping 192.168.1.1 -c 1
PING 192.168.247.108 (192.168.247.108) 56(84) bytes of data.
64 bytes from 192.168.247.108: icmp_seq=1 ttl=128 time=3.25 ms
```

- Here `-c` is count tag, which only sends packets defined in number next to it.
- Here `1` means single packet checked in ping command.

### cut
`cut` command is used to cut out and filter the results we can gonna see on terminal.
We can use it by putting a pipe next to a command. e.g.

```
$ ping 192.168.1.1 | cut -d " " -f 4
```

Command:

```
cut -d " " -f 4
```

- Here `-d` means delimeter, and delimeter checks for defined pattern in qoutes as in command `" "` , here delimeter will check for spaces in output and catch them.
- Here `-f` means field, field is used to start filtering what delimeter catches and begin cut form there. e.g.

Output without `cut`:

```
$ ping 192.168.1.1 -c 1
PING 192.168.247.108 (192.168.247.108) 56(84) bytes of data.
64 bytes from 192.168.247.108: icmp_seq=1 ttl=128 time=3.25 ms
```

Output with `cut`:

```
$ ping 192.168.1.1 -c 1 | grep "64 bytes" | cut -d " " -f 4
192.168.247.108:
```

### tr
Translate `tr` command is used to caputre specific character and remove it from output.
For example we have out of ip address like: `192.168.1.1` and if we use `tr` command and cutout `.` from output then ip address will become like: `19216811`

```
tr -d "."
```

- Here `-d` is delimtere as in `cut` command.
- And `"."` is aurguement to cutout `.` from output.

Code 1:
```
$ ping 192.168.1.1 -c 1 | grep "64 bytes" | cut -d " " -f 4
192.168.247.108:
```

Code 2:
```
$ ping 192.168.1.1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" 
192.168.247.108
```

- Here in above example we are cutting out `:` from last of ip address as it was in **code 1** and removed in **code 2** with the help of `tr` command/tool.

### if else
By using conditional statments in bash we can make our script more strong and usful. In our case we can use `if else` to make our script more functioning.

./ipsweep 

```
#!/bin/bash
if ["$1" == ""]
then
echo "You forgot IP address!"
echo "Syntax: ./ipsweep.sh"
else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi 
```

- Here `$1` is the first index value of `for` loop and a aurgument to check ping in script. So any ip is typed like this `./ipsweep 175.50.0` will run like `ping -c 1 175.50.0.1..254` 
- Here `&` is used at line 8. to keep the `ping` running , to fast the process.
- Here `fi` is the **closing** syntax of `if else` statement at line 10.

Output:

```
175.50.0.1
175.50.0.12
175.50.0.14
175.50.0.17
175.50.0.45
175.50.0.43
175.50.0.49
175.50.0.48
175.50.0.50
175.50.0.56
175.50.0.60
175.50.0.63
175.50.0.64
175.50.0.68
175.50.0.77
175.50.0.32
175.50.0.98
175.50.0.102
175.50.0.106
175.50.0.105
175.50.0.112
175.50.0.120
175.50.0.152
175.50.0.190
175.50.0.233
```

### for loop
Syntax:

```
for n in a b c;
do
   echo $n
done
```

### one-liner
If we want to run `nmap` for whole network we have to run this command to scan for valid ip from whole network we can use following command using CIDR notation.

```
nmap 192.168.24.1/24
```

But the problem with this command is that it have to find valid IPs first then run `nmap` on valid IPs. Which is very time consuming with `nmap`.
We can simply create **ipsweep** script and pass those valid IPs to `nmap` in `one-liner`.

For example:
First we have to **redirect** output of **ipsweep** script in a file. e.g. 

```
./ipsweep.sh 192.168.24 > validips.txt
```

And then need to write one liner script to run `nmap` using `validips.txt` file.

```
for ip in $(cat validips.txt); do nmap $ip & done
```

This one liner will `nmap` each ip in validips.txt file.