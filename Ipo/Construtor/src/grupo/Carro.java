package grupo;

public class Carro {
	private String modelo,cor;
	private int ano;
	private boolean ar;
	
	Carro(String modelo, String cor, int ano, boolean ar) {
		this.modelo = modelo;
		this.cor = cor;
		this.ano = ano;
		this.ar = ar;
	}
	
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public void setAno(int ano) {
		this.ano = ano;
	}

	public void setAr(boolean ar) {
		this.ar = ar;
	}
	
	public void imp() {
		System.out.println(modelo + cor + ano + ar);
	}
	
}
