package programa3;

import java.util.Scanner;

public class Casa {
	boolean porta1,porta2,porta3;
	String cor;
	
	Scanner sc = new Scanner(System.in);
	
	public void setdados() {
		System.out.println("Digite a cor da sua casa: ");
		pinta (sc.nextLine());

	}
	public void pinta(String s) {
		cor = s;
	}
	public int portasabertas(int i){
		if (porta1 == true) {
			i++;
		}
		if (porta2 == true) {
			i++;
		}
		if (porta3 == true) {
			i++;
		}
		return i;
	}
	
	
}
