from DNSB import DNSB

server = DNSB()

while (command!='q'):
    
    server.update()
    server.lookup()
    #process command
    command = input("prompt")