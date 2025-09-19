from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Village:
    id: int
    name_ar: str
    name_en: str
    name_ar_tashkeel: Optional[str] = None
    name_ar_normalized: Optional[str] = None
    name_en_normalized: Optional[str] = None

    def get_name(self, lang: 'Language') -> str:
        return self.name_ar if lang == Language.ARABIC else self.name_en

@dataclass
class Uzlah:
    id: int
    name_en: str
    name_ar: str
    name_ar_tashkeel: Optional[str] = None
    name_ar_normalized: Optional[str] = None
    name_en_normalized: Optional[str] = None
    villages: List[Village] = field(default_factory=list)

    def get_name(self, lang: 'Language') -> str:
        return self.name_ar if lang == Language.ARABIC else self.name_en

@dataclass
class District:
    id: int
    name_en: str
    name_ar: str
    name_ar_tashkeel: Optional[str] = None
    name_ar_normalized: Optional[str] = None
    name_en_normalized: Optional[str] = None
    uzlahs: List[Uzlah] = field(default_factory=list)

    def get_name(self, lang: 'Language') -> str:
        return self.name_ar if lang == Language.ARABIC else self.name_en

@dataclass
class Governorate:
    id: int
    name_en: str
    name_ar: str
    name_ar_tashkeel: Optional[str] = None
    phone_numbering_plan: Optional[str] = None
    capital_name_ar: Optional[str] = None
    capital_name_en: Optional[str] = None
    name_ar_normalized: Optional[str] = None
    name_en_normalized: Optional[str] = None
    districts: List[District] = field(default_factory=list)

    def get_name(self, lang: 'Language') -> str:
        return self.name_ar if lang == Language.ARABIC else self.name_en

@dataclass
class YemenData:
    english_name: str
    arabic_name: str
    iso3: str
    iso2: str
    phone_code: str
    capital_english: str
    capital_arabic: str
    area_in_kilometer_square: str
    currency: str
    currency_name_en: str
    currency_name_ar: str
    currency_symbol: str
    tld: str
    region: str
    subregion: str
    timezones: List[Dict[str, Any]]
    translations: Dict[str, str]
    latitude: str
    longitude: str
    emoji: str
    emojiU: str
    governorates: List[Governorate]

@dataclass
class SearchResult:
    type: str
    id: int
    name: str
    name_ar: str
    name_en: str

# لتجنب الاستيراد الدائري
from .enums import Language

