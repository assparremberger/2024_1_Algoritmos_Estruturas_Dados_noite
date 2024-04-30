public abstract class Computador{

    public String modelo, cor;
    public double preco;

    public Computador(){

    }

    public Computador(String modelo, String cor, double preco){
        this.modelo = modelo;
        this.cor = cor;
        this.preco = preco;
        //System.out.println(this.modelo + " construído!");
    }

    public abstract void cadastrar();

    public String getInformacoes(){
        return  "Modelo: " + this.modelo + "\n" + 
                "Cor: " + this.cor + "\n" +
                "Preço: R$ " + this.preco;
    }

    @Override
    public String toString() {
        return getInformacoes();
    }

}