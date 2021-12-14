import PySimpleGUI as sg

from gui_helpers import *
from resume_generate import create_resume
from resume_data import *

title_font = ("Arial 18 bold")
subtitle_font = ("Arial 10 bold underline")

layout_resume = []

#Tab Title
layout_resume.append([sg.Text("RESUME", font=title_font, justification = 'center')])

#Experience Title
layout_resume.append([sg.Text("Experience Title: " , font=subtitle_font)])
layout_resume.append([sg.InputText('User Experience Intern', key='eExperienceTitle')])

#Experience Technology Used
layout_resume.append([sg.Text("Experince Technology Used:",  font=subtitle_font)])
add_checkbox(exp_tech, 'eExperienceTechUsed', layout_resume, 5, 5)

#Experience Info
layout_resume.append([sg.Text("Experience Info:", font=subtitle_font)])
add_checkbox(exp_info, 'eExperienceInfo', layout_resume, 1, 3)

#Projects
layout_resume.append([sg.Text("Projects:", font=subtitle_font)])
add_checkbox(project_names, 'eProjects', layout_resume, 1, 3)

#Coursework
layout_resume.append([sg.Text("Coursework:", font=subtitle_font)])
add_checkbox(coursework, 'eCoursework', layout_resume, 6, 15)

#Skills
layout_resume.append([sg.Text("Skills:", font=subtitle_font)])
add_checkbox(skills, 'eSkills', layout_resume, 8, 6)

layout_resume.append([sg.Button("Generate")])



layout_cover_letter = [
    [sg.Text("Cover Letter")]
]

tabgrp = [
            [sg.TabGroup(
                            [
                                [
                                    sg.Tab('Resume', layout_resume, border_width =10),
                                    sg.Tab('Cover Letter', layout_cover_letter),
                                ]
                            ],
                            tab_location='centertop',
                            # title_color='Red', tab_background_color='Purple',selected_title_color='Green',
                            # selected_background_color='Gray', border_width=5
                       ), 
                       
                       
                       sg.Text('Company Name'),

                       sg.InputText('', key='eCompanyName', size=(20,1))
            ]
        ]  




window = sg.Window("Demo", tabgrp)

# sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()

while True:
    event, values = window.read()
    if event == "Generate":
        create_resume(values)
    if event == sg.WIN_CLOSED:
        break

window.close()