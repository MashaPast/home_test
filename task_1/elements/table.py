from task_1.base_items.base_element import BaseElement


class TableElement(BaseElement):
    def __init__(self, locator: tuple):
        super().__init__(locator)


class TableRows(BaseElement):
    def __init__(self, locator: tuple):
        super().__init__(locator)

    def get_length(self) -> int:
        return len(self.find_elements())


class TableColumns(BaseElement):
    def __init__(self, locator: tuple):
        super().__init__(locator)

    def get_length(self) -> int:
        return len(self.find_elements())

