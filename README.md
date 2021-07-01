# jwtbruteforce
brute force and decode jwt
## Installation & Usage
```
python3 -m pip install gsutil 
pip3 install jwcrypto
pip3 install PyJWT==1.7.1
```
## Options
```
usage: jwtbruteforce.py [-h] [-k KIND] [-t TOKEN] [-w WORDLIST] [-p PAYLOAD] [-P PASSWORD] [-a HEADER]

optional arguments:
  -h, --help            show this help message and exit
  -k KIND, --kind KIND  you can choose the value jwt
  -t TOKEN, --token TOKEN
                        token which wanna crack
  -w WORDLIST, --wordlist WORDLIST
                        wordlist which will be used in cracking


```
## Simple usage

```
python3 jwtbruteforce.py -k jwt -t "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcInRlc3RcIixcInJvbGVcIjpcInVzZXJcIn0ifQ.XSPy0jZd8CEtHl2e3C1SjPaewco1tjO3iajbkJy2OFQ" -w /usr/share/wordlists/rockyou.txt
```
 ### tool default  usage wordlist `/usr/share/wordlists/rockyou.txt`
 ```
 python3 jwtbruteforce.py -k jwt -t "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcInRlc3RcIixcInJvbGVcIjpcInVzZXJcIn0ifQ.XSPy0jZd8CEtHl2e3C1SjPaewco1tjO3iajbkJy2OFQ"
 ```
