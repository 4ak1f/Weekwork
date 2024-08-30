#include<stdio.h>
int main(){
	int a;
	printf("Enter your number:\n ");
	scanf("%d", &a);
	if(a==0){
		printf("Number is even.");
	}
	else if(a==1){
		printf("Number is odd.");
	}
	else if (a%2==0){
		printf("Number is even.");
	}
	else{
		printf("Number is odd.");
	}
}
