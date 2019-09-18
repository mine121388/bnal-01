import sys
import os
sys.path.append(os.getcwd())
# 导包
from page.page_in import PageIn
from tool.get_driver import GetDriver
import pytest
from tool.read_yaml import read_yaml1
from tool.get_log import GetLog

log = GetLog.get_log()


def get_data(key):
    """获取数据"""
    arr = []
    if key == "address_add":
        arr.append(tuple(read_yaml1("address.yaml").get(key).values()))
        return arr
    else:
        arr.append(tuple(read_yaml1("address.yaml").get(key).values()))
        return arr


class TestAddress:

    def setup_class(self):
        """初始化页面对象"""
        self.address = PageIn().add_address()
        self.login = PageIn().get_page_login()
        self.login.page_login_address()

    def teardown_class(self):
        """退出driver对象"""
        GetDriver.quit_driver()

    @pytest.mark.parametrize("recipient, mobile, addr, postcode,pro,city,area", get_data("address_add"))
    def test01_address(self, recipient, mobile, addr, postcode, pro, city, area):
        """新增地址测试方法"""
        self.address.page_go_add_address()
        self.address.page_add_address(recipient, mobile, addr, postcode, pro, city, area)
        # 断言
        expect = recipient + "  " + mobile
        try:
            assert expect in self.address.whether_add_address()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 获取日志
            log.error(e)

    @pytest.mark.parametrize("recipient, mobile, addr, postcode,pro,city,area", get_data("address_update"))
    def test02_update_address(self, recipient, mobile, addr, postcode, pro, city, area):
        """更新地址测试方法"""
        self.address.page_update_address(recipient, mobile, addr, postcode, pro, city, area)
        # 断言
        self.expect = recipient + "  " + mobile
        try:
            assert self.expect in self.address.whether_add_address()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 获取日志
            log.error(e)

    def test03_delete(self):
        """删除地址测试方法"""
        self.address.page_delete_address()
        # 断言
        assert self.address.page_address_is_exists()
