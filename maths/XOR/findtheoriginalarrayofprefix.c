// /**
//  * Note: The returned array must be malloced, assume caller calls free().
//  */
// int* findArray(int* pref, int prefsize, int* returnsize) {
//     int x = 0;
//     int* arr = (int*)malloc(prefsize * sizeof(int));
//     if(!arr) return NULL; 
//     arr[0]=pref[0];
//     for(int i = 1; i<prefsize; i++) 
//     {
//         x = pref[i]^pref[i-1];
//         arr[i] = x;
//     }
//     *returnsize = prefsize; 
//     return arr;             
// }
// UNDERSTAND IT PROPERLY