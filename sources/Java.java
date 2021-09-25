import java.util.*;
import java.io.*;
import java.text.DecimalFormat;

public class Java {

	public static void main(String[] args) {
		int range = 0;
		int trials = 0;
		
		try {
			range = Integer.parseInt(args[0]);
			trials = Integer.parseInt(args[1]);
		} catch (Exception e) {
			System.out.println("Invalid Arguments");
			System.out.println("java Java <longegerValue> <longegerValue>");
		}
		
		prng(range, trials);
	}

	static void prng(int numbers, int trials) {
		
		double frequency[] = new double[numbers];
		double probability[] = new double[numbers];
		long start_time = System.currentTimeMillis();
		Random random = new Random();
		String output = "";
		
		for (int i = 0; i < trials; i++) {
			int r_number = random.nextInt(numbers);
			frequency[r_number] += 1;
		}
		
		for (int i = 0; i < numbers; i++) {
			if (frequency[i] == 0) {
				output += String.format("%d 0\n", i);
			} else {
				probability[i] = frequency[i] / trials;
				DecimalFormat df = new DecimalFormat("#.######");
				output += String.format("%d : %s\n", i, df.format(probability[i]));
			}
		}
		
		long duration = System.currentTimeMillis() - start_time;	
		String filename = String.format("%s\\outputs\\java_%s_%s.txt", System.getProperty("user.dir"), numbers, trials);
		
		try {
			FileWriter fw = new FileWriter(filename);
			fw.write(output);
			fw.close();
		} catch (Exception e) {
			System.out.println(e);
		}
		
		System.out.println(String.format("--- %f seconds ---", (duration * 0.001)));
	}
}
