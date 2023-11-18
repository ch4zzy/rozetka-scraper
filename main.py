from modules.parser import parse_html


url = "https://rozetka.com.ua/ua/notebooks/c80004/"


if __name__ == '__main__':
    parse_html(url=url, max_pages=67)
