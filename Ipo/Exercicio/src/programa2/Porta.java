package programa2;
import java.util.Scanner;

public class Porta {
	Scanner sc = new Scanner (System.in);
	boolean aberta;
	String s,cor,dimensaoX,dimensaoY,dimensaoZ;
	
	public void abre() {
		aberta = true;
	}
	public void fecha() {
		aberta = false;
	}
	public void pinta(String s ) {
		cor = s;
	}
	public void setDados() {
		System.out.println("Digite a Cor: ");
		pinta(sc.nextLine());
		System.out.println("Digite a dimensão X: ");
		dimensaoX = sc.nextLine();
		System.out.println("Digite a dimensão Y: ");
		dimensaoY = sc.nextLine();
		System.out.println("Digite a dimensão Z: ");
		dimensaoZ = sc.nextLine();
		
	}

	public boolean estaAberta() {
		if (aberta == true) {
			System.out.println("Está aberta");
		}
		else {
			System.out.println("Está Fechada");
		}
		return aberta;
		
	}
}
