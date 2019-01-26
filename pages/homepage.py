from client.web_driver_client import WebDriverClient


class Homepage:

    INPUT_WHAT = 'css=#text-input-what'
    INPUT_WHERE = 'css=#text-input-where'
    FIND_JOBS = 'css=.icl-WhatWhere-buttonWrapper button'
    URL = 'https://www.indeed.com'

    def __init__(self, webdriver_client: WebDriverClient):
        self.webdriver_client = webdriver_client

    def type_in_what(self, text: str):
        web_element = self.webdriver_client.wait_until_visible(self.INPUT_WHAT)
        self.webdriver_client.execute_js('arguments[0].focus()', web_element)
        web_element.clear()
        web_element.send_keys(text)

    def type_in_where(self, text: str):
        web_element = self.webdriver_client.wait_until_visible(self.INPUT_WHERE)
        self.webdriver_client.execute_js('arguments[0].focus()', web_element)
        web_element.clear()
        web_element.send_keys(text)

    def find_jobs(self):
        web_element = self.webdriver_client.wait_until_visible(self.FIND_JOBS)
        web_element.click()

    def open(self):
        self.webdriver_client.open_page(self.URL)
