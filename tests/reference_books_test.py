import allure


@allure.label("owner", "khilko")
@allure.label("layer", "ui")
@allure.label("module", "Администрирование")
@allure.label("microservice", "referenceBooks")
class TestReferenceBooks:

    @allure.manual
    @allure.label("submodule", "Справочник оплат")
    @allure.feature("Создание новой позиции справочника оплат")
    @allure.tag("pozitive", "smoke")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/referenceBooksPayment', '', 'Справочник оплат')
    @allure.title("Создание новой позиции справочника оплат (название: валидное)")
    def test_reference_books_payment_add_valid_all(self):
        pass

    @allure.manual
    @allure.label("submodule", "Справочник оплат")
    @allure.feature("Создание новой позиции справочника оплат")
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/referenceBooksPayment', '', 'Справочник оплат')
    @allure.title("Создание новой позиции справочника оплат (~название: пусто)")
    def test_reference_books_payment_add_empty_title(self):
        pass

    @allure.manual
    @allure.label("submodule", "Справочник оплат")
    @allure.feature("Создание новой позиции справочника оплат")
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/referenceBooksPayment', '', 'Справочник оплат')
    @allure.title("Создание новой позиции справочника оплат (~название: больше 250 символов)")
    def test_reference_books_payment_add_big_title(self):
        pass


