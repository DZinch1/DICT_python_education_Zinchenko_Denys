import os
import string
import urllib.parse
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
base_url = "https://www.nature.com"


def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Number must be a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input.")


def clean_filename(title):
    title_with_spaces = title.replace("_", " ")
    cleaned = "".join(
        char
        for char in title_with_spaces
        if char not in string.punctuation or char == " "
    )
    final_filename = "_".join(cleaned.split())
    return final_filename


def create_directory(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{dir_name}': {e}")
        return


def scrape_nature_multipage():
    max_pages = read_int(">")
    target_type = input(">").strip()

    for page_num in range(1, max_pages + 1):
        dir_name = f"Page_{page_num}"
        create_directory(dir_name)
        page_url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page_num}"

        try:
            response = requests.get(page_url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article")

            for article in articles:
                type_tag = article.find("span", {"data-test": "article.type"})
                if not type_tag:
                    continue
                article_type = type_tag.text.strip()

                if article_type.lower() == target_type.lower():
                    link_tag = article.find("a", {"data-track-action": "view article"})
                    if not link_tag:
                        continue

                    article_link = urllib.parse.urljoin(base_url, link_tag.get("href"))
                    original_title = link_tag.text.strip()
                    art_response = requests.get(article_link, headers=headers, timeout=15)
                    art_response.raise_for_status()

                    art_soup = BeautifulSoup(art_response.text, "html.parser")
                    body_tag = art_soup.find("div", class_=lambda x: x and any("body" in c for c in x.split()))
                    if not body_tag:
                        body_tag = art_soup.find("div", class_=lambda x: x and "article-item__body" in x)
                    if not body_tag:
                        body_tag = art_soup.find("main")

                    if body_tag:
                        article_text = body_tag.get_text()
                        no_spaces_title = original_title.replace(" ", "_")
                        no_spaces_text = article_text.replace(" ", "_")

                        file_content = f"{no_spaces_title}\n\n{no_spaces_text}"
                        filename = f"{clean_filename(original_title)}.txt"
                        file_path = os.path.join(dir_name, filename)
                        with open(file_path, "wb") as file:
                            file.write(file_content.encode("utf-8"))
                    else:
                        print(f"Not found {original_title}")

        except requests.exceptions.RequestException as e:
            print(f"Error on page {page_num}: {e}")
        except Exception as e:
            print(f"Unexpected error on page {page_num}: {e}")


if __name__ == "__main__":
    scrape_nature_multipage()
