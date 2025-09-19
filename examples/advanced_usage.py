from flask import Flask, jsonify, request
from yemen_regions_py import YemenRegionsService, Language

app = Flask(__name__)
service = YemenRegionsService() # Default language is Arabic

@app.route("/api/governorates")
def get_governorates():
    lang = request.args.get("lang", "ar")
    service.set_language(Language.ARABIC if lang == "ar" else Language.ENGLISH)
    
    governorates = service.get_all_governorates()
    return jsonify([
        {
            "id": gov.id,
            "name": gov.get_name(service.language),
            "districts_count": len(gov.districts)
        }
        for gov in governorates
    ])

@app.route("/api/governorates/<int:gov_id>/districts")
def get_districts(gov_id):
    lang = request.args.get("lang", "ar")
    service.set_language(Language.ARABIC if lang == "ar" else Language.ENGLISH)
    
    districts = service.get_districts_by_governorate(gov_id)
    return jsonify([
        {
            "id": dist.id,
            "name": dist.get_name(service.language),
            "uzlahs_count": len(dist.uzlahs)
        }
        for dist in districts
    ])

@app.route("/api/search")
def search_regions():
    query = request.args.get("q", "")
    lang = request.args.get("lang", "ar")
    service.set_language(Language.ARABIC if lang == "ar" else Language.ENGLISH)
    
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    results = service.search_all(query)
    return jsonify([
        {
            "type": result.type,
            "id": result.id,
            "name": result.name,
            "name_ar": result.name_ar,
            "name_en": result.name_en
        }
        for result in results
    ])

if __name__ == "__main__":
    app.run(debug=True)

