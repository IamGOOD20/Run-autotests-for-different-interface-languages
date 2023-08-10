from selenium.webdriver.common.by import By


class TestPageElements():
    def test_basket_bottom_solution2(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        assert len(browser.find_elements(By.CLASS_NAME, 'add-to-basket')) == 1, '"add to cart" button was not found'
