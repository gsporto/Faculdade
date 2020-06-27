package exer;

import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Carro c1 = new Carro();
		int controle = 0;
		System.out.println("Digite 1 para modelo"
				+ "\nDigite 2 para Ano"
				+ "\nDigite 3 para cor");
		controle = sc.nextInt();
		

		switch (controle){
			case 1:
				System.out.println("Modelo: ");
				c1.setModelo(sc.nextLine());
			break;
			case 2:
				System.out.println("Ano: ");
				c1.setAno(sc.nextInt());
			break;
			case 3:
				System.out.println("Cor: ");
				c1.setCor(sc.nextLine());
			break;
			//case default:
				
				
			//	break;
				
		}
		c1.pegaDados();
		
	}

}
