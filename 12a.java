import java.util.*;

public class 12a
{
	public static void main(String[] args) 
  {
        int n,a,d,val=0;
		Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=sc.nextInt();
        d=sc.nextInt();
        val=(n*(2*a+(n-1)*d))/2;
        System.out.println(val);
        
	}

}
