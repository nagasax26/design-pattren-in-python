class SubSystemA:
    def method_a(self):
        print('method a')


class SubSystemB:
    def method_b(self):
        print('method b')


class SubSystemC:
    def method_c(self):
        print('method c')


class Facade:
    """Simplify the subsystems to a facade"""
    def sub_system_a(self):
        return SubSystemA().method_a()

    def sub_system_b(self):
        return SubSystemB().method_b()

    def sub_system_c(self):
        return SubSystemC().method_c()


Facade().sub_system_a()
Facade().sub_system_b()
Facade().sub_system_c()