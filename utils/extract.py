from playwright.sync_api import sync_playwright
import time


def extract_full_body_html(url, wait_for=None):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
    
        time.sleep(3)
        page.evaluate("() => window.scroll(0, document.body.scrollHeight / 1.5)")
        time.sleep(2)

        if wait_for:
            page.wait_for_selector(wait_for)

        return page.inner_html("body")