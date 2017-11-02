#include "tabuleiro.hpp"

using namespace std;

void Tabuleiro::init(){
	unsigned seed = rand();
	vector<pair<int, int> > bombs;
	//inicializa tabuleiro com 0 (quantidade de bombas ao redor de cada celula)
	//inicializa visible com false (para não mostrar aquelas celulas)
	for (int i=0; i<h+2; i++){
		for (int j=0; j<w+2; j++){
			board[i][j] = 0;
			//insere no vetor apenas posicoes validas (tabuleiro indexado de 1)
			if (i > 0 && i < h + 1 && j > 0 && j < w + 1) bombs.push_back(make_pair(i, j));
		}
	}
	
	//da shuffle nas posicoes a atribui bombas as numBombs primeiras posicoes
	shuffle(bombs.begin(), bombs.end(), default_random_engine(seed));
	for (int i=0; i<numBombs; i++){
		int x = bombs[i].first;
		int y = bombs[i].second;
		board[x][y] = -1;
	}

	int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
	int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

	//calcula a quantidade de bombas adjacentes para cada celula
	for (int i = 1; i <= h; i++){
		for (int j = 1; j <= w; j++){
			if (board[i][j] == -1) continue; //se for bomba continue
			for (int k = 0; k < 8; k++)
				board[i][j] += (board[ i + dx[k] ][ j + dy[k] ] == -1); 
		}
	}
}

void Tabuleiro::show(){
	for (int i = 1; i <= h; i++){
		for (int j = 1; j <= w; j++){
			if (board[i][j] == -1) cout << "* ";
			else cout << board[i][j] << " ";
		}
		cout << endl;
	}
}