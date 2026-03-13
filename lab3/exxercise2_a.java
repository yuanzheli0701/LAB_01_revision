
class ActivityNode {
    String activity;
    ActivityNode next;

    public ActivityNode(String activity) {
        this.activity = activity;
        this.next = null;
    }
}

class ActivityStack {
    private ActivityNode top;
    private int sizeCount;

    public ActivityStack() {
        this.top = null;
        this.sizeCount = 0;
    }

    public void push(String activity) {
        ActivityNode newNode = new ActivityNode(activity);
        newNode.next = this.top;
        this.top = newNode;
        this.sizeCount++;
    }

    public String pop() {
        if (isEmpty()) {
            return null; 
        }
        String removedData = this.top.activity;
        this.top = this.top.next;
        this.sizeCount--;
        return removedData;
    }

    public String peek() {
        if (isEmpty()) return null;
        return this.top.activity;
    }

    public boolean isEmpty() {
        return this.top == null;
    }

    public int size() {
        return this.sizeCount;
    }

    public void displayRecent(int n) {
        ActivityNode current = this.top;
        int count = 0;
        while (current != null && count < n) {
            System.out.println(current.activity);
            current = current.next;
            count++;
        }
    }
}
class ActivityManager {
    ActivityStack mainStack = new ActivityStack();
    ActivityStack undoStack = new ActivityStack();

    public void performAction(String action) {
        mainStack.push(action);
    }

    public void undoLast() {
        if (!mainStack.isEmpty()) {
            String lastAction = mainStack.pop();
            undoStack.push(lastAction);
            System.out.println("Action reverted: " + lastAction);
        }
    }
}
public class exercise2_a {
    public static void main(String[] args) {

        ActivityStack stack = new ActivityStack();
        stack.push("Logged in");
        stack.push("Liked a photo");

        System.out.println("Current stack size: " + stack.size());
        System.out.println("Attempting to display 5 recent activities:");

        stack.displayRecent(5);

    }
}