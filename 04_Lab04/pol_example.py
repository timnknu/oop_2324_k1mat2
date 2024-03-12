class A:
    def pr(self):
        print("I'm pr from A")
        print(self.f())
    def f(self):
        return -1

class B(A):
    def f(self):
        return 128

#obj = B()
#obj.pr()
print(type(1))
print(type(1.0))