// int subsetXORSum(int* nums, int numsize) {
//     int arr[1<<numsize];
//      for(int mask =0;mask<(1<<numsize);mask++){
//         int count =0;
//         for(int i=0;i<numsize;i++){
//             if(mask&(1<<i))
//             {
//                 count^=nums[i];
//             }
//         }
//         arr[mask]=count;
//      }
//      int count1 =0;
//      for(int i=0;i<(1<<numsize);i++){
//         count1+=arr[i];
//      }
//      return count1 ;
// }