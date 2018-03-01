from time import sleep
from projectBase import ProjectBase

class Authentication(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def enterEmail(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="text"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="password"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit" and @class="login"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()
        sleep(3)

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.tapSubmit()

    def tapCreateAccount(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.secondary')
        el = self.testCase.UIType.Button(el)
        el.tap()
