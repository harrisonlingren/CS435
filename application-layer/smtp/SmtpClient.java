import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;


public class SmtpClient {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String serverAddress = null;

        System.out.println("enter the IP address of the server: ");

        try {
           serverAddress = in.readLine();
        } catch (IOException ioe) {
           System.out.println("IO error trying to read server IP address!");
           System.exit(1);
        }

        Socket s = new Socket(serverAddress, 25);
        BufferedReader input =
            new BufferedReader(new InputStreamReader(s.getInputStream()));
        String answer = input.readLine();
        s.close();
        System.out.println(answer);
        System.exit(0);
    }
}
