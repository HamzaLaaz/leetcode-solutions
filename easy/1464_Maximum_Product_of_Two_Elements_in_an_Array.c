int maxProduct(int* nums, int numsSize) {
    int k = 0;
    for (int i = 0; i < numsSize; i++){
        if (k < nums[i])
            k = nums[i];
    }
    int check = 1;
    int j = 0;
    for (int i = 0; i < numsSize; i++){
        if (k == nums[i]){
            if (check == 0)
                j = nums[i];
            check = 0;
        }
        else if (j < nums[i])
            j = nums[i];
    }
    int result = (k - 1) * (j - 1);
    return result;
}
