#include<stdio.h>
void main()
{
    int k;
    scanf("%d",&k);
    
    while(k%10!=0)
    {
        k++;
    }
    printf("%d",k);
}
