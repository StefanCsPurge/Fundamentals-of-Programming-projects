package Controller;

import Model.Bike;
import Model.Car;
import Model.Motorbike;
import Model.Vehicle;
import Repository.*;

public class Controller {
    private final Repository repo;

    public Controller(Repository r){
        repo = r;
    }

    public Vehicle[] getAllVehicles(){
        return repo.getAll();
    }

    public void addCar(String model, String color, int year) throws Exception{
        this.repo.addElement(new Car(model, color, year));
    }

    public void addBike(String type, String color, int year) throws Exception{
        this.repo.addElement(new Bike(type, color, year));
    }

    public void addMotorbike(String model, String color, int year) throws Exception{
        this.repo.addElement(new Motorbike(model, color, year));
    }

    public void removeVehicle(int idx) throws Exception{
        this.repo.deleteElement(idx);
    }

    public Vehicle[] filterByColor(String wantedColor){
        Vehicle[] allVehicles = repo.getAll();
        int repoSize = repo.getSize();
        Vehicle[] newVehicles = new Vehicle[repoSize];
        int newLen = 0;
        for(int i=0; i<repoSize; i++)
            if(allVehicles[i].getColor().equals(wantedColor))
                newVehicles[newLen++] = allVehicles[i];
        return newVehicles;
    }
}
