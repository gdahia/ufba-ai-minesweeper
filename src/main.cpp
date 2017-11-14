#include "game.hpp"

#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int h, w, numBombs;

  cout << "Digite a altura do jogo\n";
  cin >> h;

  cout << "Digite a largura do jogo\n";
  cin >> w;

  cout << "Digite o numero de bombas\n";
  cin >> numBombs;

  int seed;
  if (argc >= 2)
    seed = std::stoi(argv[1]);
  else
    seed = 1;

  Game game(h, w, numBombs, seed);
  game.show(cout);
}
