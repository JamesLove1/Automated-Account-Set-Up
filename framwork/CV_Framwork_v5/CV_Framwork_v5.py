from docx2pdf import convert

#destination_folder = "./" + input("Destination Folder:")
#company_name = "/" + input("Company Name:") + " - James Love CV.pdf"

def cv_to_pdf( destination):
    return convert(r"D:/SynologyDrive/Projects/1.  Employment - Projects/Job Hunt/Industrys/Tech Job Hunt\Applications & Interviews/framwork/CV_Framwork_v5/Tech - James Love CV.docx",  destination)