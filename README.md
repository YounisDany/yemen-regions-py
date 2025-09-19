# Yemen Regions Python

<div align="center">

[![PyPI version](https://badge.fury.io/py/yemen-regions-py.svg)](https://badge.fury.io/py/yemen-regions-py)
[![Python versions](https://img.shields.io/pypi/pyversions/yemen-regions-py.svg)](https://pypi.org/project/yemen-regions-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**مكتبة Python للمناطق اليمنية مع دعم اللغتين العربية والإنجليزية**

*A Python library for Yemen regions with Arabic and English support*

</div>

## المميزات | Features

**بيانات شاملة**: جميع المحافظات والمديريات والعزل والقرى في اليمن مع دعم اللغتين العربية والإنجليزية. تتضمن المكتبة بيانات كاملة ومحدثة للتقسيمات الإدارية اليمنية، مما يجعلها مثالية للتطبيقات التي تحتاج إلى معلومات جغرافية دقيقة.

**سهولة الاستخدام**: واجهة برمجية بسيطة وواضحة تسمح للمطورين بالوصول السريع إلى البيانات المطلوبة. تم تصميم المكتبة لتكون سهلة التعلم والاستخدام، مع توثيق شامل وأمثلة عملية.

**أداء محسن**: تحميل سريع للبيانات مع إمكانية البحث والتصفية المتقدمة. تستخدم المكتبة تقنيات محسنة لضمان الأداء العالي حتى مع كميات البيانات الكبيرة.

**مرونة في الاستخدام**: دعم للبحث بالمعرف أو الاسم، مع إمكانية اختيار اللغة المفضلة. يمكن للمطورين تخصيص سلوك المكتبة حسب احتياجات تطبيقاتهم.

---

- 🇾🇪 **Comprehensive Data**: All governorates, districts, uzlahs, and villages in Yemen
- 🌐 **Bilingual Support**: Arabic and English with full localization
- ⚡ **High Performance**: Fast data loading with advanced search and filtering
- 🔍 **Flexible Search**: Search by ID, name, or custom criteria
- 📦 **Easy Integration**: Simple API with comprehensive documentation
- 🧪 **Well Tested**: Comprehensive test suite ensuring reliability

## التثبيت | Installation

### عبر pip

```bash
pip install yemen-regions-py
```

### من المصدر

```bash
git clone https://github.com/YounisDany/yemen-regions-py.git
cd yemen-regions-py
pip install -e .
```

## الاستخدام السريع | Quick Usage

### استيراد المكتبة | Import the library

```python
from yemen_regions_py import YemenRegionsService, Language
```

### مثال بسيط | Basic Example

```python
# إنشاء خدمة المناطق اليمنية
service = YemenRegionsService(language=Language.ARABIC)

# الحصول على جميع المحافظات
governorates = service.get_all_governorates()
print(f"عدد المحافظات: {len(governorates)}")

# البحث عن محافظة
sanaa = service.search_governorates("صنعاء")[0]
print(f"المحافظة: {sanaa.name_ar}")

# الحصول على مديريات المحافظة
districts = service.get_districts_by_governorate(sanaa.id)
print(f"عدد المديريات: {len(districts)}")
```

### مثال متقدم | Advanced Example

```python
from yemen_regions_py import YemenRegionsService, Language

# إنشاء خدمة باللغة الإنجليزية
service = YemenRegionsService(language=Language.ENGLISH)

# البحث المتقدم
results = service.search_all("Sanaa")
for result in results:
    print(f"Type: {result.type}, Name: {result.name}")

# الحصول على التسلسل الهرمي الكامل
governorate = service.get_governorate_by_id(1)
if governorate:
    print(f"Governorate: {governorate.name_en}")
    for district in governorate.districts:
        print(f"  District: {district.name_en}")
        for uzlah in district.uzlahs:
            print(f"    Uzlah: {uzlah.name_en}")
            for village in uzlah.villages[:3]:  # أول 3 قرى فقط
                print(f"      Village: {village.name_en}")
```

## واجهة برمجة التطبيقات | API Reference

### YemenRegionsService

الفئة الرئيسية للوصول إلى بيانات المناطق اليمنية.

```python
class YemenRegionsService:
    def __init__(self, language: Language = Language.ARABIC)
```

#### المعاملات | Parameters

- `language`: اللغة المفضلة للعرض (`Language.ARABIC` أو `Language.ENGLISH`)

#### الطرق الرئيسية | Main Methods

##### `get_all_governorates() -> List[Governorate]`

الحصول على جميع المحافظات.

```python
governorates = service.get_all_governorates()
for gov in governorates:
    print(gov.name_ar, gov.name_en)
```

##### `get_governorate_by_id(gov_id: int) -> Optional[Governorate]`

الحصول على محافظة بالمعرف.

```python
governorate = service.get_governorate_by_id(1)
if governorate:
    print(f"المحافظة: {governorate.name_ar}")
```

##### `search_governorates(query: str) -> List[Governorate]`

البحث في المحافظات بالاسم.

```python
results = service.search_governorates("صنعاء")
print(f"تم العثور على {len(results)} محافظة")
```

##### `get_districts_by_governorate(gov_id: int) -> List[District]`

الحصول على مديريات محافظة معينة.

```python
districts = service.get_districts_by_governorate(1)
for district in districts:
    print(district.name_ar)
```

##### `search_all(query: str) -> List[SearchResult]`

البحث الشامل في جميع المستويات.

```python
results = service.search_all("الوحدة")
for result in results:
    print(f"{result.type}: {result.name}")
```

### النماذج | Models

#### Governorate (المحافظة)

```python
@dataclass
class Governorate:
    id: int
    name_ar: str
    name_en: str
    name_ar_tashkeel: Optional[str]
    phone_numbering_plan: str
    districts: List[District]
```

#### District (المديرية)

```python
@dataclass
class District:
    id: int
    name_ar: str
    name_en: str
    name_ar_tashkeel: Optional[str]
    uzlahs: List[Uzlah]
```

#### Uzlah (العزلة)

```python
@dataclass
class Uzlah:
    id: int
    name_ar: str
    name_en: str
    name_ar_tashkeel: Optional[str]
    villages: List[Village]
```

#### Village (القرية)

```python
@dataclass
class Village:
    id: int
    name_ar: str
    name_en: str
    name_ar_tashkeel: Optional[str]
```

### التعدادات | Enums

#### Language

```python
class Language(Enum):
    ARABIC = "ar"
    ENGLISH = "en"
```

#### RegionLevel

```python
class RegionLevel(Enum):
    GOVERNORATE = "governorate"
    DISTRICT = "district"
    UZLAH = "uzlah"
    VILLAGE = "village"
```

## أمثلة متقدمة | Advanced Examples

### مثال Django

```python
# views.py
from django.http import JsonResponse
from yemen_regions_py import YemenRegionsService, Language

def get_governorates(request):
    service = YemenRegionsService(language=Language.ARABIC)
    governorates = service.get_all_governorates()
    
    data = [
        {
            'id': gov.id,
            'name': gov.name_ar,
            'districts_count': len(gov.districts)
        }
        for gov in governorates
    ]
    
    return JsonResponse({'governorates': data})

def get_districts(request, governorate_id):
    service = YemenRegionsService()
    districts = service.get_districts_by_governorate(governorate_id)
    
    data = [
        {
            'id': dist.id,
            'name': dist.name_ar,
            'uzlahs_count': len(dist.uzlahs)
        }
        for dist in districts
    ]
    
    return JsonResponse({'districts': data})
```

### مثال Flask

```python
from flask import Flask, jsonify, request
from yemen_regions_py import YemenRegionsService, Language

app = Flask(__name__)

@app.route('/api/governorates')
def api_governorates():
    lang = request.args.get('lang', 'ar')
    language = Language.ARABIC if lang == 'ar' else Language.ENGLISH
    
    service = YemenRegionsService(language=language)
    governorates = service.get_all_governorates()
    
    return jsonify([
        {
            'id': gov.id,
            'name': gov.name_ar if language == Language.ARABIC else gov.name_en,
            'districts_count': len(gov.districts)
        }
        for gov in governorates
    ])

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    service = YemenRegionsService()
    results = service.search_all(query)
    
    return jsonify([
        {
            'type': result.type,
            'id': result.id,
            'name': result.name
        }
        for result in results
    ])

if __name__ == '__main__':
    app.run(debug=True)
```

### مثال FastAPI

```python
from fastapi import FastAPI, Query
from typing import List, Optional
from yemen_regions_py import YemenRegionsService, Language

app = FastAPI(title="Yemen Regions API")

@app.get("/governorates")
async def get_governorates(lang: str = Query("ar", regex="^(ar|en)$")):
    """الحصول على جميع المحافظات"""
    language = Language.ARABIC if lang == "ar" else Language.ENGLISH
    service = YemenRegionsService(language=language)
    governorates = service.get_all_governorates()
    
    return [
        {
            "id": gov.id,
            "name": gov.name_ar if language == Language.ARABIC else gov.name_en,
            "districts_count": len(gov.districts)
        }
        for gov in governorates
    ]

@app.get("/governorates/{governorate_id}/districts")
async def get_districts(governorate_id: int):
    """الحصول على مديريات محافظة معينة"""
    service = YemenRegionsService()
    districts = service.get_districts_by_governorate(governorate_id)
    
    return [
        {
            "id": dist.id,
            "name_ar": dist.name_ar,
            "name_en": dist.name_en,
            "uzlahs_count": len(dist.uzlahs)
        }
        for dist in districts
    ]

@app.get("/search")
async def search_regions(q: str = Query(..., min_length=2)):
    """البحث في جميع المناطق"""
    service = YemenRegionsService()
    results = service.search_all(q)
    
    return [
        {
            "type": result.type,
            "id": result.id,
            "name": result.name,
            "name_ar": getattr(result, 'name_ar', ''),
            "name_en": getattr(result, 'name_en', '')
        }
        for result in results
    ]
```

### مثال تحليل البيانات

```python
import pandas as pd
from yemen_regions_py import YemenRegionsService

def analyze_yemen_regions():
    """تحليل بيانات المناطق اليمنية"""
    service = YemenRegionsService()
    
    # إحصائيات عامة
    governorates = service.get_all_governorates()
    total_districts = sum(len(gov.districts) for gov in governorates)
    total_uzlahs = sum(
        len(district.uzlahs) 
        for gov in governorates 
        for district in gov.districts
    )
    total_villages = sum(
        len(uzlah.villages)
        for gov in governorates
        for district in gov.districts
        for uzlah in district.uzlahs
    )
    
    print(f"إحصائيات المناطق اليمنية:")
    print(f"المحافظات: {len(governorates)}")
    print(f"المديريات: {total_districts}")
    print(f"العزل: {total_uzlahs}")
    print(f"القرى: {total_villages}")
    
    # إنشاء DataFrame للتحليل
    data = []
    for gov in governorates:
        for district in gov.districts:
            for uzlah in district.uzlahs:
                data.append({
                    'governorate_id': gov.id,
                    'governorate_name': gov.name_ar,
                    'district_id': district.id,
                    'district_name': district.name_ar,
                    'uzlah_id': uzlah.id,
                    'uzlah_name': uzlah.name_ar,
                    'villages_count': len(uzlah.villages)
                })
    
    df = pd.DataFrame(data)
    
    # تحليل توزيع القرى حسب المحافظات
    gov_analysis = df.groupby('governorate_name')['villages_count'].agg([
        'count', 'sum', 'mean', 'std'
    ]).round(2)
    
    print("\nتوزيع القرى حسب المحافظات:")
    print(gov_analysis)
    
    return df

if __name__ == "__main__":
    df = analyze_yemen_regions()
```

## التطوير | Development

### إعداد بيئة التطوير

```bash
# استنساخ المستودع
git clone https://github.com/YounisDany/yemen-regions-py.git
cd yemen-regions-py

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate  # Windows

# تثبيت التبعيات
pip install -e ".[dev]"
```

### تشغيل الاختبارات

```bash
# تشغيل جميع الاختبارات
pytest

# تشغيل الاختبارات مع تقرير التغطية
pytest --cov=yemen_regions_py

# تشغيل اختبارات محددة
pytest tests/test_service.py::test_get_all_governorates
```

### فحص جودة الكود

```bash
# تنسيق الكود
black yemen_regions_py/

# فحص الأخطاء
flake8 yemen_regions_py/

# فحص الأنواع
mypy yemen_regions_py/
```

## المساهمة | Contributing

نرحب بالمساهمات من المجتمع. يرجى اتباع الخطوات التالية:

1. **Fork** المستودع
2. إنشاء فرع جديد للميزة (`git checkout -b feature/amazing-feature`)
3. تثبيت التغييرات (`git commit -m 'Add amazing feature'`)
4. رفع الفرع (`git push origin feature/amazing-feature`)
5. فتح **Pull Request**

### إرشادات المساهمة

- تأكد من أن جميع الاختبارات تمر بنجاح
- اتبع معايير تنسيق الكود المحددة
- أضف اختبارات للميزات الجديدة
- حدث التوثيق عند الضرورة

## الترخيص | License

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## الشكر والتقدير | Acknowledgments

- بيانات المناطق اليمنية من [Yemen Open Source](https://github.com/YemenOpenSource/Yemen-info)
- مستوحى من [Yemen Regions Widget](https://github.com/YounisDany/yemen-regions-widget)

---

<div align="center">

**صنع بـ ❤️ للمطورين اليمنيين**

*Made with ❤️ for Yemeni developers*

</div>
