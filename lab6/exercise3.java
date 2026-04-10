import java.util.*;
public class Exercise3 {

    private Map<String, List<String>> network;

    public Exercise3() {
        this.network = new HashMap<>();
    }

    public void addUser(String user) {
        network.putIfAbsent(user, new ArrayList<>());
    }

    public void addFriendship(String user1, String user2) {
        addUser(user1);
        addUser(user2);
        network.get(user1).add(user2);
        network.get(user2).add(user1);
    }


    public List<String> bfs(String startUser) {
        List<String> result = new ArrayList<>();
        if (!network.containsKey(startUser)) return result;

        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(startUser);
        visited.add(startUser);

        while (!queue.isEmpty()) {
            String current = queue.poll();
            result.add(current);

            for (String neighbor : network.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        return result;
    }

    public Map<String, Integer> bfsWithDistances(String startUser) {
        Map<String, Integer> distances = new HashMap<>();
        if (!network.containsKey(startUser)) return distances;

        Queue<String> queue = new LinkedList<>();
        queue.offer(startUser);
        distances.put(startUser, 0);

        while (!queue.isEmpty()) {
            String current = queue.poll();
            int currentDist = distances.get(current);

            for (String neighbor : network.get(current)) {
                if (!distances.containsKey(neighbor)) {
                    distances.put(neighbor, currentDist + 1);
                    queue.offer(neighbor);
                }
            }
        }
        return distances;
    }

    public List<String> shortestPath(String startUser, String targetUser) {
        if (!network.containsKey(startUser) || !network.containsKey(targetUser)) {
            return new ArrayList<>();
        }
        if (startUser.equals(targetUser)) {
            return Collections.singletonList(startUser);
        }

        Queue<String> queue = new LinkedList<>();
        Map<String, String> parentMap = new HashMap<>();
        Set<String> visited = new HashSet<>();

        queue.offer(startUser);
        visited.add(startUser);
        boolean found = false;

        while (!queue.isEmpty() && !found) {
            String current = queue.poll();

            for (String neighbor : network.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    parentMap.put(neighbor, current);
                    queue.offer(neighbor);

                    if (neighbor.equals(targetUser)) {
                        found = true;
                        break;
                    }
                }
            }
        }

        if (!found) return new ArrayList<>();

        List<String> path = new ArrayList<>();
        String curr = targetUser;
        while (curr != null) {
            path.add(curr);
            curr = parentMap.get(curr);
        }

        Collections.reverse(path); 
        return path;
    }


    public int degreesOfSeparation(String startUser, String targetUser) {
        Map<String, Integer> distances = bfsWithDistances(startUser);
        return distances.getOrDefault(targetUser, -1);
    }

    public Set<String> friendsWithinKHops(String startUser, int k) {
        Map<String, Integer> distances = bfsWithDistances(startUser);
        Set<String> result = new HashSet<>();

        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            int dist = entry.getValue();
            if (dist > 0 && dist <= k) {
                result.add(entry.getKey());
            }
        }
        return result;
    }

    public double computeAverageDegreesOfSeparation() {
        int totalDistance = 0;
        int connectedPairs = 0;

        for (String user : network.keySet()) {
            Map<String, Integer> distances = bfsWithDistances(user);
            for (int dist : distances.values()) {
                if (dist > 0) {
                    totalDistance += dist;
                    connectedPairs++;
                }
            }
        }

        if (connectedPairs == 0) return 0.0;
        return (double) totalDistance / connectedPairs;
    }


    public Map<Integer, Integer> getDistanceDistribution(String startUser) {
        Map<String, Integer> distances = bfsWithDistances(startUser);
        Map<Integer, Integer> distribution = new HashMap<>();

        for (int dist : distances.values()) {
            distribution.put(dist, distribution.getOrDefault(dist, 0) + 1);
        }
        return distribution;
    }

    public List<String> recommendFriends(String startUser, int maxRecommendations) {
        Map<String, Integer> distances = bfsWithDistances(startUser);
        List<String> recommendations = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            if (entry.getValue() == 2) {
                recommendations.add(entry.getKey());
                if (recommendations.size() >= maxRecommendations) {
                    break;
                }
            }
        }
        return recommendations;
    }

    public static void main(String[] args) {
        Exercise3 graph = new Exercise3();

        graph.addFriendship("Alice", "Bob");
        graph.addFriendship("Bob", "Charlie");
        graph.addFriendship("Charlie", "David");
        graph.addFriendship("Alice", "Eve");
        graph.addFriendship("Eve", "Charlie");
        graph.addFriendship("Eve", "Frank");
        graph.addUser("George"); 

        System.out.println("BFS from Alice: " + graph.bfs("Alice"));
        System.out.println("Distances from Alice: " + graph.bfsWithDistances("Alice"));
  
        System.out.println("Shortest path Alice -> David: " + graph.shortestPath("Alice", "David"));
        System.out.println("Degrees of separation Alice -> David: " + graph.degreesOfSeparation("Alice", "David"));
        System.out.println("Degrees of separation Alice -> George: " + graph.degreesOfSeparation("Alice", "George"));
        
        System.out.println("\nFriends within 2 hops of Alice: " + graph.friendsWithinKHops("Alice", 2));
        
        System.out.printf("Average degrees of separation (entire network): %.2f\n", graph.computeAverageDegreesOfSeparation());
        System.out.println("Distance distribution from Alice: " + graph.getDistanceDistribution("Alice"));
        
        System.out.println("Recommend 5 friends for Alice: " + graph.recommendFriends("Alice", 5));
        System.out.println("Recommend 1 friend for Alice: " + graph.recommendFriends("Alice", 1));
    }
}