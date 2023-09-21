# import numpy
class Solution:
    def average(self, salary: List[int]) -> float:
        for i in range(len(salary)):
            salary.remove(max(salary))
            salary.remove(min(salary))
            return (sum(salary)/ len(salary))

            # avg = numpy.average(salary)
            # return avg