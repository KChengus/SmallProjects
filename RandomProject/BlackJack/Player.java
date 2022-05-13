import java.util.ArrayList;

public abstract class Player {
    int money;
    ArrayList<String> cards_store;
    int cardsSum;
    Cards cardClass;
    String playerName;
    public Player(int money, Cards cardClass) {
        this.money = money;
        this.cardClass = cardClass;
        cards_store = new ArrayList<>();
        cardsSum = 0;
        
    }

    public void addCard(String card) {
        cards_store.add(card);
        cardsSum += cardClass.cards_value.get(card);
    }

    public abstract boolean decideMove();

}
