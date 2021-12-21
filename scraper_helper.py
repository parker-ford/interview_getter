include_desc_search_terms = [
    ["entry", "software", "engineer"],
    ["software", "development"],
    ["software", "programming"],
    ["technical", "artist"],
    ["graphic", "engineer"],
    [" unity"],
    ["hlsl"],
    ["glsl"],
    ["shader"],
    ["three", "js"],
    ["new" , "grad", "software", "engineer"],
    ["new", "grad" , "computer", "science"],
    ["opengl"],
]

inlcude_title_search_terms = [
    ["software", "engineer"],
    ["technical", "artist"],
    ["associate"]
]

exclude_desc_search_terms = [
    ["4+ years"],
    ["5+ years"],
    ["5 years"],
    ["6+ years"],
    ["6 years"],
    ["7+ years"],
    ["7 years"],
    ["8+ years"],
    ["8 years"],
    ["9+ years"],
    ["9 years"],
    ["10+ years"],
    ["10 years"],
    ["ios development"],
    ["php"]
]

exclude_title_search_terms = [
    ["senior"],
    ["sr."],
    ["mobile"],
    ["android"],
    ["qa"],
    ["cloud"],
    ["ii"],
    ["ios"],
    ["test"],
    ["lead"],
    ["flutter"]
]

exclude_company_search_terms = [
    ["amazon"]
]

def search_job(job,link_set , f):

    

    desc = job["description"]
    title = job["title"]
    link = job["URL"]
    company = job["company"]
    if link in link_set:
        f.write(title + " was in link set\n")
        f.write(link + "\n")
        f.write("===================================\n")
        return False

    for term in exclude_desc_search_terms:
        search = True
        for item in term:
            search = search and item in desc.lower()
        if search == True:
            f.write(title + " had term " + term[0] + " in description\n")
            f.write(link + "\n")
            f.write("===================================\n")
            return False

    for term in exclude_title_search_terms:
        search = True
        for item in term:
            search = search and item in title.lower()
        if search == True:
            f.write(title + " had term " + term[0] + " in title")
            f.write(link + "\n")
            f.write("===================================\n")
            return False
    
    for term in exclude_company_search_terms:
        search = True
        for item in term:
            search = search and item in company.lower()
        if search == True:
            f.write("company was amazon LOL \n")
            f.write("===================================\n")
            return False

    for term in inlcude_title_search_terms:
        search = True
        for item in term:
            search = search and item in title.lower()
        if search == True:
            return True

    for term in include_desc_search_terms:
        search = True
        for item in term:
            search = search and item in desc.lower()
        if search == True:
            return True

    f.write(title + " did not have any include terms in descriptions")
    f.write(link + "\n")
    f.write("===================================\n")

    return False


def search_title(job):

    title = job

    
    
    for term in exclude_title_search_terms:
        search = True
        for item in term:
            search = search and item in title.lower()
        if search == True:
            return False

    return True

def create_job(title, company, description, url):
    job = {
        'title' : title,
        'company' : company,
        'description' : description,
        'URL' : url
    }

    return job



"""
Scrape Ideas:

Boards:
Hitmarker
angel list
builtinseattle

companies:
-- gaming --
- bio ware: https://www.bioware.com/careers/
wizareds of the coast: https://company.wizards.com/en/careers 
geocaching: https://www.geocaching.com/careers
bungie: https://careers.bungie.com/jobs
twitch: https://www.twitch.tv/jobs/careers/?location=seattle-wa
rainway: https://www.notion.so/rainway/Work-at-Rainway-d8bc37380f484b9a8ec48ba209dbf805#b2187bc6b59b4dafaedac0274c0ef94c https://www.notion.so/Code-Challenges-f1bc61fecf754d06be253ad4300e565a
flowplay: https://www.flowplay.com/contact
runic games: https://www.runicgames.com/careers/
arena net: https://www.arena.net/en/careers#listings
big fish games: https://careers.aristocrat.com/aristocratdigital/au/en/big-fish-jobs
harebrained schemes: https://harebrained-schemes.com/careers/
probably monsters: https://www.probablymonsters.com/careers/
tenacious entertainment: https://tenaciousentertainment.com/careers/#careers
starform: https://starform.co/careers
undeadlabs: https://undeadlabs.com/jobs/
lightfox games: https://www.lightfoxgames.com/careers
rec room: https://recroom.com/careers#openings
cat daddy games: https://boards.greenhouse.io/catdaddy
niantic: https://careers.nianticlabs.com/openings/?office=seattle-area-bellevue-wa#positions
keywords studios: https://www.keywordsstudios.com/careers/
leaftail labs: https://www.leaftaillabs.com/careers
ncsoft: https://us.ncsoft.com/en-us/careers?sort=location#all
suckerpunch: https://jobs.suckerpunch.com/?host=jobs.suckerpunch.com
hopoo games: https://hopoogames.com/jobs-at-hopoo-games/
play every ware: https://www.playeveryware.com/careers
theory craft games: https://www.theorycraftgames.com/careers
gamesight: https://angel.co/company/gamesight/jobs
valve: https://www.valvesoftware.com/en/?job_cat=software-engineering
-mythical games: https://mythicalgames.com/careers

--startups--


--completed--:
unity: https://careers.unity.com/location/bellevue
epic games: https://www.epicgames.com/site/en-US/careers/jobs?country=United%20States&state=Washington&page=1
double down interactive: https://www.doubledowninteractive.com/jobs/
343 industries: https://www.343industries.com/careers
pokemon: https://boards.greenhouse.io/pokemoncareers
intercept games: https://www.interceptgames.com/#jobs

"""