class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]

        for i in students:
            counts[i] += 1

        for i in sandwiches:
            if counts[i] > 0:
                counts[i] -= 1
            else:
                break

        return sum(counts)