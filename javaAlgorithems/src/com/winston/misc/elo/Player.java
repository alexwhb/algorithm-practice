package com.winston.misc.elo;


public class Player {

    private float rating;

    public Player(){
        // Base rating of 1600 always
        this.rating = 1600;
    }

    public float getWinningProbibility(Player opponent){
         // Probablility that this player will win against opponent
        return 1.0f/ ( 10 * (( opponent.rating - this.rating)/400) + 1 );
    }

    public float getRating(){
        return rating;
    }


    public void setRating(float newRating){
        this.rating = newRating;
    }

}
