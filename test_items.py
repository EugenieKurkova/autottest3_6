link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket_button(browser):
    browser.implicitly_wait(25)
    browser.get(link)
    assert browser.find_element_by_class_name("btn-add-to-basket").is_displayed(), \
    "add-to-basket-button is not found"
