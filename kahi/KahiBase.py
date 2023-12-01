
class KahiBase:
    def __init__(self):
        pass

    def empty_affiliation(self):
        entry = {
            "updated": [],
            "names": [],
            "aliases": [],
            "abbreviations": [],
            "types": [],
            "year_established": None,
            "status": [],
            "relations": [],
            "addresses": [],
            "external_urls": [],
            "external_ids": [],
            "subjects": [],
            "ranking": [],
            "description": []
        }
        return entry

    def empty_source(self):
        return {
            "updated": [],
            "names": [],
            "abbreviations": [],
            "types": [],
            "keywords": [],
            "languages": [],
            "publisher": "",
            "relations": [],
            "addresses": [],
            "external_ids": [],
            "external_urls": [],
            "review_processes": [],
            "waiver": {},
            "plagiarism_detection": False,
            "open_access_start_year": None,
            "publication_time_weeks": None,
            "apc": {},
            "copyright": {},
            "licenses": [],
            "subjects": [],
            "ranking": []
        }

    def empty_subjects(self):
        return {
            "updated": [],
            "names": [],
            "abbreviations": [],
            "descriptions": [],
            "external_ids": [],
            "external_urls": [],
            "level": None,
            "relations": []
        }

    def empty_person(self):
        entry = {
            "updated": [],
            "full_name": "",
            "first_names": [],
            "last_names": [],
            "initials": "",
            "aliases": [],
            "affiliations": [],
            "keywords": [],
            "external_ids": [],
            "sex": "",
            "marital_status": None,
            "ranking": [],
            "birthplace": {},
            "birthdate": -1,
            "degrees": [],
            "subjects": []
        }
        return entry

    def empty_work(self):
        return {
            "titles": [],
            "updated": [],
            "subtitle": "",
            "abstract": "",
            "keywords": [],
            "types": [],
            "external_ids": [],
            "external_urls": [],
            "date_published": None,
            "year_published": None,
            "bibliographic_info": {},
            "references_count": None,
            "references": [],
            "citations_count": [],
            "citations": [],
            "author_count": None,
            "authors": [],
            "source": {},
            "ranking": [],
            "subjects": [],
            "citations_by_year": []
        }

    def empty_mobility(self):
        return {
            "updated": "",
            "year": "",
            "semester": "",
            "via": "",
            "modality": "",
            "category": "",
            "start_date": "",
            "end_date": "",
            "duration": "",
            "document_type": "",
            "document": "",
            "birth_date": "",
            "first_name" : "",
            "second_name" : "",
            "first_surname" : "",
            "second_surname" : "",
            "nationality" : [],
            "email" : "",
            "migration_status" : {},
            "country": [],
            "dependency" : "",
            "program" : "",
            "group" : "",
            "mobility_type_id" : "",
            "mobility_type" : "",
            "student_category" : "",
            "institution" : "",
            "campus" : "",
            "mobility_by_agreement" : "",
            "agreement_code" : "",
            "national_financing_id" : "",
            "source_national_financing" : "",
            "national_funding_value" : "",
            "international_funding_id" : "",
            "international_funding_source" : "",
            "other_international_funding_source" : "",
            "international_financing_source_value" : "",
            "international_financing_country" : {},  
        }
    
    def empty_agreement(self):
        return {
            "updated": "",
            "scope": "",
            "agreement_code": "",
            "internal_institution": "",
            "external_institution": "",
            "modality": "",
            "categories": "",
            "abstract": "",
            "renovation": "",
            "signatory": "",
            "signing_date": "",
            "signing_year": "",
            "expiration_date": "",
            "language": "",
            "remarks": "",
            "exemption": "",
            "physical_file": "",
            "current_agreement_link": "",
            "previous_agreements_link": "",
            "international_shipping_data": "",
            "remarks": "",
            "documentary_transfer": ""
        }
    
    def run(self):
        """
        entry point for the execution of the plugin, this method must be implemented
        """
        raise NotImplementedError(
            self.__class__.__name__ + '.run() not implemented')
