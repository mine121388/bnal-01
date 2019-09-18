# 导包
import time
from appium import webdriver


class GetDriver:
    """操作driver对象类"""
    driver = None

    @classmethod
    def get_driver(cls):
        """获取driver对象"""
        if cls.driver is None:
            # 服务端启动参数
            desired_caps = {}
            # 手机 系统信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            # 设备号
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # 包名
            desired_caps['appPackage'] = 'com.yunmall.lc'
            # 启动名
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # 指定toast消息
            desired_caps['automationName'] = 'Uiautomator2'
            # 允许输入中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 手机驱动对象
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """关闭driver对象"""
        time.sleep(3)
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    GetDriver.get_driver()
    GetDriver.quit_driver()
