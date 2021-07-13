from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def dir():
        pass

    @staticmethod
    @abstractmethod
    def detach():
        pass


class File(IComponent):
    def __init__(self, name):
        self.name = name

    def dir(self):
        return self.name

    def detach(self):
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)


class Folder(IComponent):
    def __init__(self, name):
        self.components = []
        self.name = name

    def dir(self, is_root_folder=True, indent=''):
        for f in self.components:
            if isinstance(f, File):
                if not is_root_folder:
                    print(f'{indent}{f.dir()}')
                else:
                    print(f.dir())
            else:
                if not is_root_folder:
                    print(indent+'/' + f.name)
                else:
                    print('/' + f.name)
                f.dir(False, indent+'--')

    def attach(self, component):
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        self.components.remove(component)

    def detach(self):
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None


file1 = File('new.text')
file2 = File('car.json')
file3 = File('text.json')
file4 = File('lol.json')
file5 = File('users.json')

folder_1 = Folder('jsons')
folder_12 = Folder('useful texts')
folder_2 = Folder('texts')
folder_3 = Folder('images')

folder_1.attach(file1)
folder_1.attach(folder_12)
folder_12.attach(file3)
folder_12.attach(file4)
folder_12.attach(file5)

folder_2.attach(folder_1)
folder_2.attach(file2)
folder_2.attach(folder_3)

folder_3.attach(folder_12)

folder_2.dir()
