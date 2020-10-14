import java.util.Scanner;
import java.util.Stack;
import java.util.HashSet;

class Calculator {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;
		while (true) {
			input = scanner.nextLine();
			if (input.length() < 1) break;
			System.out.print(calculate(input) + " ");
		}
	}

	public static long calculate(String input) {
		HashSet<String> operands = createOperands();
		String[] values = input.split(" ");
		Stack<Long> stack = new Stack<Long>();
		for (int i = values.length - 1; i >= 0; i--) {
			if (operands.contains(values[i])) {
				Long l1 = stack.pop();
				Long l2 = stack.pop();

				switch (values[i]) {
					case "+":
						stack.push(l1 + l2);
						break;
					case "-":
						stack.push(l1 - l2);
						break;
					case "*":
						stack.push(l1 * l2);
						break;
				}
			} else {
				stack.push(Long.parseLong(values[i]));
			}
		}
		return stack.peek();
	}

	public static HashSet<String> createOperands() {
		HashSet<String> operands = new HashSet<String>();
		operands.add("+");
		operands.add("-");
		operands.add("*");
		return operands;
	}
}