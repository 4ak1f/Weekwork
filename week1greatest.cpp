#include<stdio.h>
int main(){
	int a,b,c;
	printf("Enter three numbers:\n ");
	scanf("%d\n%d\n%d", &a,&b,&c);
	if((a>b && a>c)){
		printf("First number is the greatest.");
	}
	else if((b>a && b>c)){
		printf("Second number is the greatest.");
	}
	else{
		printf("Third number is the greatest.");
	}
}
