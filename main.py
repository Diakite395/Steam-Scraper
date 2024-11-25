from selectolax.parser import HTMLParser
from config.tools import get_config
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform, save_to_file
from utils.extract import extract_full_body_html

URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":
    config = get_config()

    html = extract_full_body_html(
        url=config.get("url"),
        wait_for=config.get("container").get("url")
    )
    
    ##### nodes or divs #####
    nodes = parse_raw_attributes(html, [config.get("container")])
    ##### nodes or divs #####
    # tree = HTMLParser(html)
    # divs = tree.css(config.get("container").get("selector"))

    game_data = []
    for node in nodes.get("store_sale_divs"): # I replace divs by nodes
        attrs = parse_raw_attributes(node, config.get("item"))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        save_to_file("extract", game_data)


        # title = d.css_first("div[class*='_3rrH9dPdtHVRMzAEw82AId']").text()
        # image_link = d.css_first("img[class*='_2eQ4mkpf4IzUp1e9NnM2Wr']")
        # tags = [a.text() for a in d.css("div[class*=_2bkP-3b7dvr0a_qPdZEfHY] > a")]
        # reviewed_by = d.css_first("div[class*='_1wXL_MfRpdKQ3wZiNP5lrH']").text()
        # review_score = d.css_first("div[class*='_3ZWs0kB-1tuqQtie9KK-E7'] > div").text()
        # release_date = d.css_first("div[class*='_3a6HRK-P6LK0-pxRKXYgyP'] > div").text()
        # sale_price = d.css_first("div[class*='_3fFFsvII7Y2KXNLDk_krOW']").text()
        # original_price = d.css_first("div[class*='_3j4dI1yA7cRfCvK8h406OB']").text()

        # attrs = {
        #     "ti tle": title,
        #     "tags": tags,
        #     "image": image_link,
        #     "reviewed_by": reviewed_by,
        #     "review_score": review_score,
        #     "release_date": release_date,
        #     "sale_price": sale_price,
        #     "original_price": original_price
        # } 

        # print(attrs)
    