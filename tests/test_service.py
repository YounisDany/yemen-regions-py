import pytest
from yemen_regions_py import YemenRegionsService, Language, RegionLevel
from yemen_regions_py.models import Governorate, District, Uzlah, Village

@pytest.fixture
def service():
    return YemenRegionsService()

def test_get_all_governorates(service):
    governorates = service.get_all_governorates()
    assert isinstance(governorates, list)
    assert len(governorates) > 0
    assert isinstance(governorates[0], Governorate)

def test_get_governorate_by_id(service):
    gov = service.get_governorate_by_id(1) # أمانة العاصمة
    assert gov is not None
    assert gov.name_ar == "أمانة العاصمة"
    assert gov.name_en == "Amant Al-Asmah"

    gov_none = service.get_governorate_by_id(9999)
    assert gov_none is None

def test_search_governorates(service):
    results_ar = service.search_governorates("صنعاء")
    assert len(results_ar) > 0
    assert any("صنعاء" in g.name_ar for g in results_ar)

    service.set_language(Language.ENGLISH)
    results_en = service.search_governorates("Sanaa")
    assert len(results_en) > 0
    assert any("Sanaa" in g.name_en for g in results_en)

def test_get_districts_by_governorate(service):
    districts = service.get_districts_by_governorate(1) # أمانة العاصمة
    assert isinstance(districts, list)
    assert len(districts) > 0
    assert isinstance(districts[0], District)

    districts_none = service.get_districts_by_governorate(9999)
    assert len(districts_none) == 0

def test_get_district_by_id(service):
    dist = service.get_district_by_id(1) # صنعاء القديمة
    assert dist is not None
    assert dist.name_ar == "صنعاء القديمة"

    dist_none = service.get_district_by_id(99999)
    assert dist_none is None

def test_search_districts(service):
    results_ar = service.search_districts("الوحدة")
    assert len(results_ar) > 0
    assert any("الوحدة" in d.name_ar for d in results_ar)

    results_filtered = service.search_districts("الوحدة", gov_id=1) # الوحدة في أمانة العاصمة
    assert len(results_filtered) > 0
    assert all(d.name_ar == "الوحدة" for d in results_filtered)

def test_get_uzlahs_by_district(service):
    uzlahs = service.get_uzlahs_by_district(1) # صنعاء القديمة
    assert isinstance(uzlahs, list)
    assert len(uzlahs) > 0
    assert isinstance(uzlahs[0], Uzlah)

    uzlahs_none = service.get_uzlahs_by_district(99999)
    assert len(uzlahs_none) == 0

def test_get_uzlah_by_id(service):
    uzlah = service.get_uzlah_by_id(1) # صنعاء القديمه
    assert uzlah is not None
    assert uzlah.name_ar == "صنعاء القديمه"

    uzlah_none = service.get_uzlah_by_id(999999)
    assert uzlah_none is None

def test_search_uzlahs(service):
    results_ar = service.search_uzlahs("ازال")
    assert len(results_ar) > 0
    assert any("ازال" in u.name_ar for u in results_ar)

    results_filtered = service.search_uzlahs("ازال", district_id=2) # ازال في مديرية ازال
    assert len(results_filtered) > 0
    assert all(u.name_ar == "ازال" for u in results_filtered)

def test_get_villages_by_uzlah(service):
    villages = service.get_villages_by_uzlah(1) # صنعاء القديمه
    assert isinstance(villages, list)
    assert len(villages) > 0
    assert isinstance(villages[0], Village)

    villages_none = service.get_villages_by_uzlah(999999)
    assert len(villages_none) == 0

def test_get_village_by_id(service):
    village = service.get_village_by_id(1) # الامانة
    assert village is not None
    assert village.name_ar == "الامانة"

    village_none = service.get_village_by_id(9999999)
    assert village_none is None

def test_search_villages(service):
    results_ar = service.search_villages("الامانة")
    assert len(results_ar) > 0
    assert any("الامانة" in v.name_ar for v in results_ar)

    results_filtered = service.search_villages("الامانة", uzlah_id=1) # الامانة في عزلة صنعاء القديمه
    assert len(results_filtered) > 0
    assert all(v.name_ar == "الامانة" for v in results_filtered)

def test_search_all(service):
    results = service.search_all("صنعاء")
    assert len(results) > 0
    assert any(r.type == RegionLevel.GOVERNORATE.value for r in results)
    assert any(r.type == RegionLevel.DISTRICT.value for r in results)

def test_get_country_info(service):
    info = service.get_country_info()
    assert info is not None
    assert info.english_name == "Yemen"

def test_get_statistics(service):
    stats = service.get_statistics()
    assert isinstance(stats, dict)
    assert "governorates" in stats
    assert "districts" in stats
    assert "uzlahs" in stats
    assert "villages" in stats
    assert stats["governorates"] > 0

def test_language_switching(service):
    service.set_language(Language.ENGLISH)
    gov = service.get_governorate_by_id(1)
    assert gov.get_name(service.language) == "Amant Al-Asmah"

    service.set_language(Language.ARABIC)
    gov = service.get_governorate_by_id(1)
    assert gov.get_name(service.language) == "أمانة العاصمة"
