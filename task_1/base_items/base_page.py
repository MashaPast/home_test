from abc import ABC
from task_1.browser.browser_factory import Browser
from task_1.helpers.config_parser import config


class BasePage(ABC):
    driver = Browser.get_browser_by_name(config["default"]["browser"])

    def open(self, url):
        return self.driver.get(url)

