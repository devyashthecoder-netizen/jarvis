import java.util.*;

class world2 {
    public static void main(String[] args) {

        Scanner ss = new Scanner(System.in);
        char choice;

        do {
            System.out.println("Enter 1st number = ");
            int num = ss.nextInt();

            System.out.println("Enter 2nd number = ");
            int num2 = ss.nextInt();

            int sum = num + num2;

            System.out.println("Sum = " + sum);

            System.out.println("Do you want to add again? (y/n)");
            choice = ss.next().charAt(0);

        } while (choice == 'y' || choice == 'Y');
    }
}