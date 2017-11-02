#include <algorithm>
#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

class Tabuleiro{
	int h, w, numBombs;
	int board[102][102];
	public:
		Tabuleiro(int h, int w, int numBombs) : h(h), w(w), numBombs(numBombs) {};
		void init();
		void show();
};