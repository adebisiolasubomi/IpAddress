import ipaddress

def check_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False
    

ip = input("Enter an IP address: ")
if check_private_ip(ip):
    print(f"{ip} is a private IP address")
else:
    print(f"{ip} is not a private IP address")