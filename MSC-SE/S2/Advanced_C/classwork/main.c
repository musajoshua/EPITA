#include <stdio.h>

float square(float x);

int main()
{
    float input, sq;

    scanf("%f", &input);

    sq = square(input);

    printf("%f\n", sq);

    return 0;
}