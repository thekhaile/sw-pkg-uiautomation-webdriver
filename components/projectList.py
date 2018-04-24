from time import sleep
from projectBase import ProjectBase

class ProjectList(object):
    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getAProject(self, rowOrder):
        # get table
        table= self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,'tbody')
        # get the list of rows from the table
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
        count = 0
        while not self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody') or count <= 100:
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

    def getProjectCount(self):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')
        return len(rows)

    def _getProjectOverflow(self, rowOrder):
        els = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        selectedRow = els[rowOrder]
        return selectedRow

    def tapOverflow(self, rowOrder=0):
        el = self._getProjectOverflow(rowOrder)
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditSettings(self, rowOrder=0):
        overflow = self._getProjectOverflow(rowOrder)
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Edit Settings"]')
        el = self.testCase.UIType.Button(el)
        el.tap()