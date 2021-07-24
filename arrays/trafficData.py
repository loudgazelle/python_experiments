#/usr/local/bin/python3

import urllib.request
import random

# Load the data from remote location (URL)
file = urllib.request.urlopen("http://hci.stanford.edu/courses/cs448b/data/ipasn/cs448b_ipasn.csv", data=None)
# file and description below from: http://statweb.stanford.edu/~sabatti/data.html
# Computer Network Traffic Data - A ~500K CSV with summary of some real network traffic data from the past. The dataset has ~21K rows and covers 10 local workstation IPs over a three month period. Half of these local IPs were compromised at some point during this period and became members of various botnets. Can you discover when a compromise has occurred by a change in the pattern of communication?
#   Each row consists of four columns:
#   * date: yyyy-mm-dd (from 2006-07-01 through 2006-09-30)
#   * l_ipn: local IP (coded as an integer from 0-9)
#   * r_asn: remote ASN (an integer which identifies the remote ISP)
#   * f: flows (count of connnections for that day)

f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')

# Split this single string at the end of lines
lines = text.split("\n")

# Initalising the dictionary
trafficData = {}

# Filling the dictionary
id = 0
print("Number of lines: " + str(len(lines)))

for line in lines:
  if line == "":
    id += 1
  else:
    l = line.strip().split(",")
    #print(id)  
    trafficData[id] = {"date" : l[0], "local_ipn" : l[1], "remote_asn" : l[2], "flows" : l[3]}  
    id += 1
  
# Take a random key from the dictionary and print its value
print(trafficData[random.choice(list(trafficData.keys()))])