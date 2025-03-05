class Room:
    def __init__(self, room_number, room_type, price, amenities):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.amenities = amenities  # List of amenities (e.g., Wi-Fi, air conditioning)
    def __repr__(self):
        return f"Room {self.room_number}: {self.room_type}, Price: ${self.price},      Amenities: {', '.join(self.amenities)}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []  # List to store available rooms

    def add_room(self, room):
        self.rooms.append(room)

    def get_available_rooms(self):
        return self.rooms

class Customer:
    def __init__(self, budget, preferred_room_type, required_amenities):
        self.budget = budget
        self.preferred_room_type = preferred_room_type
        self.required_amenities = required_amenities

    def filter_rooms(self, rooms):
        matching_rooms = [
            room for room in rooms
            if room.price <= self.budget
            and (self.preferred_room_type.lower() in room.room_type.lower() or self.preferred_room_type == "")
            and all(amenity in room.amenities for amenity in self.required_amenities)
        ]
        return matching_rooms

    def offer_room(self, hotel):
        available_rooms = hotel.get_available_rooms()
        filtered_rooms = self.filter_rooms(available_rooms)
        if not filtered_rooms:
            print("No rooms match your criteria. Please adjust your preferences.")
        else:
            print(f"\nHere are the rooms that match your preferences (Price <= ${self.budget}, Preferred Room Type: {self.preferred_room_type}, Amenities: {', '.join(self.required_amenities)}):")
            for room in filtered_rooms:
                print(room)
