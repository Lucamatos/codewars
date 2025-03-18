def domain_name(url):
    if "//www." in url or "www." in url:
        firstDot = url.find(".")
        secondDot = url.find(".", firstDot + 1)
        return url[firstDot+1:secondDot]
    if "//" in url:
        firstBarIndex = url.find("/")
        secondBarIndex = url.find("/", firstBarIndex + 1)
        dotIndex = url.find(".")
        return url[secondBarIndex+1:dotIndex]
    if "." in url:
        return url[:url.find(".")]

"""
Possíveis otimizações:

def domain_name(url):


    #Retorna o nome do domínio extraído da URL.


    # Remove os prefixos de protocolo e 'www.'
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    # Divide a string pelo ponto e retorna o primeiro elemento
    return url.split('.')[0]


import re

def domain_name(url):

    #Retorna o nome do domínio extraído da URL utilizando #expressões regulares.

    # A expressão regular procura por padrões com ou sem protocolo e 'www.'
    match = re.search(r"(?:https?://)?(?:www\.)?([^.]+)", url)
    return match.group(1) if match else None


from urllib.parse import urlparse

def domain_name(url):

    Retorna o nome do domínio extraído da URL utilizando a biblioteca urlparse.

    # Extrai o componente netloc da URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path  # Em casos sem protocolo, urlparse coloca o domínio em path
    # Remove 'www.' se presente
    domain = domain.replace("www.", "")
    # Retorna a primeira parte antes do ponto
    return domain.split('.')[0]
"""
