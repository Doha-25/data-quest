from typing import Dict, List, Any


def analyze_dashboard(data: Dict[str, Any]) -> None:
    """تحليل بيانات اللاعبين لتطابق المخرجات المطلوبة بدقة."""
    # القائمة الأصلية كما تظهر في الـ Output
    players: List[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    # محاكاة بيانات النتائج المرتبطة بكل لاعب
    scores: Dict[str, int] = {
        'Alice': 263, 'Bob': 666, 'Charlie': 907, 'Dylan': 170,
        'Emma': 568, 'Gregory': 446, 'John': 90, 'Kevin': 527, 'Liam': 54
    }

    # 1. القائمة الأولية
    print(f"Initial list of players: {players}")

    # 2. القائمة بعد تطبيق Capitalize
    capitalized: List[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized}")

    # 3. القائمة المصفاة (فقط الأسماء التي تبدأ بـ a, c, e, g, l)
    filtered: List[str] = [p.capitalize() for p in players
                           if p.lower().startswith(('a', 'c', 'e', 'g', 'l'))]
    print(f"New list of capitalized names only: {filtered}")
    print()

    # 4. قاموس النتائج (Score dict)
    print(f"Score dict: {scores}")

    # 5. حساب المتوسط الحسابي (410.11)
    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {avg:.2f}")

    # 6. النتائج العالية (High scores) > 400
    high_scores: Dict[str, int] = {
        name: score for name, score in scores.items() if score > 400
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    # تمرير بيانات وهمية تطابق الـ Output
    dummy_data: Dict[str, Any] = {"players": {}}
    print("=== Game Data Alchemist ===")
    print()
    analyze_dashboard(dummy_data)
