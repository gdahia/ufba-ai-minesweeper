#include "game.hpp"

#include <algorithm>
#include <random>
#include <tuple>

Game::Game(const int height, const int width, const int num_bombs,
           const int seed)
    : height(height),
      width(width),
      num_bombs(num_bombs),
      board(height + 2, std::vector<char>(width + 2)) {
  // da shuffle nas posicoes a atribui bombas
  // as num_bombs primeiras posicoes
  std::vector<std::pair<int, int>> bombs;
  for (int i = 1; i <= height; i++)
    for (int j = 1; j <= width; j++) bombs.emplace_back(i, j);
  std::shuffle(bombs.begin(), bombs.end(), std::default_random_engine(seed));
  for (int i = 0; i < num_bombs; i++) {
    int x, y;
    std::tie(x, y) = bombs[i];
    board[x][y] = -1;
  }

  // calcula a quantidade de bombas adjacentes
  // para cada celula olhando a sua vizinhanca
  const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
  const int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
  for (int i = 1; i <= height; i++)
    for (int j = 1; j <= width; j++)
      if (board[i][j] != -1) {
        board[i][j] = 0;
        for (int k = 0; k < 8; k++) {
          int x = i + dx[k];
          int y = j + dy[k];
          if (board[x][y] == -1) board[i][j]++;
        }
      }
}

void Game::show(std::ostream& os) {
  for (int i = 1; i <= height; i++) {
    for (int j = 1; j <= width; j++)
      if (board[i][j] == -1)
        os << "* ";
      else
        os << (int)board[i][j] << " ";
    os << std::endl;
  }
}
