from pypdf import PdfReader

reader = PdfReader('knowledge.pdf')

# print(reader.pages[0].extract_text())
data = ""

for page in reader.pages:
    data = data + page.extract_text()

print(f"Total words in pdf : {len(data)}")
print('\n\n')

print(data[:1000])
print('\n\n')
print('Next chunk')
print('\n\n')
print(data[900:1900])