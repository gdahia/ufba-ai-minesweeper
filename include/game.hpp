#ifndef GAME_HPP
#define GAME_HPP

#include <ostream>
#include <vector>

class Game {
 public:
  Game(const int, const int, const int, const int);
  ~Game() = default;
  void show(std::ostream&);

 private:
  const int height, width, num_bombs;
  std::vector<std::vector<char>> board;
};

#endif
