import java.util.Scanner;
//Exercice17

public class TriangleIsoceleEtoiles{
    public static void main( String[] args){

        //On demande la hauteur du triangle a l'utilisateur
        Scanner sc = new Scanner(System.in);
        System.out.print("Combien de lignes? ");
        int hauteur = sc.nextInt();

        afficher(hauteur);

        sc.close();

    }
    static void afficher( int hauteur ){
        for(int i =0; i <= hauteur ; i++){
            String espaces = "";
            String etoiles = "";
            String ligne = "";

            //on calcule puis met les espaces necessaires dans la variable espaces
            for(int a = 1; a <= (hauteur - i); a++){
                espaces = espaces + " ";
            }

            //on calcule puis met les etoiles necessaires dans la variable etoiles
            for(int a = 1; a <= (2*i - 1); a++){
                etoiles = etoiles + "*";
            }
            
            //on met les espaces puis les etoiles sur la ligne i
            ligne = espaces + etoiles;

            //on affiche la ligne i et on part a la ligne.
            System.out.println(ligne);
            
            
        }
    }
}
