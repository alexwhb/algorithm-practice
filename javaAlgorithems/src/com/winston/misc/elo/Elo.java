package com.winston.misc.elo;

public class Elo {


    private final Player winner;
    private final Player looser;

    private static final int k = 20; // this is a constant for elo

    public Elo(Player winner, Player looser){
        this.winner = winner;
        this.looser = looser;
        updateWinner();
        updateLooser();
    }

    private void updateLooser() {
        float newElo = looser.getRating() + (k * (0 - looser.getWinningProbibility(winner)));
        looser.setRating(newElo);
    }

    private void updateWinner() {
        float newElo = winner.getRating() + (k * ( 1 - winner.getWinningProbibility(looser)));
        winner.setRating(newElo);
    }


    public static void main(String[] args) {

        Player player1 = new Player();
        Player player2 = new Player();

        for(int i = 0; i < 10; i++) {
            new Elo(player1, player2);

            System.out.println("Player 1: "+player1.getRating());
            System.out.println("player 2: "+ player2.getRating());
        }
    }

}

