# Enumerating HTTP and HTTPS
Ports we are going to enumerate:

| Service | Port | IP Address | Default Page | 
| ------- | ------ | --------- | ---- |
| Apache Webserver | 80 | 192.168.209.199:80 | Default Page |
| Apache Webserver | 443 | 192.168.209.199:443 | Error Page |

## ID 404 Page
To get ID (Information Disclosure) information.
You can simply click on Manual/Documentation link or any **bad link** (information disclouser) to get this info in error page.

#### Info:
1. Webserver: Apache/1.3.20
2. Hostname: kioptrix level one (Patched)

## Nikto
 Nikto is a web server scanner which performs tests against web servers for multiple items.
[More information](https://cirt.net/Nikto2)

It's a beginner tool to scan web servers. The only problem with it is that modren websites with good security practices, can easily detect and stop nikto scans.

For a simple scan use this command:

```
nikto -h http://192.168.209.199
```

| Flag | Description |
| --- | ---- |
| -h | Used to enter Host next to it.|

Nikto found many vulns saved in `niktoScan` file.

## Dirbuster
Dirbuster is used to brute force web application directories.

```
disbuster&
```

will open dirbuster as a background process so you can work on dirbuster.








