from selenium.webdriver.common.by import By
from task_1.base_items.base_page import BasePage
from task_1.elements.table import Table

from task_1.helpers.helper_functions import modify_string
from task_1.models.table_dataclasses import ProgrammingLanguagesTableRaw, ProgrammingLanguagesTable


class WikiPage(BasePage):
    WEBSITES = Table((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[1]"))
    PROGRAMMING_LANG = Table((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[2]"))
    FRONTEND = Table((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[3]"))
    BACKEND = Table((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[4]"))

    def __init__(self):
        super().__init__()

    def get_popularity_values(self):
        elements_with_websites = self.WEBSITES.find_elements()
        elements_with_popularity_values = self.PROGRAMMING_LANG.find_elements()
        elements_with_frontend_technologies = self.FRONTEND.find_elements()
        elements_with_backend_technologies = self.BACKEND.find_elements()

        websites = []
        for i in range(len(elements_with_websites)):
            table_raw = ProgrammingLanguagesTableRaw(website_name=elements_with_websites[i].text,
                                                     popularity=int(
                                                         modify_string(elements_with_popularity_values[i].text)),
                                                     frontend=elements_with_frontend_technologies[i].text,
                                                     backend=elements_with_backend_technologies[i].text)
            websites.append(table_raw)

        return ProgrammingLanguagesTable(rows=websites)
