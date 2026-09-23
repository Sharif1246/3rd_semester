from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


# --- Demo ---
if __name__ == "__main__":   # (typo guard: use __name__ == "__main__")
    s: Stack[int] = Stack()
    s.push(1); s.push(2); s.push(3)
    print(s.peek(), s.size(), s.is_empty())   # 3 3 False
    print(s.pop(), s.pop())                    # 3 2

    names: Stack[str] = Stack()
    names.push("Alice"); names.push("Bob")
    print(names.pop())                         # Bob

    empty: Stack[int] = Stack()
    try:
        empty.pop()
    except IndexError as e:
        print("Error:", e)