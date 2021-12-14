import os
import datetime

from fpdf import FPDF
from resume_data import *

h = 4
sub_size = 13
txt_size = 11.5 

class PDF(FPDF):
    pass

def add_values_inline(key, values, data, pdf, w, h, spacer, max):
    active = []
    for i in range(len(data)):
        if values[key+str(i)] == True:
            active.append(data[i])
    values_str = ""
    for i in range(len(active)):
        values_str += active[i]
        if i != len(active) - 1:
            values_str += spacer
        if i % max == 0 and i != 0:
            pdf.cell(w,h,values_str,ln=0, border = False)
            values_str = ""

    pdf.cell(w,h,values_str,ln=0, border=False)

def add_values(key, values, data, pdf, w, h):
    active = []
    for i in range(len(data)):
        if values[key+str(i)] == True:
            active.append(data[i])
    values_str = ""
    for i in range(len(active)):
        values_str += active[i]
        if i != len(active) - 1:
            values_str += " | "
 
    pdf.multi_cell(w,h,values_str, border=False)

def add_values_bulleted(key, values, data, pdf, w, h):
    for i in range(len(data)):
        if values[key+str(i)] == True:
            txt = chr(127) + "  " + data[i]
            pdf.cell(4,h,chr(127) + "  ", border=False)
            pdf.multi_cell(w,5,data[i], border=False)
            pdf.ln(0)

def add_projects(key, values, data, pdf, h):
    active = []
    for i in range(len(data)):
        if values[key+str(i)]:
            active.append(data[i])

    for i in range(len(active)):
        #Project Title
        pdf.set_font('Times', 'B', sub_size)
        pdf.cell(0,h,active[i]["name"],ln=0)
        pdf.ln(6)
        #Project Tech Used:
        pdf.set_font('Times', 'U', txt_size)
        w = pdf.get_string_width('Tech Used:') + 2
        pdf.cell(w,h,"Tech Used:")
        pdf.set_font('Times', '', txt_size)
        tech_used = ""
        for j in range(len(active[i]["tech"])):
            tech_used += active[i]["tech"][j]
            if j != len(active[i]["tech"]) - 1:
                tech_used += ' | '
        w = pdf.get_string_width(tech_used) + 2
        pdf.cell(w,h,tech_used, ln=0)
        pdf.ln(6)
        #Project Desc
        pdf.set_font('Times', '', txt_size)
        pdf.multi_cell(0,5,active[i]["desc"], ln=0)
        pdf.ln(1)
        #Project Info
        for j in range(len(active[i]["info"])):
            pdf.cell(4,h,chr(127) + "  ", border=False)
            pdf.multi_cell(0,4,active[i]["info"][j], ln=0, border=False)
            pdf.ln(1)
        pdf.ln(2)

def add_title(pdf, title):

    pdf.set_left_margin(2)
    pdf.set_right_margin(2)

    pdf.set_font('Times', 'B', sub_size + 1)
    pdf.set_fill_color(240,240,240)
    pdf.cell(0,7,title,ln=1,border=True, align='C', fill=1)
    pdf.set_fill_color(255,255,255)
    pdf.set_font('Times', '', 6)

    pdf.set_left_margin(5)
    pdf.set_right_margin(5)

def create_resume(values):

    parent_dir = "D:\Documents\Resumes"
    dir = values["eCompanyName"]
    path = os.path.join(parent_dir,dir)
    if os.path.isfile(path):
        os.mkdir(path)
    print(path)

    pdf = PDF('P' , 'mm', 'Letter')
    pdf.set_auto_page_break(auto=True, margin = 5)
    pdf.set_left_margin(5)
    pdf.set_right_margin(5)
    pdf.set_top_margin(5)
    pdf.add_page()
    #specify fontS
    #helvetica, regular weight, size 16
    pdf.set_font('Times', 'B', 22,)

    #Name
    pdf.cell(0,8, full_name, border=False, ln=1, align='C')

    #Contact Info
    pdf.set_font('Times', 'B', 8)

    contact_info1 = cell + ' | ' + email + ' | ' + area
    pdf.cell(0,5, contact_info1, border=False, ln=1, align='C')
    contact_info2 = website + ' | ' + github + ' | ' + linkedin
    pdf.cell(0,5, contact_info2, border=False, ln=1, align='C')
    pdf.cell(0,3,ln=1)


    #Professional Experience
    add_title(pdf, "Professional Experience")
    pdf.ln(4)
    pdf.set_font('Times' , 'B', sub_size)
    exp_title = values["eExperienceTitle"]
    exp_w = pdf.get_string_width(exp_title) + 2
    pdf.cell(exp_w,h, exp_title, ln=0, border = False)
    pdf.cell(3,h,' | ')
    pdf.set_font('Times' , 'U', sub_size)
    exp_w = pdf.get_string_width(experience_company) + 2
    pdf.cell(exp_w , h, experience_company)

    pdf.cell(90.5,h,"", border=False)

    pdf.set_font('Times' , 'B', sub_size)
    exp_w = pdf.get_string_width(experience_date) + 2
    pdf.cell(exp_w,h, experience_date, ln=0, border=False)

    pdf.ln(6)

    pdf.set_font('Times' , 'U', txt_size)
    w = pdf.get_string_width("Tech Used:") + 2
    pdf.cell(w,h,"Tech Used:", border = False)
    pdf.set_font('Times' , '', txt_size)
    add_values_inline("eExperienceTechUsed", values, exp_tech, pdf, 10, h, ' | ', 10)

    pdf.ln(6)

    add_values_bulleted("eExperienceInfo", values, exp_info, pdf, 0, h)
    pdf.ln(4)

    #Relevant Projects
    add_title(pdf, "Relevant Projects")
    pdf.ln(4)
    add_projects("eProjects", values, projects, pdf, h)
    pdf.ln(1)

    #Education
    #pdf.cell(0,8, "EDUCATION", border = True, ln=1, align='C')
    add_title(pdf, "Education")
    pdf.ln(4)
    education_title1 = degree  + concentration + ' | ' 
    education_title2 = school
    education_title3 = school_date
    pdf.set_font('Times' , 'B', sub_size)
    pdf.cell(pdf.get_string_width(education_title1) + 1, h , education_title1)
    pdf.set_font('Times', 'U', sub_size)
    pdf.cell(pdf.get_string_width(education_title2), h, education_title2)
    pdf.cell(20.5, w, "")
    pdf.set_font('Times' , 'B', sub_size)
    pdf.cell(pdf.get_string_width(education_title3) + 2, h, education_title3, border=False)
    pdf.set_font('Times' , '', txt_size)
    pdf.ln(6)
    pdf.set_font('Times', 'U', txt_size)
    pdf.cell(pdf.get_string_width("Minor: "), 4, "Minor: ")
    pdf.set_font('Times', '', txt_size)
    pdf.cell(pdf.get_string_width(minor), 4, minor)
    pdf.ln(5)
    pdf.set_font('Times' , 'U', txt_size)
    pdf.cell(pdf.get_string_width("Relevant Coursework:"), 5, "Relevant Coursework:")
    pdf.ln(0)
    pdf.set_font('Times' , '', txt_size)
    add_values("eCoursework", values, coursework, pdf, 180, 5)
    pdf.ln(6)

    #Skills
    #pdf.cell(0,8, "SKILLS", border = True, ln=1, align='C')
    add_title(pdf, "Skills")
    pdf.ln(4)
    pdf.set_font('Times', '', txt_size)
    add_values("eSkills", values, skills, pdf, 180, 5,)
    if pdf.page > 1:
        print("WARNING: Resume over 1 page")
    
    dt = datetime.datetime.today()
    filename = "Resume_" + values["eCompanyName"] + "_" + str(dt.month) + "_" + str(dt.day) + "_" + str(dt.year) + ".pdf"

    filepath = os.path.join(path,filename)

    pdf.output(filepath)
    os.startfile(path)


