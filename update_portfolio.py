import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Header
content = content.replace("الخدمات</a>", "المهارات</a>")
content = content.replace("استشارة فورية", "استشارة مجانية")

# Hero
old_hero = 'أبني حلولًا تعتمد على الذكاء الاصطناعي والأتمتة لتحويل العمليات المعقدة إلى <strong class="text-white font-bold">أنظمة أكثر ذكاءً، كفاءةً وقابليةً للتوسع</strong>؛ من أتمتة سير العمل والنماذج المالية والمحاسبية، إلى البنية السحابية وأنظمة الإنتاج الرقمي — أصمم حلولًا تقنية تخدم <strong class="text-purple-300 font-bold">القرار، الكفاءة، والنمو</strong>.'
new_hero = 'مسيرة شغف في هندسة الذكاء الاصطناعي والأتمتة، أُسخر فيها التقنية لبناء <strong class="text-white font-bold">أنظمة ذكية تعكس طموحي وشغفي بالابتكار</strong>؛ من أتمتة سير العمل والنماذج المالية، إلى البنية السحابية وأنظمة الإنتاج الرقمي — أُوثق هنا رحلتي كمهندس يعشق تحويل التعقيد إلى إبداع تقني، وأرحب دوماً بتقديم أي استشارات مجانية.'
content = content.replace(old_hero, new_hero)

# Services to Skills
content = content.replace("مجالات التميز والخدمات الهندسية", "المهارات والخبرات الهندسية")
content = content.replace('كيف نُسهم في تطوير <span class="purple-gradient-text">وتسريع وتيرة أعمالكم؟</span>', 'شغف بناء المنظومات <span class="purple-gradient-text">وإتقان الحلول الذكية</span>')
content = content.replace('نُحوّل التحديات المعقدة إلى منظومات ذكية ومستقرة تضمن أعلى درجات الكفاءة التشغيلية والنمو المستمر لأعمالك.', 'توثيق لمسيرتي وخبراتي في تحويل الأفكار والتحديات إلى منظومات ذكية ومستقرة، وبناء معماريات برمجية تعكس دقة التنفيذ والابتكار.')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
