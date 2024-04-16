import argparse
import requests
import os


def download_file(url, file_path):
    response = requests.get(url)
    print(f"File path : {file_path}")
    print(f"Abs Path : {os.path.abspath(file_path)}")
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully")
    else:
        print("Failed to download file")


parser = argparse.ArgumentParser()

parser.add_argument("url", help="The url of the image that should be downloaded")
parser.add_argument("file_path", help="Path of the file where it should be downloaded")

args = parser.parse_args()

print(args.url)
print(args.file_path)
download_file(args.url, args.file_path)
