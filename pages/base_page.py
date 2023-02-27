# Класс с базовыми операциями для работы с объектами страничек
class BasePage():
    
    # Инициализируем
    def __init__(self, browser):
        self.browser = browser
        self.url = '127.0.0.1'
    
    # Открываем страничку
    def open(self):
        self.browser.get(self.url)
    
    # Ищем элемент по локатору
    def find_element(self, locator):
        return self.browser.find_element(*locator)
    
    # Ищем элементЫ по локатору
    def find_elements(self, locator):
        return self.browser.find_elements(*locator)
    
    # Получаем текущую ссылку
    def get_url(self):
        return self.browser.current_url
    
    # Ловим ссылку на картинку по локатору
    def get_pic(self, locator):
        return self.browser.find_element(*locator).get_attribute("src")
