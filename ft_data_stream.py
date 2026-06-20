import random
from typing import Generator, Tuple, List


# 1. تعريف الـ Generator اللانهائي الذي ينتج أحداثاً كـ tuple
def gen_event() -> Generator[Tuple[str, str], None, None]:
    # قائمة بأسماء اللاعبين
    players: List[str] = ["alice", "bob", "charlie", "dylan"]
    # قائمة بالإجراءات الممكنة
    actions: List[str] = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]
    # حلقة لانهائية لإنتاج الأحداث باستمرار
    while True:
        # إرجاع tuple يحتوي على لاعب وإجراء عشوائي
        yield (random.choice(players), random.choice(actions))


# 2. تعريف الـ Generator الذي يستهلك القائمة ويحذف منها عشوائياً
def consume_event(events: List[Tuple[str, str]]) -> Generator[Tuple[str, str], None, None]:
    # الاستمرار في الإنتاج طالما القائمة تحتوي على عناصر
    while events:
        # اختيار مؤشر عشوائي للعنصر الذي سيتم حذفه
        idx: int = random.randint(0, len(events) - 1)
        # حذف العنصر من القائمة وإرجاعه للمستهلك
        yield events.pop(idx)


# الدالة الرئيسية لتنفيذ المتطلبات
def main() -> None:
    # تهيئة الـ generator اللانهائي
    event_gen = gen_event()

    # تنفيذ 1000 حدث وطباعتها بالتنسيق المطلوب
    for i in range(1000):
        # الحصول على الحدث التالي باستخدام next
        player, action = next(event_gen)
        # طباعة الحدث
        print(f"Event {i}: Player {player} did action {action}")

    # إنشاء قائمة بـ 10 عناصر باستخدام الـ generator
    event_list: List[Tuple[str, str]] = [next(event_gen) for _ in range(10)]
    # طباعة قائمة الأحداث التي تم إنشاؤها
    print(f"List of 10 events: {event_list}")

    # استهلاك الأحداث من القائمة وطباعة الحالة في كل خطوة
    for event in consume_event(event_list):
        # طباعة الحدث الذي تم استهلاكه
        print(f"Got event from list: {event}")
        # طباعة ما تبقى من أحداث في القائمة
        print(f"Remains in list: {event_list}")


# التأكد من تنفيذ البرنامج عند تشغيله مباشرة
if __name__ == "__main__":
    main()
