#include<stdio.h>
void main()
{
int a;
printf("\n Enter the number:");
scanf("%d",&a);
while(a%2==0)
{
printf(\n"%d",(a/2));
a=a/2;
}
}
