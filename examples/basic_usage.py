from yemen_regions_py import YemenRegionsService, Language

def main():
    # إنشاء خدمة المناطق اليمنية باللغة العربية
    service_ar = YemenRegionsService(language=Language.ARABIC)
    print("\n--- استخدام اللغة العربية ---")
    
    # الحصول على جميع المحافظات
    governorates_ar = service_ar.get_all_governorates()
    print(f"عدد المحافظات: {len(governorates_ar)}")
    print(f"أول محافظة: {governorates_ar[0].name_ar}")
    
    # البحث عن محافظة "صنعاء"
    sanaa_gov_ar = service_ar.search_governorates("صنعاء")
    if sanaa_gov_ar:
        print(f"المحافظة التي تم العثور عليها: {sanaa_gov_ar[0].name_ar}")
        
        # الحصول على مديريات هذه المحافظة
        districts_of_sanaa_ar = service_ar.get_districts_by_governorate(sanaa_gov_ar[0].id)
        print(f"عدد مديريات {sanaa_gov_ar[0].name_ar}: {len(districts_of_sanaa_ar)}")
        if districts_of_sanaa_ar:
            print(f"أول مديرية في {sanaa_gov_ar[0].name_ar}: {districts_of_sanaa_ar[0].name_ar}")
            
            # الحصول على عزل هذه المديرية
            uzlahs_of_district_ar = service_ar.get_uzlahs_by_district(districts_of_sanaa_ar[0].id)
            print(f"عدد عزل {districts_of_sanaa_ar[0].name_ar}: {len(uzlahs_of_district_ar)}")
            if uzlahs_of_district_ar:
                print(f"أول عزلة في {districts_of_sanaa_ar[0].name_ar}: {uzlahs_of_district_ar[0].name_ar}")
                
                # الحصول على قرى هذه العزلة
                villages_of_uzlah_ar = service_ar.get_villages_by_uzlah(uzlahs_of_district_ar[0].id)
                print(f"عدد قرى {uzlahs_of_district_ar[0].name_ar}: {len(villages_of_uzlah_ar)}")
                if villages_of_uzlah_ar:
                    print(f"أول قرية في {uzlahs_of_district_ar[0].name_ar}: {villages_of_uzlah_ar[0].name_ar}")

    # إنشاء خدمة المناطق اليمنية باللغة الإنجليزية
    service_en = YemenRegionsService(language=Language.ENGLISH)
    print("\n--- Using English Language ---")
    
    # Get all governorates
    governorates_en = service_en.get_all_governorates()
    print(f"Number of governorates: {len(governorates_en)}")
    print(f"First governorate: {governorates_en[0].name_en}")
    
    # Search for "Sanaa" governorate
    sanaa_gov_en = service_en.search_governorates("Sanaa")
    if sanaa_gov_en:
        print(f"Found governorate: {sanaa_gov_en[0].name_en}")
        
        # Get districts of this governorate
        districts_of_sanaa_en = service_en.get_districts_by_governorate(sanaa_gov_en[0].id)
        print(f"Number of districts in {sanaa_gov_en[0].name_en}: {len(districts_of_sanaa_en)}")
        if districts_of_sanaa_en:
            print(f"First district in {sanaa_gov_en[0].name_en}: {districts_of_sanaa_en[0].name_en}")

    # البحث الشامل
    print("\n--- البحث الشامل ---")
    search_results = service_ar.search_all("التحرير")
    for result in search_results:
        print(f"تم العثور على: {result.name} (النوع: {result.type})")

    # الحصول على إحصائيات
    stats = service_ar.get_statistics()
    print("\n--- إحصائيات المناطق ---")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
