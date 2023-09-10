from playwright.sync_api import Playwright

class App:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)  # создание экземпляра раузера
        self.context = self.browser.new_context()  # создание контекста (то что аля анонимный вход)
        self.page = self.context.new_page()  # создание страницы (там где вкладки браузера) - экземпляр страницы
        self.page.goto("http://127.0.0.1:5000/login") # открываем ссылку на сайт

    # методы взаимодействия со страницей
    def signUp(self):
        self.page.get_by_role("link", name="Sign Up").click()
        self.page.get_by_placeholder("Enter email").fill("tim2@gmail.com")
        self.page.get_by_placeholder("Enter first name").fill("Tim")
        self.page.get_by_placeholder("Enter password").fill("1234567")
        self.page.get_by_placeholder("Confirm password").fill("1234567")
        self.page.get_by_role("button", name="Submit").click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
