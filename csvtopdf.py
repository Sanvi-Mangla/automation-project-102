import tabula
file_name="file.pdf"
df=tabula.read_pdf(file_name,encoding="utf-8",spreadsheet=True,pages="1")
df.to_csv("file.csv")