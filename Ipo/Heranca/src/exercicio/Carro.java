package exercicio;

public class Carro extends Veiculos {
	private boolean ar,airbag;
	
	Carro(){
		this.ar = false;
		this.airbag = false;
	}

	public boolean getAirbag() {
		return airbag;
	}

	public void setAirbag(boolean airbag) {
		this.airbag = airbag;
	}

	public boolean getAr() {
		return ar;
	}

	public void setAr(boolean ar) {
		this.ar = ar;
	}
}
