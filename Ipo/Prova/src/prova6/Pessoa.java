package prova6;

import javax.swing.JOptionPane;

public class Pessoa {
	String nome;
	int idade;
	
	public void setDados() {
		nome = JOptionPane.showInputDialog ("Nome: ");
		idade = Integer.parseInt(JOptionPane.showInputDialog("Idade: "));
	}
	
	public void fazAniversario() {
		idade++;
		System.out.println(nome + idade);
	}

}
