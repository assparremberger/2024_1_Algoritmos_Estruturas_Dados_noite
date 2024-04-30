public class Main{

    public static void main(String[] args) {
        System.out.println("Teste");

        //Computador c1 = new Computador("Dell");
        Desktop d1 = new Desktop("Dell" , "Preto" , 
        3985.69 , 500);
        System.out.println( d1.getInformacoes() );

        Notebook n1 = new Notebook("Dell Inspirion" , "Black Piano" , 
        5689.25 , 5000);
        System.out.println( n1 );
    }
}