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
  
  loop(init, users)

def loop(init, users):
  time = 0
  minValue, maxvalue, win, gold, times = init
  stake = int(gold / times) * len(users)

  if win == 'odd':
    winStr = '双数有，单数无'
  elif win == 'even':
    winStr = '单数有，双数无'
  elif win == '<=50':
    winStr = '50及以下有，50以上无'
  elif win == '>50':
    winStr = '50以上有，50及以下无'

  while time < times:
    isGo = input("\033[1;32m载入完成，请选择是否继续（y/n）？\033[0m")
    if isGo == 'y' or isGo == 'yes':
      print("\033[1;31mroll 点开始！------------------第\033[0m \033[1;32m%d\033[0m \033[1;31m场, %s\033[0m" % (time + 1, winStr))
      roll(minValue, maxvalue, win, stake, users)
      time += 1
    else:
      print("欢迎下次再来！")
      break
  
  print("游戏结束！赌资分配如下：")

  userList = []
  for k, v in users.items():
    userList.append(v)
  
  winner = max(userList, key = lambda x:x['balance'])
  loser = min(userList, key = lambda y:y['balance'])

  for k, v in users.items():
    rewardStr = ''
    if v['balance'] == winner['balance']:
      rewardStr = '。恭喜您，大赢家！'
    elif v['balance'] == loser['balance']:
      rewardStr = '。下次努力，放炮王！'
    else:
      rewardStr = ''
    print("%s 分得 %d %s" % (v['name'], v['balance'], rewardStr))

def isWin(score, win):
  if win == 'odd':
    return score % 2 == 0
  elif win == 'even':
    return score % 2 == 1
  elif win == '<=50':
    return score <= 50
  elif win == '>50':
    return score > 50

def argsParse(users):
  parser = apa.ArgumentParser()
  parser.add_argument("win", help="win method")
  parser.add_argument("-t", "--times", help="times", default=10)
  parser.add_argument("-min", "--min", help="min value", default=1)
  parser.add_argument("-g", "--gold", help="gold count", default=200)
  parser.add_argument("-max", "--max", help="max value", default=100)
  args = parser.parse_args()

  min = int(args.min)
  max = int(args.max)
  win = args.win
  times = int(args.times)
  gold = int(args.gold)
  for v in users.values():
    v['gold'] = gold
    v['balance'] = 0

  return (min, max, win, gold, times)

def roll(min, max, win, gold, users):
  for v in users.values():
    score = round(random.random() * 100)
    v['score'] = score
    v['win'] = isWin(score, win)
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("%s %s 掷出 %d (%s - %s)" % (date, v['name'], v['score'], min, max))

  winUsers = []

  for k, v in users.items():
    if v['win'] == True:
      winUsers.append(v)

  if len(winUsers) == 0:
    averageGold = gold / len(users)
  else:
    averageGold = gold / len(winUsers)

  print('本次有 %d 名玩家获胜！' % len(winUsers))

  for v in winUsers:
    print('%s 分得 %d 金' % (v['name'], averageGold))

  print("实时赌资：")
  for k, v in users.items():
    winGold = 0
    if v['win'] == True:
      winGold = averageGold
    else:
      winGold = 0
    print("%s: %d + %d = %d" % (v['name'], v['balance'], winGold, v['balance'] + winGold))
    v['balance'] = int(v['balance']+ winGold)

if __name__ == "__main__":
  main()