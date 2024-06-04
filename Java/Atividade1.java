import javax.swing.*;

class Atividade1

{  
    public static void main(String entrada[])
    {
        int n1, n2, div;
        Double potencia;
        String msg = "";
        
        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro: "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite o segundo número inteiro: "));
        
        div = n1 / n2;
        potencia = Math.pow(n1 , n2);
        
        msg = msg + ("O resultado de " +n1+ " / " +n2+ " é = " +div+ "\n");
        msg = msg + ("A potência de " +n1+ " pelo " +n2+ " é = " + potencia);
        JOptionPane.showMessageDialog(null, msg);
    }
}