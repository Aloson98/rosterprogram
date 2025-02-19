"""
Here are the data to be feed to the roster for testing
"""

#provide list of the staff names you have
staff = [
    "grayson", "weston", "patrick", "mwaisaka", "lugano", "mkumba", "martin", "beldina", "felister", "nyandaro", "dorice", "magreth",
    "joshua", "jordan", "geofrey", "hansfrida", "Mariam"
    ]

#For the starting week, provide the must have monday duties based on the ending roster
special_names = {
    "grayson": "SD",
    "lugano": "DO",
    "mkumba": "SD"
}

#automatically calculate the number of morning shift and night shift required on your roster
req_m = (len(staff) * 4) // 15
req_en = (len(staff) * 1) // 5
