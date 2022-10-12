#!/usr/bin/python3
# Coded by - WebDux -
import os
import time
import requests
from termcolor import colored
import sys

def headers(protocol, target):
	try:
		print(colored("|=========[","yellow"), colored("ზედაპირული სკანირება","red") , colored("]=========|","yellow"))
		r = requests.get(protocol + target)
		for key, value in r.headers.items():
			print(colored(key + ":", "red"),value)
	except:
		print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))

def dnsScan(target):
	try:
        	r = requests.get("https://api.hackertarget.com/dnslookup/?q=" + target)
		if r.text == "error input invalid - enter IP or Hostname":
        		print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
        	else:
        		print(colored("|=========[","yellow"), colored("DNS ჩანაწერები","red") , colored("]=========|","yellow"))
        		print(r.text)
			print(colored("____________________________","red"),"\n")
	except KeyboardInterrupt:
		pass

def network(target):
	try:
		print(colored("|=========[","yellow"), colored("ქსელის ზოგადი სკანირება","red") , colored("]=========|","yellow"))
		os.system("nmap -sV --resolve-all " + target)
		print(colored("____________________________","red"),"\n")
	except KeyboardInterrupt:
		pass

def networkVulns(target): # გასასწორებელია
	try:
		print(colored("|=========[","yellow"), colored("ქსელის სკანირება მოწყვლადობებზე","red") , colored("]=========|","yellow"))
		os.system("nmap -sV --resolve-all --script vulners " + target)
		print(colored("____________________________","red"),"\n")
	except KeyboardInterrupt:
		pass

def geoIp(target):
	try:
		print(colored("|=========[","yellow"), colored("სერვერის გეო ლოკაცია","red") , colored("]=========|","yellow"), "\n")
		r = requests.get("https://api.hackertarget.com/geoip/?q=" + target)
		print(r.text)
		print(colored("____________________________","red"),"\n")
	except KeyboardInterrupt:
		pass

def directory(protocol, target):
	try:
		firstTest = requests.get(protocol + target)
		print(colored("|=========[","yellow"), colored("დირექტორიების ბრუტფორსი","red") , colored("]=========|","yellow"))
		print(colored("\n[INFO] შესაჩერებლად", "green"), colored("CTL + C\n", "yellow"))
		with open('wordlist/wordlist.txt', 'r') as wordlist:
			wordlist = wordlist.readlines()
			for line in wordlist:	
				targetRequest = protocol + target + "/" + line
				r = requests.get(targetRequest)
				if r.status_code == 200:
					print("[+] დირექტორია მოიძებნა: ", colored(targetRequest, "green"))
				elif r.status_code == 403:
					print("[*] წვდომა დახურულია: ", colored(targetRequest, "yellow"))
				else:
					print("[-] დირექტორია არ არსებობს: ", colored(targetRequest, "red"))
			print(colored("[!] ბრუტფორსი დასრულებულია", "green"))
			print(colored("____________________________","red"),"\n")
	except http.client.RemoteDisconnected:
		pass # ხდება მაშინ როცა ssl შეცდომაა
	except KeyboardInterrupt:
		pass # დააჭირე c გასაგრძელებლად ან enter დასასრულებლად

def cms(protocol, target):
	try:
		print(colored("|=========[","yellow"), colored("მოწმდება Content Managment System","red") , colored("]=========|\n","yellow"))
		targetRequest = protocol + target + "/wp-content"
		ifWordpress = requests.get(targetRequest)
		if ifWordpress.status_code == 404:
			pass
			# print(colored("[-] სერვერი არ არის WordPress ძრავზე", "red"))
		elif ifWordpress.status_code == 200 or 401:
			print(colored("[+] სერვერი არის WordPress ძრავზე", "green"))
		else:
			print(colored("\n  Sorry, ძრავი ვერ ამოვიცანი :("))
			print(colored("____________________________","red"),"\n")
	except KeyboardInterrupt:
		pass
	except urllib3.exceptions.LocationParseError:
		pass
	except NameError:
		pass

def waf(target):
	print(colored("|=========[","yellow"), colored("იწყება WAF-ის დადგენა","red") , colored("]=========|","yellow"))
	os.system("wafw00f " + target)
	print(colored("____________________________","red"),"\n")


def subDomains(protocol, target):
	try:
		firstTest = requests.get(protocol + target)
		print(colored("|=========[","yellow"), colored("ქვედომენების ძიება","red") , colored("]=========|","yellow"))
		r = requests.get("https://api.hackertarget.com/hostsearch/?q=" + target)
		domainText = r.text.split("\n")
		# newd = d.replace(",", " [IP]: ")
		out = {}
		numerate = 0
		for domain in domainText:
			out["domain"] = domain
			for values in out.values():
				subdomain = values.replace(",",colored(" [IP]:  ","green"))
				print(colored("[+] ვიპოვე დომენი: ", "green"), colored(subdomain,"red"))
				numerate += 1
		print(colored("\n[*] სულ მოიძებნა", "green"), numerate ,colored("დომენი", "green"))
		print(colored("____________________________","red"),"\n")
	except:
		print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
