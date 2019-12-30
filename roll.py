#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   roll.py
@Time    :   2019/12/31 00:40:16
@Author  :   yanxiaosong 
@Contact :   yanxiaosong@qiniu.com
@Desc    :   None
'''

import time
import random
import sys
import argparse as apa


def main():
  users = {
    'Junc': {
      'name': 'Junc',
      'score': 0,
      'win': False
    },
    'qinbao': {
      'name': '沁宝',
      'score': 0,
      'win': False
    },
    'jianming': {
      'name': '小弦弦',
      'score': 0,
      'win': False
    },
    'dapeng': {
      'name': '雨魔',
      'score': 0,
      'win': False
    },
    'guli': {
      'name': '十字军打击',
      'score': 0,
      'win': False
    },
    'jiangqi': {
      'name': '吹胡子咬耳朵',
      'score': 0,
      'win': False
    }
  }
  gold = argsParse(users)
  winUsers = []

  for v in users.items():
    if v[1]['win'] == True:
      winUsers.append(v[1])

  print('本次有 %d 名玩家获胜！' % len(winUsers))

  for v in winUsers:
    print('%s 分得 %d 金' % ( v['name'], gold / len(winUsers)))

def isWin(score, win):
  if win == 'odd':
    return score % 2 == 0
  if win == 'even':
    return score % 2 == 1

def argsParse(users):
  parser = apa.ArgumentParser()
  parser.add_argument("win", help="win method")
  parser.add_argument("-min", "--min", help="min value", default=1)
  parser.add_argument("-max", "--max", help="max value", default=100)
  parser.add_argument("-g", "--gold", help="gold count", default=100)
  args = parser.parse_args()

  min = args.min
  max = args.max
  win = args.win

  for v in users.values():
    score = round(random.random() * 100)
    v['score'] = score
    v['win'] = isWin(score, win)
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("%s %s 掷出 %d (%s - %s)" % (date, v['name'], score, min, max))
  
  return int(args.gold)

if __name__ == "__main__":
  main()