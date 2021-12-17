import bo_boxes

cursor = bo_boxes.Cursor(0, 0)
#selection = bo_boxes.listBox(cursor, ["Stable", "Bleeding Edge", "Nightly"], {"pady": 0, "bullet": "○", "bulletSelection": "●", "bulletSpacing": " ", "selectionHighlight": None, "highlightBullet": False, "selectionTextColor": None, "textColor": None, "bulletColor": None, "bulletSelectionColor": None})
selection = bo_boxes.listBox(cursor, ["Stable", "Bleeding Edge", "Nightly"])

if selection == "Stable":
    print("Okay downloading stable version")

elif selection == "Bleeding Edge":
    print("Okay downloading bleeding edge version")

elif selection == "Nightly":
    print("Okay downloading nightly version")
    
