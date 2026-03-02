from dataclasses import dataclass
from typing import Self, ClassVar

@dataclass(frozen=True, slots=True)
class Config:
    env: str
    debug: bool = False

    _cache: ClassVar[dict[str, Self]] = {}

    @classmethod
    def for_env(cls, env: str, debug: bool = False) -> Self:

        if env not in cls._cache:
            cls._cache[env] = cls(env=env, debug=debug)
        
        return cls._cache[env]

def some_other_function() -> None:
    x = Config.for_env('dev')
    print(x)

def main() -> None:
    a = Config.for_env('prod', debug=True)
    b = Config.for_env('prod')
    c = Config.for_env('dev', True)


    print(a.debug)
    print(b.debug)
    print(c.debug)
    some_other_function()

if __name__ == "__main__":
    main()