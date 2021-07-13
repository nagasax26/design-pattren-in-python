from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method():
        "A method each Leaf and composite container shoud implement"
        pass

    @staticmethod
    @abstractmethod
    def detach():
        "Called before a leaf is attached to a composite"
        pass


class Leaf(IComponent):
    "A Leaf can be added to a composite, but a leaf cant be added to other leafs"

    def method(self):
        parent_id = id(self.reference_to_parent) if self.reference_to_parent is not None else None
        print(f'Leaf={id(self)}\tparent:={parent_id}')

    def detach(self):
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None


class Composite(IComponent):
    "A Composite can contain leaves and composites"

    def __init__(self):
        self.components = []

    def method(self):
        parent_id = id(self.reference_to_parent) if self.reference_to_parent is not None else None
        print(f'Composite={id(self)}\tParent={parent_id}',f'Components={len(self.components)}')

        for component in self.components:
            component.method()

    def attach(self, component):
        """
        Detach leaf/composite from any current parent
        reference and than set the parent reference to this composite
        """
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        self.components.remove(component)

    def detach(self):
        "Detaching this composites from its parent composite"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None


leaf_a = Leaf()
leaf_b = Leaf()

composite_a = Composite()
composite_b = Composite()

composite_a.attach(leaf_a)

composite_b.attach(composite_a)

leaf_b.method()
print()

composite_b.method()
print()

leaf_a.detach()
composite_b.method()

