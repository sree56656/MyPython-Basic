import PyPDF2

# # open pdf with permission
# f = open("Working_Business_Proposal.pdf", 'rb')
#
# # read pdf
# pdf_reader = PyPDF2.PdfFileReader(f)
# print(pdf_reader.numPages)
# # access required page
# page_one = pdf_reader.getPage(0)
# # extract text from page
# page_one_text = page_one.extractText()
# print(page_one_text)
#
# # add pages to pdf
#
# #  close file
# f.close()

# Example
f = open("Working_Business_Proposal.pdf", 'rb')
page_reader = PyPDF2.PdfFileReader(f)

pdf_text = []
for num in range(page_reader.numPages):
    page = page_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[0])


