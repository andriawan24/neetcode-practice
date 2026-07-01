class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentPos = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currentPos + 1]
        print(self.history)
        self.history.append(url)
        self.currentPos += 1

    def back(self, steps: int) -> str:
        self.currentPos -= steps
        self.currentPos = max(0, self.currentPos)

        return self.history[self.currentPos]

    def forward(self, steps: int) -> str:
        self.currentPos += steps
        self.currentPos = min(len(self.history) - 1, self.currentPos)

        return self.history[self.currentPos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)