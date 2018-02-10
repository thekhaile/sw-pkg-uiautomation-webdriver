import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
print sys.path
from projectBase import ProjectBase
# from  import Navigation
# from ..sharedComponents.textField import TextField

class TestSandbox(ProjectBase):
    def __init__(self, *args, **kwargs):
        super(TestSandbox, self).__init__(*args, **kwargs)
        # self.navigation = Navigation(self)
        # self.textField = TextField(self)

    def testOpen(self):
        # self.navigation.navigateToLoginPage()
        # self.textField.enterKeyword()
        print 'hello world'

# def main():
#     sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
#     print sys.path
#
# main()