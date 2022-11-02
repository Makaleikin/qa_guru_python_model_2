from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.pages.registration_form import RegistrationForm

from test_data.user_data import User, Gender


def test_filling_and_submit_student_registration_form():
    student = User(first_name='Artem', gender=Gender.Male)
    RegistrationForm().filling_registration_form(user=student)