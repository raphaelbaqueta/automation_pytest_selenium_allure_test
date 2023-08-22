import allure
import pytest
from selenium.webdriver.common.by import By
import conftest
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
from secrets import USER, PASSWORD_CORRECT


@allure.title("CT04 - Compra realizada")
@allure.testcase("https://jirait.embraer.com.br/browse/TQS-2320")
@allure.description("Realizando o processo E2E de compra")
@allure.suite("Suite de Compras")
@allure.story("Funcionalidade de compras")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestCT04:
    def test_ct04_compra_produto_carrinho(self):
        driver = conftest.driver
        base_page = BasePage()
        login_page = LoginPage()
        login_page.fazer_login(USER, PASSWORD_CORRECT)
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        #validaçäo do item no carrinho
        assert driver.find_element(By.XPATH,
                                   "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        driver.find_element(By.ID, 'checkout').click()
        driver.find_element(By.ID, 'first-name').send_keys('Raphael')
        driver.find_element(By.ID, 'last-name').send_keys('Barbosa')
        driver.find_element(By.ID, 'postal-code').send_keys('12345-689')
        driver.find_element(By.ID, 'continue').click()
        driver.find_element(By.ID, 'finish').click()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='complete-header' and text()='Thank you for your order!']").is_displayed(

        ), "Mensagem não exibida"
        with allure.step("CT05 - Compra realizada"):
            base_page.test_with_attachments("CT05_compra_feita")
