#!/usr/bin/env python3
"""Defines a VerboseList class that reports changes to itself."""


class VerboseList(list):
    """A list that prints a message when items are added or removed."""

    def append(self, item):
        """Add an item to the end of the list and print a message.

        Args:
            item: the item to add.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print how many items were added.

        Args:
            iterable: the items to add.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a message, then remove the first match of item.

        Args:
            item: the item to remove.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a message, then remove and return the item at index.

        Args:
            index (int): position of the item, the last one by default.

        Returns:
            The item that was removed.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)