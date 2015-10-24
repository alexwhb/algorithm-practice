package com.winston.sort;

public class InsertionSort {

    /*
        pretty much this is a really slow algorithm on large data sets, but it's a really simple one.
        It is however, very fast on small data sets.
     */

    public static void main(String[] args) {
        int[] sortableArr = {1, 4, 7, 2, 3, 8 , 12, 16, 3, -5, 2 , 6};
        insertionSort(sortableArr);
        for(int item: sortableArr){
            System.out.println(item);
        }
    }


    public static void insertionSort(int[] arr){
        int j, i;
        for(i = 1; i < arr.length; i++){
            int key = arr[i];
            for(j = i-1; ( j >= 0 ) && (arr[j] > key); j--){
                arr[j+1] = arr[j];
            }
            arr[j+1] = key;
        }
    }

}
