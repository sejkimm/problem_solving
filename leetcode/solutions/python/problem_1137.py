class Solution:
    tribonacci_numbers = []

    def calculate_tribonacci(self):
        self.tribonacci_numbers = [0, 1, 1]

        for _ in range(2, 38):
            self.tribonacci_numbers.append(
                self.tribonacci_numbers[-3] + self.tribonacci_numbers[-2] + self.tribonacci_numbers[-1]
            )

    def tribonacci(self, n: int) -> int:
        try:
            self.tribonacci_numbers[37]
        except IndexError:
            self.calculate_tribonacci()

        return self.tribonacci_numbers[n]
