package exer;

public class Carro {
	String modelo,cor;
	int ano;
	boolean ar;
	
	public void setModelo(String a) {
		modelo = a;
		
	}
	
	public int setAno (int ano) {
		return ano;
		
	}
	
	public void setCor (String cor) {
		cor = cor;
	}
	
	public boolean setAr() {
		
		return ar;
	}
	
	public void pegaDados() {
		System.out.println(modelo);
		System.out.println(cor);
		System.out.println(modelo);
		System.out.println(ano);
		if (setAr() == true) {
			System.out.println("Tem Ar");
		}
		else {
			System.out.println("Não Tem Ar");
		}
	
		
	}
	

}
