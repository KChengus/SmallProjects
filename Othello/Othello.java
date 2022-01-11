package Othello;

public class Othello{

	// Polymorfism
	Player p1;
	Player p2;

	// Komposition, has-a relation
	Board board = new Board();
	// Botens svårighets grad
	int botDiff = 1;
	// spelare 1 o 2
	Othello() {
		p1 = new Human();
		p2 = new Bot(botDiff, board);
		start();
	}
	
	// Sätter färg och motståndare
	public void start() {
		
		p1.setColor(1);
		p2.setColor(-1);
		
		p1.setEnemy(p2);
		p2.setEnemy(p1);
		// startar
		board.start();
		everyoneProcessMoves();
	}
	// Genomför alla moves
	public void everyoneProcessMoves() {
		board.processMoves(p1);
		board.processMoves(p2);
	}
	// kollar om spelet är slut
	public boolean isGameOver() {
		return (p1.getMap().isEmpty() && p2.getMap().isEmpty());
	}
	// resetar spelet
	public void reset() {
		board.reset();
		everyoneProcessMoves();
	}
}
