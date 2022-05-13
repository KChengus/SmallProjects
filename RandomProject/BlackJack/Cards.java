import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;
import java.util.Random;
import java.util.ArrayList;
public class Cards {

    List<String> cards_available = new ArrayList<String>();
    Map<String, Integer> cards_value = new HashMap<>();
    Random random = new Random();
    Cards() {
        cards_available.addAll(Arrays.asList(new String[]{"2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S", "5C", "5D", "5H", "5S", "6C", "6D", "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S", "10C", "10D", "10H", "10S", "JC", "JD", "JH", "JS", "QC", "QD", "QH", "QS", "KC", "KD", "KH", "KS", "AC", "AD", "AH", "AS"}));
        System.out.println("card Created");
        for (int i = 0; i < cards_available.size(); i++) {
            String cards = cards_available.get(i);
            if (i >= cards_available.size() - 4*4) {
                int a = 0;
                if (i >= cards_available.size() - 4) {
                    a += 1;
                }
                cards_value.put(cards, 10 + a);
            } else {
                cards_value.put(cards, i / 4 + 2);
            }
        }
    }

    public String pickRandomCard() {
        int numInd = random.nextInt(cards_available.size());
        return cards_available.remove(numInd);
    }



}
