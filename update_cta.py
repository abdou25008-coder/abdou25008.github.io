import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's replace CTA titles to be about consultations and networking rather than business
content = content.replace("هل أنت مستعد لتطوير منظومة أعمالك؟", "هل نتشارك الشغف ذاته؟")
content = content.replace("دعنا نبني نظامًا بيئيًا ذكيًا يضاعف إنتاجيتك ويقود مسيرة نجاحك الرقمي.", "أسعد دائماً بالتواصل مع الشغوفين، ومشاركة الرؤى، ولا مانع من تقديم استشارات مجانية في مجالات الذكاء الاصطناعي وهندسة الأنظمة.")
content = content.replace("ابدأ مشروعك الآن", "تواصل معي لاستشارة مجانية")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
