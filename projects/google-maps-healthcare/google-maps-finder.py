import googlemaps



gmaps = googlemaps.Client(key='PUT_YOUR_OWN_API_KEY_HERE')

hospital = input("Hi! It looks like you need medical attention. Is it an emergency? ")
if hospital == "yes":
    highest_rating = 0
    hospital = ""
    hospital_address = ""
    for place in gmaps.places(query="hospital", type="hospital").get("results"):
        if int(place.get("rating")) > highest_rating:
            hospital = place.get("name")
            hospital_address = place.get("formatted_address")
            highest_rating = place.get("rating")
    print("Here is the name and address of the hospital near you with the highest rating:")
    print(hospital)
    print(hospital_address)

else:
    dentist = input("It sounds like it is not an emergency. Do you need dental or primary care? ")
    if dentist == "dental":
        highest_rating = 0
        dental_practice = ""
        dental_address = ""
        for place in gmaps.places(query="dentist", type="dentist").get("results"):
            if place.get("rating") > highest_rating:
                dental_practice = place.get("name")
                dental_address = place.get("formatted_address")
                highest_rating = place.get("rating")
        print("Here is the name and address of the dental practice near you with the highest rating:")
        print(dental_practice)
        print(dental_address)

    else:
        highest_rating = 0
        doctor_practice = ""
        doctor_address = ""
        for place in gmaps.places(query="doctor", type="doctor").get("results"):
            if place.get("rating") > highest_rating:
                doctor_practice = place.get("name")
                doctor_address = place.get("formatted_address")
                highest_rating = place.get("rating")
        print("Here is the name and address of the doctor practice near you with the highest rating:")
        print(doctor_practice)
        print(doctor_address)

