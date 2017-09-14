import java.io.*;
import java.util.*;
public class Alphabet
{
 public static void main(String [] args)
 {
   char c;
   Scanner input=new Scanner(System.in);
   c=input.nextInt();
   if((c>='a' && c<='z')||(c>='A' && c<='Z'))
   {
    System.out.println(c+"is an alphabet");
   }
   else
   {
    System.out.println(c+"is not an alphabet");
   }
  }
 }
