#include "tabuleiro.hpp"

using namespace std;

int main(){
	srand(1);
	int h, w, numBombs;

	cout << "Digite a altura do tabuleiro\n";
	cin >> h;
	
	cout << "Digite a largura do tabuleiro\n";
	cin >> w;
	
	cout << "Digite o numero de bombas\n";
	cin >> numBombs;
	
	Tabuleiro tabuleiro(h, w, numBombs);
	tabuleiro.init();
	tabuleiro.show();
}