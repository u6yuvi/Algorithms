import string


''' Function Requirement
1. Long to short
2. Short to long
3. When same url ,create a new short url


Encoding Process

1. Approach-1 - Naive Way
    
    Encoding Proces
    1. Use a global counter to keep the count of the incoming long url.
    2. Append this counter value in the the array.
    3. The counter value becomes the short url endpart of the url and is appended with the first part and is returned back.
    
    Decoding Process
    1. Extract the end part of the url which is the counter index
    2. Check the array at the counter index to get the original long url.
    3. Return back the long url.

    Pros
    1. Simple to implenent
    2. No collision issues

    Disadvantage
    1. Predictable
    2. The short url is not really short,Think about the billionth url index 100000.....

2. Using Base-64 [0...9A...Za...z-_]

    Encoding Process
    1. Convert the counter index using the Base64 function.
    2. Continue as described in Approach 1.


    Decoder Process
    1. Same as Approach -1


    Advantage
    1. No collision
    2. Short url

    Disadvantage
    1. Predictable

3. Use hash function [ to remove predictability]
    Make short url by generating them in a random way by keepin the collision low.

    1. Append the long url with the counter value  to make it unique incase same url comes again. 
    2. Convert the new long url to a hash by using any of the MD5[128 bit] ,SHA-1[160 bit],SHA-2 cryptographic hash function.
    2. 128 or 160 bit long hash value is converted using base64. 

    Advantage
    1. No more predictability
    
    Disadvantage
    1. Short url is not that short
    2. Chances of collision although very low

    One way to overcome collision is to run the hash function again until the key is unique.


Summarize
1. Counter Method -----------------------[]
2. Generate random/unpredictable short url
    1. Generate random string ------------[]
    2. Timestamp --------------------------[]
    3. Apply cryptographic hash function to 
        1. Long url
        2. Counter/Timestamp   --------------[]
        3. Combination of these

All the ------[] strategy of short url generation donot use the long url. 
So we could pregenerate short URL and store them in advance.

4. Pregenerate the short_urls offline [Key Generation Service]
    Advantage 
    1. no_collision [will remove the similar one from the batch] + unpredictable
    Disadvantage
    1. Need space to store all pregenerated short urls



'''


'''
Network Protocol
1. Short url
2. DNS
3. IP and Port
4. HTTP Get request
5. HTML to render the request body
'''


'''
Webserver

1. Consists of UI + Business Logic + DB
2. Stateful or Stateless
'''


'''Reason for Distributed System

1. Check how much data is needs to be stored:may need to scale DB and cache tier if size of the data is too huge.
2. If the number of requests per second is too high,need to scale for throughput.
3. If the response time is too high ,need to parallelise the computation.
4. Availability/Reliability in the face of the faults.
5. Geolocation - Minimize network latency by using multiple servers at different locations.
6. Hotspots- Disproportinality  high load on a piece of data.
'''

'''
Non functions /Capacity Requirements
1. 2-3 billion short link creation per year i.e. 73 qps(queries per second)
2. 20 billion clicks per month i.e 7700 qps
'''

'''
For URL Shortner
Assumption
Point5 and Point6 above is not relevant.

Consideration
1. Response time  is dependent on search or insert which is one seek operation on database.Cannot reduce it further \
    also no scope for parallelisation.


------------------------Scaling for DATA SIZE--------------------------------------
Motivation for horizontal scaling
1. Huge Data Size
2. Large number of requests per sec(throughput)
3. Single point of failure - Replication factor of 3 is common.
'''

'''
-------Calculation of Data size for DB-----

##No of queries 

Storage for 3 yrs ~1000 days

Q queries/second [~73]
No of seconds per day
Q*24*60*60 ~100000
In 3 yrs ~ 1000 days = 1000 * 100000 ~ 10^8
No of queries in 3 yrs = Q*10^8  ~ 10^10
No of key-value pairs = 10^10  ~ 10 billion


##Size of each query

Long url  size = 2kb
For short url ??

2^10 = 10^3 will require 10 bits
for (10^3)^3(1 billion) -> 30 bits
For 2 billion - 31 bits , for 4 billion - 32 bits , for 8 billion - 33bits , for 16 billion - 34 bits

For conversion in base 64
Shift by 6
34/6 -> 6 characters for short url which is 6 bytes <<< 2KB.

Total size(short url + long url) -> 2KB

Total size of Hashtable -> 2KB * 10 billion  -> 10 billion * 2*10^3 ~ 20*10^12 ~ 20TB

Per DB 1~2 TB 
Scale horizontlally - 20/2 -> 10 machines
Partition/sharding our hashtable  across 10 servers.

For replication ,each server should be replicated 3 times , total 30 servers.


-------Calculation of Data Size for Cache--------

1. 10% of data ~90% hit rate
2. 20% data ~98-99% hitrate

20%0f 20TB = 4TB

Per Server Cache-128GB
No of servers - > 4TB/128 GB = 30 partitions/shards

No of replications -> 30 *3 = 90



------------------Scaling for Throughput------------------








'''

def base_converseion(value,base_value):
    #digits = [0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g]
    digits = [i for i in string.digits]
    digits.extend([i for i in string.ascii_letters])
    digits.extend(['-','_'])

    digitlist = []
    currvalue = value
    while currvalue >=base_value:
        quotient = value//base_value
        remainder = value % base_value
        digitlist.append(digits[remainder])
        currvalue = quotient

    if currvalue>0:
        digitlist.append(digits[currvalue])
    
    rev_digitlist = digitlist[::-1]
    return "".join(rev_digitlist)

counter = 0
def encode(long_url,base64):
    counter = long_url+1
    short_url = base_converseion(counter,base64)
    #add the front half of the url
    return short_url

def decode(short_url,digitlist):
    #index the digitlist with the short_url
    long_url = digitlist[short_url]
    return long_url
        
print(base_converseion(65,64))