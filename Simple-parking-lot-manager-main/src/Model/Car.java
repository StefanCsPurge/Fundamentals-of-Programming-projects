package Model;

public class Car implements Vehicle{
    String color, model;
    int year;
    public Car(String m, String c, int y){
        this.color = c;
        this.model = m;
        this.year = y;
    }

    public String getColor(){
        return color;
    }

    public String toString(){
        return "Car ->  model: " + model + "  -  " + "color: " + color + "  -  " + "year: " + year;
    }

}
