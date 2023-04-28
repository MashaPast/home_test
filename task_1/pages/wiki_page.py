from selenium.webdriver.common.by import By
from task_1.base_items.base_page import BasePage
from task_1.elements.table import TableElement, TableRows, TableColumns

from task_1.helpers.helper_functions import modify_string
from task_1.models.table_dataclasses import ProgrammingLanguagesTableRaw, ProgrammingLanguagesTable


class WikiPage(BasePage):
    TABLEROWS = TableRows((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr"))
    TABLECOLUMNS = TableColumns((By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr[1]/td"))

    def __init__(self):
        super().__init__()

    def get_four_columns_data(self) -> ProgrammingLanguagesTable:

        len_rows = self.TABLEROWS.get_length()
        len_cols = self.TABLECOLUMNS.get_length()
        list_of_rows = []
        for r in range(1, len_rows + 1):
            row = []
            for c in range(1, len_cols - 1):
                value_from_table = TableElement((By.XPATH,
                                                 f"//table[@class='wikitable sortable jquery-tablesorter'][1]"
                                                 f"/tbody/tr[{r}]/td[{c}]")).get_text()
                row.append(value_from_table)
            table_row = ProgrammingLanguagesTableRaw(website_name=modify_string(row[0]),
                                                     popularity=int(modify_string(row[1])),
                                                     frontend=row[2], backend=row[3])
            list_of_rows.append(table_row)

        return ProgrammingLanguagesTable(rows=list_of_rows)

