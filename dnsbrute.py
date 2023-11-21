#antes é preciso instalar dnspython no terminal

import dns.resolver

res = dns.resolver.Resolver()
arquivo = open ("diretorio/da/wordlist/", "r")
subdominios = arquivo.read().splitlines()

alvo = "DOMINIO.COM"

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." _ alvo
		resultado = res.resolve(sub_alvo, "A")
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass