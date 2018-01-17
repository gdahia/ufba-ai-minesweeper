from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import players
import game


def read_int(msg=''):
  return int(input(msg))


def main(rows, cols, n_bombs, seed):
  # se algum dos argumentos nao foi passado, tomar interativamente
  if rows is None or cols is None or n_bombs is None:
    rows = read_int('linhas: ')
    cols = read_int('colunas: ')
    n_bombs = read_int('bombas: ')

  g = game.Game(rows, cols, n_bombs, seed)
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
  # parseia argumentos da linha de comando
  parser = argparse.ArgumentParser()
  parser.add_argument('--rows', type=int, help='Número de linhas do campo.')
  parser.add_argument('--cols', type=int, help='Número de colunas do campo.')
  parser.add_argument('--n_bombs', type=int, help='Número de bombas no campo.')
  parser.add_argument('--seed', type=str, help='Semente aleatoria.')
  FLAGS, _ = parser.parse_known_args()

  main(FLAGS.rows, FLAGS.cols, FLAGS.n_bombs, FLAGS.seed)
