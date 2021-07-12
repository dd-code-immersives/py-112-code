""" 
using the ipaddress library, justin
"""

from ipaddress import ip_address, IPv6Address, IPv4Address

newip = '19.117.63.258'
newip2 = '2001:0db8:0a0b:12f0:0000:0000:0000:0001'


def is_valid_ipv6(ip):
    if type(ip_address(ip)) is IPv6Address:
        return True
    return False
    
is_valid_ipv6(newip2)


def is_valid_ipv4(ip):
    if type(ip_address(ip)) is IPv4Address:
        return True
    return False
    
is_valid_ipv4(newip2)


def ipv4_or_ipv6(ip):
    if type(ip_address(ip)) is IPv4Address:
        return "IPv4"
    if type(ip_address(ip)) is IPv6Address:
        return "IPv6"
    else:
        return "Invalid IP Address"

ipv4_or_ipv6(newip2) 


""" 
ip addresses solution taro 

""" 

#IPv4_ADDRESS
def bitLength(x):
    return int(x).bit_length()

def IPv4_checker_single(x):
    rng = range(0, 9)
    n = (x.split("."))
    if len(n) == 4 and n[0][0] != '0' and bitLength(n[0]) in rng and bitLength(n[1]) in rng and bitLength(n[2]) in rng and bitLength(n[3]) in rng:
        print(f"{x} is valid IPv4 address")
    else:
        print(f"{x} is NOT a valid IPv4 address")

def IPv4_checker_list(x):
    for num in x:
        IPv4_checker_single(num)
        
def IPv4_checker(x):
    if type(x) == str:
        IPv4_checker_single(x)
    elif type(x) == list:
        IPv4_checker_list(x)
    else:
        print(f"Unexpected error: {x} cannot be evaluated'")
  
  #IPv6 ADDRESS
  def IPv6_checker_single(x):
    rng = range(0, 5)
    hexd_alpha = ['a', 'b', 'c', 'd', 'e', 'f']
    x1 = x.split(":")
    if len(x1) < 9:
        for hxt in x1:
            hxt = hxt.lower()
            if len(hxt) in rng:
                for s in hxt:
                    if (s.isalpha()) and (s in hexd_alpha):
                        continue
                    elif (s.isalpha()) and (s not in hexd_alpha):
                        return(print(f"{x} is not a valid IPv6 address"))
            else:
                return(print (f"{x} is not a valid IPv6 address"))
    else:
        return(print (f"{x} is not a valid IPv6 address"))
    return(print(f"{x} is a valid IPv6 address"))

def IPv6_checker_list(x):
    for i in x:
        IPv6_checker_single(i)

def IPv6_checker(x):
    if type(x) == str:
       print(IPv6_checker_single(x))
    elif type(x) == list:
        print(IPv6_checker_list(x))
    else:
        print(f"Unexpected error: {x} cannot be evaluated'")
 
#IPv4_OR_IPv6
 
 def ip_address_checker(x):
    if type(x) == str:
        if len(x.split(".")) == 4:
            IPv4_checker_single(x)
        elif len(x.split(".")) > 4:
            IPv6_checker_single(x)
    elif type(x) == list:
        for ip in x:
            if len(ip.split(".")) == 4:
               IPv4_checker_single(ip)
            elif len(ip.split(":")) > 4:
                IPv6_checker_single(ip) 

""" 

ip address solution dakota 
"""
def isIpv4(ip_address):
  listOfIndividualIpNumbers = ip_address.split(".")
  count = 0
  for x in listOfIndividualIpNumbers:
    x = int(x)
    if(x >= 0 and x <= 255):
      count += 1
  
  if(count == 4):
    print('True')
    return True
  else:
    print('False')
    return False

# isIpv4('19.243.63.126')
# isIpv4('127.256.0.1')


def isIpv6(ip_address):
  strippedIp = ip_address.replace(" ", '')
  count = 0
  for x in strippedIp:
    if(x.isdigit() or x.isalpha() or x == ':'):
      count += 1
  
  if(count == len(strippedIp)):
    print('True')
    return True
  else:
    print('False')
    return False

# isIpv6('2001 ; db8 : 3333 : 4444 : 5555 : 6666 : 7777 : 8888')
# isIpv6('2001 : db8 : 3333 : 4444 : CCCC : DDDD : EEEE : FFFF')