import os
from datetime import date
import datetime
from fpdf import FPDF

h = 6
font = 'Times'
font_size = 12


class PDF(FPDF):
    pass


def get_greeting(values):
    greeting_str = ""
    for i in range(3):
        if values["eGreeting"+str(i)] == True:
            if i == 0:
                greeting_str += "Hello "
                greeting_str += values["eGreeting0Txt"]
                greeting_str += " team,"
            elif i ==1:
                greeting_str += "Dear "
                greeting_str += values["eGreeting1Txt"]
                greeting_str += ","
            else:
                greeting_str += "To whom it may concern,"

    return greeting_str

def get_intro(values):
    intro_str = ""
    intro_str += "My name is Parker Ford and I'm contacting you about the "
    intro_str += values["ePosition"]
    intro_str += " position that was recently posted on "
    intro_str += values["ePostedOn"]
    intro_str += "."

    return intro_str


def get_body(values):
    body_text = ""
    for i in range(4):
        if values["eBody"+ str(i+1)] == True:
            if i == 0:
                body_text += "I'm a highly determined and hard-working individual who is passionate about learning "
                body_text += values["eBody1-1"]
                body_text += ". Along with my college experience in the subject, I have devoted much of my free-time to further developing my skills in "
                body_text += values["eBody1-2"]
                body_text += ", which would be transferable  and valuable to someone in "
                body_text += values["eBody1-3"]
                body_text += " position."
            elif i == 1:
                body_text += " I have a background in the user experience field designing and implementing interfaces with a focus on user enjoyment and efficiency. I feel as if this experience will bring unique value to any project as I believe all products should be designed with the user in mind."
            elif i == 2:
                body_text += " It's important to me to work for a company that cares so much about "
                body_text += values["eBody3-1"]
                body_text += ". Your mission to "
                body_text += values["eBody3-2"]
                body_text += " is very exciting and is something that is deeply important to me."
            elif i == 3:
                print(values["eBody4-1"])
                body_text += values["eBody4-1"]

    return body_text 

def get_outro(values):
    outro_text = ""
    outro_text += "I would love to join your team as a "
    outro_text += values["eOutro"].strip()
    outro_text += "! My phone number is 425-478-8221 and my email is parker.g.ford@gmail.com if you would like to contact me for an interview. Thank you for your time and consideration!"
    return outro_text        

def create_cover_letter(values):

    parent_dir = "D:\Documents\Resumes"
    dir = values["eCompanyName"]
    path = os.path.join(parent_dir,dir)
    if os.path.isfile(path):
        os.mkdir(path)

    pdf = PDF('P' , 'mm', 'Letter')
    pdf.set_auto_page_break(auto=True, margin = 5)
    pdf.set_left_margin(25)
    pdf.set_right_margin(25)
    pdf.set_top_margin(30)
    pdf.add_page()
    pdf.set_font(font, '', font_size)

    #Date
    today = date.today()
    date_txt = today.strftime("%B %d, %Y")
    pdf.cell(0, h, str(date_txt))
    pdf.ln(40)

    #Greeting
    greeting = get_greeting(values)
    pdf.multi_cell(0, h, greeting)
    pdf.ln(5)

    pdf.set_left_margin(45)
    pdf.set_right_margin(45)

    #Intro
    intro = get_intro(values)
    pdf.multi_cell(0, h, intro)
    pdf.ln(5)

    #Body
    body = get_body(values)
    pdf.multi_cell(0,h, body)
    pdf.ln(5)

    #Outro
    outro = get_outro(values).strip()
    #pdf.multi_cell(0,h,"I would love to join your team as a Technical Game Designer! My phone number is 4254788221 and my email is parker.g.ford@gmail.com if you would like to contact me for an interview. Thank you for your time and consideration!", border=True)
    pdf.multi_cell(0,h, outro, border=False)
    pdf.ln(5)

    pdf.multi_cell(0,h+2,"-Parker Ford")

    dt = datetime.datetime.today()
    filename = "Cover_Letter_" + values["eCompanyName"] + "_" + str(dt.month) + "_" + str(dt.day) + "_" + str(dt.year) + ".pdf"
    filepath = os.path.join(path,filename)

    pdf.output(filepath)
    print("output done")