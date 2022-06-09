package Model;

public class Motorbike implements Vehicle{
    String color, model;
    int year;
    public Motorbike(String m, String c, int y){
        this.color = c;
        this.model = m;
        this.year = y;
    }

    public String getColor(){
        return color;
    }

    public String toString(){
        return "Motorbike ->  model: " + model + "  -  " + "color: " + color + "  -  " + "year: " + year;
    }
}
