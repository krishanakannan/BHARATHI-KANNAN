
#include <stdio.h>
#include<string.h>
int main(void) {
	char c[100],o[100];
	scanf("%s %s",c,o);
	int m,n,i,j,u,k,l,x,y,z,flag=0;
	m=strlen(c);
	n=strlen(o);
	if(m==n)
	{
	for(i=0;i<m;i++)
	{
	for(j=i+1;j<m;j++)
	{
	u=c[i];
	k=c[j];
	l=o[i];
	x=o[j];
  y=u-k;
	z=l-x;
	if(y==z)
			{
				flag=1;
			}
			else
			{
				flag=0;
				break;
			}
		}
	}
	}
	if(flag==1)
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
	return 0;
}
