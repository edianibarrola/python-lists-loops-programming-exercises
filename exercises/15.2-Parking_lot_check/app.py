parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]
slots = { "total_slots": 0, "available_slots": 0, "occupied_slots": 0}
#Your code go here:
def get_parking_lot(lot):
    for row_of_spots in lot:
        
        for spot in row_of_spots:

            if spot != 0:
                slots["total_slots"] += 1
                if spot == 1:
                    slots["occupied_slots"] += 1
                if spot == 2:
                    slots["available_slots"] += 1




    return slots

print(get_parking_lot(parking_state))
