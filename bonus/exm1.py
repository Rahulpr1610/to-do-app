contents = ['apple catched by a boy ','mobile phone is waste of time ','hi im rahul ']
filenames = ['dox.txt','presentation.txt','report.txt']

for content,filename in zip(contents,filenames):
    file = open( f"../files/{filename}",'w')
    file.write(content)
