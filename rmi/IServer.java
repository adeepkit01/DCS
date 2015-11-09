

import java.rmi.Remote;
import java.rmi.RemoteException;


public interface IServer extends Remote{
    public void listClients(IClient client) throws RemoteException;
    public void enter(IClient client) throws RemoteException;
    public void removeClient(IClient client) throws RemoteException;
    public void broadcast(String message) throws RemoteException;
}
