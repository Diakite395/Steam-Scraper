from selectolax.parser import Node
from datetime import datetime
import pandas as pd
import re

def get_attrs_from_node(node: Node, attr: str):
    if node is Node or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node to be provided")
    
    return node.attrs.get("src")


def get_first_n(input_list: list, n: int):
    return input_list[:n]


def reform_date(date_raw: str, input_format: str="%b %d, %Y", output_format: str="%Y-%m-%d"):
    try:
        dt_obj = datetime.strptime(date_raw, input_format)
        return datetime.strftime(dt_obj, output_format)
    except ValueError:
        return date_raw


def regex(input_str: str, pattern: str, do_what: str="findall"):
    if do_what == "findall":
        return re.findall(pattern, input_str)
    elif do_what == "split":
        return re.split(pattern, input_str)
    else:
        raise ValueError('The function expects findall or split to be provided')


def get_currency(raw: str):
    return raw[0]

def get_price(raw) -> float:
    return float(raw[1:])


def format_and_transform(attrs: dict):
    transforms = {
        "image_link": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda input_list: get_first_n(input_list, 5),
        "release_date": lambda date: reform_date(date, "%b %d, %Y", "%Y-%m-%d"),
        "reviewed_by": lambda raw: int(''.join(regex(raw, r"\d+"))),
        "price_currency": lambda raw: get_currency(raw),
        "sale_price": lambda raw: get_price(raw),
        "original_price": lambda raw: get_price(raw)
    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])

    attrs["discount_pct"] = round((attrs["original_price"] - attrs["sale_price"]) / attrs["original_price"] * 100)

    return attrs


def save_to_file(filename="extract", data: list[dict]=None):
    if data is None:
        raise ValueError("The function expects data to be provided as a list of dictionaries")
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime("%Y_%m_%d")}_{filename}.csv"
    df.to_csv(filename, index=False)