#include<stdio.h>
int main()
{
char a[50];
int i=0;
printf("Enter the string:");
scanf("%s",a);
if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U')
{
printf("yes\n");
}
else
{
printf("no\n");
}

return 0;
}
