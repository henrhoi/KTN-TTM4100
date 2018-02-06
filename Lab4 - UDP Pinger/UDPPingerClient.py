# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *
from sys import argv


# Get the server hostname and port as command line arguments
#address = (argv[1],int(argv[2]))
#host =  address[0]
#port = address[1]
timeout = 1 # in seconds

host = "localhost"
port = 12000
 
# Create UDP client socket

clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout as 1 second
clientSocket.settimeout(1)


# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = "Ping " + str(ptime) + " "
    
    try:

        # Record the "sent time"
        text_time = time.asctime()
        sent_time = time.time()


        # Message format: Ping sequence_number time
        data += str(text_time)

        # Send the UDP packet with the ping message

        clientSocket.sendto(data.encode(), (host,port))

        # Receive the server response
        message, clientAddress = clientSocket.recvfrom(2048)

        # Record the "received time"
        recv_time = time.time()


        # Display the server response as an output
        print("MESSAGE: "+ message.decode())

        # Round trip time is the difference between sent and received time
        RTT = recv_time - sent_time
        print("SENT TIME: " + str(sent_time))
        print("RECV TIME: " + str(recv_time))
        print("RTT = " + str(RTT))
        print()
        print()
        

    except:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        print()
        continue

# Close the client socket
clientSocket.close()
