public class Dealer extends Player{

    int playerCardsSum;
    public Dealer(int money, Cards cardClass) {
        super(money, cardClass);
        playerCardsSum = 0;
        playerName = "Dealer";
    }

    @Override
    public boolean decideMove() {
        // TODO Auto-generated method stub
        String card;
        while (cardsSum < playerCardsSum && cardsSum <= 16) {
            card = cardClass.pickRandomCard();
            addCard(card);
            System.out.println("Dealer picked up " + card + ", sum is now " + cardsSum);
        }
        return (cardsSum > 21);
    }
    
}
