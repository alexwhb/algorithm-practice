package com.winston.sort;

public class BubbleSort {

    public static void main(String[] args) {
        int[] sortableArr = {1, 4, 7, 2, 3, 8 , 12, 16, 3, -5, 2 , 6};
        bubbleSort(sortableArr);
        for(int item: sortableArr){
            System.out.println(item);
        }
    }

    public static void bubbleSort(int[] arr){
        boolean swapped = true;
        int j = 0;
        int temp;
        while(swapped){
            swapped = false;
            j++;
            for(int i=1; i < arr.length - j; i++){
                if(arr[i] > arr[i+1]){
                    temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    swapped = true;
                }
            }
        }
    }
}