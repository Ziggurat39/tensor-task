import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from pages.yandex_main_page import YandexMain
from pages.yandex_pictures_page import YandexPictures


# Пишем фикстуру драйвера для работы со страничками.
@pytest.fixture
def browser():
    op = webdriver.ChromeOptions()
    op.add_argument("--window-size=1280,800") # Размер окна установил, поскольку именно при этих значениях капча выпадала реже.
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome(options=op) # Если драйвер не определен в PATH, вставляем executable_path="путь до драйвера".
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


# Первый тест из задания.
def test_yandex_search(browser):
    
    # Задаем булевые переменные согласно требованиям.
    isSearchFieldDisplayed = False
    isSuggestMenuActive = False
    isTensorOnTop = False
    
    page = YandexMain(browser)
    page.open()
    
    isSearchFieldDisplayed = page.check_if_search_field_is_presented()
    
    page.input_text("Тензор")
    
    isSuggestMenuActive = page.check_suggest_menu()
    
    page.click_search_button()
    
    isTensorOnTop = page.check_if_tensor_on_top()
    
    # Смотрим, чтобы все что мы хотели - имеет значение True.
    assert isSearchFieldDisplayed and isSuggestMenuActive and isTensorOnTop == True


# Второй тест из задания.
def test_yandex_pictures(browser):
    
    # Задаем булевые переменные согласно требованиям.
    isServicesButtonDisplayed = False
    isCurrentUrlCorrect = False
    isTitleAndQueryAreTheSame = False
    isGalleryWorkCorrect = False
    
    page = YandexMain(browser)
    page.open()
    
    isServicesButtonDisplayed = page.check_if_services_menu_displayed()
    
    page.click_services_menu()
    
    page.click_pictures_services_menu()
    
    page = YandexPictures(browser)
    browser.switch_to.window(browser.window_handles[1])
    
    isCurrentUrlCorrect = page.check_if_url_is_correct()
    
    preview_title = page.get_first_preview_title()
    page.click_first_preview()
    
    isTitleAndQueryAreTheSame = page.compare_query_text(preview_title)
    
    page.click_first_picture()
    
    isGalleryWorkCorrect = page.check_if_gallery_works()
    
    # Смотрим, чтобы все что мы хотели - имеет значение True.
    assert isServicesButtonDisplayed and isCurrentUrlCorrect and isTitleAndQueryAreTheSame and isGalleryWorkCorrect == True
