package Repository;

import Model.Vehicle;
import CustomExceptions.RepoException;

public interface Repository {
    void addElement(Vehicle v) throws RepoException;
    void deleteElement(int index) throws RepoException;
    Vehicle[] getAll();
    int getSize();
    //void removeElement(int index) throws Exception;
}
