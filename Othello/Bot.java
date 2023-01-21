import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

// child class to Player
public class Bot extends Player{
	
	// 1 - Easy
	// 2 - Normal
	// 3 - Hard

	private Board board;

	// konstruktor
	Bot(int difficulty, Board board) {
		this.difficulty = difficulty;
		this.board = board;
	}
	// vilken move ska boten göra
	public int move() {
		if (getMap().isEmpty()) {
			return -2;
		}
		// bestämmer svårighets grad
		if (difficulty == 1) {// tar random move
			return moveRandom();
		} else if (difficulty == 2) {// tar den moven som ger fläst chips
			int bestPos = (int) getMap().keySet().toArray()[0];
			
			for (int yx : getMap().keySet()) {
				if (getMap().get(yx).size() > getMap().get(bestPos).size()) {
					bestPos = yx;
				}
			}
			return bestPos;
		} else {// kör miniMax
			return miniMaxPrep();
		}
	}
	// minimax algoritm för svårighetsgrad 3
	private int miniMaxPrep() {
		// titta på hörn
		for (int edge : board.getEdges()) {
			if (getMap().containsKey(edge)) {
				return edge;
			}
		}
		int[] ret = miniMax(4, this, true);// kollar 4 steg framåt
		return ret[0];
	}
	// gör en kopia av brädan
	private int[][] deepCopyBoard(int[][] originalBoard) {

		int[][] result = new int[originalBoard.length][];
		for (int i = 0; i < originalBoard.length; i++) {
	        result[i] = Arrays.copyOf(originalBoard[i], originalBoard[i].length);
	    }
		return result;
	}
	// gör en kopia av mapen med alla moves
	private Map<Integer, List<Integer>> deepCopyMap(Map<Integer, List<Integer>> someMap) {
		
		Map<Integer, List<Integer>> retMap = new HashMap<>();
		for (Map.Entry<Integer, List<Integer>> entry : someMap.entrySet()) {
			List<Integer> willAdd = new ArrayList<>(entry.getValue());
			retMap.put(entry.getKey(), willAdd);
		}
		return retMap;
	}
	// väljer chipen som ger bästa resultat efter 4 stegs undersökning
	private int[] evaluateBoard(Player player, boolean isMaximizingPlayer) {
		int retFlips = 0; 
		int flipCount = 0;
		int retPos = 0;
		board.processMoves(player);
		Set<Integer> set = player.getMap().keySet();
		// loopar igenom alla möjliga drag
		for (int yx : player.getMap().keySet()) {
			flipCount = set.size();
			// om det finns möjlighet för hörn
			for (int edge : board.getEdges()) {
				if (yx == edge) {
					flipCount += 10;
					break;
				}
			}
			// om det är maximizingplayer då tar den draget med flest övertagningar
			if (isMaximizingPlayer) {
			
				if (flipCount >= retFlips) {
					retFlips = flipCount;
					retPos = yx;
				}
			// annars tar den minsta
			} else {
				if (flipCount <= retFlips) {
					retFlips = flipCount;
					retPos = yx;
				}
			}
		}
		// returnerar positionen och antalet övertagningar
		return new int[] {retPos, retFlips};
	}

	private int[] miniMax(int depth, Player player, boolean isMaximizingPlayer) {

		// maximizing player will be the bot

		if (depth <= 0) {
			return evaluateBoard(player, isMaximizingPlayer);
			
		}
		//värdet från evaluateboard classen
		int[] eval;
		// original board
		int[][] original = deepCopyBoard(board.getGrid());
		// array som returneras efter maximizingplayer eller minimizingplayer
		// retEval = {Position, antalFlips}
		int[] retEval;
		// initialiserar retEval baserat på isMaximizingPlayer
		if (isMaximizingPlayer) {
			
			retEval = new int[] {Integer.MIN_VALUE, Integer.MIN_VALUE}; 
		} else {
			retEval = new int[] {Integer.MAX_VALUE, Integer.MAX_VALUE};
		}
		// kopierar players map
		Map<Integer, List<Integer>> mapForLoop = deepCopyMap(player.getMap());
		for (int yx : mapForLoop.keySet()) {
			
			board.addChip(yx / 10, yx % 10, player);
			// om maximizingPlayer kallas klassen igen men med motståndaren istället som inte är maximizingPlayer
			if (isMaximizingPlayer) {
				board.processMoves(getEnemy());
				// kallar metoden igen men med motståndaren
				eval = miniMax(depth-1, getEnemy(), false);
			
				// tar den position som ger flest antal övertagningar
				int antalFlips = eval[1];
				if (antalFlips >= retEval[1]) {
					retEval[0] = yx;
					retEval[1] = eval[1];
				} 
			} else {
				board.processMoves(this);
				// kallar metoden igen men med moståndaren
				eval = miniMax(depth-1, this, true);
				// tar den position som ger minst antal övertagningar
				int antalFlips = eval[1];
				if (antalFlips <= retEval[1]) {
					retEval[0] = yx;
					retEval[1] = eval[1];
				}
			}
			// kopierar den originala brädan och den originala player mappen
			board.setGrid( deepCopyBoard(original) );
			player.setMap(deepCopyMap(mapForLoop));
				
		}
		return retEval;
	} 
	// returnerar namnet
	public String toString() {
		return "Bot";
	}
}
