# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 14:42
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : prodcategpage.py
# @Software: PyCharm

import allure
from public.pages import basepage
from config import globalparam


class FolderPgae(basepage.Page):
    pass


class ProdCategPage(FolderPgae):
    """产品分类"""

    @allure.step("服务目录-产品分类页面")
    def open_prod_catg_page(self):
        self.log.debug("打开服务目录-产品分类页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/folder/prodCateg")

    @allure.step("单击新建按钮")
    def click_new_create_prod_button(self):
        self.log.debug("单击新建按钮")
        self.dr.click("xpath->//button[contains(.,'新建')]")

    # 新建产品分类
    @allure.step("")
    def input_systematic_name(self, value):
        self.log.debug("输入分类名称")
        self.dr.type_and_enter("xpath->//input[@name='name']", value)

    def input_systematic_number(self, value):
        self.log.debug("输入分类序号")
        self.dr.type_and_enter("xpath->//input[@name='id']", value)

    def click_produc_category_icon(self):
        self.log.debug("单击产品分类图标")
        self.dr.click("xpath->//button[contains(.,'选择产品分类图标')]")

    def click_cloud_host_icon(self):
        self.log.debug("单击云主机图标")
        # self.dr.click("xpath->//div/ul/li[contains(.,'云主机')]")
        self.dr.click("xpath->//div[2]/div/ul/li[2]/i")

    def click_cloud_disk_icon(self):
        self.log.debug("单击云磁盘图标")
        self.dr.click("xpath->//li[contains(.,'云磁盘')]")

    def click_bare_metal_server_icon(self):
        self.log.debug("单击裸金属服务器图标")
        self.dr.click("xpath->//div[2]/div/ul/li/i")

    def click_phy_res_icon(self):
        self.log.debug("单击物理资源图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[4]/i")

    def click_loadbalance_icon(self):
        self.log.debug("单击负载均衡器图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[5]/i")

    def click_public_ip_icon(self):
        self.log.debug("单击公网IP图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[6]/i")

    def click_cloud_host_backup_icon(self):
        self.log.debug("单击云主机备份图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[7]/i")

    def click_container_service_icon(self):
        self.log.debug("单击容器服务图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[8]/i")

    def click_bandwidth_icon(self):
        self.log.debug("d单击外网带宽图标")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[2]/div/ul/li[9]/i")

    def click_commit_button(self):
        self.log.debug("单击确认按钮")
        self.dr.click(
            "xpath->//div[@id='selectprodcateModal']/div[3]/div/button")

    def click_cancel_button(self):
        self.log.debug("单击取消按钮")
        self.dr.click("xpath->//a[contains(.,'取消')]")

    def input_describ(self, value):
        self.log.debug("输入描述")
        self.dr.type_and_enter("xpath->//div[5]/div/textarea", value)

    def click_submit_button(self):
        self.log.debug("单击保存按钮")
        self.dr.click("xpath->//button[@type='submit']")

    def click_create_page_cancel_button(self):
        self.log.debug("单击取消按钮")
        self.dr.click("xpath->//a[contains(.,'取消')]")

    def select_product_class(self, value):
        self.log.debug("查找产品分类")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]", value)

    def get_table_text(self):
        self.log.debug("获取表格下的数据")
        text = self.dr.get_text(
            "xpath->//manage-component/div/div/div/div/div/div/div/table-component/div")
        return text


class ProductManagePage(FolderPgae):
    @allure.step("打开产品管理页面")
    def open_product_manage_page(self):
        self.log.debug("打开产品管理页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/folder/productManage")

    def click_create_product_button(self):
        self.log.debug("单击新建产品按钮")
        self.dr.click("xpath->//div[3]/button")

    def click_product_class_box(self):
        self.log.debug("单击产品分类框")
        self.dr.click("xpath->//div[2]/div/div/div/span/span[2]/span")

    def select_product_class_name(self, value):
        self.log.debug("输入:%s并且按enter" % value)
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]", value)

    def click_platform_box(self):
        self.log.debug("单击平台选择框")
        self.dr.click("xpath->(//input[@type='search'])[4]")

    def select_platform(self, value):
        self.log.debug("输入：%s，并按enter" % value)
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]", value)

    def click_resource_type_box(self):
        self.log.debug("单击资源类型框")
        self.dr.click("xpath->//div[4]/div/div/div/span")

    def select_resource_type(self, value):
        self.log.debug("选择资源类型")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[5]", value)

    def input_product_name(self, value):
        self.log.debug("输入产品名称")
        self.dr.clear_type("xpath->//input[@name='name']", value)\


    def input_product_num(self, value):
        self.log.debug("输入产品序号")
        self.dr.clear_type("xpath->//input[@name='id']", value)

    def click_get_url_button(self):
        self.log.debug("单击获取url按钮")
        self.dr.click("xpath->//button[contains(.,'获取URL')]")

    def click_cloud_res_openup_button(self):
        self.log.debug("勾选云资源沟通")
        # self.dr.click("xpath->//span[contains(.,'云主机资源开通')]")
        self.dr.click("xpath->//div[2]/div/form/div/div/div/div/label")

    def click_cloud_dick_openup_button(self):
        self.log.debug("单击云磁盘开通")
        self.dr.click("xpath->//div[@id='uniform-optionsRadios22']/span")

    def click_commit_button(self):
        self.log.debug("单击确定按钮")
        self.dr.click(
            "xpath->//div[@id='load_formUrl_Modal']/div[2]/div[2]/button")

    def input_product_des(self, value):
        self.log.debug("输入产品描述")
        self.dr.clear_type("xpath->//div[8]/div/textarea", value)

    def click_save_button(self):
        self.log.debug("单击保存按钮")
        self.dr.click("xpath->//form/div[2]/div/div/button")

    def select_product(self, value):
        self.log.debug("查询产品")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]", value)

    def click_more_button(self):
        self.log.debug("单击更多按钮")
        self.dr.move_to_element("xpath->//span[contains(.,'更多')]")
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_online_button(self):
        self.log.debug("单击上线按钮")
        self.dr.click("xpath->//button[contains(.,'上线')]")

    def click_offline_button(self):
        self.log.debug("单击下线按钮")
        self.dr.click("xpath->//button[contains(.,'下线')]")

    def get_table_text(self):
        self.log.debug("获取产品表格下的数据")
        text = self.dr.get_text(
            "xpath->//manage-component/div/div/div/div/div/div/div/table-component/div")
        return text


class SpecificationPage(FolderPgae):
    def open_specification_page(self):
        self.log.debug("打开产品规格")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/folder/specification")

    def click_create_sp_button(self):
        self.log.debug("单击新建按钮")
        self.dr.click("xpath->//button[contains(.,'新建')]")

# 新建规格页面
    def select_product_name(self, value):
        self.log.debug("单击产品名称后的输入框")
        self.dr.click("xpath->//div[2]/div/div/div/span/span[2]/span")
        self.log.debug("选择产品名称")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]", value)

    def input_spn_name(self, value):
        self.log.debug("输入规格名称")
        self.dr.clear_type("xpath->//input[@name='specName']", value)

    def click_new_create_box(self):
        self.log.debug("点击新建选择框")
        self.dr.click("xpath->//label/div/span")

    def click_change_box(self):
        self.log.debug("点击变更选择框")
        self.dr.click("xpath->//label[2]/div/span")

    def input_sp_tag(self, value):
        self.log.debug("输入标签")
        self.dr.clear_type("xpath->(//input[@type='text'])[14]", value)

    def input_sp_des(self, value):
        self.log.debug("输入描述")
        self.dr.clear_type("xpath->//div[6]/div/textarea", value)

    def click_next_step_button(self):
        self.log.debug("单击下一步按钮")
        self.dr.click("xpath->//button[contains(.,'下一步')]")
# 配置属性

    def select_vpool(self, value):
        self.log.debug("单击vpool选择框")
        self.dr.click("xpath->(//input[@type='search'])[3]")
        self.log.debug("选择可用去")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]", value)

    def input_volume_type(self, value):
        self.log.debug("输入磁盘类型")
        self.dr.clear_type("xpath->//input[@name='volume_disk_type']", value)

    def input_volume_disk_type_tag(self, value):
        self.log.debug("输入底层存储标签")
        self.dr.clear_type(
            "xpath->//input[@name='volume_disk_type_tag']", value)

    def select_host_type(self, value):
        self.log.debug("单击云主机类型选择框")
        self.dr.click("xpath->(//input[@type='search'])[4]")
        self.log.debug("选择云主机类型")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]", value)

    def select_test_period(self, value):
        if value not in range(1, 6):
            self.log.error("测试期限必须在1-6个月之间，请输入1，2，3，4，5，6")
        self.log.debug("单击测试期限选择框")
        self.dr.click("xpath->(//input[@type='search'])[5]")
        self.log.debug("选择测试期限")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[5]", value)

    def click_complete_button(self):
        self.log.debug("单击完成按钮")
        self.dr.click("xpath->//button[contains(.,'完成')]")


    def click_more_button(self):
        self.log.debug("单击更多按钮")
        self.dr.move_to_element("xpath->//span[contains(.,'更多')]")
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_online_button(self):
        self.log.debug("单击产品规格上线按钮")
        self.dr.click("xpath->//button[contains(.,'上线')]")

    def click_offline_button(self):
        self.log.debug("单击产品规格下线按钮")
        self.dr.click("xpath->//button[contains(.,'下线')]")

    def click_delete_sp_button(self):
        self.log.debug("单击删除按钮")
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def select_sp_name(self, value):
        self.log.debug("选择产品规格名称")
        self.dr.type_and_enter("xpath->//div/div/div/div/div/div/div/div/form/div/div/input", value)

    def get_table_text(self):
        self.log.debug("获取表格下的数据")
        text = self.dr.get_text(
            "xpath->//manage-component/div/div/div/div/div/div/div/table-component/div")
        return text

# 操作系统管理


class OperationSystemPage(FolderPgae):
    @allure.step("打开：服务目录-操作系统管理")
    def open_operation_sys_page(self):
        self.log.debug("打开操作系统管理页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/folder/operationsystem")

    @allure.step("单击新建按钮")
    def click_new_create_button(self):
        self.log.debug("单击新建按钮")
        self.dr.click("xpath->//button[contains(.,'新建')]")
    #
    # @allure.step("")
