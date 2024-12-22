import os
import requests
from tqdm import tqdm
from urllib.parse import urlparse
import re

def get_filename_from_url(url):
    """Get the file name from the URL or the Content-Disposition header."""
    # First, try to extract the filename from the URL itself
    filename = os.path.basename(urlparse(url).path)
    
    # If the filename is empty, try to get it from the 'Content-Disposition' header
    if not filename:
        try:
            response = requests.head(url, allow_redirects=True)
            content_disposition = response.headers.get('Content-Disposition', '')
            if 'filename=' in content_disposition:
                filename = re.findall('filename="([^"]+)"', content_disposition)[0]
        except requests.RequestException:
            pass

    # If filename is still empty, use a default name
    if not filename:
        filename = 'downloaded_file'
    
    return filename

def download_file(url):
    # Get the filename from the URL or the headers
    filename = get_filename_from_url(url)
    
    # Send a GET request to the URL to fetch the file
    response = requests.get(url, stream=True)
    
    # Raise an exception if the GET request fails
    if response.status_code != 200:
        print(f"Error: {response.status_code}. Failed to fetch URL.")
        return
    
    # Get the total file size from the content-length header
    total_size = int(response.headers.get('content-length', 0))
    
    # Open the file to save it locally
    with open(filename, 'wb') as file, tqdm(
            desc=filename, 
            total=total_size, 
            unit='B', 
            unit_scale=True, 
            ncols=100) as bar:
        
        # Download the file in chunks and write to disk
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))
    
    print(f"Download completed! File saved as {filename}.")

def choice():
    choice = input("\nDo you want to download something again (y/n): ")
    if choice == "y":
        main(0)



def header():
        print('''

     ,     .                                     
     )   . |- ,-.                                
    /    | |  |-'                                
    `--' ' `' `-'                                
    .-,--.                .            .         
    ' |   | ,-. . , , ,-. |  ,-. ,-. ,-| ,-. ,-. 
    , |   | | | |/|/  | | |  | | ,-| | | |-' |   
    `-^--'  `-' ' '   ' ' `' `-' `-^ `-^ `-' '    v1.0  
    - Malinda Vitharana @NEroousl

        ''')
def main_opt():
    # Ask the user to input the download URL
    url = input("Enter the download link: ").strip()
    
    # Check if the URL is valid
    if not url.startswith('http'):
        print("Invalid URL. Please make sure the URL starts with 'http' or 'https'.")
        choice()
    else:
        # Call the download function
        download_file(url)
        choice()


def main(prop):
    if prop==1:
        header()
        main_opt()
    main_opt()


if __name__ == '__main__':
    main(1)