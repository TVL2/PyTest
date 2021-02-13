def test_item(browser):
    import time

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    assert browser.find_elements_by_css_selector('button.btn-add-to-basket') != [], "НЕТ КНОПКИ"
