__author__ = 'ningxinliao'
import random
import string
from time import sleep

from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList


class Reel(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.reelList = ReelList(self.testCase)

    # Required Fields
    def generateRandomName(self):
        randomName = ''.join([random.choice(string.letters + string.digits + " ") for i in range(30)])
        return randomName

    def enterRandomReelName(self):
        name = self.generateRandomName()
        self.enterReelName(name)

    def enterReelName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Reel Name"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomHeight(self):
        randomHeight = ''.join([random.choice(string.digits) for i in range(10)])
        return randomHeight

    def enterRandomHeight(self):
        height = self.getRandomHeight()
        self.enterHeight(height)

    def enterHeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Height"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomWidth(self):
        randomWidth = ''.join([random.choice(string.digits) for i in range(10)])
        return randomWidth

    def enterRandomWidth(self):
        width = self.getRandomWidth()
        self.enterWidth(width)

    def enterWidth(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Width"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomWeight(self):
        randomWeight = ''.join([random.choice(string.digits) for i in range(10)])
        return randomWeight

    def enterRandomWeight(self):
        weight = self.getRandomWeight()
        self.enterWeight(weight)

    def enterWeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Weight"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getSIMpullReelToggle(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="checkbox"]')
        el = self.testCase.UIType.Switch(el)
        return el

    def toggleSIMpullReel(self):
        el = self.getSIMpullReelToggle()
        if self.testCase.isSafari:
            el.tapByLocation()
        else:
            el.tap()

    def getReelNameErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getHeightErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.height')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWidthErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.width')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWeightErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.weight')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

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
        if self.testCase.isChromium:
            self.testCase.app.driver.refresh()
            sleep(6)

    # create reel with different restrictions
    def createReelWithNoRestriction(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelOverRestrictions(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        self.enterHeight('999999')
        self.enterWidth('999999')
        self.enterWeight('999999')
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createSIMpullReelWithNoRestriction(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        toggle = self.getSIMpullReelToggle()
        if not toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelWithHeightRestrictionOf31(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        self.enterHeight('31')
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelWithWidthRestrictionOf21(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        self.enterWidth('21')
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelWithWeightRestrictionOf1000(self):
        self.reelList.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        self.enterWeight('1000')
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    # get inputs
    def getHeightInput(self):
        height = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[text()="Height"]')
        els = height.find_elements(self.testCase.app.getStrategy().XPATH, '//div[@class="text"]')
        el = els[0]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWidthInput(self):
        width = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[text()="Width"]')
        els = width.find_elements(self.testCase.app.getStrategy().XPATH, '//div[@class="text"]')
        el = els[1]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWeightInput(self):
        weight = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//*[text()="Weight"]')
        els = weight.find_elements(self.testCase.app.getStrategy().XPATH, '//div[@class="text"]')
        el = els[-1]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()