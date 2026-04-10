import java.util.ArrayList;
import java.util.List;

class CategoryNode {
    String categoryId;
    String name;
    int postCount;
    CategoryNode left;
    CategoryNode right;
    CategoryNode parent;

    public CategoryNode(String categoryId, String name, int postCount) {
        this.categoryId = categoryId;
        this.name = name;
        this.postCount = postCount;
    }
}
public class exercise2 {

    public List<String> inOrderCollect(CategoryNode root) {
        List<String> result = new ArrayList<>();
        inOrderCollectHelper(root, result); 
        return result;
    }

    private void inOrderCollectHelper(CategoryNode node, List<String> result) {
        if (node == null) return;
        inOrderCollectHelper(node.left, result);
        result.add(node.name);
        inOrderCollectHelper(node.right, result);
    }


    public void inOrderAccumulatePosts(CategoryNode root) {
        int[] runningTotal = {0}; 
        inOrderAccumulateHelper(root, runningTotal);
    }

    private void inOrderAccumulateHelper(CategoryNode node, int[] total) {
        if (node == null) return;
        inOrderAccumulateHelper(node.left, total);
        
        total[0] += node.postCount;
        System.out.println(node.name + " running total: " + total[0]);
        
        inOrderAccumulateHelper(node.right, total);
    }

    public CategoryNode inOrderFindKth(int k, CategoryNode root) {
        int[] counter = {0};
        return inOrderFindKthHelper(k, root, counter);
    }

    private CategoryNode inOrderFindKthHelper(int k, CategoryNode node, int[] counter) {
        if (node == null) return null;

        CategoryNode leftResult = inOrderFindKthHelper(k, node.left, counter);
        if (leftResult != null) return leftResult; 
        counter[0]++;
        if (counter[0] == k) return node;
        return inOrderFindKthHelper(k, node.right, counter);
    }

    public String preOrderExport(CategoryNode root) {
        StringBuilder sb = new StringBuilder();
        preOrderExportHelper(root, 0, sb);
        return sb.toString();
    }

    private void preOrderExportHelper(CategoryNode node, int depth, StringBuilder sb) {
        if (node == null) return;

        for (int i = 0; i < depth; i++) sb.append("  ");
        sb.append(node.name).append("(").append(node.postCount).append(")\n");
        
        preOrderExportHelper(node.left, depth + 1, sb);
        preOrderExportHelper(node.right, depth + 1, sb);
    }

    public CategoryNode preOrderCopy(CategoryNode root) {
        if (root == null) return null;
        
        CategoryNode copy = new CategoryNode(root.categoryId, root.name, root.postCount);
        
        copy.left = preOrderCopy(root.left);
        if (copy.left != null) copy.left.parent = copy; 
        
        copy.right = preOrderCopy(root.right);
        if (copy.right != null) copy.right.parent = copy;
        
        return copy;
    }

    public String preOrderSerialize(CategoryNode root) {
        List<String> items = new ArrayList<>();
        preOrderSerializeHelper(root, items);

        return String.join("|", items); 
    }

    private void preOrderSerializeHelper(CategoryNode node, List<String> items) {
        if (node == null) return;
        items.add(node.name + "(" + node.postCount + ")");
        preOrderSerializeHelper(node.left, items);
        preOrderSerializeHelper(node.right, items);
    }

    public int postOrderTotalPosts(CategoryNode node) {
        if (node == null) return 0;
        int leftTotal = postOrderTotalPosts(node.left);
        int rightTotal = postOrderTotalPosts(node.right);
        return node.postCount + leftTotal + rightTotal;
    }

    public double postOrderAverageDepth(CategoryNode root) {

        int[] stats = {0, 0}; 

        calculateDepthHelper(root, 0, stats); 
        
        if (stats[1] == 0) return 0.0;
        return (double) stats[0] / stats[1];
    }

    private void calculateDepthHelper(CategoryNode node, int depth, int[] stats) {
        if (node == null) return;
        
        calculateDepthHelper(node.left, depth + 1, stats);
        calculateDepthHelper(node.right, depth + 1, stats);
        
 
        if (node.left == null && node.right == null) {
            stats[0] += depth;
            stats[1]++;
        }
    }

    // 3. post_order_collect_leaves
    public List<CategoryNode> postOrderCollectLeaves(CategoryNode root) {
        List<CategoryNode> leaves = new ArrayList<>();
        collectLeavesHelper(root, leaves);
        return leaves;
    }

    private void collectLeavesHelper(CategoryNode node, List<CategoryNode> leaves) {
        if (node == null) return;
        
        collectLeavesHelper(node.left, leaves);
        collectLeavesHelper(node.right, leaves);
        
        if (node.left == null && node.right == null) {
            leaves.add(node);
        }
    }



    public CategoryNode findMostPopularCategory(CategoryNode root) {
        CategoryNode[] bestNode = {null};
        int[] maxPosts = {-1};
        findPopularHelper(root, bestNode, maxPosts);
        return bestNode[0];
    }

    private void findPopularHelper(CategoryNode node, CategoryNode[] bestNode, int[] maxPosts) {
        if (node == null) return;
        
        if (node.postCount > maxPosts[0]) {
            maxPosts[0] = node.postCount;
            bestNode[0] = node;
        }
        
        findPopularHelper(node.left, bestNode, maxPosts);
        findPopularHelper(node.right, bestNode, maxPosts);
    }

    public CategoryNode categoryWithMostSubcategories(CategoryNode root) {
        CategoryNode[] topParent = {null};
        int[] maxChildren = {-1};
        findMostSubcategoriesHelper(root, topParent, maxChildren);
        return topParent[0];
    }

    private void findMostSubcategoriesHelper(CategoryNode node, CategoryNode[] topParent, int[] maxChildren) {
        if (node == null) return;
        
        int count = 0;
        if (node.left != null) count++;
        if (node.right != null) count++;
        
        if (count > maxChildren[0]) {
            maxChildren[0] = count;
            topParent[0] = node;
        }
        
        findMostSubcategoriesHelper(node.left, topParent, maxChildren);
        findMostSubcategoriesHelper(node.right, topParent, maxChildren);
    }
}