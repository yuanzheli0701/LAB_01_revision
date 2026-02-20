import java.util.*;

public class exercise3 {

    static class Result {
        int id;
        double score;

        Result(int id, double score) {
            this.id = id;
            this.score = score;
        }
    }

    public static void main(String[] args) {
        mainSystem();
    }

    public static void mainSystem() {
        double[][] dataMatrix = loadData();
        int targetID = 0;
        int K = 2;
        List<Result> resultsList = new ArrayList<>();

        for (int i = 0; i < dataMatrix.length; i++) {
            double[] rowA = dataMatrix[targetID];
            double[] rowB = dataMatrix[i];
            double sim = cosineCalc(rowA, rowB);
            resultsList.add(new Result(i, sim));
        }

        resultsList.sort((a, b) -> Double.compare(b.score, a.score));

        int count = 0;
        Integer bestMatch = null;

        System.out.println("Recommended Friend:");
        for (Result item : resultsList) {
            if (item.id != targetID && !checkIfFriend(targetID, item.id)) {
                System.out.println(item.id);

                if (bestMatch == null) {
                    bestMatch = item.id;
                }

                count++;
                if (count >= K) break;
            }
        }

        if (bestMatch != null) {
            double[] userRatings = dataMatrix[targetID];
            double[] friendRatings = dataMatrix[bestMatch];

            for (int j = 0; j < userRatings.length; j++) {
                if (userRatings[j] == 0 && friendRatings[j] > 5) {
                    System.out.println("You should try topic " + j);
                }
            }
        }
    }

    public static double cosineCalc(double[] vec1, double[] vec2) {
        double dotProd = 0;
        double sumA = 0;
        double sumB = 0;

        for (int k = 0; k < vec1.length; k++) {
            dotProd += (vec1[k] * vec2[k]);
            sumA += (vec1[k] * vec1[k]);
            sumB += (vec2[k] * vec2[k]);
        }

        if (sumA == 0 || sumB == 0) return 0;
        return dotProd / (Math.sqrt(sumA) * Math.sqrt(sumB));
    }

    private static double[][] loadData() {
        return new double[][]{
                {5, 0, 8, 0, 2},
                {4, 9, 0, 7, 1},
                {5, 0, 7, 0, 3},
                {0, 0, 0, 9, 9},
                {4, 0, 9, 2, 0}
        };
    }

    private static boolean checkIfFriend(int id1, int id2) {
        return false;
    }
}