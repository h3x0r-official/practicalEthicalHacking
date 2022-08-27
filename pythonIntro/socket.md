# Sockets
Python provides two levels of access to network services. At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.
[Source]([Python - Sockets Programming (tutorialspoint.com)](https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm#))

> Do not name its python script file 'socket'. 

## Example:

```
import socket

HOST = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
```

- Here we are importing `socket` module/lib.
- Creating variables  `HOST` and `PORT` and assigned it Localhost IP address and Port number on which we are going to listen.
- Created another variable `s` and assigned it value. Values are `methods` from `socket` library/module.
- Here `socket.AN_INET` can be called IP address method.
- And `socket.SOCK_STRAM` port number.
- At last we used `.connect()` method to connect back to `HOST` and `PORT`.

## Listening
I started a listener on port 4444 and run the script.
And successfuly got connection.
