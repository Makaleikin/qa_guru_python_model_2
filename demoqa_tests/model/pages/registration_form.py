import os
from typing import Tuple
from selene import Element
from selene import have
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys
from demoqa_tests.model.contols import dropdown, modal
from demoqa_tests.model.contols.datepicker import DatePicker
from tests.test_data.user_data import Subject
from tests.test_data.user_data import User
from demoqa_tests.model.contols.dropdown import Select


class RegistrationForm:
    state = Select(browser.element('#state'))
    city = Select(browser.element('#city'))
    hobbies = {'1': 'Sports', '2': 'Reading', '3': 'Music'}

    def filling_registration_form(self, user: [User]):
        browser.open('/automation-practice-form')
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[for^=gender-radio]').by(have.exact_text(user.gender.value)).first.click()
        browser.element('#userNumber').type(user.user_number)
        date_picker = DatePicker(browser.element('#dateOfBirthInput'))
        date_picker.select_date(user.birth_day, user.birth_month, user.birth_year)
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a').type(
        user.birth_day + user.birth_month + user.birth_year).press_enter()
        for subject in user.subjects:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(user.picture_file))
        browser.element('#currentAddress').type(user.current_address)
        self.state.select(user.state)
        self.city.select(user.city)
        browser.element('#submit').click()
        self.should_have_submitted([
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender.value),
            ('Mobile', user.user_number),
            ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
            ('Subjects', 'History, Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'qapicture.png'),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}')
        ])

    def should_have_submitted(self, data):
        rows = modal.dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self
