import java.util.Scanner;
//Exercice 16

public class RacineCarree{
    public static void main(String[] args){

        double nombrePositif;
        Scanner sc = new Scanner(System.in);

        do {
            do{
                System.out.print("Donnez un nombre positif:");
                nombrePositif = sc.nextDouble();
               

                if(nombrePositif < 0){
                    System.out.println("svp positif\n\n");
                }
            } while(nombrePositif < 0);
            
            if(nombrePositif != 0){
                System.out.println("sa racine carree est: " + Math.sqrt(nombrePositif)  + "\n\n");
            }

        } while (nombrePositif != 0);

         
        System.out.println("Merci, A bientôt");

        sc.close();
    }
}
