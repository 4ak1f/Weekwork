#include<stdio.h>
int main(){
	
	double a,b,result;
	char op;
	printf("Enter the operation you want to perform: ");
	scanf("%c", &op);
	printf("Enter two numbers: ");
	scanf("%lf\t%lf", &a,&b);
	switch (op){
		case '+':
			result=a+b;
			break;
			case '-':
				result=a-b;
				break;
				case'*':
					result=a*b;
					break;
					case'/':
						if((a==0) || (b==0)){
							printf("Invalid input check your numbers again.");
						}
						else{
						
						result=a/b;
					}
						break;
						default:
							printf("Invalid operator!");
	}
	printf("Result: %.2lf %c %.2lf = %lf\n", a,op,b,result);
}
