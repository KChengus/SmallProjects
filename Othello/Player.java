import java.util.Map;
import java.util.Random;
import java.util.List;
import java.util.HashMap;

// parent abstract class
public abstract class Player {
	
	// incapsling
	private int myColor;
	private Map<Integer, List<Integer>> map;
	private Player enemy;
	protected int difficulty;
	// constructor
	Player() {
		map = new HashMap<>();
	}
	// abstrakta metoder
	public abstract int move();
	public abstract String toString();
	// genererar random move
	public int moveRandom() {
		int yx = new Random().nextInt(getMap().size());
		return (int) getMap().keySet().toArray()[yx];
	}
	// getter setter metoder
	public void setEnemy(Player enemy) {
		this.enemy = enemy;
	}
	
	public Player getEnemy() {
		return enemy;
	}

	public int getColor() {
		return myColor;
	}
	
	public void setColor(int myColor) {
		this.myColor = myColor;
	}
	
	public void setMap(Map<Integer, List<Integer>> newMap) {
		// shallow copy
		map = newMap;
	}
	
	public Map<Integer, List<Integer>> getMap() {
		return map;
	}
	
	public void setDiff (int diff) {
		difficulty = diff;
	}
	
	public int getDiff () {
		return difficulty;
	}
	
		
}
