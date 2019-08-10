package prova8;

public class Horario {
	private String dia, mes, ano, hora, minuto;
	private Paciente paciente;

	public void setDia(String dia,String mes,String ano) {
		this.dia = dia;
		this.mes = mes;
		this.ano = ano;
	}
	public void setHorario(String hora, String minuto) {
		this.hora = hora;
		this.minuto = minuto;
	}

	public Paciente getPaciente() {
		return paciente;
	}

	public void setPaciente(Paciente paciente) {
		this.paciente = paciente;
	}
	
	public void imp() {
		System.out.println("Nome: " +paciente.getNome());
		System.out.println("Dia: " +paciente.getIdade());
		System.out.println("Dia: " +dia +"/" +mes +"/" +ano );
		System.out.println("Hora: " +hora +":" +minuto);
	}
}
