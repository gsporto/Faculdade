package exercicio;

public class Veiculos {
	private String marca,modelo,cor;
	
	Veiculos(){
		this.marca = "S/marca";
		this.modelo = "S/modelo";
		this.cor = "S/cor";
	}

	public String getCor() {
		return cor;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
}
