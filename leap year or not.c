#include<stdio.h>
int main()
{
int year;
printf("\nEnter the year");
scanf("%d",&year);
if((year%4)==0)
{
printf("%d is leap year \n");
}
else
{
printf("%d is not leap year \n");
}
return 0;
}
