import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_xpath('//*[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    # If the "button" variable has an empty list, it will cause an error.
    assert button, 'Error! The "Add to basket" button was not found.'
