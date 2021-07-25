#!/usr/local/bin/python3

import urllib.request
import random
from collections import defaultdict

# Load the data from remote location (URL)
file = urllib.request.urlopen("http://hci.stanford.edu/courses/cs448b/data/ipasn/cs448b_ipasn.csv", data=None)
# file and description below from: http://statweb.stanford.edu/~sabatti/data.html
# Computer Network Traffic Data - A ~500K CSV with summary of some real network traffic data from the past. The dataset has ~21K rows and covers 10 local workstation IPs over a three month period. Half of these local IPs were compromised at some point during this period and became members of various botnets. Can you discover when a compromise has occurred by a change in the pattern of communication?
#   Each row consists of four columns:
#   * date:   yyyy-mm-dd  (from 2006-07-01 through 2006-09-30)
#   * l_ipn:  local IP    (coded as an integer from 0-9)
#   * r_asn:  remote ASN  (an integer which identifies the remote ISP)
#   * f:      flows       (count of connnections for that day)

f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')

# Split this single string at the end of lines
lines = text.split("\n")

trafficData = {}

id = 0
print(str(len(lines)) + " rows of data to load")

for line in lines:
  if line == "":
    id += 1
  elif id == 0: #skip the header
    id += 1
  else:
    column = line.strip().split(",")
    trafficData[id] = {"date" : column[0], "local_ipn" : column[1], "remote_asn" : column[2], "flows" : column[3]}  
    id += 1
  
print(str(id) + " rows loaded")
# Take a random key from the dictionary and print its value
print(trafficData[random.choice(list(trafficData.keys()))])

p = 1
while(p <= len(lines)-2 ):
  #print(trafficData[p(list(trafficData.keys()))])
  print(trafficData[p])
  p +=1

# get some stats on this data
# this isn't doing anything valuable yet, i'm not sure what it's doing
# sum(value == 0 for value in trafficData.keys())

# todo
# create something to group by host + asn and sort by number of flows per day
# analyze to determine the date that each host saw a big increase in flows to a specific asn

local_ipn_freqdict = defaultdict(int)
remote_asn_freqdict = defaultdict(int)
combo_freqdict = defaultdict(int)
for item in trafficData:
  local_ipn = trafficData[item]["local_ipn"]
  remote_asn = trafficData[item]["remote_asn"]
  combo = trafficData[item]["local_ipn"] + trafficData[item]["remote_asn"]


  local_ipn_freqdict[local_ipn] += 1
  remote_asn_freqdict[remote_asn] += 1
  combo_freqdict[local_ipn, remote_asn] += 1

print(str(len(local_ipn_freqdict)) + " unique local hosts")
print(str(len(remote_asn_freqdict)) + " unique remote ASNs")
print(str(len(combo_freqdict)) + " unique local hosts and remote ASNs")

# print(freqdict)
print(combo_freqdict)
# s = set( val for dic in trafficData for val in dic.values())