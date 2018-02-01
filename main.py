from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import players
import game
import gui


def simulate_game(rows, cols, n_bombs, seed, callback, player):
  # instancia jogo
  g = game.Game(rows, cols, n_bombs, seed, callback)

  # simula jogo
  while not (g.game_over or g.victory):
    type_of_move, row, col = player.make_move(g.board)
    if type_of_move == 'C':
      g.click(row, col)
    elif type_of_move == 'F':
      g.flag(row, col)

  # checa como jogo terminou
  if g.victory:
    print('VENCEU')
  else:
    print('PERDEU')


def read_int(msg=''):
  return int(input(msg))


def main(player_type, rows, cols, n_bombs, seed, heuristic):
  # se algum dos argumentos nao foi passado, tomar interativamente
  if rows is None or cols is None or n_bombs is None:
    rows = read_int('linhas: ')
    cols = read_int('colunas: ')
    n_bombs = read_int('bombas: ')

  # define o tipo de jogador
  player = None
  if player_type == 'user':
    player = players.player.Player(players.user)
  elif player_type == 'logical':
    # define a heuristica
    no_move_strategy = None
    if heuristic == 'model_counting':
      no_move_strategy = players.logical.model_counting_heuristic

    logical_player = players.logical.LogicalPlayer(no_move_strategy)
    player = players.player.Player(logical_player)
  else:
    print('Tipo de jogador especificado nao implementado.')
    sys.exit(1)

  # chama interface grafica
  gui.GUI.main(
      rows, cols,
      lambda callback: simulate_game(rows, cols, n_bombs, seed, callback, player)
  )


if __name__ == "__main__":
  # parseia argumentos da linha de comando
  parser = argparse.ArgumentParser()
  parser.add_argument('--rows', type=int, help='Numero de linhas do campo.')
  parser.add_argument('--cols', type=int, help='Numero de colunas do campo.')
  parser.add_argument('--n_bombs', type=int, help='Numero de bombas no campo.')
  parser.add_argument('--seed', type=str, help='Semente aleatoria.')
  parser.add_argument('--player_type', type=str, help='Tipo de jogador.')
  parser.add_argument(
      '--heuristic', type=str, help='Heuristica a ser utilizada.')
  FLAGS, _ = parser.parse_known_args()

  main(FLAGS.player_type, FLAGS.rows, FLAGS.cols, FLAGS.n_bombs, FLAGS.seed,
       FLAGS.heuristic)
