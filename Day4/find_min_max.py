def get_input():
    return [int(input(f"Enter number {i+1}:")) for i in range(int(input("Enter the size of nums:")))]

def smallest(nums):
    return min(nums)

def biggest(nums):
    return max(nums)

def main():
    nums = get_input()
    print("Smallest Number:", smallest(nums))
    print("Biggest Number:", biggest(nums))

main()
