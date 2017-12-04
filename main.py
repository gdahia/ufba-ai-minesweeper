from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import players
import game


def read_int(msg=''):
  return int(input(msg))


def main():
  rows = read_int('linhas: ')
  cols = read_int('colunas: ')
  n_bombs = read_int('bombas: ')

  g = game.Game(rows, cols, n_bombs)
  p = players.player.Player(players.user)

  # simula jogo
  while not (g.game_over or g.victory):
    type_of_move, row, col = p.make_move(g.board)
    if type_of_move == 'C':
    	g.click(row, col)
    elif type_of_move == 'F':
    	g.flag(row, col)

  # checa como jogo terminou
  if g.victory:
    print('VENCEU')
  else:
    print('PERDEU')

if __name__ == "__main__":
  main()
