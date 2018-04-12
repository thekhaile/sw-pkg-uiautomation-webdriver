__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.feederSchedule import FeederSchedule


class Reels(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.feederSchedule = FeederSchedule(self.testCase)

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

    # overflow for edit and delete
    def tapOverflow(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditReel(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDeleteReel(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'li.actionable')
        delete = el[1]
        delete = self.testCase.UIType.Button(delete)
        delete.tap()

    def tapConfirmDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.confirm')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapCancelDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.cancel')
        el = self.testCase.UIType.Button(el)
        el.tap()

    # get the reels table info
    def getSeletedReel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                           'div.selected.reel-list-item-container')
        el = self.testCase.UIType.Element(el)
        return el

    def getReelName(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        reelName = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.header-left')
        reelName = self.testCase.UIType.Element(reelName)
        return reelName.getLabel()

    def getReelPackage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        package = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.package-name')
        package = self.testCase.UIType.Element(package)
        return package.getLabel()

    def getReelSize(self):
        # get reel size info
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[contains(text(), "Reel Size")]')
        # get numeric size
        size = el.text
        number = size.split(' ')[-1]
        number = self.testCase.UIType.Element(number)
        return number

    def getVolumePercentage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        # get volume bar
        reelBar = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.reel-bar')
        volumeBar = reelBar[0]
        percentage = volumeBar.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.display')
        percentage = self.testCase.UIType.Element(percentage)
        return percentage.getLabel()

    def getWeightPercentage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        # get weight bar
        reelBar = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.reel-bar')
        weightBar = reelBar[1]
        percentage = weightBar.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.display')
        percentage = self.testCase.UIType.Element(percentage)
        return percentage.getLabel()

    # create reel with different restrictions
    def createReelWithNoRestriction(self):
        self.feederSchedule.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelOverRestrictions(self):
        self.feederSchedule.tapCreateReel()
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
        self.feederSchedule.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        toggle = self.getSIMpullReelToggle()
        if not toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)

    def createReelWithHeightRestrictionOf31(self):
        self.feederSchedule.tapCreateReel()
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
        self.feederSchedule.tapCreateReel()
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
        self.feederSchedule.tapCreateReel()
        self.enterRandomReelName()
        sleep(1)
        self.enterWeight('1000')
        toggle = self.getSIMpullReelToggle()
        if toggle.isOn():
            self.toggleSIMpullReel()
        sleep(1)
        self.tapSubmit()
        sleep(3)











