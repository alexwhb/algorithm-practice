package com.winston.sort;

public class SelectionSort {

    public static void main(String[] args) {
        int[] sortableArr = {1, 4, 7, 2, 3, 8 , 12, 16, 3, -5, 2 , 6};
        selectionSort(sortableArr);
        for(int item: sortableArr){
            System.out.println(item);
        }
    }

    public static void selectionSort(int[] arr){
        int i, j;
        int jMin;

        for(i = 0; i < arr.length -1; i++){
            jMin = i;
            for(j = i+1; j < arr.length; j++){
                if(arr[j] < arr[jMin]){
                    jMin = j;
                }
            }

            if(jMin != i){
                //swap numbers
               int temp =  arr[i];
               arr[i] = arr[jMin];
               arr[jMin] = temp;
            }
        }
    }

}
