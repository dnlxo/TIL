class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        num_of_boats = 0
        sorted_people = sorted(people, reverse=True)
        while left <= right:
            if sorted_people[left] + sorted_people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            num_of_boats += 1
        return num_of_boats


sol = Solution()
print(sol.numRescueBoats([3,2,2,1], 3))