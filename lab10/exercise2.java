import java.util.*;

public class exercise2 {

    public boolean isWithinBudget(List<Integer> selection, int[] costs, int budget) {
        int total = 0;
        for (int id : selection) total += costs[id];
        return total <= budget;
    }

    public Object[] maximizeReachExact(int budget, int[] costs, int[] reaches) {
        int n = costs.length;
        int[][] dp = new int[n + 1][budget + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= budget; w++) {
                if (costs[i - 1] <= w) {
                    dp[i][w] = Math.max(reaches[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        List<Integer> selected = new ArrayList<>();
        int w = budget;
        for (int i = n; i > 0; i--) {
            if (dp[i][w] != dp[i - 1][w]) {
                selected.add(i - 1);
                w -= costs[i - 1];
            }
        }
        return new Object[]{dp[n][budget], selected};
    }

    public Object[] maximizeReachGreedy(int budget, int[] costs, int[] reaches) {
        int n = costs.length;
        Double[][] ratios = new Double[n][2];
        for (int i = 0; i < n; i++) {
            ratios[i][0] = (double) reaches[i] / costs[i];
            ratios[i][1] = (double) i;
        }

        Arrays.sort(ratios, (a, b) -> b[0].compareTo(a[0]));

        int totalReach = 0;
        int currentCost = 0;
        List<Integer> selected = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int idx = ratios[i][1].intValue();
            if (currentCost + costs[idx] <= budget) {
                currentCost += costs[idx];
                totalReach += reaches[idx];
                selected.add(idx);
            }
        }
        return new Object[]{totalReach, selected};
    }

    public static void main(String[] args) {
        exercise2 ex = new exercise2();
        int budget = 10;
        int[] costs = {6, 5, 5};
        int[] reaches = {10, 7, 7};

        Object[] exact = ex.maximizeReachExact(budget, costs, reaches);
        Object[] greedy = ex.maximizeReachGreedy(budget, costs, reaches);

        System.out.println(exact[0] + " " + exact[1]);
        System.out.println(greedy[0] + " " + greedy[1]);
    }
}
