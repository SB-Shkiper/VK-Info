import colorama
import requests
from bs4 import BeautifulSoup
from colorama import Fore
colorama.init()
nad = (Fore.LIGHTBLUE_EX + r"""__      ___      _____        __      
\ \    / / |    |_   _|      / _|     
 \ \  / /| | __   | |  _ __ | |_ ___  
  \ \/ / | |/ /   | | | '_ \|  _/ _ \  
   \  /  |   <   _| |_| | | | || (_) |
    \/   |_|\_\ |_____|_| |_|_| \___/
""")

print(nad)

def get_vk_info(vk_id):
    url = f"https://vk.com/foaf.php?id={vk_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = 'windows-1251'
            soup = BeautifulSoup(response.content, 'lxml-xml')
            text = soup.get_text(separator=' ', strip=True)
            return text
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_vk_friends_info(vk_id):
    url = f"https://onli-vk.ru/pivatfriends.php?id={vk_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml-xml')

            # Extracting all links
            links = [a['href'] for a in soup.find_all('a', href=True)]

            # Extracting all images
            images = [img['src'] for img in soup.find_all('img', src=True)]

            return links, images
        else:
            return f"Error: Received status code {response.status_code}", []
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}", []

if __name__ == "__main__":
    vk_id = input("Enter VK ID: ")
    info = get_vk_info(vk_id)
    links, images = get_vk_friends_info(vk_id)

    print("User  Info:")
    print(info)

    print("\nFriends Links:")
    for link in links:
        print(link)

    print("\nImages:")
    for img in images:
        print(img)

input("Press Enter to exit")
colorama.deinit()
