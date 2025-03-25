import java.util.ArrayList;
import java.util.List;

public class ProcessoSeletivo {
    private double salarioBase = 2000.00;
    private List<Candidato> candidatos;

    public ProcessoSeletivo() {
        this.candidatos = new ArrayList<>();
    }

    // Método para adicionar candidatos à lista
    public void adicionarCandidato(Candidato candidato) {
        candidatos.add(candidato);
    }

    // Método para selecionar candidatos com base em algum critério
    public List<Candidato> selecionarCandidatos(double experienciaMinima) {
        List<Candidato> candidatosSelecionados = new ArrayList<>();
        for (Candidato candidato : candidatos) {
            if (candidato.getExperiencia() >= experienciaMinima) {
                candidatosSelecionados.add(candidato);
            }
        }
        return candidatosSelecionados;
    }

    // Método para ligar para candidatos selecionados
    public void ligarParaCandidato(Candidato candidato) {
        System.out.println("Ligando para " + candidato.getNome() + " no telefone " + candidato.getTelefone());
    }

    // Método para importar lista de candidatos selecionados
    public void importarListaCandidatos(List<Candidato> lista) {
        candidatos.addAll(lista);
    }

    // Método para calcular salário final baseado na experiência do candidato
    public double calcularSalarioFinal(Candidato candidato) {
        return salarioBase + (candidato.getExperiencia() * 100); // Exemplo simples de cálculo
    }
}
