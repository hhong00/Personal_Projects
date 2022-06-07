import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;
import org.xml.sax.SAXException;

public class financeProject {
    Map<String, Double> financeList;

    public financeProject (String thisName, double finStats)
    {
        financeList = new HashMap<String, Double>();
        financeList.put(thisName.toUpperCase(), finStats);

    }

    public double getFinStats(String name) {
        return financeList.get(name.toUpperCase());
    }

    public void addStock(String name, double finStats)
    {
        financeList.put(name.toUpperCase(), finStats);
    }

    public int numStocks() {
        return financeList.size();
    }

    public static void main(String[] args) {

        try {
            URL wsj = new URL("https://www.wsj.com/watchlist");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }

        financeProject test = new financeProject("Googl", 100);

        System.out.println(test.getFinStats("googl"));
    }

}

