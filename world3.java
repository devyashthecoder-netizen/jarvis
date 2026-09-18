import java.util.*;
class world3{
     public static void main(String[] args){
        Scanner ss = new Scanner(System.in);
        System.out.println("Enter name ");
        String name = ss.nextLine();
        switch (name) {
            case "amit":
                System.out.println("hello " + name);
                break;
            case "ajay":
                System.out.println("hello " + name);
                break;
            default:
                System.out.println("Guest = "+ name);
        }
     }
}