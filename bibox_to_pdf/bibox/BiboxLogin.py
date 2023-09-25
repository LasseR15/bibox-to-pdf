import typer
from playwright.sync_api import sync_playwright
from bibox_to_pdf.values.BiboxSelectors import BiboxSelectors
from bibox_to_pdf.values.Constants import Constants
from rich import print


def login_to_bibox(username: str, password: str) -> str:
    with sync_playwright() as p:
        print(f"Logging in to BiBox with user '{username}'")

        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(Constants.biboxLoginUrl)
        page.wait_for_selector(BiboxSelectors.loginBtn)

        page.type(BiboxSelectors.loginUsernameField, username)
        page.type(BiboxSelectors.loginPasswordField, password)

        with page.expect_navigation():
            page.click(BiboxSelectors.loginBtn)

        try:
            page.wait_for_selector(BiboxSelectors.logoutBtn, timeout=10000)
        except:
            print('Login credentials incorrect or a network error occurred.')
            typer.Exit(1)

        access_token = page.evaluate('() => window.localStorage.getItem("oauth.accessToken")')

        page.close()
        browser.close()

        return access_token
