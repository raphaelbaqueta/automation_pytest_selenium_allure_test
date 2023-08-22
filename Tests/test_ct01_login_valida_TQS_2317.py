import allure
import pytest
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
from secrets import USER, PASSWORD_CORRECT


@allure.title("CT01 - Login Válido - TQS-2317")
@allure.testcase("https://jirait.embraer.com.br/browse/TQS-2317")
@allure.description("Teste de login")
@allure.suite("Suite de Login")
@allure.story("Funcionalidade de login")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestCT01:
    def test_ct01_login_valido_TQS_2317(self):
        # Instância os objetos a serem usados nos testes
        base_page = BasePage()
        login_page = LoginPage()
        home_page = HomePage()
        # Fazer login
        with allure.step("CT01 - login screen"):
            base_page.test_with_attachments("CT01_login")
        login_page.fazer_login(USER, PASSWORD_CORRECT)
        # Verifica o login foi realizado
        home_page.verificar_login_com_sucesso()
        with allure.step("CT01 - login success"):
            base_page.test_with_attachments("CT01_login_success")
