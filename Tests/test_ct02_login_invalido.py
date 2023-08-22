import allure
import pytest
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
from secrets import USER, PASSWORD_INCORRECT


@allure.title("CT02 - Login inválido")
@allure.testcase("https://jirait.embraer.com.br/browse/TQS-2318")
@allure.description("Teste de login inválido")
@allure.suite("Suite de Login")
@allure.story("Funcionalidade de login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestCT02:
    def test_ct02_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        # Instância os objetos a serem usados nos testes
        base_page = BasePage()
        login_page = LoginPage()
        # Fazer login
        with allure.step("CT02 - Step1 - login screen"):
            base_page.test_with_attachments("CT02_login_screen")
        login_page.fazer_login(USER, PASSWORD_INCORRECT)
        # Verificar se o login não foi feito
        login_page.verificar_mensagem_erro_login_existe()
        with allure.step("CT02 - Step2 - Error message displayed"):
            base_page.test_with_attachments("CT02_error_screen")
        # Verificar a mensagem do erro
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)
