# jwtbruteforce

### WordList
#### you can use your own wordlist or use other [wordlists](https://github.com/digination/dirbuster-ng/tree/master/wordlists)

## Installation & Usage

# How To Use

#### you can use -h argument
#### you should install [JWT/PyJWT & colorama] on python using requirements file
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
  -p PAYLOAD, --payload PAYLOAD
                        PAYLOAD:DATA
  -P PASSWORD, --password PASSWORD
                        key
  -a HEADER, --header HEADER
                        HEADER:ALGORITHM & TOKEN TYPE

```
## Simple usage

```
python3 jwtbruteforce.py -k jwt -t "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcInRlc3RcIixcInJvbGVcIjpcInVzZXJcIn0ifQ.XSPy0jZd8CEtHl2e3C1SjPaewco1tjO3iajbkJy2OFQ" -w /usr/share/wordlists/rockyou.txt

```
# create token
```
python3 jwtbruteforce.py  -P 123456 -a "{"typ":"JWT","alg":"HS256"}" -p {"user":"admin"}  
```
