# from Scrape import scrapper
# # from Detect import read_images_from_folder

# search_key=input("Please Enter the Search key:")
# no_of_images=int(input("Please Enter the number of images to be retrived:"))

# scrapper(search_key,no_of_images)
# # read_images_from_folder(search_key)
import requests
from bs4 import BeautifulSoup
import os
import shutil
import urllib.request 
from cairosvg import svg2png
from PIL import Image
import io

def is_valid_png(data):
    if data[:8] != b'\xff\xd8\xff':
        return False
    

    
def imgsize(data):
    try:
        image = Image.open(io.BytesIO(data))
        image.verify()  # This will raise an exception if the data is not a valid PNG
        return image.size
    except Exception as e:
        print("Failed to verify PNG:", e)
        return image.size
    



def extract_image_urls(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        images = soup.find_all('img')
        
        # Extract src attribute from each image tag
        image_urls = [img['src'] for img in images if 'src' in img.attrs]
        
        return image_urls
    else:
        return "Failed to retrieve webpage."

# Specify the URL you want to scrape
key=input("enter the key")
count=input("enter the count of images")
url = "https://search.brave.com/images?q="+key+"&num=100"
image_urls = extract_image_urls(url)

if(os.path.exists(os.getcwd()+"/Brave_images")):
    shutil.rmtree(os.getcwd()+"/Brave_images")
os.mkdir("Brave_images")

for i in range(0,len(image_urls)):
    try:
        res = requests.get(image_urls[i])
        valid_png = is_valid_png(res.content)

        if(valid_png==False):

            if(imgsize(res.content)!=(32,32)):
                with open('Brave_images/img'+str(i)+'.jpeg','wb') as f:
                    f.write(res.content)

    except Exception as e:
        print("error "+ str(e))
        continue