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
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[@id="root"]/div/main/div/div/form/label[1]/input')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[@id="root"]/div/main/div/div/form/label[2]/input')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)


    def tapSubmit(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[@id="root"]/div/main/div/div/form/button[1]')
        el = self.testCase.UIType.Button(el)
        if self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        sleep(2)
