from sys import argv
from googlesearch import search
from art import tprint

tprint("SUB-DORK-ER")
print("			Author : @AHMEDT1337")



def usage() :
    print("""
####################################################

Usage: 
	- If you want to dork for  subdomains : 

		python3 subdorker.py -d domain

	- If you want to dork for sub-subdomains :

		python3 subdorker.py -d *.domain

	- If you want this usage menu :

		python3 subdorker.py --help

####################################################
	    """)



def dorking(domain) :

	query = f"site:*.{domain}"

	sh = search(query)


	file = open(f"{domain}.txt", "a")


	for item in sh :

		file.writelines(item+"\n")

	file.close()

	print(f"Results are put in a file named {query}.txt")



if len(argv) < 3 or argv[1].lower() == '--help' or argv[1].lower() == '-help' :

    usage()


elif argv[1].lower() == '-d' :

    domain = str(argv[2])
    
    dorking(domain)
