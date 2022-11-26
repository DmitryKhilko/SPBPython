import allure


@allure.label("owner", "khilko")
@allure.label("layer", "ui")
@allure.label("module", "Авторизация")
@allure.feature("Вход в приложение")
@allure.label("microservice", "authentication")
@allure.link('https://bitrix.ivcmf.by/knowledge/SPB/login', '', 'Вход в приложение')
@allure.link('https://bitrix.ivcmf.by/knowledge/SPB/logout', '', 'Выход из приложения')
class TestLogin:

    @allure.id("153")
    @allure.manual
    @allure.tag("positive", "smoke")
    @allure.title("Вход в приложение под ролью Администратор (все значения валидные)")
    def test_login_admin_valid_all(self):
        with allure.step("Открыть браузер"):
            pass
        with allure.step("Ввести в браузере адрес https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что загрузилась страница с заголовком 'Авторизация'"):
                pass
        with allure.step("В поле ввода 'Логин' ввести валидный логин"):
            pass
        with allure.step("В поле ввода 'Пароль' ввести валидный пароль"):
            pass
        with allure.step("Нажать кнопку 'Войдите'"):
            with allure.step("Ожидаем, что загрузилась страница с главным меню приложения"):
                pass
            with allure.step("Ожидаем, что вывелось сообщение 'Вы успешно вошли в систему'"):
                pass
        with allure.step("Выйти из приложения"):
            with allure.step("Ожидаем, что загрузилась страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Закрыть браузер"):
            pass

    @allure.id("154")
    @allure.manual
    @allure.tag("negative")
    @allure.title("Вход в приложение под ролью Администратор (~логин: пусто; пароль: валидный)")
    def test_login_admin_empty_login(self):
        with allure.step("Открыть браузер"):
            pass
        with allure.step("Ввести в браузере адрес https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что загрузилась страница с заголовком 'Авторизация'"):
                pass
        with allure.step("Оставить поле ввода 'Логин' пустым"):
            pass
        with allure.step("В поле ввода 'Пароль' ввести валидный пароль"):
            pass
        with allure.step("Нажать кнопку 'Войдите'"):
            with allure.step("Ожидаем, что под полем ввода 'Логин' вывелось сообщение 'Поле обязательно для заполнения!"):
                pass
            with allure.step("Ожидаем, что вход в приложение не произошел"):
                pass
        with allure.step("Закрыть браузер"):
            pass

    @allure.id("155")
    @allure.manual
    @allure.tag("negative")
    @allure.title("Вход в приложение под ролью Администратор (логин: валидный; ~пароль: пусто)")
    def test_login_admin_empty_password(self):
        with allure.step("Открыть браузер"):
            pass
        with allure.step("Ввести в браузере адрес https://acc-test-loc.ivcmf.by/"):
            with allure.step("Ожидаем, что загрузилась страница с заголовком 'Авторизация'"):
                pass
        with allure.step("В поле ввода 'Логин' ввести валидный логин"):
            pass
        with allure.step("Оставить поле ввода 'Пароль' пустым"):
            pass
        with allure.step("Нажать кнопку 'Войдите'"):
            with allure.step("Ожидаем, что под полем ввода 'Пароль' вывелось сообщение 'Поле обязательно для заполнения!"):
                pass
            with allure.step("Ожидаем, что вход в приложение не произошел"):
                pass
        with allure.step("Закрыть браузер"):
            pass
