# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 10:11
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : volumeaction.py
# @Software: PyCharm

from time import sleep
from public.pages import controlcenterpage
from public.common import log
from public.appmodel import applyfromaction


class VolumeAction():
    def __init__(self, driver):
        self.dr = driver
        self.mvp = controlcenterpage.ManageVolumePage(self.dr)
        self.cs = controlcenterpage.ShoppingcarPage(self.dr)
        self.log = log.Log()

    def create_volume(
            self,
            projectname,
            volumename,
            vpool,
            capacity,
            mounttype,
            **kwargs):
        try:

            self.mvp.open_pv_managevolume_page(projectname)
            self.mvp.click_apply_volume_button()
            self.mvp.click_vpool_box()
            self.mvp.select_vpool(vpool)
            print(capacity)
            self.mvp.input_volume_capacity(capacity)
            if mounttype == "独立磁盘":
                self.mvp.click_independent_disk()
            elif mounttype == "独享挂载":
                self.mvp.click_cloud_host_category()
                if kwargs["category"] == "已有云主机":
                    self.mvp.select_cloud_host_category("已有云主机")
                elif kwargs["category"] == "申请单中云主机":
                    self.mvp.select_cloud_host_category("申请单中云主机")
                else:
                    self.log.error("cant select loud_host_category")

                if kwargs["cloudhost"]:
                    self.mvp.select_cloud_host(kwargs["cloudhost"])
                else:
                    self.log.error("you must select a cloudhost")

            elif mounttype == "共享挂载":
                pass
            else:
                self.log.error(
                    "mounttype：%s is not in ['独立磁盘','独享挂载','共享挂载']" %
                    mounttype)
            self.mvp.input_volume_name(volumename)
            if "volume_num" in kwargs:
                host_count = kwargs["host_num"]
                while host_count - 1:
                    host_count = host_count - 1
                    self.mvp.click_number_application_add()
            sleep(2)
            self.mvp.click_entry_form_button()
            self.mvp.click_confirmation_form_button()
            self.cs.page_to_bottom()
            sleep(1)
            self.cs.click_submission_apply_form()
            sleep(1)
            self.cs.page_to_bottom()
            sleep(1)
            self.cs.commit_submit_button()
        except Exception as e:
            self.log.error("创建云磁盘失败，请确认：%s" % e)

    def attach_volume(self, projectname, volume, host, attachtype="exclusive"):
        try:
            self.mvp.open_pv_managevolume_page(projectname)
            sleep(2)
            self.mvp.select_volume(volume)
            self.mvp.click_attach_button()
            sleep(0.5)
            self.mvp.click_attach_button()
            print(attachtype)
            if attachtype != "exclusive":
                self.mvp.click_share_button()
            self.mvp.click_host_for_attach_box()
            self.mvp.select_host_for_attach(host)
            sleep(0.5)
            self.mvp.click_commit_for_attach_buttton()
        except Exception as e:
            self.log.error("挂载磁盘失败：%s" % e)

    def delete_volume(self, projectname, volume):
        try:
            self.mvp.open_pv_managevolume_page(projectname)
            sleep(1)
            self.mvp.select_volume(volume)
            self.mvp.click_volume_more_botton()
            self.mvp.click_release_button()
            self.mvp.click_release_commit_button()
        except Exception as e:
            self.log.error("删除磁盘失败:%s" % e)

    def create_volume_snap(self, projectname, volume, snapname, des):
        try:
            self.mvp.open_pv_managevolume_page(projectname)
            sleep(1)
            self.mvp.select_volume(volume)
            self.mvp.click_volume_more_botton()
            self.mvp.click_create_snap_button()
            sleep(0.5)
            self.mvp.input_volume_sanp_name(snapname)
            self.mvp.input_volume_snap_des(des)
            self.mvp.click_create_button_yellow()
        except Exception as e:
            self.log.error("创建磁盘快照失败：%s" % e)


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.wait(10)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    sleep(2)
    vc = VolumeAction(dr)
    # vc.create_volume("湖北","测试磁盘01","湖北","100",mounttype="共享挂载",category="已有云主机",cloudhost="测试111")
    vc.create_volume_snap("湖北", "测试磁盘01", "快照测试", "描述信息")
    sleep(10)
    dr.quit()
