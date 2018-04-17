from time import sleep
from projectBase import ProjectBase
import string
import random

class Projects(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getAProject(self, rowOrder):
        #get table
        table= self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,'tbody')
        #get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'tr')

        selectedRow = rows[rowOrder]
        return selectedRow

    def getProjectName(self, rowOrder=0):
        row = self.getAProject(rowOrder)
        projectName= row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR,'th')
        projectName = self.testCase.UIType.Element(projectName)
        return projectName.getLabel()

    def getProjectDate(self, rowOrder=0):
        row = self.getAProject(rowOrder)
        projectDate= row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        projectDate = self.testCase.UIType.Element(projectDate)
        return projectDate.getLabel()

    def getProjectJobCount(self, rowOrder=0):
        row = self.getAProject(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        projectjobCount = allTds[1]
        projectjobCount = self.testCase.UIType.Element(projectjobCount)
        return projectjobCount.getLabel()

    def selectAProject(self, rowOrder=0):
        # This is a work-around for MicrosoftEdge not displaying the project table in the timely manner
        if self.testCase.app.isMicrosoftEdge():
            count = 0
            while not self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,'tbody') or count <=100:
                count += 1
                continue
        row = self.getAProject(rowOrder)
        # Had to go to 'th' level to proceed, instead of 'tr' b/c of Firefox issue
        el = row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'th')
        el = self.testCase.UIType.Element(el)
        el.tap()

        sleep(3)

    def tapCreateProject(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.action.create')
        el = self.testCase.UIType.Button(el)
        el.tap()

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
        # get container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.project')
        # find all the Ps listed in the container. Be careful this is finding Ps in Selenium, not our library!!
        allPs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'p')
        # get the last P in the list
        p = allPs[-1]
        # assign P to an element type
        p = self.testCase.UIType.Element(p)
        # return the error message
        return p.getLabel()

    def createAProject(self):
        self.tapCreateProject()
        sleep(2)
        self.enterRandomProjectName()
        sleep(3)
        self.tapSubmit()
        sleep(2)
        self.selectAProject()