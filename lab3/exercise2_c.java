class FeedProcessor {
    ActivityStack recentActivities;
    NotificationQueue notificationQueue;
    NotificationQueue processedLog;

    public FeedProcessor() {
        this.recentActivities = new ActivityStack();
        this.notificationQueue = new NotificationQueue();
        this.processedLog = new NotificationQueue(); 
    }

    public void processIncoming() {
        if (!this.notificationQueue.isEmpty()) {
            String notif = this.notificationQueue.dequeue();
            this.recentActivities.push(notif);
        }
    }

    public void batchProcess(int k) {
        int count = 0;
        while (count < k && !this.notificationQueue.isEmpty()) {
            processIncoming();
            count++;
        }
    }

    public void clearHistory() {
        while (!this.recentActivities.isEmpty()) {
            String act = this.recentActivities.pop();
            this.processedLog.enqueue(act);
        }
    }

    public String getStats() {
        int actSize = this.recentActivities.size();
        int notifSize = this.notificationQueue.size();
        int logSize = this.processedLog.size();
        
        return "Activities: " + actSize + 
               ", Pending Notifs: " + notifSize + 
               ", Processed Log: " + logSize;
    }
}
class FeedProcessor {
    ActivityStack recentActivities;
    NotificationQueue notificationQueue;
    NotificationQueue processedLog;

    public FeedProcessor() {
        this.recentActivities = new ActivityStack();
        this.notificationQueue = new NotificationQueue();
        this.processedLog = new NotificationQueue(); 
    }

    public void processIncoming() {
        if (!this.notificationQueue.isEmpty()) {
            String notif = this.notificationQueue.dequeue();
            this.recentActivities.push(notif);
        }
    }

    public void batchProcess(int k) {
        int count = 0;
        while (count < k && !this.notificationQueue.isEmpty()) {
            processIncoming();
            count++;
        }
    }

    public void clearHistory() {
        while (!this.recentActivities.isEmpty()) {
            String act = this.recentActivities.pop();
            this.processedLog.enqueue(act);
        }
    }

    public String getStats() {
        int actSize = this.recentActivities.size();
        int notifSize = this.notificationQueue.size();
        int logSize = this.processedLog.size();
        
        return "Activities: " + actSize + 
               ", Pending Notifs: " + notifSize + 
               ", Processed Log: " + logSize;
    }
}
