import allure


@allure.label("owner", "khilko")
@allure.label("layer", "ui")
@allure.label("module", "Авторизация")
@allure.feature("Вход в приложение")
@allure.label("microservice", "authentication")
class TestLogin:

    @allure.manual
    @allure.tag("pozitive", "smoke")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (все значения валидные)")
    def test_login_admin_valid_all(self):
        pass

    @allure.manual
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (~логин: пусто; пароль: валидный)")
    def test_login_admin_empty_login(self):
        pass

    @allure.manual
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (логин: валидный; ~пароль: пусто)")
    def test_login_admin_empty_password(self):
        pass
