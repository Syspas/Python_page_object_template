from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, locator_q_formatted):
        locator_8_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, 8)
        self.scroll_to_element(locator_8_formatted)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст с ответа')
    def get_answer_text_1(self, locator_a_formatted):
        return self.get_text_from_element(locator_a_formatted)

    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_question(locator_q_formatted)
        return self.get_answer_text_1(locator_a_formatted)






class OrderPage(BasePage):

    @allure.step('Создаем заказ')
    def set_order(self, station_locator, name_locator, name,
                  last_name, address, time, button_locator):
        self.click_to_element(OrderPageLocators.Station_Locator)
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name, last_name)
        self.add_text_to_element(address, address)
        self.click_to_element(time)
        self.click_to_element(button_locator)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self, locator):
        return self.get_text_from_element(locator)
