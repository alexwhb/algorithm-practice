package com.winston.sort;

public class CombSort {

    public static void main(String[] args) {
        int[] sortableArr = {1, 4, 7, 2, 3, 8 , 12, 16, 3, -5, 2 , 6};
        combSort(sortableArr);
        for(int item: sortableArr){
            System.out.println(item);
        }
    }

    private static void combSort(int[] arr) {
        int size = arr.length;
        int gap = size;
        boolean swapped = true;
        int i;

        while(gap > 1 || swapped){
            if (gap > 1) {
                gap = (int)(gap / 1.3);
            }
            i = 0;
            swapped = false;
            // Loop through comparing numbers a gap-length apart.
            // If the first number is bigger than the second, swap them.
            while (i + gap < arr.length) {
                if (arr[i] > arr[i+gap]) {
                    swap(arr, i, i+gap);
                    swapped = true;
                }
                i++;
            }
        }
    }

    public static void swap(int[] list, int i, int j) {
        /* This method simply takes an array
        and swaps its values at index i and j */

        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }

}
