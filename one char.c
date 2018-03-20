
#include <stdio.h>
#include<string.h>
int main(void) 
{
	char a[50],b[50];
	int i,j,n1,n2,count=0;
	scanf("%s %s",a,b);
	n1=strlen(a);
	n2=strlen(b);
	if(n1==n2)
	{
		for(i=0;i<n1;i++)
		{
			if(a[i]==b[i])
			{
				count=count+0;
			}
			else
			{
				count=count+1;
			}
			
		}
		if(count==1)
		{
			printf("\nyes");
		}
		else
		{
			printf("\nno");
		}
	}
	else
	{
		printf("\nno");
	}
	return 0;
}
