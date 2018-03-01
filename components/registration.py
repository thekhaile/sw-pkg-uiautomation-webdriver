__author__ = 'ningxinliao'
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
    def getRandomEmail(self):
        randomName = ''.join([random.choice(string.letters+string.digits) for i in range(8)])
        randomEmail = randomName + '@ningxintest.com'
        return randomEmail

    def enterRandomEmail(self):
        email = self.getRandomEmail()
        self.enterEmail(email)

    def enterEmail(self,text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Email"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Password"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterConfirmPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Confirm Password"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterContactName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Name"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterCompanyName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Company Name"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRolePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Role"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectContactRole(self, role):
        el = self.getRolePicker()
        el.scrollToValue(role)

    def getCurrentRole(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Role"]')
        el = self.testCase.UIType.Picker(el)
        return el.getLabel()

    def enterCity(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="City"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    # def selectCountry(self, country = 'US'):
    #     print (country)

    def getStateOrProvince(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="State/Province"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectStateOrProvince(self, state):
        el = self.getStateOrProvince()
        el.scrollToValue(state)

    def getUnitOfMeasure(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Unit of Measure"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectUnitOfMeasure(self, UOM):
        el = self.getUnitOfMeasure()
        el.scrollToValue(UOM)

    #   Not Required fields

    # def enterAddress(self, text):
    #     el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, ' ')
    #     el = self.testCase.UIType.TextField(el)
    #     if self.testCase.isChromium:
    #         el.tap()
    #     elif self.testCase.isMobile:
    #         el.tapHybrid()
    #     else:
    #         el.tap()
    #     el.clearText()
    #     el.enterText(text)

    def enterZipCode(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Zip"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterPhoneNumber(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Phone Number"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    # Cancel & Submit button
    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        el.tap()
        sleep(3)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()
        sleep(3)

    # Error msg
    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.error-message.scroll-down')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

