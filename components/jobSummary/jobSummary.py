from projectBase import ProjectBase
import os



class JobSummary(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def uploadTemplate(self, filePath):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="file"]')
        cwd = os.getcwd()
        el.send_keys(cwd + filePath)

    def getUploadTemplateOption(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().ID, 'upload-file')
        return el

    def tapConfigureJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.tertiary')
        el = self.testCase.UIType.Button(el)
        el.tap()