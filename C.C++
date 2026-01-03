#include <iostream> // For input/output operations
#include <cmath>    // For the sqrt() function

int main() {
    int  number = 5.0; // The number for which to find the square root
    int result = std::sqrt(number); // Calculate the square root

    std::cout << "The square root of " << number << " is " << result << std::endl;

    return 0;
}