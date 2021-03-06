__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase

class RequestQuote(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        sleep(3)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()

    def getErrorMessage(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'span.toast-text')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getQuoteSubmitted(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'span.quote-submitted')
        el = self.testCase.UIType.Element(el)
        return el

    def getEmail(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'textarea')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterEmail(self,text):
        el = self.getEmail()
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRFQSubmissionBanner(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'span.toast-text')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()
