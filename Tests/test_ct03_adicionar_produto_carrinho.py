import allure
import pytest
from Pages.carrinho_page import CarrinhoPage
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
from secrets import USER, PASSWORD_CORRECT


@allure.title("CT03 - Adicionando produto ao carrinho de compras")
@allure.testcase("https://jirait.embraer.com.br/browse/TQS-2319")
@allure.description("Teste para adicionar mais de um arquivo no carrinho de compra")
@allure.suite("Suite de Compras")
@allure.story("Funcionalidade de compras")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestCT03:
    def test_ct03_adicionar_produto_carrinho(self):

        # Instância os objetos a serem usados nos testes
        base_page = BasePage()
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # Variaveis de produtos
        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bike Light"

        # Fazer login
        with allure.step("CT03 - Step1 - Login screen"):
            base_page.test_with_attachments("CT03_login_screen")
        login_page.fazer_login(USER, PASSWORD_CORRECT)

        # Adicionar os produtos ao carrinho
        with allure.step("CT03 - Step2 - Adicionar produto ao carrinho"):
            base_page.test_with_attachments("CT03_cart")
        home_page.adicionar_ao_carrinho(produto1)

        # Validaçäo do item no carrinho
        home_page.acessar_carrinho()
        with allure.step("CT03 - Step3 - Validar produto no carrinho"):
            base_page.test_with_attachments("ct03_cart_one_product")
        carrinho_page.verificar_produto_carrinho_existe(produto1)

        # Retornar e adicionar outro item no carrinho
        with allure.step("CT03 - Step4 - Continuar comprando e Adicionar mais um prouto"):
            base_page.test_with_attachments("ct03_cart_one_product")
        carrinho_page.cliclar_continuar_comprando()

        # Adicionando outro item no carrinho
        with allure.step("CT03 - Step5 - Adicionar segundo produto ao carrinho"):
            base_page.test_with_attachments("ct03_cart_two_product")
        home_page.adicionar_ao_carrinho(produto2)

        #validando os 2 itens no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        carrinho_page.verificar_produto_carrinho_existe(produto2)
        with allure.step("CT03 - Step6 - Dois produtos no carrinho"):
            base_page.test_with_attachments("ct03_cart_final")
