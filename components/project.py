from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList

class Project(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.projectList = ProjectList(self.testCase)

    def generateRandomProjectName(self):
        projectName = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(5)])
        return projectName

    def enterRandomProjectName(self):
        projectName = self.generateRandomProjectName()
        self.enterProjectName(projectName)

    def enterProjectName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()
        sleep(3)

    def tapCancelButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="button"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def createAProject(self):
        self.projectList.tapCreateProject()
        sleep(2)
        self.enterRandomProjectName()
        sleep(3)
        self.tapSubmit()
        sleep(2)
        self.projectList.selectAProject()

    def getProjectNameOnEditSettings(self):
        el = self.testCase.