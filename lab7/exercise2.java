import java.awt.Graphics;
import java.util.ArrayList;
import java.util.List;

public class Exercise2 {

    public void drawSierpinski(Graphics canvas, double x, double y, double size, int depth) {
        if (depth == 0) {
            int[] xPoints = {(int) x, (int) (x + size), (int) (x + size / 2)};
            int[] yPoints = {(int) y, (int) y, (int) (y - size * Math.sqrt(3) / 2)};
            canvas.drawPolygon(xPoints, yPoints, 3);
        } else {
            double heightOffset = size * Math.sqrt(3) / 4;
            
            drawSierpinski(canvas, x, y, size / 2, depth - 1);
            drawSierpinski(canvas, x + size / 2, y, size / 2, depth - 1);
            drawSierpinski(canvas, x + size / 4, y - heightOffset, size / 2, depth - 1);
        }
    }

    public void drawTree(Graphics canvas, double x, double y, double length, double angle, int depth) {
        double angleRad = Math.toRadians(angle);
        double newX = x + length * Math.cos(angleRad);
        double newY = y - length * Math.sin(angleRad);

        if (depth == 0) {
            canvas.drawLine((int) x, (int) y, (int) newX, (int) newY);
            return;
        }

        canvas.drawLine((int) x, (int) y, (int) newX, (int) newY);
        double nextLength = length * 0.7;
        
        drawTree(canvas, newX, newY, nextLength, angle + 30, depth - 1);
        drawTree(canvas, newX, newY, nextLength, angle - 30, depth - 1);
    }

    public double fractalDimension(int[][] fractalImage, double[] boxSizes) {
        List<Double> counts = new ArrayList<>();

        for (double size : boxSizes) {
            double numBoxes = countBoxesContainingPixels(fractalImage, size);
            counts.add(numBoxes);
        }

        double[] xValues = new double[boxSizes.length];
        double[] yValues = new double[counts.size()];

        for (int i = 0; i < boxSizes.length; i++) {
            xValues[i] = Math.log(1.0 / boxSizes[i]);
            yValues[i] = Math.log(counts.get(i));
        }

        return linearRegressionSlope(xValues, yValues);
    }

    private double countBoxesContainingPixels(int[][] image, double size) {
        return Math.random() * 100 + 1; 
    }

    private double linearRegressionSlope(double[] x, double[] y) {
        double sumX = 0;
        double sumY = 0;
        double sumXY = 0;
        double sumX2 = 0;
        int n = x.length;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
        }

        if (n * sumX2 - sumX * sumX == 0) {
            return 0;
        }

        return (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    }
}