package exemplo;

public class Pessoa {
	private String nome,cpf;
	
	Pessoa(){
		this.nome = "S/Nome";
		this.cpf = "S/Cpf";
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	

}
