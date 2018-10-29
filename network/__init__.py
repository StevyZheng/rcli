#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : Stevy
import re
import os
# import netinfaces

net_path = "/etc/sysconfig/network-scripts/"


def check_ip(*ips):
	for s in ips:
		if not isinstance(s, str):
			print("str type error.")
			return False
	pat = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
	r = [pat.match(x) for x in ips]
	if None in r:
		return False
	else:
		return True


class Network(object):
	def show(self):
		print("waiting")
	
	def set(self, ipaddr, netmask, gateway=None, dns1=None):
		if not check_ip(ipaddr, netmask, gateway, dns1):
			return False
		network_dict = {
			"ipaddr": ipaddr,
			"netmask": netmask,
			"gateway": gateway,
			"dns1": dns1
		}
		try:
			os.rename("{0}ifcfg-{1}".format(net_path, "interface"), "{0}ifcfg-{1}".format(net_path, "interface"))
		except:
			print("ifcfg_file backup failed.")
			return
		print(network_dict)
