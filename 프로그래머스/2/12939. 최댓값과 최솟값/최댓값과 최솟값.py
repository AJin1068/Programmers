def solution(s):
    nums = [int(string) for string in s.split()]
    return f"{min(nums)} {max(nums)}"