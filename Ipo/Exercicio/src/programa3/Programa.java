package programa3;

public class Programa {

	public static void main(String[] args) {
		Casa c1 = new Casa();
		c1.setdados();
		c1.porta1 = true;
		c1.porta2 = true;
		c1.porta3 = true;
		c1.porta1 = false;
		System.out.println("A quantida de portas abertar é de " + c1.portasabertas(0));
	}

}
