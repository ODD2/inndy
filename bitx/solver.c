#include <stdio.h>
#include <stdint.h>

int main()
{
 int num = 0;
 while(scanf("%x",&num)==1)
 { 
	printf("%c\n",(char)   (((num & 0xAA)>>1)|((num&0x55)*2))-9);
 }
}
