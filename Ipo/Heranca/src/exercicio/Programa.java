package exercicio;

public class Programa {
	public static void main (String args [] ) {
		Carro c1 = new Carro();
		c1.setMarca("volkswagen");
		c1.setModelo("Gol");
		c1.setCor("vermelho");
		c1.setAr(true);
		c1.setAirbag(true);
		Moto m1 = new Moto();
		m1.setMarca("Honda");
		m1.setModelo("Cg150");
		m1.setCor("azul");
		m1.setCapacete(true);
		System.out.println(" Marca: " +c1.getMarca() + " Modelo: "+ c1.getModelo()
		+ " Cor: "+ c1.getCor() + " Airbag: " + c1.getAirbag() + " Ar: " + c1.getAr());
		System.out.println(" Marca: " +m1.getMarca() + " Modelo: "+ m1.getModelo()
		+ " Cor: "+ m1.getCor() + " Capacete: " + m1.getCapacete());
	}
}