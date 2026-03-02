from dataclasses import dataclass
from typing import Any, dataclass_transform

REGISTRY: dict[str, type[Any]] = {}

@dataclass_transform
def event[T](cls: type[T]) -> type[T]:
    REGISTRY[cls.__name__] = dataclass(cls)
    return cls

@event
class UserCreated:
    user_id: int

@event
class UserDeleted:
    user: int

def main() -> None:


    e = UserCreated(123)
    print(e)
    print(REGISTRY)

if __name__ == "__main__":
    main()