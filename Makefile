CC = g++
CCFLAGS = -std=c++11
INCLUDE = -I include/

all: main.out

game.o: src/game.cpp include/game.hpp
	$(CC) $(CCFLAGS) $(INCLUDE) -c $<

main.o: src/main.cpp include/game.hpp
	$(CC) $(CCFLAGS) $(INCLUDE) -c $<

main.out: main.o game.o
	$(CC) $(CCFLAGS) $(LDFLAGS) $^ -o $@

clean:
	rm main.o
	rm game.o
	rm main.out
