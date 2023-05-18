'''
 Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

'''

def address(ip):
    lst = ip.split('.') # it will split ip address by . and gives a list
    return "[.]".join(lst) # it will join list by [.]