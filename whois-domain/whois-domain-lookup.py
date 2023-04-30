import whois

sites = ["google.com", "meta.com", "spotify.com"]
comp = [whois.whois(s).org for s in sites]
creation_date = [whois.whois(s).creation_date for s in sites]
emails = [whois.whois(s).emails for s in sites]

print(comp)
print(creation_date)
print(emails)

# whois lookup using ip address
# print(whois.whois("IP"))