import os
import requests
import time
import concurrent.futures
import asyncio
import aiohttp

def download_image(url):
    try:
        response = requests.get(url)
        img_name = url.split('/')[-1]
        with open(img_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {img_name}")
    except Exception as e:
        print(f"Failed to download image from {url}: {e}")
        
async def async_download_image(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                img_name = url.split('/')[-1]
                with open(img_name, 'wb') as file:
                    file.write(await response.read())
                print(f"Downloaded asynchronously: {img_name}")
    except Exception as e:
        print(f"Failed to download image asynchronously from {url}: {e}")
        
def main(urls):
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
        
        loop = asyncio.get_event_loop()
        tasks = [async_download_image(url) for url in urls]
        loop.run_until_complete(asyncio.gather(*tasks))
        
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
        
if __name__ == "__main__":
    urls = [
        "https://example.com/images/image1.jpg",
        "https://example.com/images/image2.jpg",
        "https://example.com/images/image3.jpg",
    ]
    
    main(urls)