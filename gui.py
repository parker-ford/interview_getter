import PySimpleGUI as sg
from arenanet_scraper import scrape_arenanet
from bungie_scraper import scrape_bungie
from doubledown_scraper import scrape_doubledown
from epic_games_scraper import scrape_epic_games
from geocahing_scraper import scrape_geocaching

from gui_helpers import *
from hair_brained_schemes_scraper import scrape_hair_brained_schemes
from hitmarker_scraper import scrape_hitmarker
from intercept_games_scraper import scrape_intercept_games
from pokemon_scraper import scrape_pokemon
from resume_generate import create_resume
from resume_data import *
from cover_letter_generate import *
# from indeed_scraper import *
import webbrowser
from linkedin_scraper import *
from suckerpunch_scraper import scrape_suckerpunch
from unity_scraper import scrape_unity
from three43_industries_scraper import *
from wizards_of_the_coast_scraper import scrape_wizards_of_the_coast

title_font = ("Arial 18 bold")
subtitle_font = ("Arial 10 bold underline")
big_title_font = ("Arial 28 bold")

job_list_linkedin = []
job_list_hitmarker = []

job_list_unity = []
job_list_epic_games = []
job_list_doubledown = []
job_list_343_industries = []
job_list_pokemon = []
job_list_intercept_games = []
job_list_wizards_of_the_coast = []
job_list_bungie = []
job_list_arenanet = []
job_list_suckerpunch = []
job_list_geocaching = []
job_list_hair_brained_schemes = []

def make_resume_layout():

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

    return layout_resume

def make_cover_letter_layout():
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
    layout_cover_letter.append([sg.Text("4.") , sg.Checkbox('Custom:', default=False, key="eBody4"), sg.Multiline(size=(60,3), key="eBody4-1")])

    #Outro
    layout_cover_letter.append([sg.Text("Outro: " , font=subtitle_font)])
    layout_cover_letter.append([sg.Text("Position: "), sg.InputText(size=(15,1), key="eOutro")])
    layout_cover_letter.append([sg.Text(""" I would love to join your team as a ________! My phone number is 425-478-8221 and my email is parker.g.ford@gmail.com \
        \nif you would like to contact me for an interview. Thank you for your time and consideration!""")])

    layout_cover_letter.append([sg.Button("Generate Cover Letter")])

    return layout_cover_letter


# layout_web_scraper = []
# for i in range(20):
#     layout_web_scraper.append([sg.Checkbox("Test",default=True)])


def scraper_layout_helper(name, job_list, scraper_layout):
    if len(job_list) > 0:
        scraper_layout.append([sg.Text(name, font=big_title_font)])
    i = 0
    for job in job_list:
        scraper_layout.append([sg.Checkbox(job["title"] + ' | ' + job["company"], default=False, key="eLink"+name+(str(i)))])
        i = i+1


def make_scraper_layout():
    scraper_layout = []
    #i = 0
    scraper_layout_helper("Unity", job_list_unity, scraper_layout)
    scraper_layout_helper("Epic Games", job_list_epic_games, scraper_layout)
    scraper_layout_helper("Doubledown Interactive", job_list_doubledown, scraper_layout)
    scraper_layout_helper("343 Industries", job_list_343_industries, scraper_layout)
    scraper_layout_helper("Pokemon", job_list_pokemon, scraper_layout)
    scraper_layout_helper("Intercept Games", job_list_intercept_games, scraper_layout)
    scraper_layout_helper("Wizards of the Coast", job_list_wizards_of_the_coast, scraper_layout)
    scraper_layout_helper("Bungie", job_list_bungie, scraper_layout)
    scraper_layout_helper("Arenanet", job_list_arenanet, scraper_layout)
    scraper_layout_helper("Suckerpunch", job_list_suckerpunch, scraper_layout)
    scraper_layout_helper('Geocaching', job_list_geocaching, scraper_layout)
    scraper_layout_helper('Hair Brained Schemes', job_list_hair_brained_schemes, scraper_layout)

    scraper_layout_helper("Linkedin", job_list_linkedin, scraper_layout)
    scraper_layout_helper('Hitmarker', job_list_hitmarker, scraper_layout)

    return scraper_layout

def open_tabs_helper(job_list, name):
    for i in range(len(job_list)):
            if(values["eLink"  +  name + str(i)]) == True:
                webbrowser.open_new(job_list[i]["URL"])
                time.sleep(.5)

def make_tab_grp():
    tabgrp = [
            [sg.TabGroup(
                            [
                                [
                                    sg.Tab('Web Scraper', [[sg.Column(make_scraper_layout(), size=(1100,750), scrollable=True, key="links")],[sg.Button("Scrape"), sg.Button("Open Tabs"), sg.Button("Print Data")]]),
                                    sg.Tab('Resume', make_resume_layout(), border_width =10),
                                    sg.Tab('Cover Letter', make_cover_letter_layout()),
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

    return tabgrp  


window = sg.Window("Interview Getter", make_tab_grp())
print(make_tab_grp())
# sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()


while True:
    event, values = window.read()
    if event == "Generate Resume":
        create_resume(values)
    if event == "Generate Cover Letter":
        create_cover_letter(values)
    if event == "Scrape":
        # job_list_unity = scrape_unity()
        # job_list_epic_games = scrape_epic_games()
        # job_list_doubledown = scrape_doubledown()
        # job_list_343_industries = scrape_343_industries()
        # job_list_pokemon = scrape_pokemon()
        # job_list_intercept_games = scrape_intercept_games()
        # job_list_wizards_of_the_coast = scrape_wizards_of_the_coast()
        # job_list_bungie = scrape_bungie()
        # job_list_arenanet = scrape_arenanet()
        # job_list_suckerpunch = scrape_suckerpunch()
        # job_list_geocaching = scrape_geocaching()
        job_list_hair_brained_schemes = scrape_hair_brained_schemes()

        #job_list_linkedin = scrape_linkedin()
        #job_list_hitmarker = scrape_hitmarker()

        layout = [make_tab_grp()]
        window1 = sg.Window("Interview Getter", layout)
        window.Close()
        window = window1
    if event == "Open Tabs":

        #TODO: MAKE THIS INTO A FUNCTION
        # for i in range(len(job_list_linkedin)):
        #     if(values["eLink"  + str(i)]) == True:
        #         webbrowser.open_new(job_list_linkedin[i]["URL"])

        # for i in range(len(job_list_unity)):
        #     if(values["eLink" + str(i)]) == True:
        #         webbrowser.open_new(job_list_unity[i]["URL"])
        open_tabs_helper(job_list_linkedin, "Linkedin")
        open_tabs_helper(job_list_unity, "Unity")
        open_tabs_helper(job_list_epic_games, "Epic Games")
        open_tabs_helper(job_list_doubledown, "Doubledown Interactive")
        open_tabs_helper(job_list_343_industries, "343 Industries")
        open_tabs_helper(job_list_pokemon, "Pokemon")
        open_tabs_helper(job_list_intercept_games, "Intercept Games")
        open_tabs_helper(job_list_wizards_of_the_coast, "Wizards of the Coast")
        open_tabs_helper(job_list_bungie, "Bungie")
        open_tabs_helper(job_list_arenanet, "Arenanet")
        open_tabs_helper(job_list_suckerpunch, "Suckerpunch")
        open_tabs_helper(job_list_hitmarker, 'Hitmarker')
        open_tabs_helper(job_list_geocaching, "Geocaching")
        open_tabs_helper(job_list_hair_brained_schemes, "Hair Brained Schemes")
    if event == "Print Data":
        print("JOB DATA:")
        for job in job_list_linkedin:
            print("Title: " + job["title"])
            print("Company: " + job["company"])
            print("URL: " + job["URL"])
            print("Desc: " + job["desc"][0:50])
            print("\n")
    if event == sg.WIN_CLOSED:
        break

window.close()