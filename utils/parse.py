from typing import Union
from selectolax.parser import Node, HTMLParser

def parse_raw_attributes(node: Union[Node, str], selectors: list[dict]) -> dict:
    # print(node)
    if not issubclass(Node, type(node)):
        node = HTMLParser(node)

    parsed = {}
    for select in selectors:
        match_ = select.get("match")
        type_ = select.get("type")
        selector = select.get("selector")
        name = select.get("name")

        if match_ == "all":
            matched = node.css(selector)
            if type_ == "text":
                parsed[name] = [node.text() for node in matched]
            elif type_ == "node":
                parsed[name] = matched
        
        elif match_ == "first":
            matched = node.css_first(selector)

            if type_ == "text":
                parsed[name] = matched.text()
            elif type_ == "node":
                parsed[name] = matched

    return parsed
            