import java.util.LinkedList;
import java.util.Queue;

class Query {
    String name;
    int time;

    public Query(String name, int time) {
        this.name = name;
        this.time = time;
    }
}

class QueryHandler {
    Queue<Query> studentQueue = new LinkedList<>();
    Queue<Query> facultyQueue = new LinkedList<>();
    int totalQueryTime = 0;
    int numQueries = 0;

    public void addQuery(Query query, boolean isStudent) {
        if (isStudent) {
            studentQueue.add(query);
        } else {
            facultyQueue.add(query);
        }
    }
