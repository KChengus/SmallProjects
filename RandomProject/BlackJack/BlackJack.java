/*
    cards_value = {'2C' : 2, '2D' : 2, '2H' : 2, '2S' : 2, '3C' : 3, '3D' : 3, '3H' : 3, '3S' : 3, '4C' : 4, '4D' : 4, '4H' : 4, '4S' : 4, '5C' : 5, '5D' : 5, '5H' : 5, '5S' : 5, '6C' : 6, '6D' : 6, '6H' : 6, '6S' : 6, '7C' : 7, '7D' : 7, '7H' : 7, '7S' : 7, '8C' : 8, '8D' : 8, '8H' : 8, '8S' : 8, '9C' : 9, '9D' : 9, '9H' : 9, '9S' : 9, '10C' : 10, '10D' : 10, '10H' : 10, '10S' : 10, 'JC' : 10, 'JD' : 10, 'JH' : 10, 'JS' : 10, 'QC' : 10, 'QD' : 10, 'QH' : 10, 'QS' : 10, 'KC' : 10, 'KD' : 10, 'KH' : 10, 'KS' : 10, 'AC' : 11, 'AD' : 11, 'AH' : 11, 'AS' : 11}
    is_busted = False
    cards_available = []
*/
public class BlackJack {
    Cards cardClass;
    Human human;
    Dealer dealer;

    BlackJack() {
        cardClass = new Cards();
        human = new Human(1000, cardClass);
        dealer = new Dealer(1000, cardClass);
    }
    public void winner(Player w, Player l) {
        w.money += 100;
        l.money -= 100;
        System.out.println("The winner is " + w.playerName + " and has a total of " + w.money + " coins");
    } 

    public void run() {
        if (human.decideMove()) {
            // human bust
            winner(dealer, human);
            return;
        }
        dealer.playerCardsSum = human.cardsSum;
        if (dealer.decideMove()) {
            // dealer bust
            winner(human, dealer);
            return;
        }
        if (human.cardsSum > dealer.cardsSum) {
            winner(human, dealer);
        } else if (human.cardsSum < dealer.cardsSum) {
            winner(dealer, human);
        } 
    }

    public static void main(String[] args) {
        new BlackJack().run();
    }
}