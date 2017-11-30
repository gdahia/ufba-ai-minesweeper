from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class Game:
    def __init__(self, rows, cols, n_bombs, seed=None):
        self.rows = rows
        self.cols = cols
        self.n_bombs = n_bombs
        _bombs = np.zeros([rows + 2, cols + 2], dtype=np.uint8)
        self._board = np.zeros([rows + 2, cols + 2], dtype=np.int16)
        np.random.seed(seed)

        # sorteia "n_bombs" posicoes para se colocar bombas
        x = np.arange(1, rows + 1, dtype=np.uint8)
        y = np.arange(1, cols + 1, dtype=np.uint8)
        pos = np.transpose([np.repeat(x, y.shape[0]), np.tile(y, x.shape[0])])
        np.random.shuffle(pos)
        x = pos[:n_bombs, 0]
        y = pos[:n_bombs, 1]
        _bombs[x, y] = 1

        # calcula quantidade bombas adjacentes a cada celula
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self._board[i, j] = np.sum(_bombs[i - 1:i + 2, j - 1:j + 2])

        # unifica tabuleiros
        self._board[_bombs == 1] = -1
