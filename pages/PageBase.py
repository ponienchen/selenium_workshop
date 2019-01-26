from abc import ABC, abstractmethod

from client.web_driver_client import WebDriverClient


class PageBase(ABC):

    def __init__(self, webdriver_client: WebDriverClient):
        self.webdriver_client = webdriver_client

    @abstractmethod
    def _required_elements(self) -> list:
        raise NotImplementedError(
            f'ERROR: Method not implemented!'
        )

    def wait_until_all_required_elements_visible(self) -> bool:
        return all(
            [self.webdriver_client.wait_until_visible(e) for e in self._required_elements()]
        )
