import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Color;

import java.util.List;
import java.util.Map;
import java.util.HashMap;
public class Main extends JFrame implements ActionListener {
	// definerar serialID
	private static final long serialVersionUID = 1L;
	// defienrar brädan och knappar
	private JPanel boardGUI;
	private JButton[][] button;
	// skapar mapen och variabler
	private Othello othello = new Othello();
	private boolean p1Turn = true;
	private Map<Integer, Color> colorMap = new HashMap<>();
	
	// definerar utseendet för hela panelen
	private Main() { 
		
		boardGUI = new JPanel(new GridLayout(8, 8));
		boardGUI.setVisible(true);
		
		this.setLayout(new BorderLayout());
		this.setSize(800, 800);
		
		this.add(boardGUI, BorderLayout.CENTER);
	}
	
	// lägger till chip på valda positionen
	private void handleEvent(Player player, int position) {
		othello.board.addChip(position/10, position%10, player);
		
		button[position/10][position%10].setBackground(colorMap.get(player.getColor()));
		changeColor(player.getMap().get(position), player.getColor());
		// process moves
		othello.everyoneProcessMoves();
	}
	
	// Ärndrar färg på chipen som man tryckte på
	public void actionPerformed(ActionEvent e) {
		// kollar om spelet är över
		if (othello.isGameOver()) {
			// kör om spelet
			JFrame jFrame = new JFrame();
			// skriver ut vem som vann
            JOptionPane.showMessageDialog(jFrame, othello.board.stats(othello.p1, othello.p2));
			reset();
			return;
		}
		// får kordinaterna
		String action = e.getActionCommand();
		String[] cords = action.split(" ");
		// vems tur det är
		Player player;
		if (p1Turn) {
			player = othello.p1;
		} else {
			player = othello.p2;
		}
		// tar kordinaten
		int yx = player.move();
		if (yx == -1) {
			yx = Integer.parseInt(cords[0]) * 10 + Integer.parseInt(cords[1]);
		}
		// om kordinaten finns i tillgängliga moves då lägger en chip på brädan
		if (player.getMap().containsKey(yx)) {
			handleEvent(player, yx);
			// byter spelare
			player = player.getEnemy();
			
			p1Turn = !p1Turn;
			changeTitle(player);
		// om det finns inga moves då byter spelare
		} else if (player.getMap().isEmpty()) {
			p1Turn = !p1Turn;
			player = player.getEnemy();
			changeTitle(player);
		}
	}
	// byter titel på spelaren
	private void changeTitle(Player player) {
		String s;
		if (p1Turn) {
			s = "p1 " + player.toString();
		} else {
			s = "p2 " + player.toString();
		}
		// om det är boten då skriver nivån 
		if (player.toString().equals("Bot")) {
			s += " Level " + player.getDiff() + " (click anywhere to move)";
		}
		this.setTitle(s);
	}
	
	// ska byta färg på alla andra chips som blev övertagna
	private void changeColor(List<Integer> array, int color) {
		for (int elem : array) {
			
			int row = elem / 10;
			int cols = elem % 10;
	
			button[row][cols].setBackground(colorMap.get(color));
		}
	}

	private void start() {
		button = new JButton[8][8];
		changeTitle(othello.p1);		
		// bestämmer färgerna
		colorMap.put(0, (Color.GREEN).darker());
		colorMap.put(-1,(Color.BLACK));
		colorMap.put(1, (Color.WHITE));
		// skapar meny bar som är övanför brädan
        final JMenuBar menuBar = new JMenuBar();
        JMenu menu = new HorizontalMenu("Menu");
        menuBar.add(menu);
        JMenuItem instruction = new JMenuItem("Instruction");
        menu.add(instruction);
        JMenuItem reset = new JMenuItem("Reset Game");
        menu.add(reset);
        JMenuItem exit = new JMenuItem("Exit");
        menu.add(exit);
        JMenu p1p2 = new HorizontalMenu("P1 vs P2");
        menuBar.add(p1p2);
        JMenuItem hb = new JMenuItem("Human vs Bot");
        p1p2.add(hb);
        JMenuItem hh = new JMenuItem("Human vs Human");
        p1p2.add(hh);
        JMenuItem bb = new JMenuItem("Bot vs Bot");
        p1p2.add(bb);
        JMenu botLevel = new HorizontalMenu("Bot level");
        menuBar.add(botLevel);
        JMenuItem ez = new JMenuItem("EZ");
        botLevel.add(ez);
        JMenuItem aj = new JMenuItem("Avarage Joe");
        botLevel.add(aj);
        JMenuItem sth = new JMenuItem("Sweaty Tryhard");
        botLevel.add(sth);
        // deffinerar funktioner för alla knappar från menyn
        class exitact implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		System.exit(0);
        	}
        }
        
        class resetGame implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		reset();
        	}
        }
        
        class instruct implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		JFrame jFrame = new JFrame();
//        		jFrame.setTitle("Instructions");
        		String instructions = "*Man kan lägga en bricka åt gången.\n*Läs regler för Othello på google :D.\n*Spelet är slut då ingen kan lägga brickor längre\n*Spelaren med flest brickor i slutet vinner";
                JOptionPane.showMessageDialog(jFrame, instructions);
        	}
        }
        
        class hVSb implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		reset();
        		othello.p1 = new Human();
        		othello.p2 = new Bot(othello.botDiff, othello.board);
        		othello.start();
        	}
        }
        
        class hVSh implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		reset();
        		othello.p1 = new Human();
        		othello.p2 = new Human();
        		othello.start();
        	}
        }
        
        class bVSb implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		reset();
        		othello.p1 = new Bot(othello.botDiff, othello.board);
        		othello.p2 = new Bot(othello.botDiff, othello.board);
        		othello.start();
        	}
        }
        
        class easy implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		othello.p1.setDiff(1);
        		othello.p2.setDiff(1);
        	}
        }
        
        class medium implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		othello.p1.setDiff(2);
        		othello.p2.setDiff(2);
        	}
        }
        
        class hard implements ActionListener {
        	public void actionPerformed (ActionEvent e) {
        		othello.p1.setDiff(3);
        		othello.p2.setDiff(3);
        	}
        }
        // lägger till funktionerna på knapparna från menyn
        exit.addActionListener(new exitact());
        instruction.addActionListener(new instruct());
        hb.addActionListener(new hVSb());
        hh.addActionListener(new hVSh());
        bb.addActionListener(new bVSb());
        ez.addActionListener(new easy());
        aj.addActionListener(new medium());
        sth.addActionListener(new hard());
        reset.addActionListener(new resetGame());
        // skapar knapparna med kordinater och färger 
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				button[i][j] = new JButton();
				button[i][j].setEnabled(true);
				button[i][j].addActionListener(this);
				button[i][j].setActionCommand(i + " " + j);
				button[i][j].setVisible(true);
				button[i][j].setBackground(colorMap.get(othello.board.getGrid()[i][j]));
				boardGUI.add(button[i][j]);
			}
			
		}
		// skapar meny baren
		this.add(menuBar, BorderLayout.NORTH);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
	}
	// kör horizontal meny bar
	class HorizontalMenu extends JMenu {
		
		private static final long serialVersionUID = 1L;
		
		public HorizontalMenu(String aText) {
            super(aText);
        }
        @Override
        protected Point getPopupMenuOrigin() {
            return new Point(0, getHeight());
        }
    }
	// restartar spelet
	private void reset() {
		othello.reset();
		
		p1Turn = true;
		
		changeTitle(othello.p1);		
		// sätter till default
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				button[i][j].setBackground(colorMap.get(othello.board.getGrid()[i][j]));
			}
		}
	}
	// main
	public static void main(String args[])  {
		Main st = new Main();
		st.start();
		st.setVisible(true);
	}
}
