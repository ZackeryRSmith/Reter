import bo_boxes

terminal = bo_boxes.init()
print("Select a version")
#selection = bo_boxes.listBox(terminal, ["Stable", "Bleeding Edge", "Nightly"], theme={"pady": 0, "bullet": "○", "bulletSelection": "●", "bulletSpacing": " ", "selectionHighlight": None, "highlightBullet": False, "selectionTextColor": None, "textColor": None, "bulletColor": None, "bulletSelectionColor": None})
selection = bo_boxes.listBox(terminal, ["Stable", "Bleeding Edge", "Nightly"])

if selection == "Stable":
    print("Okay downloading stable version")

elif selection == "Bleeding Edge":
    print("Okay downloading bleeding edge version")

elif selection == "Nightly":
    print("Okay downloading nightly version")
