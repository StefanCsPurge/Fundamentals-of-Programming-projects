import Controller.Controller;
import Repository.*;
import View.Console;

/**
 * In a parking lot, there are cars of different colors.
 * Add, remove, or filter the cars based on their color.
 * They are stored in the Repository.
 */


public class Main {

    public static void main(String[] args) {

        Repository repo = new VehicleRepository(99);
        Controller ctrl = new Controller(repo);
        Console console = new Console(ctrl);

        console.run();
    }
}
