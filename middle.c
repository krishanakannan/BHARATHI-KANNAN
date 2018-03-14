
#include <stdio.h>
#include<string.h>
int main(void) 
{
	char a[30];
	int b,i;
	printf("enter the string:");
	scanf("%s",a);
	b=strlen(a);
	if(n%2==0)
	{
		a[b/2]='*';
		a[(b/2)-1]='*';
	}
	else
	{
		a[b/2]='*';
	}
	printf("\n%s",a);
	return 0;
}
