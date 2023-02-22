# System Desing - Foundation Materials

## Network Protocols

![](images/network_protocol.jpeg)

1. **Domain Name System [DNS]** - Service that takes in the human readable server name and returns the IP address of the destination server.

2. **Router** - Routes the request from the client server to the destination server.
3. **Port** -Identifies the specific endpoint in a server. Destination address is a combination of Server IP Address + Port Number
4. **Protocol** - Formal description of message format.Rules to be followed during the exchange.One of the famous protocol is TCP/IP.
5. **HTTP** - Protocol/Format of the request adhered by the client when sending the request to the server or from server back to the clinet.Used by the client browser to get back web pages from web servers. 
6. **HTML**- Format of the webpage text.



_**Curl Request - Response**_ 

![](images/curl-display-request-response-headers.png)

## Web Server
Web Server - Provides the framework to enable an online service.

Everything outside the brown box [Actual Processing logic] can be handled by the web server.

![](images/web-server.jpeg)

1. Parallelism - Use multiple copies of the running program (on multiple processors).

2. Multi-processing - Use multiple copies of the running program with independent resources.

3. Multi Threading - Even with a server containing only single processor ,we might want to process multipe requests as Disk /Network I/O operations takes a long time ,while one copy of request is blocked waiting for I/O,the processor can serve other requests.

In multi threading [avoiding blocking an request processing due to I/O operation], we need to ensure threads (all the copies of the running program) should have access to a single shared resource.

