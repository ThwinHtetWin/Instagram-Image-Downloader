import requests
import re

#wrote this script as birthday gift for my birthday,july 5 :) 

print("""\n[ : Instagram Image Downloader : ]  by THW \n""")

def download():

    url = input("[+] Please enter image URL: ")
    check_url = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    if check_url:
        get_img = requests.get(url)
        src = get_img.content.decode('utf-8')

        print("[+] Downloading the image ...")
        image_regex = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)',src)
        image_link = image_regex.group()
            #print("Image link : ",image_link)

        pure_image_link = re.sub('meta property="og:image" content="', '', image_link)
            #print("\nPure image link : ",pure_image_link)

        image_size = requests.get(pure_image_link, stream=True)
        final_image_size = int(image_size.headers['Content-Length'])
        default = 256

        filename = input("[+] Enter the name of image : ")

        with open(filename+'.jpg','wb')as f:
            for data in image_size.iter_content(default):
                f.write(data)
            
        print("[+] Download completed !")
    else:
        print("Not Instagram url , please check again.")
        exit()

download()