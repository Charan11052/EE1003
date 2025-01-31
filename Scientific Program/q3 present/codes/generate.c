#include <stdio.h>
#include <math.h>

int main() {
    // Define the number of points and range for x
    int n = 400;
    double x, y, step = 8.0 / (n - 1);
    FILE *fp;

    // Open a file to save points in .tex format
    fp = fopen("points_c.tex", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    fprintf(fp, "x, y\n");

    // Loop over x from -4 to 4 and calculate y = sqrt(16 - x^2)
    for (int i = 0; i < n; i++) {
        x = -4 + i * step;
        y = sqrt(16 - x * x);
        fprintf(fp, "%lf, %lf\n", x, y);  // Save points in file
    }

    fclose(fp);
    printf("Points saved in 'points_c.tex'\n");

    return 0;
}

