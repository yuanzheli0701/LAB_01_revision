import java.util.ArrayList;
import java.util.List;

public class exercise3 {

    public static List<int[]> mergeIntervals(int[][] intervals) {
        List<int[]> myList = new ArrayList<>();
        for (int[] interval : intervals) {
            myList.add(new int[]{interval[0], interval[1]});
        }
        int i = 0;
        while (i < myList.size()) {
            boolean mergedSomething = false;
            int[] first = myList.get(i);

            for (int j = i + 1; j < myList.size(); j++) {
                int[] second = myList.get(j);
                if (first[0] <= second[1] && second[0] <= first[1]) {
                    first[0] = Math.min(first[0], second[0]);
                    first[1] = Math.max(first[1], second[1]);
                    myList.remove(j);
                    mergedSomething = true;
                    break;
                }
            }
            if (!mergedSomething) {
                i = i + 1;
            }
        }
        return myList;
    }

    public static void main(String[] args) {
        int[][] data = {{1, 3}, {2, 6}, {15, 18}, {8, 10}};
        List<int[]> result = mergeIntervals(data);
        System.out.print("[");
        for (int k = 0; k < result.size(); k++) {
            int[] interval = result.get(k);
            System.out.print("[" + interval[0] + "," + interval[1] + "]");
            if (k < result.size() - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
}
