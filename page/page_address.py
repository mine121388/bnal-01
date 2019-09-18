import time
import page
from base.base_login import Base


class PageAddress(Base):
    """新增地址页面对象"""

    def click_address(self):
        """点击地址管理"""
        self.click_func(page.address_manage)

    def click_new_address(self):
        """点击新增地址"""
        self.click_func(page.address_new)

    def send_recipient(self, recipient):
        """输入收件人"""
        self.input_func(page.address_recipient, recipient)

    def send_mobile(self, mobile):
        """输入手机号"""
        self.input_func(page.address_mobile, mobile)

    def click_area(self, pro, city, area):
        """点击所在地区"""
        self.click_func(page.address_area)
        # self.click_func(page.address_bj)
        # self.click_func(page.address_city_kuang)
        # self.click_func(page.address_bj1)
        # time.sleep(2)
        # TouchAction(self.driver).tap(x=142,y=373).perform()
        # self.click_func(page.address_cp)
        time.sleep(1)
        self.base_click_area(pro)
        time.sleep(1)
        self.base_click_area(city)
        time.sleep(1)
        self.base_click_area(area)

    def send_addr(self, addr):
        """输入详细地址"""
        self.input_func(page.address_addr, addr)

    def send_postcode(self, postcode):
        """输入邮编"""
        self.input_func(page.address_postcode, postcode)

    def click_default(self):
        """点击设为默认地址"""
        self.click_func(page.address_default)

    def click_save(self):
        """点击保存"""
        self.click_func(page.address_save)

    def whether_add_address(self):
        """是否新增地址"""
        return self.base_get_text(page.address_receipt_name_phone)

    def page_click_edit(self):
        """点击编辑"""
        self.click_func(page.address_compile)

    def page_click_modify(self):
        """点击修改"""
        self.base_get_text_click("修改")

    def page_click_delete(self):
        """点击删除"""
        self.base_get_text_click("删除")

    def page_delete_ok(self):
        """确认删除"""
        self.click_func(page.address_affirm)

    def page_go_add_address(self):
        """进入新增地址业务方法"""
        self.click_address()
        self.click_new_address()

    def page_add_address(self, recipient, mobile, addr, postcode, pro, city, area):
        """新增地址业务方法"""
        self.send_recipient(recipient)
        self.send_mobile(mobile)
        self.click_area(pro, city, area)
        self.send_addr(addr)
        self.send_postcode(postcode)
        self.click_default()
        self.click_save()

    def page_update_address(self, recipient, mobile, addr, postcode, pro, city, area):
        """更新地址业务方法"""
        self.page_click_edit()
        self.page_click_modify()
        self.send_recipient(recipient)
        self.send_mobile(mobile)
        self.click_area(pro, city, area)
        self.send_addr(addr)
        self.send_postcode(postcode)
        self.click_save()

    def page_delete_address(self):
        """删除地址业务方法"""
        # self.click_address()
        for i in range(len(self.base_get_text(page.address_receipt_name_phone))):
            self.page_click_edit()
            self.page_click_delete()
            self.page_delete_ok()

    def page_address_is_exists(self):
        """判断是否删除成功"""
        try:
            self.find_elements(page.address_receipt_name_phone, timeout=2)
            return False
        except:
            return True
