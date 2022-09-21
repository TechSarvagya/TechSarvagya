import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class emojiplay extends JFrame implements MouseListener
{ 
 JLabel jl;
 ImageIcon happy;
 ImageIcon pain;
 ImageIcon suspicious;
 ImageIcon almostdead;
emojiplay()
{ happy= new ImageIcon("a.jpg");
  jl=new JLabel(happy,JLabel.CENTER);
  jl.addMouseListener(this);
  suspicious= new ImageIcon("b.jpg");
 pain=new ImageIcon("c.jpg");
 almostdead= new ImageIcon("d.png");
add(jl);

}
public void mouseEntered(MouseEvent e)
 { jl.setIcon(suspicious);
  
}
 public void mousePressed(MouseEvent e)
 { jl.setIcon(pain);
 }
 public void mouseReleased(MouseEvent e)
 { jl.setIcon(almostdead);
 
 }
public void mouseExited(MouseEvent e)
{ jl.setIcon(happy);}
public void mouseClicked(MouseEvent e)
{}
public static void main(String args[])
{emojiplay em=new emojiplay();
em.setVisible(true);
em.setSize(100,130);
}}
