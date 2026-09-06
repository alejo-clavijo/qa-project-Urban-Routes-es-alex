
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.data import card_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_button = (By.CSS_SELECTOR, '.smart-button')
    phone_field = (By.CLASS_NAME,'np-button')
    phone_number_field = (By.ID,'phone')
    phone_number = (By.CLASS_NAME, 'np-text')
    phone_code = (By.ID, 'code')
    phone_next_button = (By.XPATH, '//button[text()="Siguiente"]')
    confirm_phone_code_button = (By.XPATH, '//button[text()="Confirmar"]')
    payment_method = (By.CLASS_NAME,'pp-button')
    add_card = (By.XPATH, '//div[contains(@class, "pp-row")and .//div[text()="Agregar tarjeta"]]')
    card_number = (By.ID, 'number')
    card_code = (By.CSS_SELECTOR,'input#code.card-input')
    add_card_button = (By.XPATH,'//button[text()="Agregar"]')
    payment_method_text = (By.CLASS_NAME, 'pp-value')
    payment_method_close_button =(By.XPATH, '//div[contains(@class, "payment-picker")]//button[contains(@class,"section-close")]')
    message_for_driver = (By.ID,'comment')
    blanket_and_handkerchiefs = (By.XPATH,'//div[contains(@class,"r-type-switch")][.//div[text()="Manta y pañuelos"]]// span[contains(@class, "slider")]')
    blanket_and_handkerchiefs_checkbox = (By.XPATH, '//div[contains(@class, "r-type-switch")][.//div[text()="Manta y pañuelos"]]//input[@type="checkbox"]')
    ice_cream_plus = (By.XPATH, '//div[contains(@class, "r-type-counter")][.//div[contains(@class, "r-counter-label") and text()="Helado"]]//div[contains(@class, "counter-plus")]')
    ice_cream_value = (By.XPATH, '//div[contains(@class, "r-type-counter")][.//div[contains(@class, "r-counter-label") and text()="Helado"]]//div[contains(@class, "counter-value")]')
    search_taxi_modal = (By.CSS_SELECTOR, '.order.shown .order-header')
    order_taxi_button = (By.CLASS_NAME,'smart-button')
    driver_info = (By.CLASS_NAME,'order-header-title')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def set_from(self, from_address):
        self.wait.until(
         EC.visibility_of_element_located(self.from_field)
     ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
        EC.visibility_of_element_located(self.to_field)
    ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return self.wait.until(
        EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )

    def click_phone_field(self):
        self.driver.find_element(*self.phone_field).click()

    def set_phone_number(self,phone):
        self.driver.find_element(*self.phone_number_field).send_keys(phone)

    def click_phone_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.phone_next_button)
        ).click()

    def set_phone_code(self,code):
        self.driver.find_element(*self.phone_code).send_keys(code)

    def click_confirm_phone_code(self):
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_phone_code_button)
        ).click()

    def set_card_code(self,code):
        card_code_field = self.wait.until(
            EC.visibility_of_element_located(self.card_code)
        )
        card_code_field.send_keys(code)
        card_code_field.send_keys(Keys.TAB)

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()

    def set_card_number(self,number):
        self.driver.find_element(*self.card_number).send_keys(number)

    def click_add_card_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()


    def get_payment_method(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.payment_method_text)
        ).text

    def close_payment_method(self):
        self.wait.until(
            EC.element_to_be_clickable(self.payment_method_close_button)
        ).click()


    def set_message_for_driver(self,message):
        self.driver.find_element(*self.message_for_driver).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver).get_property('value')

    def click_blanket_and_handkerchiefs(self):
        self.wait.until(
            EC.element_to_be_clickable(self.blanket_and_handkerchiefs)
        ).click()


    def get_blanket_and_handkerchiefs(self):
        return self.driver.find_element(*self.blanket_and_handkerchiefs_checkbox).is_selected()

    def click_ice_cream_plus(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_plus)
        ).click()


    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_value).text

    def click_order_taxi_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.order_taxi_button)
        ).click()

    def get_search_taxi_modal(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.search_taxi_modal)
        ).text.split('\n')[0]

    def get_driver_info(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
        self.driver_info,"El conductor llegará en")
        )
        return self.driver.find_element(*self.driver_info).text


    def get_phone(self):
        return self.wait.until(
        EC.visibility_of_element_located(self.phone_number)
    ).text







