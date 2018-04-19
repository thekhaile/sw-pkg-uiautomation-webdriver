from time import sleep
from projectBase import ProjectBase

class PasswordReset(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def enterEmail(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.app.isMobile():
            self.testCase.app.dismissKeyboard()

    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.secondary')
        el = self.testCase.UIType.TextField(el)
        el.tap()

    def tapReset(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.reset')
        el = self.testCase.UIType.TextField(el)
        el.tap()

    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.error-message.scroll-down')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()