import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from projectBase import ProjectBase

from sharedComponents.nagivation import Navigation
from sharedComponents.authentication import Authentication

class TestAuthentication(ProjectBase):
    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)

    def testSuccessfulLoginWithValidCredentials(self):
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail('ningxin.liao@mutualmobile.com')
        self.authentication.enterPassword('password')
        self.authentication.tapSubmit()
