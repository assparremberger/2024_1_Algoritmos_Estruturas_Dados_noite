public class Desktop extends Computador {
    
    protected int potenciaDaFonte;

    public Desktop(){
        super();
    }

    public Desktop(String modelo, String cor, double preco, int potencia){
        super( modelo, cor, preco );
        this.potenciaDaFonte = potencia;
    }

    @Override
    public void cadastrar(){
        System.out.println("Desktop " + this.modelo + " cadastrado");
    }

    @Override
    public String getInformacoes() {
        return super.getInformacoes() + "\nPotência da Fonte: " + this.potenciaDaFonte;
    }

    @Override
    public String toString() {
        return getInformacoes();
    }

}
