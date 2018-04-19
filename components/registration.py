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
    def generateRandomEmail(self):
        randomName = ''.join([random.choice(string.letters+string.digits) for i in range(8)])
        randomEmail = randomName + '@ningxintest.com'
        return randomEmail

    def enterRandomEmail(self):
        email = self.generateRandomEmail()
        self.enterEmail(email)

    def enterEmail(self,text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Email"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def enterPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Password"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def enterConfirmPassword(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Confirm Password"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def generateRandomName(self):
        randomLastName = ''.join([random.choice(string.ascii_uppercase) for i in range(5)])
        name = 'Ningxin' + ' ' + randomLastName
        return name

    def enterRandomName(self):
        name = self.generateRandomName()
        self.enterContactName(name)

    def getContactName(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Name"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterContactName(self, text):
        el = self.getContactName()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def generateRandomCompanyName(self):
        companyName = ''.join([random.choice(string.ascii_uppercase) for i in range(6)])
        return companyName

    def enterRandomCompanyName(self):
        name = self.generateRandomCompanyName()
        self.enterCompanyName(name)

    def getCompanyName(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Company Name"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterCompanyName(self, text):
        el = self.getCompanyName()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def getRolePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Role"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def generateRandomRole(self):
        options = ['Southwire Employee', 'Distributor', 'Contractor', 'Sales/Agent', 'Other']
        return random.choice(options)

    def selectRandomRole(self):
        el = self.generateRandomRole()
        self.selectContactRole(el)

    def getSelectedRole(self):
        select = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Role"]')
        options = select.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'option')
        for option in options:
            if option.is_selected() == True:
                break
        el = self.testCase.UIType.Element(option)
        return el.getLabel()

    def selectContactRole(self, role):
        el = self.getRolePicker()
        el.scrollToValue(role)

    def getCurrentRole(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Role"]')
        el = self.testCase.UIType.Picker(el)
        return el.getLabel()

    def generateRandomCity(self):
        city = ''.join([random.choice(string.ascii_uppercase) for i in range(5)])
        return city

    def enterRandomCity(self):
        city = self.generateRandomCity()
        self.enterCity(city)

    def getCity(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="City"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterCity(self, text):
        el = self.getCity()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def generateRandomState(self):
        options = ['California', 'Florida', 'New York', 'Texas']
        return random.choice(options)

    def selectRandomState(self):
        el = self.generateRandomState()
        self.selectStateOrProvince(el)

    def generateRandomProvince(self):
        options = ['Quebec', 'Prince Edward Island', 'Saskatchewan', 'Ontario']
        return random.choice(options)

    def selectRandomProvince(self):
        el = self.generateRandomProvince()
        self.selectStateOrProvince(el)

    def getStateOrProvince(self):
        # This is to return the state dropdown element to be used in other method
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="State/Province"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectStateOrProvince(self, state):
        el = self.getStateOrProvince()
        el.scrollToValue(state)

    def getSelectedStateOrProvince(self):
        select = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="State/Province"]')
        options = select.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'option')
        for option in options:
            if option.is_selected() == True:
                break
        el = self.testCase.UIType.Element(option)
        return el.getLabel()

    def generateRandomUnitOfMeasure(self):
        options = ['Standard', 'Metric']
        return random.choice(options)

    def selectRandomUnitOfMeasure(self):
        el = self.generateRandomUnitOfMeasure()
        self.selectUnitOfMeasure(el)

    def getUnitOfMeasure(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Unit of Measure"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectUnitOfMeasure(self, UOM):
        el = self.getUnitOfMeasure()
        el.scrollToValue(UOM)

    def getSelectedUnitOfMeasure(self):
        select = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Unit of Measure"]')
        options = select.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'option')
        for option in options:
            if option.is_selected() == True:
                break
        el = self.testCase.UIType.Element(option)
        return el.getLabel()

    #Not required fields

    def generateRandomZip(self):
        zip = ''.join([random.choice(string.digits + string.ascii_uppercase) for i in range(6)])
        return zip

    def enterRandomZip(self):
        zip = self.generateRandomZip()
        self.enterZipCode(zip)

    def getZip(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Zip"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterZipCode(self, text):
        el = self.getZip()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

    def generateRandomPhone(self):
        phone = ''.join([random.choice(string.digits) for i in range(10)])
        return phone

    def enterRandomPhone(self):
        phone = self.generateRandomPhone()
        self.enterPhoneNumber(phone)

    def getPhone(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Phone Number"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterPhoneNumber(self, text):
        el = self.getPhone()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.isChromium:
            self.testCase.app.dismissKeyboard()

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

    # Error msg
    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.error-message.scroll-down')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    # Edit Acct Info

    def tapAccount(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.account-link')
        el = self.testCase.UIType.Element(el)
        el.tap()

    def getAccountName(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.title')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()


    """Log Out"""
    def tapLogOut(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.logout')
        el = self.testCase.UIType.Element(el)
        el.tap()





