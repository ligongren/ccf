import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);

		// int n = in.nextInt();
		// int m = in.nextInt();

		int n = 4;
		int m = 5;

		// int[][] data = new int[m][n];
		// int[][] data = { { 2, 2, 3, 1 }, { 2, 3, 4, 5 }, { 1, 4, 2, 3 }, { 2, 1, 3, 2
		// }, { 2, 2, 4, 4 } };
		int[][] data = { { 2, 2, 2, 1 }, { 2, 3, 4, 5 }, { 2, 4, 2, 3 }, { 2, 1, 3, 2 }, { 2, 2, 4, 4 } };
		int[][] empty = new int[m][n];

		for (int i = 0; i < m * n; i++) {
			// data[i / m][i % n] = in.nextInt();
			empty[i / m][i % n] = 0;
		}

		for (int i = 0; i < m; i++) {
			int lastTime = 1;// 持续次数
			int preColor = 0;// 上一个的颜色
			for (int j = 0; j < n; j++) {
				if (data[i][j] == preColor) {
					lastTime++;
				} else {
					preColor = data[i][j];
					lastTime = 1;
				}
				if (lastTime == 3) {
					empty[i][j] = 1;
					empty[i][j - 1] = 1;
					empty[i][j - 2] = 1;
				}
				if (lastTime >= 3) {
					empty[i][j] = 1;
				}
			}
		}

		for (int i = 0; i < n; i++) {
			int lastTime = 1;// 持续次数
			int preColor = 0;// 上一个的颜色
			for (int j = 0; j < m; j++) {
				if (data[j][i] == preColor) {
					lastTime++;
				} else {
					preColor = data[j][i];
					lastTime = 1;
				}
				if (lastTime == 3) {
					empty[j][i] = 1;
					empty[j - 1][i] = 1;
					empty[j - 2][i] = 1;
				}
				if (lastTime >= 3) {
					empty[j][i] = 1;
				}
			}
		}

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (empty[i][j] == 1) {
					System.out.print("0 ");
				} else {
					System.out.print(data[i][j] + " ");
				}
			}
			System.out.println();
		}

		in.close();
	}

}