class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []

        for op in operations:
            if op == "+":
                a = results[-1]
                b = results[-2]
                results.append(a + b)
            elif op == "C":
                results.pop()
            elif op == "D":
                results.append(results[-1] * 2)
            else:
                results.append(int(op))

        return sum(results)
                