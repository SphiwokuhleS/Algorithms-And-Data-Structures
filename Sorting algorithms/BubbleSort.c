#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

int main()
{
	int arraysort[SIZE];
	int x,i,j,swap;

/* populate the array */
	srand((unsigned)time(NULL));
	for(x=0;x<SIZE;x++)
		arraysort[x] = rand() % 100 + 1;

	/* Display the unsorted array */
	puts("Unsorted array:");
	for(x=0;x<SIZE;x++)
		printf(" %3d",arraysort[x]);
	putchar('\n');

	/* Sort the array */

	for(i = 0; i < SIZE -1; i++)
	{
		for(j  = 0; j < SIZE -1 -i; j++)
		{
			if(arraysort[j] > arraysort[j+1])
			{
				swap = arraysort[j];
				arraysort[j] = arraysort[j+1];
				arraysort[j+1] = swap;
			}
		}
	}
	/* Display the sorted array */
	puts("Sorted array:");
	for(x=0;x<SIZE;x++)
		printf(" %3d",arraysort[x]);
	putchar('\n');

	return(0);
}
