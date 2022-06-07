# subdorker

subdorker is basically a python script that dorks google for subdomains.
I consider adding some more features in it so please if you have any idea that might be useful drop it on my twitter
			https://twitter.com/AhmedT1337

Installation :

	git clone https://github.com/AhmedT1337/subdorker

	pip3 install -r requirements.txt
	
	
Usage:


	- If you want to dork for  subdomains : 

		python3 subdorker.py -d domain (ex: python 3 subdorker.py -d example.com)

	- If you want to dork for sub-subdomains :

		python3 subdorker.py -d *.domain (ex: python 3 subdorker.py -d *.example.com)

	- If you want this usage menu :

		python3 subdorker.py --help

Strongly suggest running this tool on a VPS or using a VPN so you don't get this error :
	
	requests.exceptions.HTTPError: 429 Client Error: Too Many Requests for url
