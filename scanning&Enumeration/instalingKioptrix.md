# Installing Kioptrix
Kioptrix is a vulnerable machine used for training purpose to practice pen testing.
[Download Link:](https://tcm-sec.com/kioptrix)

## Setup
Setup is simple just download the `.ova` file and import in
1. Vmware Player
2. VM Virtual Box

## Requirments
Kioptrix is not fancy resource consumer machine.
It just need
1. 256 MB (RAM)

## IP Address
To find ip address of machine. Simply ping google dns. Machine don't have `ifconfig` and `ip addr` command.

```
ping 8.8.8.8
```

![[Pasted image 20220904152755.png]]

Or you can use simple tool on your **kali** Machine `scan-arp`

```
sudo arp-scan -l
```

![[Pasted image 20220904154309.png]]

## Default Creds
Default creds to access the machine are:
| user | password|
|---|----|
| john | TwoCows2 |

