package grupo;

public class Programa {

	public static void main(String[] args) {
		Carro c1 = new Carro("Fusca", "azul", 1999, true);
		c1.imp();
		Moto m1 = new Moto("Honda", "Cg125", 2005 );
		System.out.println( m1.getMarca()+ m1.getModelo() + m1.getAno());

	}

}
