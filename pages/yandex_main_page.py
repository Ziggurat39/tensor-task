from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class YandexMain(BasePage):
    
    # Определяем локаторы для работы
    SEARCH_FIELD = By.ID, "text"
    SEARCH_BUTTON = By.CSS_SELECTOR, "button.search3__button"
    SUGGEST_MENU = By.CSS_SELECTOR, "ul.mini-suggest__popup-content"
    SERVICES_MENU = By.CSS_SELECTOR, "a.services-pinned__item"
    SERVICES_MENU_PICTURES = By.XPATH, "//a[@aria-label='Картинки']"
    ORGANIC_URL = By.CSS_SELECTOR, "a.organic__url"
    
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "https:/ya.ru/"
    
    # Смотрим, если поле поиска включено на странице    
    def check_if_search_field_is_presented(self):
        return self.browser.find_element(*self.SEARCH_FIELD).is_enabled()
    
    # Пишем в поле
    def input_text(self, text):
        search_field = self.find_element(self.SEARCH_FIELD)
        return search_field.send_keys(text)
    
    # Кликаем на кнопку поиска
    def click_search_button(self):
        return self.find_element(self.SEARCH_BUTTON).click()
    
    # Смотрим, включилось ли suggest меню
    def check_suggest_menu(self):
        return self.find_element(self.SUGGEST_MENU).is_enabled()
    
    # Смотрим, если меню с сервисами отображено на странице
    def check_if_services_menu_displayed(self):
        return self.find_element(self.SERVICES_MENU).is_displayed()
    
    # Нажимаем на меню с сервисами
    def click_services_menu(self):
        return self.find_element(self.SERVICES_MENU).click()
    
    # Ищем там "Картинки" и смело жмем
    def click_pictures_services_menu(self):
        return self.find_element(self.SERVICES_MENU_PICTURES).click()
    
    # Смотрим, если одна замечательная компания находится по первой ссылке :D
    def check_if_tensor_on_top(self):
        results = self.find_element(self.ORGANIC_URL)
        return results.get_attribute("href") == "https://tensor.ru/"
