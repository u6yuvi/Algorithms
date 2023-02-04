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