package Repository;

import Model.Vehicle;
import CustomExceptions.RepoException;

import java.util.stream.IntStream;

public class VehicleRepository implements Repository {
    private final Vehicle[] vehicles;
    private int length = 0;
    private final int dimension;

    public VehicleRepository(int dimension) {
        this.dimension = dimension;
        vehicles = new Vehicle[dimension];
    }
    public Vehicle[] getAll() { return vehicles; }

    public int getSize() { return length; }

    public void addElement(Vehicle v) throws RepoException{
            if(length == dimension)
                throw new RepoException("The repository is full!\n");
            vehicles[length++] = v;
    }

    public void deleteElement(int index) throws RepoException{
        if(index < 0 || index >= length)
            throw new RepoException("Index out of bounds!");
        IntStream.range(index, length - 1).forEach(i -> vehicles[i] = vehicles[i + 1]);
        length--;
        vehicles[length] = null;
    }
}
