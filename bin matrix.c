#include<stdio.h>
int main()
{
	int b[100][100],k,p,i,j,c=0;
	printf("\nenter the row size : ");
	scanf("%d",&k);
	printf("\nenter the column size : ");
	scanf("%d",&p);
	printf("\nenter the array elements : ");
	for(i=1;i<=k;i++)
	{
	    for(j=1;j<=p;j++)
		{
			scanf("%d",&b[i][j]);
		}
	}
	for(i=1;i<=k;i++)
	{
		for(j=1;j<=p;j++)
		{
		    if(b[i][j]==1)
			{
				if(b[i-1][j-1]==0&&b[i][j+1]==0&&b[i][j-1]==0&&b[i+1][j+1]==0)
				{
					c=c+1;
				}
			}
		}
	}
	printf("\nThe total island is %d",c);
	return 0;
}
