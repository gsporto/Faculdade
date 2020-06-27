package prova8;

import javax.swing.JOptionPane;

public class Programa {

	public static void main(String[] args) {
		int idade;
		Paciente p1 = new Paciente();
		p1.setNomePaciente(JOptionPane.showInputDialog("Seu nome é"));
		idade = Integer.parseInt(JOptionPane.showInputDialog("Sua Idade é"));
		p1.setIdadePaciente(idade);
		Horario h1 = new Horario();
		h1.setDia(JOptionPane.showInputDialog("Dia é"),JOptionPane.showInputDialog("Mes é: ") ,JOptionPane.showInputDialog("Ano é : "));
		h1.setHorario(JOptionPane.showInputDialog("Hora: "), JOptionPane.showInputDialog("Minuto: "));
		h1.setPaciente(p1);
		h1.imp();
		
		Paciente p2 = new Paciente();
		p2.setNomePaciente(JOptionPane.showInputDialog("Seu nome é"));
		idade = Integer.parseInt(JOptionPane.showInputDialog("Sua Idade é"));
		p2.setIdadePaciente(idade);
		Horario h2 = new Horario();
		h2.setDia(JOptionPane.showInputDialog("Dia é"),JOptionPane.showInputDialog("Mes é: ") ,JOptionPane.showInputDialog("Ano é : "));
		h2.setHorario(JOptionPane.showInputDialog("Hora: "), JOptionPane.showInputDialog("Minuto: "));
		h2.setPaciente(p2);
		h2.imp();
		h1.imp();
		
	}

}
