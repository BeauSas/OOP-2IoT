import aspose.words as cvrtor
from pathlib import Path

class MdToPDF:
    def __init__(self,file):
        self.file = file
    
    def convertOne(self,file):
        doc = cvrtor.Document(f"D:\\2.AP\\2e_Jaar\Python_OO_Programming\OOP-2IoT\Week_8\FilesToConvert\{file}.md") 
        doc.save(f"D:\\2.AP\\2e_Jaar\Python_OO_Programming\OOP-2IoT\Week_8\ConvertedFiles\{file}.pdf") 
    
    def convertMore(self):
        directory = cvrtor.Document("D:\\2.AP\\2e_Jaar\\Python_OO_Programming\OOP-2IoT\Week_8\FilesToConvert")
        files =  Path(directory).glob('*')
        for file in files:
            directory.save(f"D:\\2.AP\\2e_Jaar\Python_OO_Programming\OOP-2IoT\Week_8\ConvertedFiles\{file}.pdf")

theFile = input("Give the file name: ")
fileOne = MdToPDF(theFile)