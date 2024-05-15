# Types of Inheritance ( Single Level , Multi Level , Multiple)

'''
Example of 2 classes without Inheritance
class A():

    def state1(self):
        print("State1 is Present")

    def state2(self):
        print("State2 is Present")

    def state3(self):
        print("State3 is Present")


class B():

    def state4(self):
        print("State4 is Present")

    def state5(self):
        print("State5 is Present")

    def state6(self):
        print("State6 is Present")

ele1 = A()
ele1.state1()
ele1.state2()
ele1.state3()

ele2 = B()
ele2.state4()
ele2.state5()
ele2.state6()
'''

'''
Example of 2 classes with Single Level  Inheritance 
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