import PySimpleGUI as sg

def add_checkbox(data, box_key, layout, newline, stop_check):
    checkboxes = []
    if newline == 1:
        for i in range(len(data)):
            if i < stop_check:
                checkboxes.append(sg.Checkbox(data[i] , default = True, key=box_key + str(i)))
            else:
                checkboxes.append(sg.Checkbox(data[i] , default = False, key=box_key + str(i)))
            layout.append(checkboxes)
            checkboxes = []
        layout.append (checkboxes)
    else:
        for i in range(len(data)):
            if i < stop_check:
                checkboxes.append(sg.Checkbox(data[i] , default = True, key=box_key + str(i)))
            else:
                checkboxes.append(sg.Checkbox(data[i] , default = False, key=box_key + str(i)))
            if i % newline == 0 and i != 0:
                layout.append(checkboxes)
                checkboxes = []
        layout.append (checkboxes)


