import pytest
from _pytest.fixtures import FixtureRequest

from client.web_driver_client import WebDriverClient
from pages.homepage import Homepage


class TestOpenHomepage:

    @pytest.fixture(autouse=True)
    def pre_test_setup(self, request: FixtureRequest):
        self.webdriver_client = WebDriverClient()
        self.homepage = Homepage(self.webdriver_client)
        request.addfinalizer(
            self.teardown
        )

    def teardown(self):
        if hasattr(self, 'webdriver_client'):
            self.webdriver_client.quit()

    def test_open_homepage(self):
        self.homepage.open()
        self.homepage.type_in_what('developer')
        self.homepage.type_in_where('oakland, ca')
        self.homepage.find_jobs()
