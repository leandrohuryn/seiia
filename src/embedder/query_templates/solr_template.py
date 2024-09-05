"""Querys solr."""
PROD_SEI_SOLR = ("{ANATEL_SOLR_ADDRESS}/solr/{ANATEL_SOLR_CORE}/"
                 "select?q=id_prot:({id_documento})&q.op=OR&fl="
                 "id_prot,content,content_type&wt=json")
INTERNAL_SEI_SOLR = (
    "{ANATEL_SOLR_ADDRESS}/solr/{ANATEL_SOLR_CORE}/select?"
    "q=id_document:({id_documento})&q.op=OR&fl=id_document,content,"
    "id_type_document&wt=json",
)
