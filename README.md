# Fast Python Port Scanner 🚀

A custom-built, multithreaded TCP port scanner written in pure Python. 

## 🧠 Why I Built This
I built this tool to understand the fundamentals of networking, TCP handshakes, and how port states work at a low level. Instead of relying on pre-built tools like Nmap, I wrote this to understand how those tools actually function under the hood.

## ⚙️ Features
* **High Speed:** Uses Python's `concurrent.futures` to run 100 concurrent threads.
* **Socket Networking:** Uses the `socket` library to attempt real TCP connections (`connect_ex`).
* **Customizable:** Allows the user to specify the target IP and the exact number of ports to scan.

## 🚀 How to Run
1. Clone this repository to your machine.
2. Open your terminal and run:
   `python scanner.py`
3. Enter your target IP and the number of ports to scan.
