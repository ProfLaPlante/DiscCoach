"""
Nick
SDEV 140 Final Project Example
Disc Coach takes the distance and direction from a disc golf player to the basket and suggests a disc for them to throw, 9 discs support V1.0
"""
#about 100 lines of code counting comments 

#external imports for breezy GUI and image use
from breezypythongui import EasyFrame
from tkinter import PhotoImage

#defines primary class for GUI window
class DiscCoach(EasyFrame): 

    def __init__(self):
        #frame setup  
        EasyFrame.__init__(self, title = "Disc Coach")
        self.setResizable(True);
        self.setSize(600,440)

        #Top Logo Image
        imageLabel_1 = self.addLabel(text="",row=0,column=1,sticky="NSEW")
        self.image_1 = PhotoImage(file = "Logo.png")
        imageLabel_1["image"] = self.image_1
    
        #Distance input and label
        DistLabel = self.addLabel(text = "Distance to Basket(Yards):",row = 1,column = 0,sticky ="NSEW")
        self.DistInput = self.addIntegerField(value=0,row=1,column=1,width=5, sticky ="NSEW")

        #Direction input and label
        DirLabel = self.addLabel(text = "Direction to basket:",row = 2,column = 0,sticky ="NSEW")
        self.DirInput = self.addTextField(text="none",row=2,column=1, width = 5, sticky = "NSEW")

        #Disc Image
        imageLabel_2 = self.addLabel(text="",row=3,column=1,sticky="NSEW")
        self.image_2 = PhotoImage(file = "Blank_200px.png")
        imageLabel_2["image"] = self.image_2
        
        #Label for disc
        self.DiscLabel = self.addLabel(text = "Disc Name",row = 4,column = 1,sticky ="NSEW")

        #Buttons
        Process = self.addButton(text="Process",row=5,column=0, command=self.DiscProcess)
        Reset = self.addButton(text=" Reset ",row=5,column=1,command=self.ResetApp)
        Exit = self.addButton(text="  Exit  ",row=5,column=2, command=self.QuitApp)

    """Functions for getting the correct disc"""
    #checks user input to generate 2nd half of dictionary key and validates string input for percise value
    def GetDirection(self,UserDir):

        if UserDir=="right" or UserDir=="left" or UserDir=="straight":
            if UserDir == "right":
                return "R"
            elif UserDir =="left":
                return "L"
            elif UserDir =="straight": 
                return "S"
        else:
            self.messageBox(title="ERROR", message="Direction input needs to be a string saying right,left,or straight.")       

    #checks user input to generate 1st half of dictionary key
    def GetDistance(self,UserDis):
            if UserDis < 100:
                return "S"
            elif UserDis <= 300 and UserDis >=100:
                return "M"
            else:
                return "L"     

    #combines 1st and 2nd halfs of key to index dictionary and get disc name    
    def GetDisc(self,first,second):
        
        #dictionary that holds disc(image) names with diatance and direction/abreviation as keys
        DictionaryOfDiscs = {"SL":"Warship","ML":"Evader","LL":"Sergent","SS":"Truth","MS":"Passion","LS":"Beast","SR":"Archer","MR":"Underworld","LR":"Thrasher",}
        key=first+second
        DiscName=DictionaryOfDiscs[key]
    
        return DiscName
        
    """Button Functions"""
    #high level function for processing which disc to suggest to user, with input validation for data type    
    def DiscProcess(self):

        #input validation for string distance input
        try:
            StringInput = self.DirInput.getText()
        except:
            self.messageBox(title="ERROR", message="Direction input needs to be a string saying right,left,or straight.")

        #input validation for integer distance input
        try:
            IntInput=self.DistInput.getNumber()
        except:
            self.messageBox(title="ERROR", message="Distance input needs to be a whole number(integer).")

        #uses three sub functions to process each input into part of dict. key and then get the correct disc suggestion based off key
        Direction = self.GetDirection(StringInput)
        Distance = self.GetDistance(IntInput)
        BuiltKey = self.GetDisc(Distance,Direction)

        #uses dictionary output to update GUI
        self.DiscLabel["text"] = (BuiltKey)
        self.image_2["file"] = (BuiltKey+".png")

    #resets GUI to default state
    def ResetApp(self):
        self.DiscLabel["text"] = ("Disc Name")
        self.image_2["file"] = ("Blank_200px.png")

    #Quits app
    def QuitApp(self):
        exit()
               
#Main loop    
def main():
  DiscCoach().mainloop()

if __name__ == "__main__":
  main()
