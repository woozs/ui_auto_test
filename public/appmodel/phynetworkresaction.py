#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 15:45
# @Author  : mrwuzs
# @Site    :
# @File    : phynetworkresaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import datacenterpage
from public.common import log
from public.appmodel import datacenteraction


class PhyNetworkResAction(datacenteraction.DataCenterAction):
    @allure.step("创建物理网络")
    def create_pht_netwok(
            self,
            mrgname,
            regionname,
            vlan_start,
            vlan_end,
            phynetworkname,
            vswitchname,
            datacenter,
            netype="vlan",
            flow_type="Guest",
            flow_sub_type="DCN"):
        """
        创建物理网络
        :param mrgname:
        :param region:
        :param vlan_start:
        :param vlan_end:
        :param phynetworkname:
        :param vswitchname:
        :param datacenter:
        :param netype:
        :param flow_type:
        :param flow_sub_type:
        :return:
        """
        self.select_resouce_type(mrgname, regionname, "物理网络资源")
        self.dr.wait(5)
        self.log.debug("选择数据中心")
        self.dcPg.click_data_center(datacenter)
        self.dcPg.click_phy_net()
        self.dcPg.click_create_phy_net_button()
        if netype is not "vlan":
            self.dcPg.click_select_net_type()
            self.dr.wait(2)
            self.dcPg.input_select_net_type(netype)
        if flow_type is not "Public":
            self.dcPg.click_flow_type()
            self.dr.wait(2)
            self.dcPg.click_flow_type_guest()
        else:
            if flow_sub_type is not "DCN":
                self.dcPg.click_flow_sub_type()
                self.dcPg.click_dcn_button(flow_sub_type)
        self.dcPg.input_start_vlan(vlan_start)
        self.dcPg.input_end_vlan(vlan_end)
        sleep(2)
        self.dcPg.input_phy_network(phynetworkname)
        self.dcPg.input_switch(vswitchname)
        self.dcPg.click_save_phy_net_button()

    def delete_pht_network(
            self,
            mrgname,
            regionname,
            vlan_start,
            vlan_end,
            phynetworkname,
            vswitchname,
            datacenter):
        pass


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.common import cookiesAction

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    dr.open('http://192.168.54.13/#/login')
    dr = cookiesAction.add_cookie(dr)
    Phy = PhyNetworkResAction(dr)
    Phy.create_pht_netwok(
        "上海",
        "上海资源池",
        "1",
        "256",
        "physnet1",
        "dvs123",
        "DC2",
        flow_type="Public")
