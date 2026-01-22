port_str = "8080"

port = int(port_str)
if 1 <= port <= 65535:
    print("Valid")
else:
    print("Invalid")
