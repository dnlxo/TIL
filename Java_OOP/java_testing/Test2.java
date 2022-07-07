import java.util.*;

public class Test2 {
}

public static void quick(int[] arr, int left, int right) {
    int pivotIdx = partition(arr, left, right);
    if (left >= right) {
        return;
    }
    quick(arr, left, pivotIdx - 1);
    quick(arr, pivotIdx + 1, right);

}

public static int partition(int[] arr, int left, int right) {
    int pivot = arr[(left + right) / 2];
    while (left < right) {
        while (arr[left] < pivot) {
            left++;
        }
        while (arr[right] > pivot) {
            right--;
        }
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }
    return left;
}