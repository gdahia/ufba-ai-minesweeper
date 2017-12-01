from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import game


def read_int(msg=''):
  return int(input(msg))


def main():
  rows = read_int('linhas: ')
  cols = read_int('colunas: ')
  n_bombs = read_int('bombas: ')

  g = game.Game(rows, cols, n_bombs)
  print(g.board)

  for line in sys.stdin:
    row, col = [int(x) for x in line.split()]
    g.click(row, col)
    if g.game_over:
      print('PERDEU')
      break
    if g.victory:
      print('VENCEU')
      break
    print(g.board)


if __name__ == "__main__":
  main()
