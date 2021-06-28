# jwtbruteforce

### WordList
#### you can use your own wordlist or use other [wordlists](https://github.com/digination/dirbuster-ng/tree/master/wordlists)

# How To Use

#### you can use -h argument
#### you should install [JWT/PyJWT & colorama] on python using requirements file

Example:
```
python3 jwtbruteforce.py -k jwt -t "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcInRlc3RcIixcInJvbGVcIjpcInVzZXJcIn0ifQ.XSPy0jZd8CEtHl2e3C1SjPaewco1tjO3iajbkJy2OFQ" -w /usr/share/wordlists/rockyou.txt

```
# create token
```
python3 jwtbruteforce.py  -P 123456 -a "{"typ":"JWT","alg":"HS256"}" -p {"user":"admin"}  
```
