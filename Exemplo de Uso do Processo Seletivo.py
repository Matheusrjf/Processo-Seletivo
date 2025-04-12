public class Main {
    public static void main(String[] args) {
        // Criando o processo seletivo
        ProcessoSeletivo processo = new ProcessoSeletivo();

        // Adicionando alguns candidatos
        Candidato candidato1 = new Candidato("João", "123456789", 2.5);
        Candidato candidato2 = new Candidato("Maria", "987654321", 3.0);
        processo.adicionarCandidato(candidato1);
        processo.adicionarCandidato(candidato2);

        // Selecionando candidatos com base na experiência mínima
        List<Candidato> selecionados = processo.selecionarCandidatos(2.0);

        // Ligando para os candidatos selecionados
        for (Candidato candidato : selecionados) {
            processo.ligarParaCandidato(candidato);
        }

        // Exemplo de importação de lista de candidatos
        List<Candidato> novaLista = new ArrayList<>();
        novaLista.add(new Candidato("Pedro", "555555555", 1.5));
        novaLista.add(new Candidato("Ana", "999999999", 2.8));
        processo.importarListaCandidatos(novaLista);

        // Exemplo de cálculo de salário final para um candidato
        Candidato candidatoParaCalculo = processo.selecionarCandidatos(2.5).get(0);
        double salarioFinal = processo.calcularSalarioFinal(candidatoParaCalculo);
        System.out.println("Salário final de " + candidatoParaCalculo.getNome() + ": R$" + salarioFinal);
    }
}
