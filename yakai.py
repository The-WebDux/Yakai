#!/usr/bin/python3
# Coded by - WebDux (vakh0) -

import scans
import requests
import os
from termcolor import colored

target = "#"
fromCommand = False
getMenu = False

def menu(clear=0):
	if clear == 1:
		os.system("cls" if os.name == "nt" else "clear")

	if fromCommand == False:
		print("\n")
		print(colored("██╗   ██╗ █████╗ ██╗  ██╗ █████╗ ██╗","yellow"))
		print(colored("╚██╗ ██╔╝██╔══██╗██║ ██╔╝██╔══██╗██║","yellow"))
		print(colored(" ╚████╔╝ ███████║█████╔╝ ███████║██║","yellow"))
		print(colored("  ╚██╔╝  ██╔══██║██╔═██╗ ██╔══██║██║","yellow"))
		print(colored("   ██║   ██║  ██║██║  ██╗██║  ██║██║","yellow"))
		print(colored("   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝","yellow"))
		print(colored("   https://github.com/vakh0/Yakai","grey"))
		print("  #Coded by " + colored("- WebDux -\n", "red"))

	if getMenu == True:
		print(colored("\n      COMMANDS", "yellow") + "\n")
		print(colored("target", "red"), "- სამიზნე ვებ აპლიკაციის Domain/IP")
		print(colored("headers", "red"), "- სერვერის ზედაპირული სკანირება")
		print(colored("dns", "red"), "- DNS სკანირება")
		print(colored("geoip", "red"), "- სერვერის გეო ლოკაციის გაგება")
		print(colored("network", "red"), "- საბაზისო ქსელის სკანირება")
		print(colored("network vulns", "red"), "- ქსელის სკანირება მოწყვლადობებზე")
		print(colored("cms", "red"), "- სერვერის ძრავის სკანირება")
		print(colored("waf", "red"), "- ფაიერვოლის სკანირება")
		# print(colored("cloudfail", "red"), "- სერვერის რეალური აიპის გაგება")
		print(colored("subdomains", "red"), "- ქვედომენების სკანირება")
		print(colored("directory", "red"), "- დამალული ფაილებისა და დირექტორიების ძიება")
		print("") # Seperator for system commands
		print(colored("recon", "red"), "- ზოგადი დაზვერვა")
		print("") # Seperator for system commands
		print(colored("help", "red"), "- ბრძანებების ინსტრუქციის ნახვა")
		print(colored("	", "red"), "- ტერმინალის გასუფთავება")
		# print(colored("tor", "red"), "- ტრაფიკის ტორის ქსელში გადაყვანა")
		print(colored("exit", "red"), "- პროგრამიდან გასვლა")

	terminal()

def setTarget():
	global target
	global protocol
	print(colored("[?] აირჩიე პროტოკოლი", "green"), colored("http", "red"), colored("თუ", "green"), colored("https", "red"), colored("(1/2)", "green"), end="")
	whichProtocol = input(": ")
	if whichProtocol == "1":
		protocol = "http://"
	elif whichProtocol == "2":
		protocol = "https://"
	else:
		print(colored("[შეცდომა] აირჩიე 1 ან 2", "red"))
		setTarget()
	target = input(colored("[?] Domain/IP: ", "green"))

def terminal(command=0):
	global protocol
	global getMenu
	global fromCommand

	if command == "clear":
		os.system("cls" if os.name == "nt" else "clear")
	
	print(colored("\n╭───", "green")+ "(" + colored("Scanner", "red") + colored("@", "green") + colored("Yakai", "red") + ")" + colored("-", "green") + "[" + colored(target, "blue") + "]")
	virtualTerminal = input(colored("╰─$ ", "green"))

	match virtualTerminal:
		case "exit":
			pass
		case "help":
			fromCommand = True
			getMenu = True
			menu()
		case "clear":
			terminal("clear")
		case "headers":
			scans.headers(protocol, target)
			terminal()
		case "dns":
			scans.dnsScan(target)
			terminal()
		case "geoip":
			scans.geoIp(target)
			terminal()
		case "network":
			scans.network(target)
			terminal()
		case "network vulns":
			scans.networkVulns(target)
			terminal()
		case "cms":
			try:
				scans.cms(protocol, target)
				terminal()
			except NameError:
				print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
				terminal()
		case "waf":
			try:
				scans.waf(target)
				terminal()
			except TypeError:
				print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
				terminal()
		case "subdomains":
			try:
				scans.subDomains(protocol, target)
				terminal()
			except NameError:
				print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
		case "directory":
			try:
				scans.directory(protocol, target)
				terminal()
			except NameError:
				print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
				terminal()
		case "recon":
			try:
				scans.headers(protocol.target)
				scans.dnsScan(target)
				scans.network(target)
				scans.networkVulns(target)
				scans.cms(protocol,target)
				scans.subDomains(protocol,target)
				terminal()
			except TypeError:
				print(colored("[შეცდომა] ვერ ვუკავშირდები სერვერს! აკრიფე ", "red"), colored("target","yellow"))
		case "target":
			setTarget()
			terminal()
		case _:
			print(colored("\n[!] ასეთი ბრძანება ვერ მოიძებნა, აკრიფე", "red"), colored("help", "yellow"))
			terminal()
		
if __name__ == "__main__":
	try:
		menu(1)
	except KeyboardInterrupt:
		pass
	except EOFError:
		pass
