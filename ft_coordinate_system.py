import math
from typing import Tuple


# تعريف دالة لاستقبال الإحداثيات من المستخدم وإرجاعها على شكل Tuple
def get_player_pos() -> Tuple[float, float, float]:
    # حلقة تكرارية مستمرة لضمان إدخال بيانات صحيحة
    while True:
        try:
            # طلب المدخلات من المستخدم بصيغة محددة
            user_input: str = input("Enter new coordinates as floats in "
                                    "format 'x,y,z': ")
            # تقسيم النص المدخل إلى قائمة بناءً على الفاصلة
            coords: list[str] = user_input.split(",")
            # التحقق من أن المستخدم أدخل بالضبط 3 قيم
            if len(coords) != 3:
                raise ValueError("Invalid number of coordinates")
            # قائمة مؤقتة لتخزين الأرقام بعد التحويل
            results: list[float] = []
            # المرور على كل إحداثي للتأكد من كونه رقماً
            for item in coords:
                try:
                    results.append(float(item))
                except ValueError:
                    # رمي خطأ مخصص يحتوي على قيمة البارامتر الخاطئ
                    raise ValueError(f"Error on parameter '{item}': "
                                     f"could not convert string to float: "
                                     f"'{item}'")
            # إرجاع القيم في Tuple ثابت
            return (results[0], results[1], results[2])
        # التقاط الأخطاء المرفوعة داخل الكتلة
        except ValueError as e:
            # إذا كان الخطأ هو نقص عدد الإحداثيات نطبع الرسالة العامة
            if str(e) == "Invalid number of coordinates":
                print("Invalid syntax")
            else:
                # طباعة رسالة الخطأ المخصصة للبارامتر الخاطئ
                print(e)


# دالة لحساب المسافة الإقليدية بين نقطتين في فضاء ثلاثي الأبعاد
def calculate_distance(p1: Tuple[float, float, float],
                       p2: Tuple[float, float, float]) -> float:
    # تطبيق قانون المسافة الإقليدية في 3 أبعاد
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2])**2)


# الدالة الرئيسية لتنفيذ منطق البرنامج وتنسيق المخرجات
def main() -> None:
    # طباعة العنوان الترحيبي
    print("--- Game Coordinate System ---")
    # طباعة سطر فارغ للمطابقة مع شكل المخرجات
    print("")
    # طباعة عنوان المجموعة الأولى
    print("Get a first set of coordinates")
    # استدعاء الدالة لجلب المجموعة الأولى
    pos1: Tuple[float, float, float] = get_player_pos()
    # طباعة الـ Tuple الناتج
    print(f"Got a first tuple: {pos1}")
    # عرض الإحداثيات كل على حدة
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    # حساب المسافة من المركز (0,0,0)
    dist_to_center: float = calculate_distance(pos1, (0.0, 0.0, 0.0))
    # طباعة النتيجة مقربة لـ 4 خانات عشرية
    print(f"Distance to center: {dist_to_center:.4f}")
    # طباعة سطر فارغ للمطابقة مع الشكل
    print("")

    # طباعة عنوان المجموعة الثانية
    print("Get a second set of coordinates")
    # الحصول على الإحداثيات الثانية
    pos2: Tuple[float, float, float] = get_player_pos()
    # حساب المسافة بين النقطتين
    dist: float = calculate_distance(pos1, pos2)
    # طباعة النتيجة النهائية مقربة لـ 4 خانات عشرية
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


# التأكد من تنفيذ البرنامج كملف رئيسي
if __name__ == "__main__":
    # تشغيل البرنامج
    main()
