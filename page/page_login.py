# 导包
import time

import allure
from base.base_login import Base
import page
from tool.get_log import GetLog


class PageLogin(Base):
    """页面对象类"""

    def click_close(self):
        """关闭更新"""
        self.click_func(page.login_img_close)

    def click_my(self):
        """点击我"""
        self.click_func(page.login_my)

    def click_go_input(self):
        """点击已有账号,去登录"""
        self.click_func(page.login_go_input)

    def input_name(self, username):
        """输入用户名"""
        self.input_func(page.login_username, username)

    def input_pwd(self, pwd):
        """输入密码"""
        self.input_func(page.login_pwd, pwd)

    def click_btn(self):
        """点击登录"""
        self.click_func(page.login_btn)

    def get_msg(self):
        """获取昵称"""
        return self.get_text(page.login_nickname)

    def get_toast(self, msg):
        """获取toast"""
        return self.get_toast_msg(msg)

    def click_op(self):
        """点击设置"""
        self.click_func(page.login_op)

    def drag_drop(self):
        """滑动"""
        self.base_scroll(page.login_push_mes, page.login_modify)

    def click_quit(self):
        """点击退出"""
        self.click_func(page.login_quit)

    def click_quit_ok(self):
        """确认退出"""
        self.click_func(page.login_out_ok)

    def page_login(self, username, pwd):
        """组合业务"""
        # GetLog.get_log().info("【登录业务】输入的用户名: {} 输入的密码: {}".format(username, pwd))
        # allure.attach("登录业务: ","输入的用户名: {} 输入的密码: {}".format(username,pwd))
        self.input_name(username)
        self.input_pwd(pwd)
        self.click_btn()

    def page_logout(self):
        """退出业务方法"""
        self.click_op()
        self.drag_drop()
        self.click_quit()
        self.click_quit_ok()

    def page_go_to_login(self):
        """点击我去登陆"""
        self.click_my()
        self.click_go_input()

    def page_login_address(self):
        """登录用于地址管理调用"""
        self.click_close()
        self.page_go_to_login()
        self.page_login(username=13478603122, pwd=123456)
        time.sleep(2)
        self.click_op()

