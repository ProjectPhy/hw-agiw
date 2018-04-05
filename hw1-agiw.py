import json
import os
from urllib import request


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
        counter = 0
        for value in values:

            domain_path = key

            if not os.path.exists(monitor + "/" + domain_path):
                os.makedirs(monitor + "/" + domain_path)

            counter += 1

            complete_name_html = os.path.join(monitor + "/" + domain_path, f'{counter}.html')
            complete_name_index = os.path.join(monitor + "/" + domain_path, "index.txt")

            index = open(complete_name_index, 'a')

            try:

                site = request.urlopen(value)
                data = site.read()

                file_html = open(complete_name_html, "wb")  # open file in binary mode

                index.write(f'{value} \t {counter}.html\n')
                file_html.write(data)
                file_html.close()

            except (request.HTTPError, request.URLError) as code:
                index.write(f'{value} \t {code}\n')
            except ConnectionResetError:
                index.write(f'{value} \t Connection reset error\n')

            index.close()


load_url()
