#include <stdio.h>


void main()
{
	int num2=0;
	int num1=0;
	scanf("%x",&num1);
	while(scanf("%x",&num2)!=EOF)
	{
		printf("%c",(char)num2-num1);
		num1=num2;
	}


}
