from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class LogicalPlayer:
  _no_move_strategy = None
  _sure_moves = []

  def __init__(self, no_move_strategy=None):
    if no_move_strategy is not None:
      self._no_move_strategy = no_move_strategy
    else:
      self._no_move_strategy = self._random_coherent_move

  def init():
    pass

  def strategy(self, board):
    # se ainda movimentos no buffer, executa o proximo desses movimentos
    if self._sure_bombs:
      move = self._sure_moves[0]
      self._sure_moves = self._sure_moves[1:]
      return move

    # determina posicoes totalmente determinadas pelo campo ja preenchido
    self._sure_moves = self._get_sure_moves(board)

    # joga nas aberturas possiveis se existirem, usa estrategia predefinida para essa situacao, caso contrario
    if self._sure_moves:
      move = self._sure_moves[0]
      self._sure_moves = self._sure_moves[1:]
      return move
    else:
      return self._no_move_strategy(board)

  def _random_coherent_move(self, board):
    # determina celulas fechadas
    closed_cels = np.where(board == -1)

    # sorteia uniformemente uma das celulas disponiveis
    move_index = np.random.choice(len(closed_cells), 1)
    row, col = closed_cells[move_index]

    return 'C', row, col

  def _get_sure_moves(self, board):
    # todo
    pass
