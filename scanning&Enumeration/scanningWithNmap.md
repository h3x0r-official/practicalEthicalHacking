# Scanning With Nmap
nmap is most used network mapper tool, used to scan network to look for open ports, services and their versions even OS version can be found using nmap.

## Scanning Kioptrix
To scan kioptrix we used this command:

```
nmap -T4 -p- -A 192.168.209.199
```

| Flag | Description |
| --- | ----| 
| -T4 | Is the speed to scan (0 to 5) 5 is fastest |
| -p- | Is to scan all ports |
| -A | Means (All) Version, OS, And default script scan|


