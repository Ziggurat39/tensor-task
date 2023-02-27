from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class YandexPictures(BasePage):
    
    # Определяем локаторы для работы.
    SEARCH_FIELD = By.CSS_SELECTOR, "input.input__control"
    FIRST_PREVIEW_TITLE = By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0 > a.Link > div.PopularRequestList-SearchText"
    FIRST_PREVIEW = By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0"
    FIRST_PICTURE = By.CSS_SELECTOR, "div.serp-item__preview"
    NEXT_BUTTON = By.CSS_SELECTOR, "div.CircleButton_type_next"
    PREV_BUTTON = By.CSS_SELECTOR, "div.CircleButton_type_prev"
    PIC_ORIGIN = By.CSS_SELECTOR, "img.MMImage-Origin"

    def __init__(self, browser):
        super().__init__(browser)
        self.url = "https://yandex.ru/images/"
    
    # Нажимаем первое популярное превью.
    def click_first_preview(self):
        return self.find_element(self.FIRST_PREVIEW).click()
    
    # Нажимаем первую картиночку. Реализация через AC, поскольку грубо по DOM'у тыкнуть на элемент нельзя, скрипт меняет селекторы.
    def click_first_picture(self):
        ac = ActionChains(self.browser)
        elem = self.find_element(self.FIRST_PICTURE)
        return ac.move_to_element(elem).click().perform()
    
    # Нажимаем кнопку "Вперед" в галерее.
    def click_next_button(self):
        return self.find_element(self.NEXT_BUTTON).click()
    
    # Нажимаем кнопку "Назад" в галерее.
    def click_prev_button(self):
        return self.find_element(self.PREV_BUTTON).click()
    
    # Смотрим, чтобы картиночки менялись (сравниваем по ссылкам).
    # Порой спим, чтобы дождаться full res картинку, поскольку изначально Яндекс грузит превью с другой ссылкой.
    def check_if_gallery_works(self): 
        time.sleep(3) 
        pic1 = self.get_pic(self.PIC_ORIGIN)
        self.click_next_button()
        time.sleep(3)
        pic2 = self.get_pic(self.PIC_ORIGIN)
        self.click_prev_button()
        
        return pic1 == self.get_pic(self.PIC_ORIGIN) and pic1 != pic2
    
    # Смотрим, туда ли мы попали.
    def check_if_url_is_correct(self):
        return self.get_url() == "https://yandex.ru/images/"
    
    # Получаем название первого превью.
    def get_first_preview_title(self):
        return self.find_element(self.FIRST_PREVIEW_TITLE).text
    
    # Сравниваем, что название превью и вправду попало в строку поиска.
    def compare_query_text(self, first_title):
        text_in_field = self.find_element(self.SEARCH_FIELD).get_attribute("value")
        return first_title == text_in_field
