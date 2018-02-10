from time import sleep
from projectBase import ProjectBase

class TextField(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def enterKeyword(self):
        el = self.testCase.app.find_element(self.testCase.app.getStrategy().ID, 'lst-ib')
        el = self.testCase.UIType.TextField(el)
        if self.testCase.app.is_mobile():
            el.tap_hybrid()
        else:
            el.tap()
        el.enter_text('hello world')
        sleep(5)