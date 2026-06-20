import sys
from typing import List


def command_quest() -> None:
    args: List[str] = sys.argv[1:]
    program_name: str = sys.argv[0]

    print("=== Command Quest ===")
    print(f"Program name: {program_name}")

    if not args:
        print("No arguments provided!")
    else:
        # نطبع عدد المعاملات المستلمة
        print(f"Arguments received: {len(args)}")
        # استخدام enumerate للترقيم بدءاً من 1
        for i, arg in enumerate(args, 1):
            print(f"Argument {i}: {arg}")

    # العدد الكلي يتضمن اسم البرنامج والمعاملات
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
