#include <stdio.h>
#include <stdlib.h>
int main()
{
	int accumulate=0;
	int hex=0;
	int count =0;
	while(scanf("%x",&hex)==1)
	{
//		printf("%#x\n",hex);
		count +=1;
		accumulate+=hex<<(8*(count-1));
		if(count ==4)
		{
			printf("%#.8x\n",accumulate);
			accumulate=0;	
			count =0;
		}
	}
}
