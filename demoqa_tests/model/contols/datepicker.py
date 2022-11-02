import selene
from selene.support.shared import browser
from selene import Element


# def select_date(day, month, year):
#     browser.element('#dateOfBirthInput').click()
#     browser.element('.react-datepicker__month-select').send_keys(month)
#     browser.element('.react-datepicker__year-select').send_keys(year)
#     browser.element(f'.react-datepicker__day--0{day}').click()

class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_date(self, day, month, year):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self
