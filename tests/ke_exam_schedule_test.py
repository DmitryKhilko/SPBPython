import allure


@allure.label("owner", "khilko")
@allure.label("layer", "ui")
@allure.label("module", "Квалификационный экзамен")
@allure.label("submodule", "Расписание тестирования")
@allure.label("microservice", "ke_exam")
class TestKE:

    @allure.manual
    @allure.feature("Создание экзамена")
    @allure.tag("pozitive", "smoke")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/keExam', '', 'Расписание КЭ в форме тестирования')
    @allure.title("Создание нового экзамена (все значения валидные)")
    def test_ke_test_valid_all(self):
        pass

    @allure.manual
    @allure.feature("Создание экзамена")
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/keExam', '', 'Расписание КЭ в форме тестирования')
    @allure.title("Создание нового экзамена (все значения пустые)")
    def test_ke_test_empty_all(self):
        pass

    @allure.manual
    @allure.feature("Создание экзамена")
    @allure.tag("negative")
    @allure.link('https://bitrix.ivcmf.by/knowledge/SPB/keExam', '', 'Расписание КЭ в форме тестирования')
    @allure.title("Создание нового экзамена (дата экзамена: пусто; остальные поля валидные)")
    def test_ke_test_empty_exam_date(self):
        pass


