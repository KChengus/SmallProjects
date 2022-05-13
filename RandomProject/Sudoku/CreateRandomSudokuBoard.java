public class CreateRandomSudokuBoard {
    Board sudokuBoard = new Board();
    
    public void run() {
        int d = 0;
        sudokuBoard.generateRandomBoard();
        sudokuBoard.printBoard();
        for (d = 0; d < sudokuBoard.getsizeOfBoard(); d++) {
            if (!sudokuBoard.isValidRowOrCol(d, d)) {
                break;
            }
        }
        if (d == sudokuBoard.getsizeOfBoard()) {
            // isvalid on row and column;
            // check each boxes
            int r = 0;
            int c = 0;
            for (r = 0; r < sudokuBoard.getsizeOfSquare(); r++) {
                for (c = 0; c < sudokuBoard.getsizeOfSquare(); c++) {
                    if (!sudokuBoard.isValidBox(d, d)) {
                        break;
                    }
                }
                if (!(c == sudokuBoard.getsizeOfBoard())) {
                    break;
                }
            }
            if (r == sudokuBoard.getsizeOfBoard()) {
                // valid board
                System.out.println("VALID BOARD");
            } else {
                System.out.println("Invalid board because of invalid box");
            }

        } else {
            System.out.println("Invalid board because of invalid row or column");
        }
    }
    public static void main(String[] args) {
        new CreateRandomSudokuBoard().run();

    }
}
