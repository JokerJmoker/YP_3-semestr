from abc import ABC, abstractmethod
import math


class Base(ABC):
    def __init__(self,data,result): # применимо для всех наследников
        self.data = data
        self.result = result


    @abstractmethod
    def get_answer(self):
        pass
        

    @abstractmethod
    def get_score(self):
        pass


    @abstractmethod
    def get_loss(self):
        pass


class BaseExtended(Base):
    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]
        

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
            / len(ans)


class A(BaseExtended):
    def get_loss(self):
        return sum(
            [(x - y) * (x - y) for (x, y) in zip(self.data, self.result)])


class B(BaseExtended):
    def get_loss(self):
        return -sum([
            y * math.log(x) + (1 - y) * math.log(1 - x)
            for (x, y) in zip(self.data, self.result)
        ])


    def get_pre(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(ans)


    def get_rec(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(self.result)


    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(BaseExtended):
    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data, self.result)])
    
data = [0.1, 0.4, 0.6, 0.8]
result = [0, 0, 1, 1]

a = A(data, result)
b = B(data, result)
c = C(data, result)

print("A loss:", a.get_loss())
print("A score:", a.get_score())

print("B loss:", b.get_loss())
print("B score:", b.get_score())

print("C loss:", c.get_loss())
print("C score:", c.get_score())