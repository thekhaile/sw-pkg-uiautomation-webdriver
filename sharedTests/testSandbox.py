from projectBase import ProjectBase



class TestSandbox(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestSandbox, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.textField = TextField(self)

    def testOpen(self):
        self.navigation.navigateToLoginPage()
        self.textField.enterKeyword()