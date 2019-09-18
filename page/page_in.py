# 导包
from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:
    """统一工厂类"""

    def get_page_login(self):
        """实例化页面对象"""
        return PageLogin()

    def add_address(self):
        """实例化新增地址页面对象"""
        return PageAddress()

