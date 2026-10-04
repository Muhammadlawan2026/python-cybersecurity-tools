# python cybersecurity & Network Auditing Tools
A collection of lightweight, efficient python scripts built for scanning, service detection ,and web directory brute-forcing.Designed for penetration testing learning and security reseach.

---

## included Tools

### 1. port scanners
* **'scanner_fast.py'**: A multi-threaded scanner built using 'Concurrent.futures' to scan network ports rapidly
* **'scanner_final.py'**: Advanced port scanner with built-in service detection ('socket.getservbyport') to identify Runnning service on open ports.

* ## 2. Directory Brute-forcer
* * **'dir_bruter.py'**: web enumeration tool that sends HTTP requests to discover direction and sensitive paths on target web servers.
    ---
    ## how to RUN
    ### prerequests
    make sure you have python 3 installed on your system:
    '''bash
    python --version

    python scanner_final.py
    python dir_bruter.py
    
