from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@class="my-question-locator-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@class="my-answer-locator-{}"]'
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@class="my-question-locator-7"]'
