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
      'win': False,
      'gold': 0,
      'balance': 0
    },
    'qinbao': {
      'name': '沁宝',
      'score': 0,
      'win': False,
      'gold': 0,
      'balance': 0
    },
    'jianming': {
      'name': '小弦弦',
      'score': 0,
      'win': False,
      'gold': 0,
      'balance': 0
    },
    'dapeng': {
      'name': '雨魔',
      'score': 0,
      'win': False,
      'gold': 0,
      'balance': 0
    },
    'guli': {
      'name': '十字军打击',
      'score': 0,
      'win': False,
      'gold': 0,
      'balance': 0
    },
    'jiangqi': {
      'name': '吹胡子咬耳朵',
      'score': 0,
      'win': False,
      'gold': 0,
      'balance': 0
    }
  }
  
  init = argsParse(users)
  
  #loop(init)

def loop(init):
  time = 0
  min, max, win, gold, times = init
  stake = int(gold / times) * len(users)
  while time < times:
    isGo = input("载入完成，请选择是否继续（y/n）？")
    if isGo == 'y' or isGo == 'yes':
      print("go!")
      roll(min, max, win, stake)
    else:
      break
  print("欢迎下次再来！")

def isWin(score, win):
  if win == 'odd':
    return score % 2 == 0
  if win == 'even':
    return score % 2 == 1

def argsParse(users):
  parser = apa.ArgumentParser()
  parser.add_argument("win", "-w", "--win", help="win method")
  parser.add_argument("times", "-t", "--times", help="times", default="10")
  parser.add_argument("-min", "--min", help="min value", default=1)
  parser.add_argument("-g", "--gold", help="gold count", default=200)
  parser.add_argument("-max", "--max", help="max value", default=100)
  args = parser.parse_args()

  min = args.min
  max = args.max
  win = args.win
  time = args.times
  gold = int(args.gold)
  for v in users.values():
    v['gold'] = gold
    v['balance'] = 0

  return (min, max, win, gold, times)

def roll(min, max, win, gold):
  for v in users.values():
    score = round(random.random() * 100)
    v['score'] = score
    v['win'] = isWin(score, win)
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("%s %s 掷出 %d (%s - %s)" % (date, v['name'], score, min, max))

  winUsers = []

  for k, v in users.items():
    if v['win'] == True:
      winUsers.append(v)

  averageGold = gold / len(winUsers)
  
  for v in winUsers:
      v['balance'] += averageGold

  print('本次有 %d 名玩家获胜！' % len(winUsers))

  for v in winUsers:
    print('%s 分得 %d 金' % ( v['name'], averageGold)


if __name__ == "__main__":
  main()