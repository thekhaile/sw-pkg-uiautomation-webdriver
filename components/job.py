from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList

class Job(object):
    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.jobList = JobList(self.testCase)

    def enterJobName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Job Name*"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def enterHeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.height')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def getHeight(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.height')
        el = self.testCase.UIType.TextField(el)
        return el.getValue()

    def enterWidth(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.width')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def getWidth(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.width')
        el = self.testCase.UIType.TextField(el)
        return el.getValue()

    def enterWeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.weight')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def getWeight(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.weight')
        el = self.testCase.UIType.TextField(el)
        return el.getValue()

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

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()
        sleep(3)

    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        el.tap()
        sleep(3)

    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def generateRandomName(self):
        randomName = ''.join([random.choice(string.letters + string.digits + " " + " ") for i in range(30)])
        stripName = randomName.strip()
        replaceName = stripName.replace('  ',' ')
        return replaceName

    def enterRandomJobName(self):
        name = self.generateRandomName()
        self.enterJobName(name)

    def createAJob(self):
        self.jobList.tapCreateJob()
        sleep(2)
        self.enterRandomJobName()
        sleep(2)
        self.tapSubmit()




