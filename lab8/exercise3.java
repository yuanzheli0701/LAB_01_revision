import java.util.*;

public class Exercise3 {

    static class AutocompleteTrieNode {
        Map<Character, AutocompleteTrieNode> children = new HashMap<>();
        boolean isEndOfUsername = false;
        String userId = null;
    }
    public static class AutoCompleteResult {
        public String username;
        public String userId;

        public AutoCompleteResult(String username, String userId) {
            this.username = username;
            this.userId = userId;
        }

        @Override
        public String toString() {
            return username + " (ID: " + userId + ")";
        }
    }

    private AutocompleteTrieNode root;

    public Exercise3() {
        this.root = new AutocompleteTrieNode();
    }


    public void insert(String username, String userId) {
        if (username == null || username.isEmpty()) return;

        AutocompleteTrieNode current = root;
        for (char ch : username.toCharArray()) {
            current.children.putIfAbsent(ch, new AutocompleteTrieNode());
            current = current.children.get(ch);
        }
        current.isEndOfUsername = true;
        current.userId = userId;
    }

    public String search(String username) {
        if (username == null || username.isEmpty()) return null;

        AutocompleteTrieNode current = root;
        for (char ch : username.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return null;
            }
            current = current.children.get(ch);
        }

        return current.isEndOfUsername ? current.userId : null;
    }

    public boolean startsWith(String prefix) {
        if (prefix == null || prefix.isEmpty()) return true;

        AutocompleteTrieNode current = root;
        for (char ch : prefix.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return false;
            }
            current = current.children.get(ch);
        }
        return true;
    }

    public List<AutoCompleteResult> autocomplete(String prefix, int maxResults) {
        List<AutoCompleteResult> results = new ArrayList<>();
        if (prefix == null) return results;

        AutocompleteTrieNode current = root;
        for (char ch : prefix.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return results; // Prefix does not exist
            }
            current = current.children.get(ch);
        }

        dfsFindWords(current, prefix, results, maxResults);
        return results;
    }

    private void dfsFindWords(AutocompleteTrieNode node, String currentWord, List<AutoCompleteResult> results, int maxResults) {
        if (results.size() >= maxResults) {
            return;
        }

        if (node.isEndOfUsername) {
            results.add(new AutoCompleteResult(currentWord, node.userId));
        }

        for (Map.Entry<Character, AutocompleteTrieNode> entry : node.children.entrySet()) {
            if (results.size() >= maxResults) {
                break;
            }
            dfsFindWords(entry.getValue(), currentWord + entry.getKey(), results, maxResults);
        }
    }


    public int countWords() {
        return countWordsHelper(root);
    }

    private int countWordsHelper(AutocompleteTrieNode node) {
        int count = node.isEndOfUsername ? 1 : 0;
        for (AutocompleteTrieNode child : node.children.values()) {
            count += countWordsHelper(child);
        }
        return count;
    }

    public int getHeight() {
        return getHeightHelper(root);
    }

    private int getHeightHelper(AutocompleteTrieNode node) {
        if (node.children.isEmpty()) {
            return 0;
        }
        int maxChildHeight = 0;
        for (AutocompleteTrieNode child : node.children.values()) {
            maxChildHeight = Math.max(maxChildHeight, getHeightHelper(child));
        }
        return 1 + maxChildHeight;
    }

    public int getTotalNodes() {
        return getTotalNodesHelper(root);
    }

    private int getTotalNodesHelper(AutocompleteTrieNode node) {
        int total = 1; 
        for (AutocompleteTrieNode child : node.children.values()) {
            total += getTotalNodesHelper(child);
        }
        return total;
    }

    public void delete(String username) {
        if (username == null || username.isEmpty()) return;

        AutocompleteTrieNode current = root;
        for (char ch : username.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return; 
            }
            current = current.children.get(ch);
        }

        if (current.isEndOfUsername) {
            current.isEndOfUsername = false;
            current.userId = null;
        }
    }

    public static void main(String[] args) {
        Exercise3 trie = new Exercise3();

        trie.insert("alice", "U001");
        trie.insert("alice123", "U002");
        trie.insert("alice_smith", "U003");
        trie.insert("alicia", "U004");
        trie.insert("bob", "U005");
        trie.insert("bobby", "U006");

        System.out.println("Search 'alice': " + trie.search("alice")); // Expected: U001
        System.out.println("Search 'ali': " + trie.search("ali"));     // Expected: null (not a full word)
        System.out.println("Starts with 'ali': " + trie.startsWith("ali")); // Expected: true
        System.out.println("Starts with 'cat': " + trie.startsWith("cat")); // Expected: false

        System.out.println("Autocomplete 'ali' (max 10):");
        List<AutoCompleteResult> aliResults = trie.autocomplete("ali", 10);
        for (AutoCompleteResult res : aliResults) {
            System.out.println("  - " + res);
        }

        System.out.println("Autocomplete 'ali' (max 2):");
        List<AutoCompleteResult> aliResultsLimited = trie.autocomplete("ali", 2);
        for (AutoCompleteResult res : aliResultsLimited) {
            System.out.println("  - " + res);
        }

        System.out.println("Total words: " + trie.countWords()); // Expected: 6
        System.out.println("Total nodes: " + trie.getTotalNodes()); 
        System.out.println("Tree height: " + trie.getHeight()); // Expected: 11 (length of "alice_smith")

        trie.delete("alice");
        System.out.println("Search 'alice' after deletion: " + trie.search("alice")); // Expected: null
        System.out.println("Total words after deletion: " + trie.countWords()); // Expected: 5
    }
}