package View;

import java.util.Scanner;
import Controller.Controller;
import Model.Vehicle;

public class Console {
    private final Controller ctrl;
    private final Scanner reader = new Scanner(System.in);

    public Console(Controller c){
        this.ctrl = c;
    }

    private void displayAllVehicles(){
        Vehicle[] allVehicles = ctrl.getAllVehicles();
        if(allVehicles[0] == null)
        {
            System.out.println("There are no vehicles!");
            return;
        }
        for(int i=0; i < allVehicles.length; i++)
            if(allVehicles[i] != null)
                System.out.println(i + ". " + allVehicles[i].toString());

        pressAnyKeyToContinue();
    }

    private void addVehicle() throws Exception
    {
        System.out.print("\n1 to add a car \n2 to add a bike \n3 to add a motorbike \n>>");
        int option = reader.nextInt();
        switch (option) {
            case 1 -> {
                System.out.print("Model: ");
                String model = reader.next();
                System.out.print("Color: ");
                String color = reader.next().toLowerCase();
                System.out.print("Year: ");
                int year = reader.nextInt();
                ctrl.addCar(model, color, year);
            }
            case 2 -> {
                System.out.print("Type: ");
                String type = reader.next();
                System.out.print("Color: ");
                String bikeColor = reader.next().toLowerCase();
                System.out.print("Year: ");
                int bikeYear = reader.nextInt();
                ctrl.addBike(type, bikeColor, bikeYear);
            }
            case 3 -> {
                System.out.print("model: ");
                String mModel = reader.next();
                System.out.print("Color: ");
                String mColor = reader.next().toLowerCase();
                System.out.print("Year: ");
                int mYear = reader.nextInt();
                ctrl.addMotorbike(mModel, mColor, mYear);
            }
            default -> {
                System.out.println("Non existent option!");
                return;
            }
        }
        pressAnyKeyToContinue();
    }

    private void removeVehicle() throws Exception
    {
        System.out.print("Index of the vehicle to be deleted: ");
        int idx = reader.nextInt();
        ctrl.removeVehicle(idx);
        pressAnyKeyToContinue();
    }

    private void filterByColor()
    {
        System.out.print("Color: ");
        String color = reader.next().toLowerCase();
        Vehicle[] selectedVehicles = ctrl.filterByColor(color);
        if(selectedVehicles[0] == null)
        {
            System.out.println("There are no vehicles with this color!");
            return;
        }
        for(Vehicle v : selectedVehicles)
            if(v != null)
                System.out.println(v.toString());

        pressAnyKeyToContinue();
    }

    private void pressAnyKeyToContinue()
    {
        System.out.print("\nDone. Press Enter key to continue...");
        int xd = 0;
        try
        {
            xd = System.in.read();
        }
        catch(Exception e)
        {
            System.out.println(" You failed ¯\\_(ツ)_/¯ " + xd);
        }
    }

    public void run() {
        boolean done = false, addEntries = true;
        int option;

        while(!done)
        {
            String menuOptions = "\n1. Add vehicle\n" +
                    "2. Remove vehicle\n" +
                    "3. Filter vehicles by color\n" +
                    "4. Show all vehicles\n" +
                    "0. Exit";
            System.out.println(menuOptions);

            try {
                if(addEntries) {
                    // Adding hardcoded entries
                    ctrl.addCar("BMW_M4", "yellow", 2016);
                    ctrl.addCar("BMW_X3", "white", 2019);
                    ctrl.addCar("Lamborghini_URUS", "grey", 2020);
                    ctrl.addBike("MTB", "red", 2018);
                    ctrl.addMotorbike("Dirt_bike", "red", 2015);
                    /// End of the hardcoded entries
                    addEntries = false;
                }

                System.out.print("Input option number: ");
                option = reader.nextInt();

                switch (option) {
                    case 1 -> addVehicle();
                    case 2 -> removeVehicle();
                    case 3 -> filterByColor();
                    case 4 -> displayAllVehicles();
                    case 0 -> {
                        System.out.println("We out...");
                        done = true;
                    }
                    default -> System.out.println("Non existent option!");
                }

            } catch (Exception e){
                System.out.println("Error - " + e.getMessage());
                reader.nextLine();
            }
        }
    }
}
