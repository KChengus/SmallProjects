package Othello;
import java.util.ArrayList;
import java.util.List;

public class Board {
	// definerar griden och hörn
	private int[][] grid = new int[8][8];
	private int[] edges = {00, 07, 70, 77};
	// alla 8 riktningar från sin position
	private int[][] directions = {
			 {1,0}, {1,1}, {0,1},
			  	{-1,1}, {-1,0}, 
			 {-1,-1}, {0, -1}, {1, -1}
		 };
	// lägger till ett chip på valda positionen
	public void addChip(int y, int x, Player player) {
		if (player.getMap().isEmpty()) {
			return;
		}
		grid[y][x] = player.getColor();
		// byter färg på chipsen som blir övertagna
		for (int pos : player.getMap().get(y*10+x)) {
			grid[pos/10][pos%10] = grid[pos/10][pos%10]*-1;
		}
	}
	// hjälp metod till processMoves
	private void processMovesHelper(int yValue, int xValue, int[] direcAdd, int myColor, List<Integer> positions) {
		List<Integer> temp = new ArrayList<>();
		while (isWithinBounds(yValue, xValue) && grid[yValue][xValue] == myColor*-1) {
			temp.add(yValue*10+xValue);
			yValue += direcAdd[0];
			xValue += direcAdd[1]; 
		} 
		// kollar om den är inom brädgränserna
		if (isWithinBounds(yValue, xValue) && grid[yValue][xValue] == myColor) {
			positions.addAll(temp);
		} 
	}

	public void processMoves(Player player) {
		
		// loop over the 2d array and check for allowed moves
		
		player.getMap().clear();
		
		for (int yValue = 0; yValue < grid.length; yValue++) {
			for (int xValue = 0; xValue < grid[0].length; xValue++) {
				// yValue för rad nummer och xValue för kolumn
				if (grid[yValue][xValue] == 0) {
					// titta alla 8 riktningar
					List<Integer> positions = new ArrayList<>();
					for (int[] direcAdd : directions) {
						processMovesHelper(yValue+direcAdd[0], xValue+direcAdd[1], direcAdd, player.getColor(), positions);
					}	
					// om spelarens map har kordinaten så läggs den på i listan 
					if (player.getMap().containsKey(yValue*10+xValue)) {
						player.getMap().get(yValue*10+xValue).addAll(positions);
					} else {
						if (!positions.isEmpty()) {
							player.getMap().put(yValue*10+xValue, positions);

						}
					}
				}
			}
		}
	}
	
	
	// start Bräda
	public void start() {
		
		grid[3][3] = 1;
		grid[4][4] = 1;
		grid[3][4] = -1;
		grid[4][3] = -1;
	}
	// inom gränserna
	private boolean isWithinBounds(int y, int x) {
		return ((y >= 0) && (y <= 7) && (x >= 0) && (x <= 7));
	}
	
	// restartar brädan
	public void reset() {
		grid = new int[8][8];
		start();
	}
	// kollar resultatet
	public String stats(Player p1, Player p2) {
		int p1Chip = 0;
		int p2Chip = 0;
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[0].length; j++) {
				if (grid[i][j] == 1) {
					p1Chip++;
				} else if (grid[i][j] == -1) {
					p2Chip++;
				}
			}
		}
		// returnerar vinnaren
		String ret;
		if (p1Chip > p2Chip) {
			ret = "Player 1 won";
		} else if (p1Chip < p2Chip) {
			ret = "Player 2 won";
		} else {
			ret = "Draw";
		}
		
		ret += "\np1 : " + p1Chip + "\np2 : " + p2Chip;
		
		return ret;
	}
	
	// getter and setter metoder
	public void setGrid(int[][] grid) {
		this.grid = grid;
	}
	
	public int[][] getGrid() {
		return grid;
	}

	public int[] getEdges() {
		return edges;
	}
}
