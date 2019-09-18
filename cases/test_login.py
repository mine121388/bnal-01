import sys
import os
sys.path.append(os.getcwd())
# 导包
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml
import allure
from tool.get_log import GetLog


def data_build():
    """参数化方法"""
    return read_yaml("login.yaml")


class TestLogin:
    """自定义测试类"""

    def setup_class(self):
        """初始化页面对象"""
        self.login = PageIn().get_page_login()
        self.login.click_close()
        self.login.page_go_to_login()

    def teardown_class(self):
        """关闭driver对象"""
        GetDriver.quit_driver()

    @allure.step(title="登录测试方法")
    @pytest.mark.parametrize("username,pwd, expect, succeed", data_build())
    # @pytest.mark.parametrize("username,pwd,expect, succeed", [(13478603121, 123456, "此用户不存在", False)])
    def test_login(self, username, pwd, expect, succeed):
        """登录测试方法"""
        self.login.page_login(username, pwd)
        # 判断是否是正向
        if succeed:
            try:
                msg = self.login.get_msg()
                print("获取的昵称为: ", msg)
                assert msg == expect
            except Exception as e:
                GetLog.get_log().info(e)
                # 截图
                self.login.base_get_img()
                # 抛异常
                raise
            finally:
                self.login.page_logout()
                self.login.page_go_to_login()
        else:
            try:
                toast = self.login.get_toast_msg(expect)
                print("获取的toast为: ", toast)
                assert toast == expect
            except Exception as e:
                GetLog.get_log().info(e)
                # 截图
                self.login.base_get_img()
                # 抛异常
                raise
