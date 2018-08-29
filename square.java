import java.util.*;
import java.lang.*;
import java.io.*;
class square
{
public static void main (String[] args) throws java.lang.Exception	
{
int a,b,i,exp=1;	
Scanner s=new Scanner(System.in);
a=s.nextInt();
b=s.nextInt();
for(i=1;i<=b;i++)
{
exp=exp*a;	
}
System.out.print(exp);	
}
}
