import requests
import pandas as pd

api_url = "https://berita-indo-api-next.vercel.app/api/cnn-news/teknologi"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    berita_list = []

    for artikel in data["data"]:
        # Mengambil bagian terakhir dari URL sebagai 'creator'
        name = artikel["link"].split('/')[-1]
        creator = name.replace('-', ' ').title()

        # Menambahkan data ke list
        berita_list.append({
            'Judul': artikel["title"],
            'Link': artikel["link"],
            'Deskripsi Singkat': artikel["contentSnippet"],
            'Tanggal': pd.to_datetime(artikel["isoDate"]),
            'Gambar Kecil': artikel["image"]["small"],
            'Gambar Besar': artikel["image"]["large"],
            'Creator': creator
        })

    df = pd.DataFrame(berita_list)

    creator_counts = df['Creator'].value_counts().reset_index()
    creator_counts.columns = ['Creator', 'Jumlah Berita']
    creator_counts_sorted = creator_counts.sort_values(by='Jumlah Berita', ascending=False)

    print("\nDataFrame setelah diurutkan berdasarkan jumlah berita terbanyak:")
    print(creator_counts_sorted)
else:
    print("Error:", response.status_code)