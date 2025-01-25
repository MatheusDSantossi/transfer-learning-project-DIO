from google_images_download import google_images_download
from icrawler.builtin import GoogleImageCrawler

def download_images(query, limit, output_dir):
    response = google_images_download.googleimagesdownload()
    arguments = {
        'keywords': query,
        'limit': limit,
        'print_urls': True,
        'output_directory': output_dir,
        'format': 'jpg',
        'safe_search': False,
    }
    try:
        paths = response.download(arguments)
        # response.download(arguments)
        print(paths)
        print(f"Downloaded {limit} images for '{query}' to '{output_dir}'")
    except Exception as e:
        print(f"Error downloading images for '{query}': {str(e)}")

def download_images_v2(query, max_num, output_dir):
    crawler = GoogleImageCrawler(storage={"root_dir": output_dir})
    crawler.crawl(keyword=query, max_num=max_num)

# download_images("goose photos", 100, "datasets/gansos")
# download_images_v2("goose photos", 100, "datasets/gansos")
download_images_v2("fotos de gansos animal", 100, "datasets/gansos")
# download_images("duck photos", 100, "datasets/patos")
download_images_v2("fotos de um pato animal", 100, "datasets/patos")
