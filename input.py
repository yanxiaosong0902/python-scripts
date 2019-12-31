#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   roll.py
@Time    :   2019/12/31 00:40:16
@Author  :   yanxiaosong 
@Contact :   yanxiaosong@qiniu.com
@Desc    :   None
'''

import keyboard

def inputStr():
  str = input("请输入：")
  print("您输入的是：%s" % str)

def abc(x):
  a = keyboard.KeyboardEvent('down', 28, 'enter')

  if x.event_type == 'down' and x.name == a.name:
    print("123")

if __name__ == "__main__":
  # inputStr()
  keyboard.hook(abc)
  keyboard.wait()