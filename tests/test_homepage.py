import pytest
from _pytest.fixtures import FixtureRequest

from client.web_driver_client import WebDriverClient
from pages.homepage import Homepage


class TestHomepage:

    @pytest.fixture(autouse=True)
    def pre_test_setup(self, env: str, request: FixtureRequest):
        self.webdriver_client = WebDriverClient()
        self.homepage = Homepage(env, self.webdriver_client)
        request.addfinalizer(
            self.teardown
        )

    def teardown(self):
        if hasattr(self, 'webdriver_client'):
            self.webdriver_client.quit()

    def test_perform_one_super_basic_search_without_checking_search_results(self):
        self.homepage.open()
        self.homepage.type_in_what('developer')
        self.homepage.type_in_where('oakland, ca')
        self.homepage.find_jobs()
