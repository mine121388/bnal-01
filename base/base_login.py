# 导包
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_driver import GetDriver
from tool.get_log import GetLog


class Base:
    """页面对象操作类"""

    def __init__(self):
        """初始化driver对象"""
        self.driver = GetDriver.get_driver()
        GetLog.get_log().info("初始化driver对象: {}".format(self.driver))

    def find_element(self, loc, timeout=30, poll=0.2):
        """获取元素方法"""
        GetLog.get_log().info("查找元素: {} 持续时间: {} 查找频率: {}".format(loc, timeout, poll))
        """定位元素方法加显示等待"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=30, poll=0.2):
        """获取一组元素方法"""
        GetLog.get_log().info("查找元素: {} 持续时间: {} 查找频率: {}".format(loc, timeout, poll))
        """定位元素方法加显示等待"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def input_func(self, loc, values):
        """输入方法"""
        el = self.find_element(loc)
        GetLog.get_log().info("清除{}元素方法".format(loc))
        el.clear()
        GetLog.get_log().info("{}元素输入{}".format(loc, values))
        el.send_keys(values)

    def click_func(self, loc):
        """点击登录方法"""
        self.find_element(loc).click()

    def get_text(self, loc):
        """获取昵称方法"""
        GetLog.get_log().info("获取{}昵称: ".format(loc))
        return self.find_element(loc).text

    def get_toast_msg(self, msg):
        """获取toast消息"""
        GetLog.get_log().info("获取{}昵称: ".format(msg))
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        return self.find_element(loc, timeout=3, poll=0.1).text

    def base_scroll(self, loc1, loc2):
        """滑动"""
        el1 = self.find_element(loc2)
        el22 = self.find_element(loc1)
        self.driver.drag_and_drop(el22, el1)

    def base_get_img(self):
        """截图"""
        self.driver.get_screenshot_as_file("./image/err.png")
        # 将图片写入报告
        self.base_write_img()

    def base_write_img(self):
        """将图片写入报告"""
        with open("./image/err.png", "rb")as f:
            allure.attach("失败原因: ", f.read(), allure.attach_type.PNG)

    def base_click_area(self, text):
        """点击省市区"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.click_func(loc)

    def base_get_text(self, loc):
        """获取一组元素的文本方法"""
        return [el.text for el in self.find_elements(loc)]

    def base_get_text_click(self, text, num=0):
        """用文本获取一组元素并默认点击第一个"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.find_elements(loc)[num].click()
