import java.util.*;

public class RecommendationSystem {
    static class Result {
        int id;
        double score;
        Result(int id, double score) { this.id = id; this.score = score; }
    }

    public static void main(String[] args) {
        double[][] dataMatrix = {
            {5, 0, 8, 0, 2},
            {4, 9, 0, 7, 1},
            {5, 0, 7, 0, 3},
            {0, 0, 0, 9, 9},
            {4, 0, 9, 2, 0}
        };
        int targetID = 0;
        int K = 2;
        List<Result> resultsList = new ArrayList<>();

        for (int i = 0; i < dataMatrix.length; i++) {
            double dotProd = 0, sumA = 0, sumB = 0;
            for (int k = 0; k < dataMatrix[0].length; k++) {
                dotProd += dataMatrix[targetID][k] * dataMatrix[i][k];
                sumA += Math.pow(dataMatrix[targetID][k], 2);
                sumB += Math.pow(dataMatrix[i][k], 2);
            }
            double sim = (sumA == 0 || sumB == 0) ? 0 : dotProd / (Math.sqrt(sumA) * Math.sqrt(sumB));
            resultsList.add(new Result(i, sim));
        }

        resultsList.sort((a, b) -> Double.compare(b.score, a.score));
        int count = 0;
        Integer bestMatch = null;
        for (Result item : resultsList) {
            if (item.id != targetID) { 
                System.out.println("Recommended Friend: " + item.id);
                if (bestMatch == null) bestMatch = item.id;
                if (++count >= K) break;
            }
        }
        if (bestMatch != null) {
            for (int j = 0; j < dataMatrix[0].length; j++) {
                if (dataMatrix[targetID][j] == 0 && dataMatrix[bestMatch][j] > 5) {
                    System.out.println("You should try topic " + j);
                }
            }
        }
    }
}
