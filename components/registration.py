from time import sleep
from projectBase import ProjectBase
import string
import random

class Registration(object):
    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    # Required fields
    def enterContactName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, '')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    # def getContactRole(self):
    #     el = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, ' ')
    #     el = self.testCase.UIType.Picker(el)
    #     return el

    def selectContactRole(self, role = 'Southwire Employee'):
        print role

    def enterCompanyName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterEmail(self,text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '  ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterCity(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def selectStateOrProvince(self, state = 'some state/province'):
        print state

    def selectUnitOfMeasure(self, UOM = 'Standard'):
        print UOM

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterConfirmPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    #   Not Required fields
    def enterTitle(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterAddress(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterZipCode(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    def enterPhoneNumber(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        el.clearText()
        el.enterText(text)

    # Cancel & Submit button
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
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        sleep(3)

    # Error msg
    def getErrorMsg(self):
        # get container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.project.job')
        # find all the Ps listed in the container. Be careful this is finding Ps in Selenium, not our library!!
        allPs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'p')
        #get the last P in the list
        p = allPs[-1]
        #assign P to an element type
        p = self.testCase.UIType.Element(p)
        #return the error message
        return p.getLabel()