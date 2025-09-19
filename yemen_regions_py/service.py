import json
import os
from typing import List, Optional, Dict, Any
from .models import YemenData, Governorate, District, Uzlah, Village, SearchResult
from .enums import Language, RegionLevel

class YemenRegionsService:
    """
    خدمة المناطق اليمنية - الفئة الرئيسية للوصول إلى بيانات المناطق اليمنية
    """
    
    def __init__(self, language: Language = Language.ARABIC):
        """
        تهيئة خدمة المناطق اليمنية
        
        Args:
            language: اللغة المفضلة للعرض (افتراضي: العربية)
        """
        self.language = language
        self._data: Optional[YemenData] = None
        self._load_data()
    
    def _load_data(self) -> None:
        """تحميل بيانات المناطق اليمنية من ملف JSON"""
        try:
            # الحصول على مسار ملف البيانات
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_file = os.path.join(current_dir, 'data', 'yemen-info.json')
            
            with open(data_file, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # تحويل البيانات إلى كائنات Python
            self._data = self._parse_data(raw_data)
            
        except FileNotFoundError:
            raise FileNotFoundError("ملف بيانات المناطق اليمنية غير موجود")
        except json.JSONDecodeError:
            raise ValueError("خطأ في تحليل ملف بيانات المناطق اليمنية")
    
    def _parse_data(self, raw_data: Dict[str, Any]) -> YemenData:
        """تحويل البيانات الخام إلى كائنات Python"""
        governorates = []
        
        for gov_data in raw_data.get('governorates', []):
            districts = []
            
            for dist_data in gov_data.get('districts', []):
                uzlahs = []
                
                for uzlah_data in dist_data.get('uzaal', []):  # ملاحظة: uzaal في JSON
                    villages = []
                    
                    for village_data in uzlah_data.get('villages', []):
                        village = Village(
                            id=village_data.get('id'),
                            name_ar=village_data.get('name_ar', ''),
                            name_en=village_data.get('name_en', ''),
                            name_ar_tashkeel=village_data.get('name_ar_tashkeel'),
                            name_ar_normalized=village_data.get('name_ar_normalized'),
                            name_en_normalized=village_data.get('name_en_normalized')
                        )
                        villages.append(village)
                    
                    uzlah = Uzlah(
                        id=uzlah_data.get('id'),
                        name_ar=uzlah_data.get('name_ar', ''),
                        name_en=uzlah_data.get('name_en', ''),
                        name_ar_tashkeel=uzlah_data.get('name_ar_tashkeel'),
                        name_ar_normalized=uzlah_data.get('name_ar_normalized'),
                        name_en_normalized=uzlah_data.get('name_en_normalized'),
                        villages=villages
                    )
                    uzlahs.append(uzlah)
                
                district = District(
                    id=dist_data.get('id'),
                    name_ar=dist_data.get('name_ar', ''),
                    name_en=dist_data.get('name_en', ''),
                    name_ar_tashkeel=dist_data.get('name_ar_tashkeel'),
                    name_ar_normalized=dist_data.get('name_ar_normalized'),
                    name_en_normalized=dist_data.get('name_en_normalized'),
                    uzlahs=uzlahs
                )
                districts.append(district)
            
            governorate = Governorate(
                id=gov_data.get('id'),
                name_ar=gov_data.get('name_ar', ''),
                name_en=gov_data.get('name_en', ''),
                name_ar_tashkeel=gov_data.get('name_ar_tashkeel'),
                phone_numbering_plan=gov_data.get('phone_numbering_plan'),
                capital_name_ar=gov_data.get('capital_name_ar'),
                capital_name_en=gov_data.get('capital_name_en'),
                name_ar_normalized=gov_data.get('name_ar_normalized'),
                name_en_normalized=gov_data.get('name_en_normalized'),
                districts=districts
            )
            governorates.append(governorate)
        
        return YemenData(
            english_name=raw_data.get('english_name', ''),
            arabic_name=raw_data.get('arabic_name', ''),
            iso3=raw_data.get('iso3', ''),
            iso2=raw_data.get('iso2', ''),
            phone_code=raw_data.get('phone_code', ''),
            capital_english=raw_data.get('capital_english', ''),
            capital_arabic=raw_data.get('capital_arabic', ''),
            area_in_kilometer_square=raw_data.get('area_in_kilometer_square', ''),
            currency=raw_data.get('currency', ''),
            currency_name_en=raw_data.get('currency_name_en', ''),
            currency_name_ar=raw_data.get('currency_name_ar', ''),
            currency_symbol=raw_data.get('currency_symbol', ''),
            tld=raw_data.get('tld', ''),
            region=raw_data.get('region', ''),
            subregion=raw_data.get('subregion', ''),
            timezones=raw_data.get('timezones', []),
            translations=raw_data.get('translations', {}),
            latitude=raw_data.get('latitude', ''),
            longitude=raw_data.get('longitude', ''),
            emoji=raw_data.get('emoji', ''),
            emojiU=raw_data.get('emojiU', ''),
            governorates=governorates
        )
    
    def set_language(self, language: Language) -> None:
        """تغيير اللغة المفضلة"""
        self.language = language
    
    def get_all_governorates(self) -> List[Governorate]:
        """الحصول على جميع المحافظات"""
        if not self._data:
            return []
        return self._data.governorates
    
    def get_governorate_by_id(self, gov_id: int) -> Optional[Governorate]:
        """الحصول على محافظة بالمعرف"""
        for gov in self.get_all_governorates():
            if gov.id == gov_id:
                return gov
        return None
    
    def search_governorates(self, query: str) -> List[Governorate]:
        """البحث في المحافظات بالاسم"""
        query = query.lower().strip()
        results = []
        
        for gov in self.get_all_governorates():
            # البحث في الأسماء العربية والإنجليزية
            if (query in gov.name_ar.lower() or 
                query in gov.name_en.lower() or
                (gov.name_ar_normalized and query in gov.name_ar_normalized.lower()) or
                (gov.name_en_normalized and query in gov.name_en_normalized.lower())):
                results.append(gov)
        
        return results
    
    def get_districts_by_governorate(self, gov_id: int) -> List[District]:
        """الحصول على مديريات محافظة معينة"""
        governorate = self.get_governorate_by_id(gov_id)
        if governorate:
            return governorate.districts
        return []
    
    def get_district_by_id(self, district_id: int) -> Optional[District]:
        """الحصول على مديرية بالمعرف"""
        for gov in self.get_all_governorates():
            for district in gov.districts:
                if district.id == district_id:
                    return district
        return None
    
    def search_districts(self, query: str, gov_id: Optional[int] = None) -> List[District]:
        """البحث في المديريات"""
        query = query.lower().strip()
        results = []
        
        governorates = [self.get_governorate_by_id(gov_id)] if gov_id else self.get_all_governorates()
        
        for gov in governorates:
            if not gov:
                continue
            for district in gov.districts:
                if (query in district.name_ar.lower() or 
                    query in district.name_en.lower() or
                    (district.name_ar_normalized and query in district.name_ar_normalized.lower()) or
                    (district.name_en_normalized and query in district.name_en_normalized.lower())):
                    results.append(district)
        
        return results
    
    def get_uzlahs_by_district(self, district_id: int) -> List[Uzlah]:
        """الحصول على عزل مديرية معينة"""
        district = self.get_district_by_id(district_id)
        if district:
            return district.uzlahs
        return []
    
    def get_uzlah_by_id(self, uzlah_id: int) -> Optional[Uzlah]:
        """الحصول على عزلة بالمعرف"""
        for gov in self.get_all_governorates():
            for district in gov.districts:
                for uzlah in district.uzlahs:
                    if uzlah.id == uzlah_id:
                        return uzlah
        return None
    
    def search_uzlahs(self, query: str, district_id: Optional[int] = None) -> List[Uzlah]:
        """البحث في العزل"""
        query = query.lower().strip()
        results = []
        
        if district_id:
            district = self.get_district_by_id(district_id)
            uzlahs_to_search = district.uzlahs if district else []
        else:
            uzlahs_to_search = []
            for gov in self.get_all_governorates():
                for district in gov.districts:
                    uzlahs_to_search.extend(district.uzlahs)
        
        for uzlah in uzlahs_to_search:
            if (query in uzlah.name_ar.lower() or 
                query in uzlah.name_en.lower() or
                (uzlah.name_ar_normalized and query in uzlah.name_ar_normalized.lower()) or
                (uzlah.name_en_normalized and query in uzlah.name_en_normalized.lower())):
                results.append(uzlah)
        
        return results
    
    def get_villages_by_uzlah(self, uzlah_id: int) -> List[Village]:
        """الحصول على قرى عزلة معينة"""
        uzlah = self.get_uzlah_by_id(uzlah_id)
        if uzlah:
            return uzlah.villages
        return []
    
    def get_village_by_id(self, village_id: int) -> Optional[Village]:
        """الحصول على قرية بالمعرف"""
        for gov in self.get_all_governorates():
            for district in gov.districts:
                for uzlah in district.uzlahs:
                    for village in uzlah.villages:
                        if village.id == village_id:
                            return village
        return None
    
    def search_villages(self, query: str, uzlah_id: Optional[int] = None) -> List[Village]:
        """البحث في القرى"""
        query = query.lower().strip()
        results = []
        
        if uzlah_id:
            uzlah = self.get_uzlah_by_id(uzlah_id)
            villages_to_search = uzlah.villages if uzlah else []
        else:
            villages_to_search = []
            for gov in self.get_all_governorates():
                for district in gov.districts:
                    for uzlah in district.uzlahs:
                        villages_to_search.extend(uzlah.villages)
        
        for village in villages_to_search:
            if (query in village.name_ar.lower() or 
                query in village.name_en.lower() or
                (village.name_ar_normalized and query in village.name_ar_normalized.lower()) or
                (village.name_en_normalized and query in village.name_en_normalized.lower())):
                results.append(village)
        
        return results
    
    def search_all(self, query: str) -> List[SearchResult]:
        """البحث الشامل في جميع المستويات"""
        results = []
        
        # البحث في المحافظات
        for gov in self.search_governorates(query):
            results.append(SearchResult(
                type=RegionLevel.GOVERNORATE.value,
                id=gov.id,
                name=gov.get_name(self.language),
                name_ar=gov.name_ar,
                name_en=gov.name_en
            ))
        
        # البحث في المديريات
        for district in self.search_districts(query):
            results.append(SearchResult(
                type=RegionLevel.DISTRICT.value,
                id=district.id,
                name=district.get_name(self.language),
                name_ar=district.name_ar,
                name_en=district.name_en
            ))
        
        # البحث في العزل
        for uzlah in self.search_uzlahs(query):
            results.append(SearchResult(
                type=RegionLevel.UZLAH.value,
                id=uzlah.id,
                name=uzlah.get_name(self.language),
                name_ar=uzlah.name_ar,
                name_en=uzlah.name_en
            ))
        
        # البحث في القرى
        for village in self.search_villages(query):
            results.append(SearchResult(
                type=RegionLevel.VILLAGE.value,
                id=village.id,
                name=village.get_name(self.language),
                name_ar=village.name_ar,
                name_en=village.name_en
            ))
        
        return results
    
    def get_country_info(self) -> Optional[YemenData]:
        """الحصول على معلومات عامة عن اليمن"""
        return self._data
    
    def get_statistics(self) -> Dict[str, int]:
        """الحصول على إحصائيات المناطق"""
        if not self._data:
            return {}
        
        total_districts = sum(len(gov.districts) for gov in self._data.governorates)
        total_uzlahs = sum(
            len(district.uzlahs) 
            for gov in self._data.governorates 
            for district in gov.districts
        )
        total_villages = sum(
            len(uzlah.villages)
            for gov in self._data.governorates
            for district in gov.districts
            for uzlah in district.uzlahs
        )
        
        return {
            'governorates': len(self._data.governorates),
            'districts': total_districts,
            'uzlahs': total_uzlahs,
            'villages': total_villages
        }
