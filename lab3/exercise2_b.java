class NotifNode {
    String notification;
    NotifNode next;

    public NotifNode(String notification) {
        this.notification = notification;
        this.next = null;
    }
}
class NotificationQueue {
    private NotifNode front;
    private NotifNode rear;
    private int sizeCount;

    public NotificationQueue() {
        this.front = null;
        this.rear = null;
        this.sizeCount = 0;
    }

    public void enqueue(String notif) {
        NotifNode newNode = new NotifNode(notif);
        if (isEmpty()) {
            this.front = newNode;
            this.rear = newNode;
        } else {
            this.rear.next = newNode;
            this.rear = newNode;
        }
        this.sizeCount++;
    }

    public String dequeue() {
        if (isEmpty()) {
            return null; 
        }
        String removedData = this.front.notification;
        this.front = this.front.next;
        if (this.front == null) {
            this.rear = null;
        }
        
        this.sizeCount--;
        return removedData;
    }

    public String front() {
        if (isEmpty()) return null;
        return this.front.notification;
    }

    public boolean isEmpty() {
        return this.front == null;
    }

    public int size() {
        return this.sizeCount;
    }

    public void displayPending() {
        NotifNode current = this.front;
        while (current != null) {
            System.out.println(current.notification);
            current = current.next;
        }
    }

    public void priorityEnqueue(String urgentNotif) {
        NotifNode newNode = new NotifNode(urgentNotif);
        if (isEmpty()) {
            this.front = newNode;
            this.rear = newNode;
        } else {
            newNode.next = this.front;
            this.front = newNode;
        }
        this.sizeCount++;
    }
}
public class Exercise2_b {
    public static void main(String[] args) {

        NotificationQueue queue = new NotificationQueue();
        
        queue.enqueue("New Follower: Alice");
        System.out.println("Enqueued 1 item. Is queue empty? " + queue.isEmpty());
        System.out.println("Is rear pointer null? " + queue.isRearNull());
        
        System.out.println("\nDequeuing the only item: " + queue.dequeue());
        
        System.out.println("Is queue empty now? " + queue.isEmpty());
        System.out.println("Is rear pointer securely set to null? " + queue.isRearNull());

    }
}
