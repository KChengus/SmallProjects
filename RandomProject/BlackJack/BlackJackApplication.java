import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;  
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class BlackJackApplication extends Application{  
    
    StackPane root;
    Button btnHit;
    Button btnStand;
    Button btnDealer;
    

    Label dealer_label; 
    Label human_label;

    Cards cardClass = new Cards();;
    Human human  = new Human(1000, cardClass);
    Dealer dealer = new Dealer(1000, cardClass);


    @Override  
    public void start(Stage primaryStage) throws FileNotFoundException {  
        // label
        dealer_label = new Label("Dealer 0"); 
        human_label = new Label("Human 0");  
        dealer_label.setTranslateY(-275);
        human_label.setTranslateY(275);
        // 700x1000
        // create scene
        root = new StackPane();
        Scene scene=new Scene(root ,400,600);
        
        // add widgets / elements to root 
        createButtons();
        root.getChildren().add(dealer_label);  
        root.getChildren().add(human_label);  
        // Set primary stage / activity
        primaryStage.setScene(scene);  
        primaryStage.setTitle("Label Class Example");  
        primaryStage.show();  
    }  

    public void createImage(String filePath, int xPos, int yPos) throws FileNotFoundException {
       
        FileInputStream input = new FileInputStream(filePath);
        Image image = new Image(input, 70, 100, false, false);
        ImageView imageview = new ImageView(image);
        imageview.setTranslateX(xPos);
        imageview.setTranslateY(yPos);
        root.getChildren().add(new Label("", imageview));
    }

    public void isDealerTurn(boolean dealerTurn) {
        if (dealerTurn) {
            dealer_label.setText("Dealer 0");
            dealer_label.setText("Human 0");
            btnHit.setDisable(true);
            btnStand.setDisable(true);
            btnDealer.setDisable(false);
        } else {
            btnHit.setDisable(false);
            btnStand.setDisable(false);
            btnDealer.setDisable(true);
        }
    }

    public void createButtons() {
        btnHit = new Button("Hit");
        btnHit.setTranslateX(-150);
        btnHit.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent arg0) {
                boolean hasBusted = human.click();
                try {
                    createImage("cards_folder/" + human.cards_store.get(human.cards_store.size()-1) + ".png", -150 + (human.cards_store.size() * 75), 200);
                    human_label.setText("Human " + human.cardsSum);
                    dealer.playerCardsSum = human.cardsSum;
                } catch (FileNotFoundException e) {
                    // TODO Auto-generated catch block
                    System.out.println("ERRIOR");
                }
                isDealerTurn(hasBusted);
            }
        });
        
        btnStand = new Button("Stand");
        btnStand.setTranslateX(-100);
        btnStand.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent arg0) {
                isDealerTurn(true);
            }
        });

        btnDealer = new Button("Dealer Move");
        btnDealer.setTranslateX(150);
        btnDealer.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent arg0) {
                boolean hasBusted = dealer.decideMove();
                try {
                    for (int i = 0; i < dealer.cards_store.size(); i++){
                        String card = dealer.cards_store.get(i);
                        createImage("cards_folder/" + card + ".png", -150 + i * 75, -200);
                    }
                    dealer_label.setText("Dealer " + dealer.cardsSum);
                    if (hasBusted || human.cardsSum > dealer.cardsSum) {
                        System.out.println("Human won");
                    } else {
                        System.out.println("Dealer won");
                    }
                } catch (FileNotFoundException e) {
                    // TODO Auto-generated catch block
                    System.out.println("ERROR");
                }
            }
        });
        Button btnReset = new Button("Reset");
        btnReset.setTranslateX(100);
        btnReset.setTranslateY(50);
        btnReset.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent arg0) {
                isDealerTurn(false);
            }
        });
        isDealerTurn(false);
        root.getChildren().add(btnReset);
        root.getChildren().add(btnDealer);
        root.getChildren().add(btnStand);
        root.getChildren().add(btnHit);
    }


    public static void main(String[] args) {  
        launch(args);  
    }  
}  