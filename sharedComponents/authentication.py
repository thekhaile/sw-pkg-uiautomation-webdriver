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
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="password"]')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="button" and @class="login"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        sleep(2)
