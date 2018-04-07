import json
import os
import requests
from requests import ConnectTimeout, HTTPError, ConnectionError


def reading_file_json():
    data = json.load(open('data.json'))
    return data


def create_category_dir():
    global monitor
    monitor = 'monitor'
    if not os.path.exists(monitor):
        os.makedirs(monitor)


create_category_dir()


def load_url():

    data = reading_file_json()

    for key, values in data.items():
        counter = 1
        for value in values:

            domain_path = key

            if not os.path.exists(monitor + "/" + domain_path):
                os.makedirs(monitor + "/" + domain_path)

            complete_name_html = os.path.join(monitor + "/" + domain_path, f'{counter}.html')
            complete_name_index = os.path.join(monitor + "/" + domain_path, "index.txt")

            index = open(complete_name_index, 'a')

            try:

                site = requests.get(value, allow_redirects=False)

                if site.status_code == 301 or site.status_code == 302:
                    index.write(f'{value} \t {site.status_code}\n')

                elif site.raise_for_status() is None or site.status_code == 200:
                    data = site.content

                    file_html = open(complete_name_html, "wb")  # open file in binary mode
                    file_html.write(data)
                    file_html.close()

                    index.write(f'{value} \t {counter}.html\n')
                    counter += 1

            except (HTTPError, ConnectionError, ConnectTimeout):
                index.write(f'{value} \t {site.status_code}\n')

            except ConnectionResetError:
                index.write(f'{value} \t Connection reset error\n')

            index.close()


load_url()
