import java.util.*;

public class exercise1 {
    private int n;
    private List<List<Integer>> adj;

    public exercise1(int n) {
        this.n = n;
        this.adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    }

    public void addEdge(int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    public boolean isValidCoverage(List<Integer> selected) {
        boolean[] covered = new boolean[n];
        for (int u : selected) {
            if (u < 0 || u >= n) continue;
            covered[u] = true;
            for (int v : adj.get(u)) covered[v] = true;
        }
        for (boolean c : covered) if (!c) return false;
        return true;
    }

    public List<Integer> findMinimumCoverage() {
        List<Integer> best = null;
        for (int i = 0; i < (1 << n); i++) {
            List<Integer> current = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) current.add(j);
            }
            if (isValidCoverage(current)) {
                if (best == null || current.size() < best.size()) {
                    best = new ArrayList<>(current);
                }
            }
        }
        return best;
    }

    public List<Integer> findFastCoverage() {
        List<Integer> selected = new ArrayList<>();
        boolean[] covered = new boolean[n];
        int count = 0;
        while (count < n) {
            int bestNode = -1;
            int maxGain = -1;
            for (int i = 0; i < n; i++) {
                int gain = 0;
                if (!covered[i]) gain++;
                for (int neighbor : adj.get(i)) if (!covered[neighbor]) gain++;
                if (gain > maxGain) {
                    maxGain = gain;
                    bestNode = i;
                }
            }
            if (bestNode == -1) break;
            selected.add(bestNode);
            if (!covered[bestNode]) { covered[bestNode] = true; count++; }
            for (int neighbor : adj.get(bestNode)) {
                if (!covered[neighbor]) { covered[neighbor] = true; count++; }
            }
        }
        return selected;
    }

    public static void main(String[] args) {
        exercise1 ex = new exercise1(6);
        ex.addEdge(0, 1);
        ex.addEdge(1, 2);
        ex.addEdge(0, 3);
        ex.addEdge(1, 4);
        ex.addEdge(3, 4);
        ex.addEdge(4, 5);

        List<Integer> min = ex.findMinimumCoverage();
        List<Integer> fast = ex.findFastCoverage();

        System.out.println(min.size() + " " + min);
        System.out.println(fast.size() + " " + fast);
    }
} 
