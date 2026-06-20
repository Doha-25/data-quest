import random
from typing import Set, Dict, List


# دالة لتوليد مجموعة عشوائية من الإنجازات لكل لاعب
def gen_player_achievements() -> Set[str]:
    # قائمة بجميع الإنجازات الممكنة بناءً على المثال
    all_achievements: List[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor", "Treasure Hunter",
        "First Steps", "Sharp Mind", "Hidden Path Finder", "Unstoppable"
    ]
    # اختيار عدد عشوائي من الإنجازات
    # بدلاً من البداية من 0، ابدأ من 1 أو 2 لضمان أن المجموعة لن تكون فارغة
    num: int = random.randint(3, 8)
    # هذا يضمن اختيار إنجازين إلى ستة لكل لاعب
    return set(random.sample(all_achievements, num))


# الدالة الرئيسية
def main() -> None:
    # تهيئة البيانات للاعبين الأربعة كما في المثال
    players: List[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    player_data: Dict[str, Set[str]] = {p: gen_player_achievements() for p in players}

    print("--- Achievement Tracker System ---")
    print("")

    # 1. طباعة إنجازات كل لاعب
    for name in players:
        print(f"Player {name}: {player_data[name]}")

    # 2. حساب وطباعة كل الإنجازات المميزة
    all_distinct: Set[str] = set().union(*player_data.values())
    print(f"\nAll distinct achievements: {all_distinct}")

    # 3. حساب وطباعة الإنجازات المشتركة
    common: Set[str] = set.intersection(*player_data.values())
    print(f"\nCommon achievements: {common}")

    # 4. طباعة ما يملكه كل لاعب ولا يملكه غيره (Only X has)
    print("")
    for name in players:
        others: Set[str] = set().union(
            *[player_data[p] for p in players if p != name]
        )
        only_player: Set[str] = player_data[name].difference(others)
        print(f"Only {name} has: {only_player}")

    # 5. طباعة الإنجازات الناقصة لكل لاعب
    print("")
    for name in players:
        missing: Set[str] = all_distinct.difference(player_data[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
