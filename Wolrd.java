import java.util.Scanner;
class Wolrd{
    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);
        System.out.println("Enter name: ");
        String name = ss.nextLine();
        System.out.println("Enter password: ");
        int pass = ss.nextInt();
        if(name.equals("admin") && pass == 12345){
            System.out.println("Welcome admin");
        }
        else{
            System.out.println("Better try next time");
        }
    }
}