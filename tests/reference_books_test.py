import allure


@allure.label("modul", "Администрирование")
@allure.label("layer", "ui")
class TestReferenceBooks:

    @allure.label("owner", "khilko")
    @allure.manual
    @allure.label("submodul", "Справочник оплат")
    @allure.feature("Создание новой позиции справочника оплат")
    @allure.tag("pozitive")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/referenceBooksPayment', '', 'Справочник оплат')
    @allure.title("Создание новой позиции справочника оплат (название: валидное)")
    def test_ReferenceBooksPaymentAddValidAll(self):
        with allure.step("Перейти на страницу 'Справочник оплат'"):
            pass
        with allure.step("Нажать кнопку 'Добавить'"):
            with allure.step("Ожидаем, что отобразилось диалоговое окно 'Добавление позиции в справочник оплат'"):
                pass
        with allure.step("Ввести в поле 'Наименование' наименование новой позиции"):
            pass
        with allure.step("Нажать кнопку 'Ок'"):
            with allure.step("Ожидаем, что новая позиция справочника отобразилась в таблице на странице 'Справочник оплат'"):
                pass

    @allure.label("owner", "khilko")
    @allure.manual
    @allure.label("submodul", "Справочник оплат")
    @allure.feature("Создание новой позиции справочника оплат")
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/referenceBooksPayment', '', 'Справочник оплат')
    @allure.title("Создание новой позиции справочника оплат (~название: пустое)")
    def test_ReferenceBooksPaymentAddEmptyTitle(self):
        pass
