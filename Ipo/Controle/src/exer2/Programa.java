package exer2;

public class Programa {

	public static void main(String[] args) {
		Conta c1 = new Conta();
		c1.setSaldo(200.0);
		c1.setTitular("Gabriel");
		System.out.println(c1.getTitular());
		System.out.println(c1.getSaldo());
		System.out.println(c1);

	}

}
