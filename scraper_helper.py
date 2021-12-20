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



"""
Scrape Ideas:

Boards:
Hitmarker
angel list
builtinseattle

companies:
bio ware: https://www.bioware.com/careers/
unity: https://careers.unity.com/location/bellevue
double down interactive: https://www.doubledowninteractive.com/jobs/
pokemon: https://boards.greenhouse.io/pokemoncareers
intercept games: https://www.interceptgames.com/#jobs
wizareds of the coast: https://company.wizards.com/en/careers 
geocaching: https://www.geocaching.com/careers
bungie: https://careers.bungie.com/jobs
twitch: https://www.twitch.tv/jobs/careers/?location=seattle-wa
rainway: https://www.notion.so/rainway/Work-at-Rainway-d8bc37380f484b9a8ec48ba209dbf805#b2187bc6b59b4dafaedac0274c0ef94c https://www.notion.so/Code-Challenges-f1bc61fecf754d06be253ad4300e565a
flowplay: https://www.flowplay.com/contact
runic games: https://www.runicgames.com/careers/


"""