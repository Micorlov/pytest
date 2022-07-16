from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#intl_homepage1-zone-1 > div.l-container > div > div.column.zn__column--idx-2 > ul > li:nth-child(1) > article > div > div.cd__content > h3 > a > span.cd__headline-text.vid-left-enabled'
        self.NAV_LINK_TEXT = 'Are we alone? The search for life in the universe'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)
