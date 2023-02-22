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


## Scaling
Reasons to go for distributed systems:

1. Check how much data needs to be stored : may need to scale DB and cache tier if size of the data is too huge.
2. If the number of requests per second is too huge , need to scale for throughput.
3. If the response time is too high , need to parallelize the computation.
4. Availability/Reliability in the face of faults.
5. Geolocation - Minimize network latency by multiple servers at different locations.
6. Hotspots - Disproportionately high load on a piece of data.


### Vertical Scaling / Scaled up/ Shared Memory Architecture

Going for a more powerful machine with many disks,many RAM chips and many CPUs

1. Cost eventually grows faster than linearly.
2. Has a ceiling 

### Horizontal Scaling / Scaling out / Shared nothing Architecture

Using large number of commodity machines and getting them to work together connected via network to provide the overall functionality.

## Performance Metrics for a Scalable System

Defining SLIs (Servive Level Indicators):
A quantitative measure of the level of service being provided.

1. **Correctness** - Is the right answer/data bbeing returned?. Error rate as a raction of all requests.
2. **Avaialbility** - Could we respond to the request? Fraction of time that a service is usable. Fraction of well-formed requests that succeeds.
	99% = 2nines , 99.999% = 5 nines , 3 1/2 nines = 99.95
	
3. **System Throughput** - The no, of requests/sec that could be handled by a server.
4. **Response Time** - How long it took to return a response to the client request.Anything below 300ms is widely accepted.**Round trip time[RTT]** is a part of response time and could be impacted by Geolocation.

![](images/performance_metrics.jpeg)

### Latency vs Response Time

Response Time = Latency(2 way Round Trip Time) + Service Time(at Server)

Latency - Duration that a request is "latent"(awaiting service), not being actually served.
Here, latency is a measure of network performance.

#### Other measures of Network Performance

1. Bandwidth [Data Rate]- No of bits that can be transmitted  over the network per second.

	Assuming 10Mbps = 10 million bits/s
	For 1 bit = 1/ (10^7) = 0.1 \mus

2. Transmission time - $Size of the message / Bandwidth$
3. Propogation Delay - $Distance / Speed of Light$
	Speed of Light - 3 x 10^8 m/s -> Vaccum
					  - 2 x 10^8 m/s -> Optical Fibre

4. Queueing Delay 
	
Total delay of the packet - Transmission Time + Propogation Delay + Queueing Delay



