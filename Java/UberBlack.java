import java.util.ArrayList;
import java.util.Map;

class UberBlack extends Car {
    Map<String, ArrayList<String,Integer >> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    
    public UberBlack(String licence, Account driver, Map<String, ArrayList<String,Integer >> typeCarAccepted){
        super(licence, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial;
    }
}