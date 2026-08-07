

func search(nums []int, target int) int {
    iz := 0;
    de := len(nums)-1;

	println(target, len(nums));
        
    for iz <= de {
        mita := (iz+de)/2;

        if nums[mita] == target {
            return mita;
        }

        if nums[iz] <= nums[mita] {
            if nums[iz] <= target && target < nums[mita] {
                de = mita - 1
            } else {
                iz = mita + 1
            }
        }else{
            if nums[mita] <  target && target <= nums[de]{
                iz = mita + 1
            }else{
                de = mita - 1
            }
        }
    }
    return -1;
}
