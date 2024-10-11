import allure
import pytest

from page_object.data import ANSWER_1, ANSWER_NUM_AND_TEXTS, ANSWER_TEXTS
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.main_page import MainPage


class TestMainPage:

    @allure.description(
        'Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_1),
            (1, ANSWER_NUM_AND_TEXTS.get(1)),
            (2, ANSWER_TEXTS[2]),
            (3, 'Ответ на вопрос 4')
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result

