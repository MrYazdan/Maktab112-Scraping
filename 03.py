# response = requests.get('https://www.tsetmc.com/instInfo/35425587644337450', headers=headers)
# response = requests.get("https://www.fotmob.com/")
from time import sleep
from typing import Any

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(options=options)
# browser.get('https://www.tsetmc.com/instInfo/35425587644337450')


def until(sleep_time=0.3):
    def _(callback):
        def __(*args, **kwargs):
            while True:
                try:
                    return callback(*args, **kwargs)
                except NoSuchElementException:
                    sleep(sleep_time)

        return __

    return _


@until()
def get_element(selector: str, element: Any = browser):
    return element.find_element(By.CSS_SELECTOR, selector)


@until(0.5)
def get_elements(selector: str, element: Any = browser):
    return element.find_elements(By.CSS_SELECTOR, selector)


# const el = document.querySelector("#d02 > div > div")
# el = get_element("#d02 > div > div", browser)
# span_el = get_element('span', el)

# browser.execute_script("arguments[0].innerHTML = '';", span_el)

# print(el.text)
# sleep(10)


# phase 2:
browser.get('https://www.tsetmc.com')

while True:
    get_element('#search').click()
    search_input = get_element('input[name="search"]')

    namad = input("لطفا نماد خود را وارد کنید: ")

    search_input.send_keys(namad)
    sleep(1)

    link_el = get_element(
        '.jss1 div[ref="eBodyViewport"] .ag-center-cols-clipper .ag-center-cols-container > div:first-child a')
    browser.execute_script('arguments[0].removeAttribute("target")', link_el)
    link_el.click()
    sleep(1)

    el = get_element("#d02 > div > div")
    span_el = get_element('span', el)
    browser.execute_script("arguments[0].innerHTML = '';", span_el)
    print(namad, el.text, "\n")

    browser.back()


