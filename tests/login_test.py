import allure


@allure.label("modul", "Авторизация")
@allure.feature("Вход в приложение")
@allure.label("microservice", "authentication")
@allure.label("layer", "ui")
class TestLogin:
    @allure.id("136")
    @allure.label("owner", "khilko")
    @allure.manual
    @allure.tag("pozitive", "smoke")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (логин: валидный; пароль: валидный)")
    def test_loginAdminValidAll(self):
        with allure.step("Ввести в браузере web-адрес тестового сервера https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что откроется страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Ввести в поле ввода логина валидный логин"):
            pass
        with allure.step("Ввести в поле ввода пароля валидный пароль"):
            pass
        with allure.step("Нажать кнопку входа в приложение"):
            with allure.step(
                    "Ожидаем, что на открывшейся странице отобразится сообщение 'Вы успешно вошли в систему'"):
                pass
        with allure.step("Выйти из приложения"):
            with allure.step("Ожидаем, что откроется страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Закрыть браузер"):
            pass
    @allure.id("139")
    @allure.label("owner", "khilko")
    @allure.manual
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (~логин: пустой; пароль: валидный)")
    def test_loginAdminEmptyLogin(self):
        with allure.step("Ввести в браузере web-адрес тестового сервера https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что откроется страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Оставить поле ввода логина пустым"):
            pass
        with allure.step("Ввести в поле ввода пароля валидный пароль"):
            pass
        with allure.step("Нажать кнопку входа в приложение"):
            with allure.step(
                    "Ожидаем, что под полем ввода логина появится сообщение 'Поле обязательно для заполнения!'"):
                pass
        with allure.step("Закрыть браузер"):
            pass
    @allure.id("140")
    @allure.label("owner", "khilko")
    @allure.manual
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
    @allure.title("Вход в приложение под ролью Администратор (логин: валидный; ~пароль: пустой)")
    def test_loginAdminEmptyPassword(self):
        with allure.step("Ввести в браузере web-адрес тестового сервера https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что откроется страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Ввести в поле ввода логина валидный логин"):
            pass
        with allure.step("Оставить поле ввода пароля пустым"):
            pass
        with allure.step("Нажать кнопку входа в приложение"):
            with allure.step(
                    "Ожидаем, что под полем ввода пароля появится сообщение 'Поле обязательно для заполнения!'"):
                pass
        with allure.step("Закрыть браузер"):
            pass

