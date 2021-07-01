#!/usr/bin/python
import jwt
import sys 
import hashlib
import base64
import json
import re
import hmac
import argparse

def get_arguments():
        parser=argparse.ArgumentParser()
        parser.add_argument("-k","--kind",dest="kind",help="you can choose the value jwt")
        parser.add_argument("-t","--token",dest="token",help="token which wanna crack")
        parser.add_argument("-w","--wordlist",dest="wordlist",default="/usr/share/wordlists/rockyou.txt",help="wordlist which will be used in cracking")
        args = parser.parse_args()
        return args


args=get_arguments()

wordlist=args.wordlist
token=args.token
kind=args.kind
passwords=open(wordlist,'r', encoding='latin-1')

def printarg():
	print("\n[+] Collect The Passwords From The Wordlist")
	print("[+] wordlist:",wordlist)
	#print("[+] Kind:",kind)
	print("[+] Token:",token)


def decodetoken():
	header1=token.split(".")[0]
	header1=base64.urlsafe_b64decode(bytes(json.dumps(header1),encoding='utf8')).decode('utf8').rstrip("=")
	print("\n[+] header",header1)

	payload1=token.split(".")[1]
	#payload1=base64.urlsafe_b64decode(bytes(json.dumps(payload1+ b'=' * (-len(payload1) % 4),encoding='utf8')).decode('utf8').rstrip("="))
	payload1= base64.b64decode(payload1 +'=' * (-len(payload1) % 4)).decode("utf-8")
	payload1=re.sub( r'\\','',payload1)
	print("[+] payload",payload1)
	try:

		signature=token.split(".")[2]
		print("[+] signature=",signature)
	except:
		pass

def jwtcrack():
	correctpassword=""
	for password in passwords:
		password=password.strip()	
		try:
			decode = jwt.decode(token, password, algorithm='HS256')
			print("\n[+] Correct password is:",''.join(password))
			correctpassword=password
			exit()
		except jwt.exceptions.InvalidSignatureError:
			pass
		except jwt.exceptions.DecodeError:
			print("\n[-] Decode Error ")
			exit()
		except KeyboardInterrupt:
			print("KeyboardInterrupt")
			exit()
		
	if correctpassword == "":
		print("[+] The passsword not found in the wordlist\n")
		exit()


if len(sys.argv) > 1:
	if kind=="jwt":
		printarg()
		decodetoken()
		jwtcrack()
		exit()
	
exit()
