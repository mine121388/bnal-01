# 导包
from selenium.webdriver.common.by import By

# 登录
# 点击我
login_my = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号,去登录
login_go_input = By.ID, "com.yunmall.lc:id/textView1"
# 用户名
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 获取昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 关闭更新
login_img_close = By.ID, "com.yunmall.lc:id/img_close"
# 设置
login_op = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 退出
login_quit = By.ID, "com.yunmall.lc:id/setting_logout"
# 修改密码
login_modify = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 消息推送
login_push_mes = By.ID, "com.yunmall.lc:id/setting_notification"
# 确认退出
login_out_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

# 新增地址
# 地址管理
address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_new = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 新增收件人
address_recipient = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 手机号
address_mobile = By.ID, "com.yunmall.lc:id/address_add_phone"
# 详细地址
address_addr = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_postcode = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 所在地区
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 北京省
address_bj = By.XPATH, "//*[contains(@text,'北京市']"
# 北京市大框
address_city_kuang = By.CLASS_NAME, "android.widget.RelativeLayout"
# 北京市
# address_bj1 = By.XPATH, "//*[@text='北京市']"
address_bj1 = By.ID, "com.yunmall.lc:id/area_title"
# 昌平区
address_cp = By.XPATH, "//*[contains(@text,'昌平区']"
# 收件人 手机
address_receipt_name = By.ID, "com.yunmall.lc:id/receipt_name"
# 收件人 地址
address_receipt_address = By.ID, "com.yunmall.lc:id/receipt_address"
# 编辑
address_compile = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 删除
address_delete = By.ID, "com.yunmall.lc:id/delete"
# 确认删除
address_affirm = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
# 收件人姓名手机号
address_receipt_name_phone = By.ID, "com.yunmall.lc:id/receipt_name"
