class Solution {
    public int removeDuplicates(int[] nums) {
     int count =1;
     int left=0; //left 
     int right=1;
        for(right=1; right<nums.length;right++){
            System.out.println("l" + left);
            System.out.println("r" + right);
            System.out.println("c" + count);
            if(nums[left] !=nums[right]){
                System.out.println("left: " + nums[left]);
                System.out.println("right: " + nums[right]);

                nums[count]=nums[right];
                count ++;
            }
            left++;
           
        }
        System.out.println(count);
        return count;
    }
   
}
