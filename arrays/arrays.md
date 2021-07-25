playing with arrays

# cs448b_ipasn.csv
file included here as an example, the TrafficData.py script downloads it directly from the source. 

source: http://statweb.stanford.edu/~sabatti/data.html

> [Computer Network Traffic Data](http://hci.stanford.edu/courses/cs448b/data/ipasn/cs448b_ipasn.csv) - A ~500K CSV with summary of some real network traffic data from the past. The dataset has ~21K rows and covers 10 local workstation IPs over a three month period. Half of these local IPs were compromised at some point during this period and became members of various botnets. Can you discover when a compromise has occurred by a change in the pattern of communication?
>
> * Each row consists of four columns:
>   * date: yyyy-mm-dd (from 2006-07-01 through 2006-09-30)
>   * l_ipn: local IP (coded as an integer from 0-9)
>   * r_asn: remote ASN (an integer which identifies the remote ISP)
>   * f: flows (count of connnections for that day)
> * Reports of "odd" activity or suspicions about a machine's behavior triggered investigations on the following days (although the machine might have been compromised earlier)
>   * Date : IP
>   * 08-24 : 1
>   * 09-04 : 5
>   * 09-18 : 4
>   * 09-26 : 3 6
