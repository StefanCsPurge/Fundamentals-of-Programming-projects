package Model;

public class Bike implements Vehicle{
    String color, type;
    int year;
    public Bike(String t, String c, int y){
        this.color = c;
        this.type = t;
        this.year = y;
    }

    public String getColor(){
        return color;
    }

    public String toString(){
        return "Bike ->  type: " + type + "  -  " + "color: " + color + "  -  " + "year: " + year;
    }
}
