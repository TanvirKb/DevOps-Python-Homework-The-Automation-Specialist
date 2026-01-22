urls = [
    "https://api.github.com/v3",
    "https://www.google.com/search?q=test",
    "http://docs.python.org/3/",
]

domains = []

for url in urls:
    host = url.split("//")[1].split("/")[0]
    if "." in host:
        parts = host.split(".", 1)
        host = parts[1]
    domains.append(host)

print(domains)
