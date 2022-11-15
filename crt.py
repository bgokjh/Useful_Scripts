from requests import get
from sys import argv
import urllib3

def get_arg():
    try:
        domain = argv[1]
        return domain
    except:
        text = "[+] Syntax: python3 crt.py <domain>\n"
        text += "    For example:\n"
        text += "\tpython3 crt.py google.com"
        print(text)
        exit(0)

def req(domain):
    url = "https://crt.sh/?output=json&q=" + domain.strip()
    res = get(url, verify=False)
    json = res.json()
    return json

def extract_sub(json):
    subs = []
    for i in json:
        if "\n" in i["name_value"]:
            s = i["name_value"].split("\n")
            subs = subs + s
        else:
            subs.append(i["name_value"])
    return subs

def unique(subs):
    temp = []
    for s in subs:
        if s not in temp:
            temp.append(s)
    return temp

def final(filtered):
    print(f"[+] Found {len(filtered)} Subdomains:")
    [print(f.strip()) for f in filtered]

if __name__ == "__main__":
    urllib3.disable_warnings()
    domain = get_arg()
    json = req(domain)
    subs = extract_sub(json)
    filtered = unique(subs)
    final(filtered)
