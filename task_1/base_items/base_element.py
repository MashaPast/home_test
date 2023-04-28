from abc import ABC
from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from task_1.browser.browser_factory import Browser
from task_1.helpers.config_parser import config


class BaseElement(ABC):
    driver = Browser.get_browser_by_name(config["default"]["browser"])

    def __init__(self, locator: tuple):
        self.locator = locator

    def find_element(self, time=config["default"]["timeout"]) -> WebElement:
        return WebDriverWait(BaseElement.driver, time).until(EC.element_to_be_clickable(self.locator),
                                                             message=f"Can't find element by locator {self.locator}")

    def find_elements(self, time=config["default"]["timeout"]) -> List[WebElement]:
        return WebDriverWait(BaseElement.driver, time).until(EC.presence_of_all_elements_located(self.locator),
                                                             message=f"Can't find elements by locator {self.locator}")

    def get_text(self) -> str:
        return self.find_element().text
