CC = g++
LDFLAGS = -std=c++11

all: targ

tabuleiro.o: tabuleiro.cpp
	$(CC) $(LDFLAGS) -c tabuleiro.cpp

main.o: main.cpp
	$(CC) $(LDFLAGS) -c main.cpp

targ: main.o tabuleiro.o
	$(CC) $(LDFLAGS) main.o tabuleiro.o -o main

clean:
	rm main.o
	rm tabuleiro.o
	rm main