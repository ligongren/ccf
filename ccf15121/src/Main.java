import java.util.*;

public class Main {
	static Scanner in = new Scanner(System.in);
	static int answer = 0;

	public static void main(String[] args) {
		String n = in.next();
		for (int i = 0; i < n.length(); i++) {
			answer += n.charAt(i) - '0';
		}
		System.out.println(answer);
	}

}
