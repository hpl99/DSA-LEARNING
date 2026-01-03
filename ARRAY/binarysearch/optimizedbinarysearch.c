// while (l <= h) {
//     int m = (l + h) / 2;

//     if (arr[m] == key) {
//         // Key found
//         printf("Key found at index %d\n", m);
//         return 0;
//     } else if (arr[m] < key) {
//         l = m + 1;  // Search right half
//     } else {
//         h = m - 1;  // Search left half
//     }
// }