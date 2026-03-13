// 处理器实现 (结合了栈和队列，完全正确版)
class FeedProcessor {
    ActivityStack recentActivities;
    NotificationQueue notificationQueue;
    NotificationQueue processedLog;

    public FeedProcessor() {
        this.recentActivities = new ActivityStack();
        this.notificationQueue = new NotificationQueue();
        this.processedLog = new NotificationQueue(); // 采用队列记录历史，保持时间顺序
    }

    public void processIncoming() {
        // 先检查队列是否为空，防止将 null 值推入栈中
        if (!this.notificationQueue.isEmpty()) {
            String notif = this.notificationQueue.dequeue();
            this.recentActivities.push(notif);
        }
    }

    public void batchProcess(int k) {
        int count = 0;
        // 增加双重校验，即使 k 大于队列实际长度，也会在队列为空时安全停止
        while (count < k && !this.notificationQueue.isEmpty()) {
            processIncoming();
            count++;
        }
    }

    public void clearHistory() {
        // 安全地将栈中所有元素转移到处理日志中
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
}// 处理器实现 (结合了栈和队列，完全正确版)
class FeedProcessor {
    ActivityStack recentActivities;
    NotificationQueue notificationQueue;
    NotificationQueue processedLog;

    public FeedProcessor() {
        this.recentActivities = new ActivityStack();
        this.notificationQueue = new NotificationQueue();
        this.processedLog = new NotificationQueue(); // 采用队列记录历史，保持时间顺序
    }

    public void processIncoming() {
        // 先检查队列是否为空，防止将 null 值推入栈中
        if (!this.notificationQueue.isEmpty()) {
            String notif = this.notificationQueue.dequeue();
            this.recentActivities.push(notif);
        }
    }

    public void batchProcess(int k) {
        int count = 0;
        // 增加双重校验，即使 k 大于队列实际长度，也会在队列为空时安全停止
        while (count < k && !this.notificationQueue.isEmpty()) {
            processIncoming();
            count++;
        }
    }

    public void clearHistory() {
        // 安全地将栈中所有元素转移到处理日志中
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
