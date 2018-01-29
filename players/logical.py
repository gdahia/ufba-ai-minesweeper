from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from six.moves import range

import numpy as np


class LogicalPlayer:

  def __init__(self, no_move_strategy=None):
    self._sure_moves = []

    if no_move_strategy is not None:
      self._no_move_strategy = no_move_strategy
    else:
      self._no_move_strategy = self._random_coherent_move

  def init(self):
    pass

  def strategy(self, board):
    # se ainda ha movimentos no buffer, executa o proximo desses movimentos
    if self._sure_moves:
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
    # determina posicoes na borda
    border_list, insiders_list = self._get_border_and_insiders(board)

    # salva os movimentos de modelos que atendem o tabuleiro
    current_moves = np.ones(len(border_list), dtype=np.bool)

    # copia o tabuleiro para fazer computacoes
    safe_board = np.zeros_like(board, dtype=np.uint8)

    # itera sobre possibilidades
    for possibility in range(2**len(border_list)):
      # preenche a copia do tabuleiro de acordo com 'possibility'
      for index, border_pos in enumerate(border_list):
        # ve se 'possibility' preve bomba na posicao 'border_pos'
        has_bomb = bool(possibility & (1 << index))

        if has_bomb:
          safe_board[border_pos] = 1
        else:
          safe_board[border_pos] = 0

      # checa se modelo gerado e possivel
      if self._check_model_veracity(board, safe_board, insiders_list):
        # itera sobre as posicoes de borda e salva movimentos determinados por 'possibility'
        for index, border_pos in enumerate(border_list):
          current_moves[index] |= not safe_board[border_pos]

    return list(border_list[current_moves])

  def _get_border_and_insiders(self, board):
    border = []
    insiders = []
    for i, row in enumerate(board[0:, 0:]):
      for j, pos in enumerate(row):
        # checa se posicao esta fechada
        if pos != -1:
          # adiciona posicao aberta aos vizinhos da borda
          insiders.append((i, j))

          # itera sobre vizinhanca de posicao fechada buscando posicoes abertas
          for di in range(-1, 2):
            for dj in range(-1, 2):
              if i + di < board.shape[0] and \
                  j + dj < board.shape[1] and \
                  board[i + di, j + dj] == -1:
                border.append((i + di, j + dj))

    # remove elementos repetidos
    border = np.array(border, dtype=np.int32)
    border = np.unique(border)

    return border, insiders

  def _check_model_veracity(self, board, safe_board, insiders):
    # itera sobre posicoes abertas vizinhas a borda
    for i, j in insiders:
      # checa se modelo atende restricoes de posicao aberta '(i, j)'
      if np.sum(safe_board[i - 1:i + 2, j - 1:j + 2]) != board[i, j]:
        return False

    return True
