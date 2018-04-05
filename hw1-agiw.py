import json
import requests
import os
from requests import HTTPError


def readingfile():
    data = json.load(open('data.json'))
    return list(data)


# def loadpage():
#     listelements = readingfile()
#
#     for elem in listelements:
#         req = urllib.request.Request(elem)
#         with urllib.request.urlopen(req) as response:
#             the_page = response.read()


# def get_headers_from_json():
#     """
# T  he function takes a json file with html_body and returns a list of headers.
# It parses the headers, based on tags starting with 'h'.
# It also parses urls and return them in a tuple: (headers, url)
# """
#     data = json.loads(open('data.json').read())
#     pattern = "h1" # | h2 | h3"
#     # pattern = re.compile("^(?!.(href)).^h", re.IGNORECASE)
#     headers_urls = []
#     all_headers = []
#     for x in tqdm(data):
#         soup = BeautifulSoup(x[0], 'html.parser')
#         html_headers = soup.find_all(re.compile(pattern))
#         all_headers.append(html_headers)
#         url = x[1]
#         tuple_title_url = all_headers, url
#         headers_urls.append(tuple_title_url)
#         return headers_urls


def create_category_dir():
    global monitor
    monitor = 'monitor'
    if not os.path.exists(monitor):
        os.makedirs(monitor)


create_category_dir()


def load_url():
    global cont

    data = json.load(open('data.json'))
    for key, value in data.items():

        domain_path = key

        if not os.path.exists(monitor + "/" + domain_path):
            os.makedirs(monitor + "/" + domain_path)

        cont = cont + 1

        complete_name_html = os.path.join(monitor + "/" + domain_path, f'{cont}.html')
        complete_name_index = os.path.join(monitor + "/" + domain_path, "index.txt")

        if not os.path.exists(complete_name_index):
            index = open(complete_name_index, 'w')

            try:
                site = requests.get(value)
                data = site.text

                file_html = open(complete_name_html, "wb")  # open file in binary mode
                index.write(f'{value} \t {cont}.html')

                file_html.write(str.encode(data))
                file_html.close()

            except HTTPError:
                index.write(f'{value} \t {site.status_code}')

            index.close()


load_url()
