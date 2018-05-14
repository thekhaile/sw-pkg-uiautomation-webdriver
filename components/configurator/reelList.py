from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule


class ReelList(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.feederSchedule = FeederSchedule(self.testCase)

    def getCreateReel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[text()="Create Reel"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapCreateReel(self):
        el = self.getCreateReel()
        el.tap()
        sleep(2)


    # overflow for edit and delete
    def _getReelOverflow(self, rowOrder):
        # find overflow container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.reel-item-container')
        # find overflow list
        els = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.overflow')
        seletedRow = els[rowOrder]
        return seletedRow

    def tapOverflow(self, rowOrder=0):
        el = self._getReelOverflow(rowOrder)
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getEditButton(self, rowOrder=0):
        overflow = self._getReelOverflow(rowOrder)
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Edit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapEditReel(self):
        el = self.getEditButton()
        el.tap()

    def getDeleteButton(self,rowOrder=0):
        overflow = self._getReelOverflow(rowOrder)
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Delete"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapDeleteReel(self):
        el = self.getDeleteButton()
        el.tap()

    def getConfirmationModal(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.modal-text')
        el = self.testCase.UIType.Element(el)
        return el

    def tapConfirmDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.confirm')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapCancelDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.cancel')
        el = self.testCase.UIType.Button(el)
        el.tap()

    # get the reels table info
    def getSeletedReel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                           'div.selected.reel-list-item-container')
        el = self.testCase.UIType.Element(el)
        return el

    def getReelName(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        reelName = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.header-left')
        reelName = self.testCase.UIType.Element(reelName)
        return reelName.getLabel()

    def getReelPackage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        package = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.package-name')
        package = self.testCase.UIType.Element(package)
        return package.getLabel()

    def getReelSize(self):
        # get reel size info
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[contains(text(), "Reel Size")]')
        # get numeric size
        size = el.text
        number = size.split(' ')[-1]
        number = self.testCase.UIType.Element(number)
        return number

    def getVolumePercentage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        # get volume bar
        reelBar = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.reel-bar')
        volumeBar = reelBar[0]
        percentage = volumeBar.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.display')
        percentage = self.testCase.UIType.Element(percentage)
        return percentage.getLabel()

    def getVolumeBar(self):
        bars = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.background-bar')
        el = bars[0]
        el = self.testCase.UIType.Element(el)
        return el

    def getWeightPercentage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        # get weight bar
        reelBar = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.reel-bar')
        weightBar = reelBar[1]
        percentage = weightBar.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.display')
        percentage = self.testCase.UIType.Element(percentage)
        return percentage.getLabel()

    def getWeightNumber(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.right-side')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWeightBar(self):
        bars = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.background-bar')
        el = bars[-1]
        el = self.testCase.UIType.Element(el)
        return el

    def getReels(self):
        els = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.header-left')
        reels = []
        for i in els:
            i = self.testCase.UIType.Element(i)
            reels.append(i.getLabel())
        return reels

    def getEmptyState(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.empty-configure-section')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()
