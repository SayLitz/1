import requests
from bs4 import BeautifulSoup
import json
import csv
url = "https://health-diet.ru/base_of_food/food_24501/"


req = requests.get(url)
src = req.text


with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)

soup = BeautifulSoup(src, "lxml")

all_products_hrefs = soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find_all("a")
all_products_title = soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find_all("title")


category_bird = {}
for item in all_products_hrefs:
    item_url = item.get("href")
    item_title = item.getText("title",)
    item_full_name = "https://health-diet.ru" + item_url
    category_bird[item_title] = item_full_name

with open("category_bird.json", "w", encoding="utf-8") as file:
    json.dump(category_bird, file, indent=4, ensure_ascii=False)
count = 0
for attribute_name, attribute_url in category_bird.items():

        req = requests.get(url=item_full_name)
        src = req.text

        soup = BeautifulSoup(src, "lxml")

        table_head = soup.find(class_="mzr-tc-chemical-table").find("tr").find_all("td")
        nutrient = table_head[0].text
        count1 = table_head[1].text
        norma = table_head[2].text
        norma_100_g = table_head[3].text
        norma_100_cll = table_head[4].text
        norm_100 = table_head[5].text

        with open(f"data/{count}_{attribute_name}.csv", "w", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=';')

        products_data = soup.find(class_="mzr-tc-chemical-table").find("tbody").find_all("tr")

        for item in products_data:

            products_tds = item.find_all("td")

            title = products_tds[0].text
            count1 = products_tds[1].text
            norma = products_tds[2].text
            norma_100_g = products_tds[3].text
            norma_100_cll = products_tds[4].text
            norm_100 = products_tds[5].text
            print(norma_100_cll)

            with open(f"data/{count}_{attribute_name}.csv", "a", encoding="utf-8-sig") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    (
                        title,
                        count1,
                        norma,
                        norma_100_g,
                        norma_100_cll
                    )
                )
        count += 1


