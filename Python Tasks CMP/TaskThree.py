#include <stdio.h>

int main() {
    // Initialize an array with sample values of average monthly rainfall
    double rainfall_Tab[12] = {50.5, 45.2, 60.0, 80.5, 120.2, 150.0, 130.5, 100.2, 90.0, 75.5, 65.2, 55.0};

    // Calculate the average rainfall for the year
    double year_sum = 0.0;
    for (int i = 0; i < 12; ++i) {
        year_sum += rainfall_Tab[i];
    }
    double year_av = year_sum / 12.0;

    // Calculate the difference between each month's rainfall and the yearly average
    double diff_month_rainfall[12];
    for (int i = 0; i < 12; ++i) {
        diff_month_rainfall[i] = rainfall_Tab[i] - year_av;
    }

    // Print a formatted table showing monthly rainfall and the difference from the yearly average
    printf("%-8s%-8s%-8s\n", "Month", "Rainfall", "Diff");
    for (int i = 0; i < 12; ++i) {
        printf("%-8d%-8.1f%-8.1f\n", i + 1, rainfall_Tab[i], diff_month_rainfall[i]);
    }

    return 0;
}
