import json

_config = {
    "meta": {
        "name": "Steam Sales Scraper",
        "description": "Extracts The Highest Discounted Games From Steam",
        "author": "Diakite Modibo",
        "version": 0.1
    },
    "url": "https://store.steampowered.com/specials",
    "container": {
            "name": "store_sale_divs",
            "selector": "div[class*='_2hhNOdcC6yLwL_rugP3YLf']",
            "match": "all",
            "type": "node"
    } ,
    "item":[
        {
            "name": "title",
            "selector": "div[class*='_2ekpT6PjwtcFaT4jLQehUK']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "image_link",
            "selector": "img[class*='_2eQ4mkpf4IzUp1e9NnM2Wr']",
            "match": "first",
            "type": "node"
        },
        {
            "name": "tags",
            "selector": "div[class*=_2bkP-3b7dvr0a_qPdZEfHY] > a",
            "match": "all",
            "type": "text"
        },
        {
            "name": "reviewed_by",
            "selector": "div[class*='_1wXL_MfRpdKQ3wZiNP5lrH']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "review_score",
            "selector": "div[class*='_3ZWs0kB-1tuqQtie9KK-E7'] > div",
            "match": "first",
            "type": "text"
        },
        {
            "name": "release_date",
            "selector": "div[class*='_3a6HRK-P6LK0-pxRKXYgyP'] > div",
            "match": "first",
            "type": "text"
        },
        {
            "name": "price_currency",
            "selector": "div[class*='_3fFFsvII7Y2KXNLDk_krOW']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "original_price",
            "selector": "div[class*='_3fFFsvII7Y2KXNLDk_krOW']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "sale_price",
            "selector": "div[class*='_3j4dI1yA7cRfCvK8h406OB']",
            "match": "first",
            "type": "text"
        },
    ]
}


def get_config(load_from_file=True) -> dict:
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)

    


def generete_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)


if __name__ == "__main__":
    generete_config()