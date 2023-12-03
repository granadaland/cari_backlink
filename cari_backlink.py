import requests
from bs4 import BeautifulSoup

def cari_situs_domain_spesifik(query, domain, jumlah_halaman):
    urls = []
    for halaman in range(0, jumlah_halaman * 10, 10):
        headers = {"User-Agent": "Mozilla/5.0"}
        query_full = f"{query} site:{domain}"
        page = requests.get(f"https://www.google.com/search?q={query_full}&start={halaman}", headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if "url?q=" in href and not "webcache" in href:
                url_potensial = href.split("url?q=")[1].split("&sa=U")[0]
                if domain in url_potensial:
                    urls.append(url_potensial)
    return urls

# Contoh query pencarian
query = "tambahkan komentar Anda"  # atau kata kunci lain yang relevan

# Domain yang diinginkan
domains = ["go.id", "ac.id", "gov", "edu"]

# Jumlah halaman yang ingin dicari per domain
jumlah_halaman = 2

for domain in domains:
    print(f"Mencari situs dengan domain {domain}...")
    urls_potensial = cari_situs_domain_spesifik(query, domain, jumlah_halaman)
    for url in urls_potensial:
        print(url)
