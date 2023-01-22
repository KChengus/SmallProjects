import java.util.Random;
import java.util.Set;
import java.util.HashSet;

public class Board {
    private int sizeOfBoard;
    private int sizeOfSquare;
    private int[][] board;
    private Random rand;
    private Set<Integer> uniqueNumbers;
    Board(){
        sizeOfSquare = 3;
        sizeOfBoard = (int) Math.pow(sizeOfSquare, 2);
        board = new int[sizeOfBoard][sizeOfBoard];
    }

    public boolean isValidRowOrCol(int row, int col) {
        uniqueNumbers = new HashSet<>();
        for (int c = 0; c < sizeOfBoard; c++) {
            uniqueNumbers.add(board[row][c]);
        }
        if (uniqueNumbers.size() < 9) {
            return false;
        }

        uniqueNumbers = new HashSet<>();
        for (int r = 0; r < sizeOfBoard; r++) {
            uniqueNumbers.add(board[r][col]);
        }
        return (uniqueNumbers.size() == 9);
    }

    public boolean isValidBox(int row, int col) {
        uniqueNumbers = new HashSet<>();
        // assume that row and col is the most left upper cell of the box
        for (int r = row; r < row+sizeOfSquare; r++) {
            for (int c = col; c < col+sizeOfSquare; c++) {
                uniqueNumbers.add(board[r][c]);
            }
        }
        return (uniqueNumbers.size()==9);
    }


    public void generateRandomBoard() {
        rand = new Random();
        // loop through each grid in the 2 dimensional board
        for (int r = 0; r < sizeOfBoard; r++) {
            // loop through each row
            for (int c = 0; c < sizeOfBoard; c++) {
                // loop through each column
                board[r][c] = rand.nextInt(sizeOfBoard + 1);
            }
        }
    }

    public void printBoard() {
        for (int r = 0; r < sizeOfBoard; r++) {
            if (r % 3 == 0) {
                System.out.println("=".repeat(40));
            }
            System.out.print("|| ");
            for (int c = 0; c < sizeOfBoard; c++) {
                System.out.print(board[r][c]);
                if ((c + 1) % 3 == 0) {
                    System.out.print(" || ");
                } else {
                    System.out.print(" | ");
                }
            }
            System.out.println();  
        }
        System.out.println("=".repeat(40));
    }

    public int getsizeOfBoard() {
        return sizeOfBoard;
    }
    public int getsizeOfSquare() {
        return sizeOfSquare;
    }
}
