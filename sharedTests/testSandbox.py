import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from projectBase import ProjectBase

from sharedComponents.nagivation import Navigation
from sharedComponents.textField import TextField

class TestSandbox(ProjectBase):
    def __init__(self, *args, **kwargs):
        super(TestSandbox, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.textField = TextField(self)

    def testOpen(self):
        self.navigation.navigateToLoginPage()
        self.textField.enterKeyword('hello world')
