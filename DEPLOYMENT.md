# دليل نشر مكتبة Yemen Regions Python على PyPI

هذا الدليل يوضح كيفية نشر مكتبة `yemen-regions-py` على PyPI (Python Package Index) خطوة بخطوة.

## المتطلبات الأساسية

قبل البدء في عملية النشر، تأكد من توفر المتطلبات التالية:

### 1. حساب PyPI

يجب أن يكون لديك حساب على PyPI. إذا لم يكن لديك حساب، يمكنك إنشاء واحد من خلال:
- الذهاب إلى [https://pypi.org/account/register/](https://pypi.org/account/register/)
- ملء النموذج وتأكيد البريد الإلكتروني

### 2. أدوات البناء والنشر

تأكد من تثبيت الأدوات المطلوبة:

```bash
pip install build twine
```

### 3. رمز API للمصادقة

للحصول على رمز API من PyPI:
1. سجل الدخول إلى حسابك على PyPI
2. اذهب إلى Account Settings
3. انقر على "Add API token"
4. اختر النطاق المناسب (Entire account أو Project-specific)
5. احفظ الرمز في مكان آمن

## خطوات النشر

### الخطوة 1: التحقق من المشروع

تأكد من أن جميع الملفات في مكانها الصحيح:

```bash
# التحقق من بنية المشروع
ls -la
# يجب أن تشاهد:
# - pyproject.toml
# - README.md
# - LICENSE
# - yemen_regions_py/
# - tests/
# - examples/
```

### الخطوة 2: تشغيل الاختبارات

تأكد من أن جميع الاختبارات تمر بنجاح:

```bash
# تثبيت المكتبة في وضع التطوير
pip install -e .

# تثبيت pytest إذا لم يكن مثبتاً
pip install pytest

# تشغيل الاختبارات
pytest tests/

# تشغيل مثال الاستخدام الأساسي
python examples/basic_usage.py
```

### الخطوة 3: بناء حزمة التوزيع

```bash
# بناء الحزمة
python -m build

# التحقق من الملفات المبنية
ls dist/
# يجب أن تشاهد:
# - yemen_regions_py-1.0.0-py3-none-any.whl
# - yemen_regions_py-1.0.0.tar.gz
```

### الخطوة 4: التحقق من الحزمة

```bash
# التحقق من صحة الحزمة
twine check dist/*
```

### الخطوة 5: النشر على TestPyPI (اختياري)

قبل النشر على PyPI الرسمي، يُنصح بالاختبار على TestPyPI:

```bash
# النشر على TestPyPI
twine upload --repository testpypi dist/*

# سيطلب منك اسم المستخدم وكلمة المرور
# Username: __token__
# Password: [your-testpypi-api-token]
```

اختبار التثبيت من TestPyPI:

```bash
# إنشاء بيئة افتراضية جديدة للاختبار
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# أو
test_env\Scripts\activate  # Windows

# تثبيت من TestPyPI
pip install --index-url https://test.pypi.org/simple/ yemen-regions-py

# اختبار المكتبة
python -c "from yemen_regions_py import YemenRegionsService; print('تم التثبيت بنجاح!')"
```

### الخطوة 6: النشر على PyPI الرسمي

```bash
# النشر على PyPI
twine upload dist/*

# سيطلب منك اسم المستخدم وكلمة المرور
# Username: __token__
# Password: [your-pypi-api-token]
```

### الخطوة 7: التحقق من النشر

بعد النشر الناجح:

1. تحقق من صفحة المشروع على PyPI: [https://pypi.org/project/yemen-regions-py/](https://pypi.org/project/yemen-regions-py/)
2. اختبر التثبيت من PyPI:

```bash
# في بيئة افتراضية جديدة
pip install yemen-regions-py

# اختبار المكتبة
python -c "from yemen_regions_py import YemenRegionsService; service = YemenRegionsService(); print(f'عدد المحافظات: {len(service.get_all_governorates())}')"
```

## نشر إصدارات جديدة

عند نشر إصدارات جديدة:

### 1. تحديث رقم الإصدار

```bash
# في pyproject.toml
version = "1.1.0"  # مثال للإصدار الجديد

# في yemen_regions_py/__init__.py
__version__ = "1.1.0"
```

### 2. تحديث CHANGELOG.md

أضف التغييرات الجديدة في ملف CHANGELOG.md:

```markdown
## [1.1.0] - 2025-XX-XX

### Added
- ميزة جديدة 1
- ميزة جديدة 2

### Fixed
- إصلاح مشكلة 1
- إصلاح مشكلة 2
```

### 3. إنشاء tag في Git

```bash
git add .
git commit -m "Release version 1.1.0"
git tag v1.1.0
git push origin main --tags
```

### 4. بناء ونشر الإصدار الجديد

```bash
# حذف الملفات القديمة
rm -rf dist/ build/ *.egg-info/

# بناء الإصدار الجديد
python -m build

# النشر
twine upload dist/*
```

## نصائح مهمة

### الأمان

- **لا تشارك رموز API أبداً** في الكود أو في المستودعات العامة
- استخدم متغيرات البيئة لتخزين رموز API:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your-api-token
twine upload dist/*
```

### إدارة الإصدارات

- اتبع [Semantic Versioning](https://semver.org/):
  - `MAJOR.MINOR.PATCH` (مثل: 1.2.3)
  - MAJOR: تغييرات غير متوافقة مع الإصدارات السابقة
  - MINOR: إضافة ميزات جديدة متوافقة
  - PATCH: إصلاحات الأخطاء

### الاختبار

- اختبر دائماً على TestPyPI قبل النشر الرسمي
- تأكد من تشغيل جميع الاختبارات قبل النشر
- اختبر التثبيت في بيئة نظيفة

### التوثيق

- تأكد من تحديث README.md مع كل إصدار
- حافظ على CHANGELOG.md محدثاً
- أضف أمثلة للميزات الجديدة

## استكشاف الأخطاء

### مشاكل شائعة وحلولها

#### خطأ: "Package already exists"

```bash
# إذا كان الإصدار موجوداً بالفعل، قم بتحديث رقم الإصدار
# في pyproject.toml و __init__.py
```

#### خطأ: "Invalid authentication credentials"

```bash
# تأكد من صحة رمز API
# تأكد من استخدام __token__ كاسم مستخدم
```

#### خطأ: "File already exists"

```bash
# حذف الملفات القديمة قبل البناء
rm -rf dist/ build/ *.egg-info/
python -m build
```

#### مشاكل في تحميل البيانات

```bash
# تأكد من وجود ملف MANIFEST.in
# تأكد من تضمين ملفات البيانات في pyproject.toml
```

## الدعم

إذا واجهت أي مشاكل في عملية النشر:

1. راجع [دليل PyPI الرسمي](https://packaging.python.org/tutorials/packaging-projects/)
2. تحقق من [وثائق twine](https://twine.readthedocs.io/)
3. ابحث في [منتدى Python Packaging](https://discuss.python.org/c/packaging/)

---

**ملاحظة**: هذا الدليل مخصص لمكتبة `yemen-regions-py`. تأكد من تعديل الأسماء والمسارات حسب مشروعك الخاص.
