import java.util.*;

class CommentNode {
    int comment_id;
    int user_id;
    String content;
    String timestamp;
    int likes;
    List<CommentNode> replies;

    CommentNode(int comment_id, int user_id, String content, String timestamp, int likes) {
        this.comment_id = comment_id;
        this.user_id = user_id;
        this.content = content;
        this.timestamp = timestamp;
        this.likes = likes;
        this.replies = new ArrayList<>();
    }
}

public class RecursiveComments {

    public static void display_thread(CommentNode comment, int level) {
        int i = 0;
        while (i < level) {
            System.out.print("  ");
            i++;
        }
        System.out.println(comment.comment_id + " : " + comment.content);

        for (CommentNode reply : comment.replies) {
            display_thread(reply, level + 1);
        }
    }

    public static int count_total_comments(CommentNode comment) {
        int total = 1;

        for (CommentNode reply : comment.replies) {
            total = total + count_total_comments(reply);
        }

        return total;
    }

    public static int total_likes(CommentNode comment) {
        int sum = comment.likes;

        for (CommentNode reply : comment.replies) {
            sum = sum + total_likes(reply);
        }

        return sum;
    }

    public static int find_deepest_reply(CommentNode comment) {
        int maxDepth = 0;

        for (CommentNode reply : comment.replies) {
            int depth = find_deepest_reply(reply);
            if (depth > maxDepth) {
                maxDepth = depth;
            }
        }

        return maxDepth + 1;
    }

    public static List<CommentNode> search_by_user(int user_id, CommentNode comment) {
        List<CommentNode> result = new ArrayList<>();

        if (comment.user_id == user_id) {
            result.add(comment);
        }

        for (CommentNode reply : comment.replies) {
            List<CommentNode> temp = search_by_user(user_id, reply);
            for (CommentNode c : temp) {
                result.add(c);
            }
        }

        return result;
    }

    public static boolean contains_keyword(String keyword, CommentNode comment) {
        if (comment.content.contains(keyword)) {
            return true;
        }

        for (CommentNode reply : comment.replies) {
            if (contains_keyword(keyword, reply)) {
                return true;
            }
        }

        return false;
    }

    public static CommentNode delete_comment(int comment_id, CommentNode comment) {
        if (comment.comment_id == comment_id) {
            return null;
        }

        List<CommentNode> newReplies = new ArrayList<>();

        for (CommentNode reply : comment.replies) {
            CommentNode temp = delete_comment(comment_id, reply);
            if (temp != null) {
                newReplies.add(temp);
            }
        }

        comment.replies = newReplies;

        return comment;
    }
}