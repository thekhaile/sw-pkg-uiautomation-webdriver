from time import sleep
from projectBase import ProjectBase

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

    def selectAProject(self, rowOrder=0):
        el = self.getAProject(rowOrder)
        el = self.testCase.UIType.Element(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()

        sleep(3)