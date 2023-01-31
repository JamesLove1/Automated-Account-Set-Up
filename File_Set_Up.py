# %%
import json 
import os 
from framwork.CV_Framwork_v5 import CV_Framwork_v5 as cv
from framwork.Cover_Letter_Tech_v1 import v1_Cover_Letter_Tech_James_Love_Cover_Letter as cover_letter
from docx2pdf import convert

#%%
#collect company info 
company_info = {}
company_info["company_name"] = input("Company Name: ")
company_info["position"] = input("Position: ") 
company_info["file_path"] = os.getcwd() + "/" + company_info["company_name"]
# %%
# Creat New Folder
os.mkdir(company_info["company_name"])
# %%
#Write JSON file
if os.getcwd() != company_info["company_name"]:
    os.chdir(company_info["company_name"])

jsondump = json.dumps(company_info)

with open("jsonfile.json", "w") as jsonfile:
    jsonfile.write(jsondump)

if os.getcwd() != company_info["company_name"]:
    os.chdir("../")
    #print(os.getcwd())
# %%
#Read JSON file
if os.getcwd() != company_info["company_name"]:
    os.chdir(company_info["company_name"])

with open("jsonfile.json") as jsonfile:
    data= json.load(jsonfile)

if os.getcwd() != company_info["company_name"]:
    os.chdir("../")
    #print(os.getcwd())
#Notes 
#https://www.geeksforgeeks.org/read-json-file-using-python/
# %%
os.chdir(company_info["file_path"])
print(os.getcwd())

cv.cv_to_pdf("./"+company_info["company_name"]+"- James Love Cover Letter.pdf")

os.chdir(r"D:/SynologyDrive/Projects/1.  Employment - Projects/Job Hunt/Industrys/Tech Job Hunt/Applications & Interviews/framwork/Cover_Letter_Tech_v1")

cover_letter.letterOne(company_info["company_name"],company_info["position"], "v1 Cover Letter Tech - James Love Cover Letter.docx",company_info["file_path"])

os.chdir(company_info["file_path"])
convert((company_info["company_name"]+" - James Love Cover Letter.docx"), "./")
# %%
