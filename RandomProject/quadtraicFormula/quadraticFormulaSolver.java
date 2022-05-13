import java.util.*;
public class quadraticFormulaSolver {
    Scanner scan = new Scanner(System.in);

    public int getConstant(String s) {
        String ret = "";
        for (char c : s.toCharArray()) {
            if (c == 'x') {
                break;
            }
            ret += c;
        }
        return Integer.parseInt(ret);
    }
    //x = (-b ± sqrt(b^2 - 4ac)) / 2a
    public void solver(int a, int b, int c, int fx) {
        
        double x1 = (-b + Math.sqrt(Math.pow(b, 2) - 4*a*(c-fx))) / 2*a;
        double x2 = (-b - Math.sqrt(Math.pow(b, 2) - 4*a*(c-fx))) / 2*a;

        System.out.println(x1);
        System.out.println(x2);

    }
    public void run() {
        // format "ax^2 + bx + c"


        System.out.println("a: ");
        int a = scan.nextInt();
        System.out.println("b: ");
        int b = scan.nextInt();
        System.out.println("c: ");
        int c = scan.nextInt();
        System.out.println("f(x): ");
        int fx = scan.nextInt();
        System.out.printf("%d %d %d\n", a, b, c);
        solver(a, b, c, fx);
    }

    public static void main(String[] args) {
        new quadraticFormulaSolver().run();
    }
}
