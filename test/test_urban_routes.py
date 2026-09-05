from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage
from utils.retrive_code import retrieve_phone_code


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        comfort_tariff = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == 'Comfort'

    def test_3_add_phone_nuber(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()

    def test_4_add_credit_card(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()

    def test_5_add_message_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()
        self.routes_page.set_message_for_driver(data.message_for_driver)
        assert self.routes_page.get_message_for_driver() == data.message_for_driver

    def test_6_add_blanket_and_handkerchiefs(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()
        self.routes_page.set_message_for_driver(data.message_for_driver)
        self.routes_page.click_blanket_and_handkerchiefs()
        assert self.routes_page.get_blanket_and_handkerchiefs()

    def test_7_add_two_ice_creams(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()
        self.routes_page.set_message_for_driver(data.message_for_driver)
        self.routes_page.click_blanket_and_handkerchiefs()
        assert self.routes_page.get_blanket_and_handkerchiefs()
        self.routes_page.click_ice_cream_plus()
        self.routes_page.click_ice_cream_plus()
        assert self.routes_page.get_ice_cream_count() == "2"

    def test_8_search_taxi_modal(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()
        self.routes_page.set_message_for_driver(data.message_for_driver)
        self.routes_page.click_blanket_and_handkerchiefs()
        assert self.routes_page.get_blanket_and_handkerchiefs()
        self.routes_page.click_ice_cream_plus()
        self.routes_page.click_ice_cream_plus()
        assert self.routes_page.get_ice_cream_count() == "2"
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.get_search_taxi_modal() == "Buscar automóvil"

    def test_9_wait_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_phone_code()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_payment_method() == "Tarjeta"
        self.routes_page.close_payment_method()
        self.routes_page.set_message_for_driver(data.message_for_driver)
        self.routes_page.click_blanket_and_handkerchiefs()
        assert self.routes_page.get_blanket_and_handkerchiefs()
        self.routes_page.click_ice_cream_plus()
        self.routes_page.click_ice_cream_plus()
        assert self.routes_page.get_ice_cream_count() == "2"
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.get_search_taxi_modal() == "Buscar automóvil"
        print(self.driver.page_source)
        driver_info = self.routes_page.get_driver_info()
        assert "El conductor llegará en" in driver_info




    def teardown_method(self):
      self.driver.quit()
