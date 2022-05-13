import java.util.Scanner;
public class Human extends Player {
    Scanner sc= new Scanner(System.in);

    public Human(int money, Cards cardClass) {
        super(money, cardClass);
        playerName = "Human";
        //TODO Auto-generated constructor stub
    }

    @Override
    public boolean decideMove() {
        String card;
        do {
            card = cardClass.pickRandomCard();
            addCard(card);
            System.out.println("Human picked up " + card + ", sum is now " + cardsSum);
        } while (cardsSum <= 21 && sc.nextLine().trim().equals("hit"));
        return (cardsSum > 21);
    }

    public boolean click() {

        String card;
        card = cardClass.pickRandomCard();
        addCard(card);
        return cardsSum > 21;
    }
}
