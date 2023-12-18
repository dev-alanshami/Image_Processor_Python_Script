// This program takes in a list of numbers from the command line.

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  // Dynamically allocated memory
  int *arrayPtr = NULL;
  arrayPtr = (int *)malloc((argc - 1) * sizeof(int));

  // Read elements from command line and convert to integers
  for (int i = 1; i < argc; i++) {
    arrayPtr[i - 1] = atoi(argv[i]);
  }

  // Increment each element by 1 and apply threshold
  for (int i = 0; i < argc - 1; i++) {
    arrayPtr[i]++; 
    if (arrayPtr[i] < 170) {
      arrayPtr[i] = 0;
    }
    printf("%d ", arrayPtr[i]); // Print the number with a space
  }

  // Free dynamically allocated memory
  free(arrayPtr);

  return 0;
}
