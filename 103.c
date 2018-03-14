#include <stdio.h>
#include<string.h>
int main() 
{
	char b[100];
    int l,i;
    scanf("%[^\t\n]s",b);
    n=strlen(b);
    b[0]=b[0]-32;
    for(i=0;i<l;i++)
    {
      if(b[i]==' ')
      {
          b[i+1]=b[i+1]-32;
      }
    }
    printf("%s",b);
	
	return 0;
}
