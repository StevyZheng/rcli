#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : Stevy
import fire
from network import *

version = "0.0.1"


class Main(object):
	def __init__(self):
		self.network = Network()
	
	def ver(self):
		print(version)


if __name__ == '__main__':
	fire.Fire(Main)
