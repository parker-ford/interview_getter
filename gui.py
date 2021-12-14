import PySimpleGUI as sg

from gui_helpers import *
from resume_generate import create_resume
from resume_data import *
from cover_letter_generate import *

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

layout_resume.append([sg.Button("Generate Resume")])

layout_cover_letter = []

#Tab Title
layout_cover_letter.append([sg.Text("COVER LETTER", font=title_font, justification = 'center')])

#Greeting
layout_cover_letter.append([sg.Text("Greeting: " , font=subtitle_font)])
layout_cover_letter.append([sg.Radio('',"greetingRadio" , default = True, key="eGreeting0") , sg.Text("Hello ") , sg.InputText(size=(15,1), key="eGreeting0Txt") , sg.Text("Team") ] )
layout_cover_letter.append([sg.Radio('',"greetingRadio" , default = False, key="eGreeting1") , sg.Text("Dear ") , sg.InputText(size=(15,1) , key='eGreeting1Txt') , sg.Text(",") ] )
layout_cover_letter.append([sg.Radio('',"greetingRadio" , default = False, key="eGreeting2") , sg.Text("To whom it may concern ") ] )

#Intro
layout_cover_letter.append([sg.Text("Intro: " , font=subtitle_font)])
layout_cover_letter.append([sg.Text("Position: ") , sg.InputText(size=(15,1) , key="ePosition")])
layout_cover_letter.append([sg.Text("Posted On: ") , sg.InputText(size=(15,1) , key="ePostedOn")])
layout_cover_letter.append([sg.Text("My name is Parker Ford an I'm contacting you about the _____ position that was recently posted on _____.")])

#Body
layout_cover_letter.append([sg.Text("Body: " , font=subtitle_font)])
layout_cover_letter.append([sg.Text("1."), sg.Checkbox('',default=True,key="eBody1") , sg.InputText(size=(15,1) , key="eBody1-1"), sg.InputText(size=(15,1), key="eBody1-2"), sg.InputText(size=(15,1), key="eBody1-3")])
layout_cover_letter.append([sg.Text(""" I'm a highly determined and hard-working indiviual who is passionate about learning _______. 
                                    \n Along with my college experience in the subject, I have devoted much of my free-time to further 
                                    \n developing my skills in_______, which would be tranferable and valuable to someone in _______ position.""")])
layout_cover_letter.append([sg.Text("2."), sg.Checkbox('', default = True,key="eBody2")])
layout_cover_letter.append([sg.Text("""I have a background in the user experience field designing and implementing interfaces with a focus on user enjoyment and efficiency. 
\nI feel as if this experience will bring unique value to any project as I believe all products should be designed with the user in mind.""")])
layout_cover_letter.append([sg.Text("3."), sg.Checkbox('',default=True,key="eBody3") , sg.InputText(size=(15,1) , key="eBody3-1"), sg.InputText(size=(15,1), key="eBody3-2")])
layout_cover_letter.append([sg.Text("""It's important to me to work for a company that cares so much about _______. 
\nYour mission to _______is very exiting and is somthing that is deeply important to me.""")])
layout_cover_letter.append([sg.Text("4.") , sg.Checkbox('Custom:', default=False, key="ebody4"), sg.Multiline(size=(60,3))])

#Outro
layout_cover_letter.append([sg.Text("Outro: " , font=subtitle_font)])
layout_cover_letter.append([sg.Text("Position: "), sg.InputText(size=(15,1), key="eOutro")])
layout_cover_letter.append([sg.Text(""" I would love to join your team as a ________! My phone number is 425-478-8221 and my email is parker.g.ford@gmail.com \
    \nif you would like to contact me for an interview. Thank you for your time and consideration!""")])

layout_cover_letter.append([sg.Button("Generate Cover Letter")])


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
    if event == "Generate Resume":
        create_resume(values)
        print(values)
    if event == "Generate Cover Letter":
        create_cover_letter(values)
    if event == sg.WIN_CLOSED:
        break

window.close()