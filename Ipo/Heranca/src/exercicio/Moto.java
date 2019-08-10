package exercicio;

public class Moto extends Veiculos {
	private boolean capacete;
	
	Moto(){
		this.capacete = false;
	}
	
	public boolean getCapacete() {
		return capacete;
	}

	public void setCapacete(boolean capacete) {
		this.capacete = capacete;
	}
	
}
