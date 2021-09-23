import java.util.*;
import java.io.*;
import java.text.DecimalFormat;
public class Java {

	public static void main(String[] args) {
		int range = Integer.parseInt(args[0]);
		int trails = Integer.parseInt(args[1]);		
		prng(range, trails);
	}
	static void prng(int numbers, int trails) {
		int frequency[] = new int[numbers];
		double probability[] = new double[numbers];
		int start_time = (int) System.currentTimeMillis();
		Random random = new Random();
		for(int i=0;i<trails;i++) {
			int r_number = random.nextInt(numbers);
			frequency[r_number] +=1;
		}		
		String output = "";
		for(int i=0;i<numbers;i++) {
			if(frequency[i] == 0) {
				output += i+" : 0\n";
			}else {
				probability[i] = frequency[i]/(double)trails;
				DecimalFormat df = new DecimalFormat("#.######");				
				output += i+" : "+df.format(probability[i])+"\n";
			}
		}
		int duration = (int)System.currentTimeMillis() - start_time;
		String filename = System.getProperty("user.dir")+"\\outputs\\"+"java_"+numbers+"_"+trails+".txt";
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
		    writer.write(output);
			writer.close();
		}catch(Exception e) {
			System.out.println(e);
		}
		System.out.println("--- "+(duration*0.001)+" seconds ---");
	}
}
