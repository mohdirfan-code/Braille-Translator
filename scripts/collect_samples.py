import os
import requests

# Make sure the raw data directory exists
raw_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'raw'))
os.makedirs(raw_dir, exist_ok=True)

# Add user-agent header to prevent blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Sample image URLs (public domain)
image_urls = [
    'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gutenberg_Bible_B42_Volume_1_Folio_260r.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/6b/Page_from_Beowulf_manuscript.jpg'
]

# Download images
for idx, url in enumerate(image_urls, start=1):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            file_path = os.path.join(raw_dir, f'page{idx}.jpg')
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded {file_path}')
        else:
            print(f'Failed to download {url} (status code {response.status_code})')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

# Download a sample HTML page (Wikipedia Main Page)
html_url = 'https://en.wikipedia.org/wiki/Main_Page'
try:
    response = requests.get(html_url, headers=headers, timeout=15)
    if response.status_code == 200:
        html_path = os.path.join(raw_dir, 'wikipedia_main.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f'Downloaded {html_path}')
    else:
        print(f'Failed to download {html_url} (status code {response.status_code})')
except Exception as e:
    print(f'Error downloading {html_url}: {e}')