#include <stdio.h>
#define MAX_STACK_SIZE 1000000

struct A {
		int stack[MAX_STACK_SIZE];
		int top_index;
		int cur_size;
	};
	
void push(struct A *a, int new_data)
{
	// push data to stack
	// TODO
	(*a).stack[(*a).cur_size] = new_data;
	(*a).cur_size += 1;
	(*a).top_index += 1;
}

void pop(struct A *a)
{
	// check that stack is empty
	if ((*a).cur_size == 0)
	{
		printf( "-1\n" );
		return;
	}

	// pop data from stack
	// TODO
	printf("%d\n", (*a).stack[(*a).cur_size - 1]);
	(*a).cur_size -= 1;
	(*a).top_index -= 1;
}

int top(struct A *a)
{
	// TODO
	return (*a).cur_size;
}

void print_stack(struct A *a)
{
	if ((*a).cur_size > 0) {
		printf("0\n");
	} else {
		printf("1\n");
	}
}

void b(struct A *a) {
	if ((*a).cur_size > 0) {
		printf("%d\n", (*a).stack[(*a).cur_size - 1]);
	} else {
		printf("-1\n");
	}
}
	
int main(void) {
	int n, i = 1;
	struct A a;
	a.cur_size = 0;
	a.top_index = -1;
	
	scanf("%d", &n);
	
	for (i; i <= n; i++) {
		int select;
		scanf( "%d", &select );
		switch( select )
		{
			case 1: // push
			{
				int new_data;
				scanf( "%d", &new_data );
				push(&a, new_data);
				break;
			}
			case 2: // pop
			{
				pop(&a);
				break;
			}
			case 3: // print top
			{
				printf("%d\n", top(&a));
				break;
			}
			case 4: // print current stack size
			{
				print_stack(&a);
				break;
			}
			case 5: // print stack
			{
				b(&a);
				break;
			}
		}
	}
}