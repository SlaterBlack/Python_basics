from DNS import DNS

server = DNS ()

command = input("prompt")
while (command!='q'):
    
    server.update()
    server.lookup()
    #process command
    command = input("prompt")