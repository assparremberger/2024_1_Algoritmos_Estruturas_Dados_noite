public class Notebook extends Computador {
    
    private int tempoDeBateria;

    public Notebook(){
        super();
    }

    public Notebook(String modelo, String cor, double preco, int tempo){
        super( modelo, cor, preco );
        this.tempoDeBateria = tempo;
    }

    @Override
    public void cadastrar(){
        System.out.println("Notebook" + this.modelo + " cadastrado");
    }

    @Override
    public String getInformacoes() {
        return super.getInformacoes() + "\nTempo de Bateria: " + this.tempoDeBateria;
    }

    @Override
    public String toString() {
        return getInformacoes();
    }

}
