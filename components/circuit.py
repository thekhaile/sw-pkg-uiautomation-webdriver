__author__ = 'ningxinliao'
import random
import string
from time import sleep

from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule


class Circuit(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.feederSchedule = FeederSchedule(self.testCase)

    # Required Fields
    def getFrom(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="From"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def generateRandomFrom(self):
        circuitFrom = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(8)])
        return circuitFrom

    def enterRandomFrom(self):
        circuitFrom = self.generateRandomFrom()
        self.enterFrom(circuitFrom)

    def enterFrom(self, text):
        el = self.getFrom()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.app.isMobile():
            self.testCase.app.dismissKeyboard()

    def getTo(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="To"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def generateRandomTo(self):
        circuitTo = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(8)])
        return circuitTo

    def enterRandomTo(self):
        circuitTo = self.generateRandomTo()
        self.enterTo(circuitTo)

    def enterTo(self, text):
        el = self.getTo()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.app.isMobile():
            self.testCase.app.dismissKeyboard()

    def getConductorTypePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Metal / Insulation"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def getConductorTypeList(self):
        conductorTypeList = []
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Metal / Insulation"]')
        values = el.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'option')
        values.pop(0)
        for i in values:
            conductorTypeList.append(i.text)
        return conductorTypeList

    def selectConductorType(self, type):
        el = self.getConductorTypePicker()
        el.scrollToValue(type)

    def getConductorSizePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Size"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def getConductorSizeList(self):
        conductorSizeList = []
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@id="conductors"]')
        sizes = el.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'option')
        sizes.pop(0)
        for i in sizes:
            conductorSizeList.append(i.text)
        return conductorSizeList

    def selectConductorSize(self, size):
        el = self.getConductorSizePicker()
        el.scrollToValue(size)

    def getLength(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Length"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def generateRandomLength(self):
        circuitLength = ''.join([random.choice(string.digits) for i in range(5)])
        return circuitLength

    def enterRandomLength(self):
        circuitLength = self.generateRandomLength()
        self.enterCircuitLength(circuitLength)

    def enterCircuitLength(self, text):
        el = self.getLength()
        el.tap()
        el.clearText()
        el.enterText(text)
        if self.testCase.app.isMobile():
            self.testCase.app.dismissKeyboard()

    def getNumOfConductorPicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@id="conductors"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectNumOfConductor(self, NOC):
        el = self.getNumOfConductorPicker()
        el.scrollToValue(NOC)

    def getCommonPreset(self, preset):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@id="%s"]' % preset)
        el = self.testCase.UIType.Button(el)
        return el

    def selectCommonPreset(self, preset):
        el = self.getCommonPreset(preset)
        el.tap()

    def getSelectedColorCircle(self, circleOrder):
        selectedColors = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//li[@class="selected-color"]')
        selectedColor = selectedColors[circleOrder]
        selectedColor= self.testCase.UIType.Element(selectedColor)
        return selectedColor

    def tapSelectedColorCircle(self, circleOrder):
        el = self.getSelectedColorCircle(circleOrder)
        el.tap()

    def getColorOption(self, color):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="button" and @id= "%s"]' % color)
        el = self.testCase.UIType.Element(el)
        return el

    def selectColorOption(self, color):
        el = self.getColorOption(color)
        el.tap()

    # Not Required field
    def getSIMpullHeadToggle(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="checkbox"]')
        el = self.testCase.UIType.Switch(el)
        return el

    def toggleSIMpullHead(self):
        el = self.getSIMpullHeadToggle()
        if self.testCase.isSafari:
            el.tapByLocation()
        else:
            el.tap()

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
        el.tap()

    # Error msg
    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()


    # create circuits with different restrictions
    def createMiniUSCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='250')
        sleep(1)
        self.enterCircuitLength('105')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.tapSubmit()

    def createSmallCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='500')
        sleep(1)
        self.enterCircuitLength('105')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.tapSubmit()

    def createMediumUSCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='600')
        sleep(1)
        self.enterCircuitLength('500')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.tapSubmit()

    def createLargeUSCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='1000')
        sleep(1)
        self.enterCircuitLength('500')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.tapSubmit()

    def createLargeCACircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / RW90')
        sleep(1)
        self.selectConductorSize(size='1000')
        sleep(1)
        self.enterCircuitLength('500')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.tapSubmit()

    def createLargeCASIMpullCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / RW90')
        sleep(1)
        self.selectConductorSize(size='600')
        sleep(1)
        self.enterCircuitLength('500')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.tapSubmit()

    def createCircuitOfDifferentColors(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='1')
        sleep(1)
        self.enterCircuitLength('500')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Brown-Orange-Yellow-Gray')
        sleep(1)
        self.tapSubmit()

    def createCircuitOfDifferentSize(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='1')
        sleep(1)
        self.enterCircuitLength('100')
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.tapSubmit()

    def createCircuitWithSIMpullHead(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='1')
        sleep(1)
        self.enterCircuitLength('100')
        sleep(1)
        self.toggleSIMpullHead()
        sleep(1)
        self.selectNumOfConductor(NOC='4')
        sleep(1)
        self.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.tapSubmit()

    def createGreenCircuit(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='4')
        sleep(1)
        self.enterCircuitLength('100')
        sleep(1)
        self.selectNumOfConductor(NOC='1')
        sleep(1)
        self.selectColorOption(color='Green')
        sleep(1)
        self.tapSubmit()

    def createGreenCircuitOfDifferentSize(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='CU / THHN')
        sleep(1)
        self.selectConductorSize(size='300')
        sleep(1)
        self.enterCircuitLength('100')
        sleep(1)
        self.selectNumOfConductor(NOC='1')
        sleep(1)
        self.selectColorOption(color='Green')
        sleep(1)
        self.tapSubmit()

    def createGreenCircuitOfDifferentMetalInsulation(self):
        self.feederSchedule.tapCreateCircuit()
        self.enterRandomFrom()
        sleep(1)
        self.enterRandomTo()
        sleep(1)
        self.selectConductorType(type='AL / THHN')
        sleep(1)
        self.selectConductorSize(size='4')
        sleep(1)
        self.enterCircuitLength('100')
        sleep(1)
        self.selectNumOfConductor(NOC='1')
        sleep(1)
        self.selectColorOption(color='Green')
        sleep(1)
        self.tapSubmit()



