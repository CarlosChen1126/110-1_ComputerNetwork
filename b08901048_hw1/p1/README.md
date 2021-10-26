# HW1 電機三 b08901048 陳宥辰 
## p1 Socket Programming - TCP
```
├── p1
│   ├── README.md
│   ├── client.py
│   └── socket_server.py
├── p2_a
│   ├── helloworld.html
│   ├── index.html
│   └── web_server.py
└── p2_b
    └── proxy_server.py

3 directories, 7 files
```
### IP=127.0.0.1 PORT=8888
## Execute
```shell=
(terminal1)
cd p1
python3 socket_server.py
```
```shell=
(terminal2)
cd p1
python3 client.py
```
**Must use python3 to execute p1/socket_server.py and p1/client.py!!**

## Usage
There are 9 kinds of math function
* addition: a+b
* subtraction:a-b
* multiplication:a*b
* division:a/b
* power:a^b
* mode:a%b
* quotient:a#b
* factorial:a!
* percentage:a~
when finish calculator, use "y" or "Y" to continue and use "n" or "N" to close 
p2_b discussing with 電機三 b08901152 王政邦
## Execution of p2_b
```shell=
(terminal1)
cd p2_a
python web_server.py
```
```shell=
(terminal2)
cd p2_b
python proxy_server.py 127.0.0.1
```