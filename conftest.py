import pytest
from task_1.browser.browser_factory import Browser
from task_1.helpers.config_parser import config
from task_1.logger.logger import log
from task_1.pages.wiki_page import WikiPage


@pytest.fixture(scope="session", params=[config["default"]["browser"]])
def browser(request):
    log.debug('Set-up browser')
    driver = Browser.get_browser_by_name(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    log.debug('Quit browser')
    driver.quit()


@pytest.fixture(scope="session")
def get_table_data():
    log.info('Opening page')
    wiki_page = WikiPage()
    wiki_page.open(config["default"]["url"])
    websites = wiki_page.get_four_columns_data()
    yield websites
