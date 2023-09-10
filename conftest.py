from pytest import fixture
from playwright.sync_api import sync_playwright
from pageObjects.application import App

@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def desctop_app(get_playwright):
    app = App(get_playwright)
    yield app
    app.close()
