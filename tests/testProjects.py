from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
# from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs

class TestProjects(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestProjects, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        #self.jobs = Jobs(self)

    @pytest.mark.ac6
    def testCreateAProject(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        currentUrl = self.driver.current_url
        self.projects.enterProjectName('Test Project Name 2')
        sleep(2)
        self.projects.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)