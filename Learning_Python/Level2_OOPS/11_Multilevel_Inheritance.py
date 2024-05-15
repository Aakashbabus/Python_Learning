'''
Example of 3 classes with multi Level  Inheritance
Here C is inheriting B which intern has inherited A so C is inheriting both B and A
'''

class A():

    def state1(self):
        print("State1 is Present")

    def state2(self):
        print("State2 is Present")

    def state3(self):
        print("State3 is Present")


class B(A):

    def state4(self):
        print("State4 is Present")

    def state5(self):
        print("State5 is Present")

    def state6(self):
        print("State6 is Present")

class C(B):

    def state7(self):
        print("State7 is Present")

    def state8(self):
        print("State8 is Present")

    def state9(self):
        print("State9 is Present")

ele1 = A()
ele1.state1()
ele1.state2()
ele1.state3()

ele2 = B()
ele2.state1()
ele2.state2()
ele2.state3()
ele2.state4()
ele2.state5()
ele2.state6()

ele3 = C()
ele3.state1()
ele3.state2()
ele3.state3()
ele3.state4()
ele3.state5()
ele3.state6()
ele3.state7()
ele3.state8()
ele3.state9()