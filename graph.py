from scapy.all import *
import matplotlib.pyplot as plt
import numpy as np


#Interactive Mode
plt.ion()

#Labels
plt.ylabel("Bytes")
plt.xlabel("Count")
plt.title("Real time Network Traffic")

yData=[]
i=0
while True:
    #Listen for 1 packet
    for pkt in sniff(iface="Intel(R) Dual Band Wireless-AC 8265",count=1):
        if IP in pkt:
                yData.append(pkt[IP].len)
                plt.plot(yData)
                
                # Pause and draw
                plt.pause(0.1)
                i+=1
                #print(yData)
                print(i)
