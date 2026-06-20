import sys
from typing import List


# تعريف الدالة الرئيسية التي ستقوم بمعالجة الدرجات
def score_cruncher() -> None:
    # استخراج المدخلات من سطر الأوامر واستبعاد اسم الملف
    args: List[str] = sys.argv[1:]

    # طباعة العنوان الثابت للبرنامج
    print("=== Player Score Analytics ===")

    # التحقق من أن القائمة فارغة في حال عدم إدخال أي شيء
    if not args:
        # طباعة رسالة توضيحية للمستخدم حول كيفية الاستخدام
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        # الخروج من الدالة لأن البرنامج لا يملك بيانات
        return

    # تهيئة قائمة فارغة لتخزين الأرقام الصحيحة بعد التنظيف
    valid_scores: List[int] = []

    # المرور على كل مدخل في قائمة المدخلات
    for arg in args:
        # بداية كتلة محاولة التعامل مع الأخطاء
        try:
            # محاولة تحويل المدخل النصي إلى رقم صحيح
            score: int = int(arg)
            # التحقق من أن الرقم موجب (الدرجات لا يجب أن تكون سالبة)
            if score >= 0:
                # إضافة الرقم الصحيح إلى القائمة
                valid_scores.append(score)
            else:
                # طباعة رسالة خطأ في حال كان الرقم سالباً
                print(f"Invalid parameter: '{arg}'")
        # في حال حدوث خطأ أثناء التحويل (مثلاً إدخال حرف)
        except ValueError:
            # طباعة رسالة خطأ للمستخدم وتجاهل القيمة
            print(f"Invalid parameter: '{arg}'")

    # التحقق مما إذا كانت القائمة فارغة بعد معالجة جميع المدخلات
    if not valid_scores:
        # طباعة رسالة تنبيه للمستخدم في حال عدم وجود بيانات صالحة للتحليل
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        # الخروج من البرنامج
        return

    # حساب مجموع الدرجات الصحيحة
    total: int = sum(valid_scores)
    # حساب المتوسط الحسابي للدرجات
    average: float = float(total) / len(valid_scores)
    # العثور على أعلى درجة في القائمة
    highest: int = max(valid_scores)
    # العثور على أقل درجة في القائمة
    lowest: int = min(valid_scores)

    # طباعة النتائج النهائية بالتنسيق المطلوب
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {highest - lowest}")


# نقطة دخول البرنامج للتأكد من تشغيله كملف رئيسي
if __name__ == "__main__":
    # استدعاء الدالة لتنفيذ الكود
    score_cruncher()
