#Imports all of the predefined modules 
from tkinter import *
from tkinter.font import Font
import random
import time
import linecache
import threading
import os
from tkinter import messagebox

#This class is used to set up the initial shape
class ShapeSetup:
    def __init__(self,Coordinates, xy):
        #The coordinates required for the shape to be generated are set here
        self.x1=xy
        self.y1=xy
        self.Coordinates=Coordinates
        self.Coordinates2=[]
        self.Coordinates3=[]
        #The placeholder remembers the Coordinates before a transformation so that the shape can be loaded as default
        self.CoordinatesPlaceholder=Coordinates
        self.ShapeType="Shape"

#This class is used to store the window size
class SizeOfWindow:
    def __init__(self):
        #This gets and stores the window size
        self.WindowHeight=root.winfo_height()
        self.WindowWidth=root.winfo_width()

#This class stores a number that will be added to the coordinates to move the shape to vary the questions
class ClassForRotation:
    def __init__(self):
        self.RandomNumberX=2
        self.RandomNumberY=2

#This class stores the text box which is the text widget
class TextBoxClass:
    def __init__(self):
        self.TextBox=""



#This class will remember whether the answer button has been pressed since the new question button was pressed
class QuestionAnswerClass:
    def __init__(self):
        self.QuestionAnswerShown=""

#This class will be used to store the sizes of the widgets as they will change when the window size changes
class ButtonSizes:
    def __init__(self):
        #This sets up the initial widget sizes based on the window size
        self.ButtonHeight=WindowSize.WindowHeight//150
        self.ButtonWidth=WindowSize.WindowWidth//50
        self.PaddingX=WindowSize.WindowWidth//100
        self.PaddingY=WindowSize.WindowHeight//200
        self.FontSize=WindowSize.WindowHeight//70

#This class is used to save widgets that will need to be destroyed
class ThingsToDestroy:
    def __init__(self):
        self.DropDown=""
        self.Button=""

#This class will be used to save the widgets that change to display help
class CheckButtonClass:
    def __init__(self):
        self.CB1=""
        self.CB2=""
        self.CB3=""
        self.CB4=""
        self.CB5=""
        self.CB6=""
        self.CB7=""
        self.Testing=""
        self.ShowShape=""
        self.HideShape=""
        self.NewQuestion=""
        self.Answer=""
        self.NewShape=""
        self.NewStudentGroup=""
        self.MainWindow=""
        self.DeleteShape=""
        self.DeleteGroup=""

#This class will be used to remember whether the user has clicked the help button
class HelpClass:
    def __init__(self):
        self.HelpRequired=False

#This class will be used by the feedback section to remember some of the widgets
class SuggestionButtons:
    def __init__(self):
        self.SuggestionButtonFrame=Frame()
        self.MakeSuggestionButton=Button()

#This will save some frames so that they won't need to be passed through subroutines
class EntryFrameClass:
    def __init__(self):
        self.EntryFrame=""

#This class will be used to generate the width of 2 lines which will be used to make 2 canvases
#This size of the lines will be dependent on the height of the window
class LineWidthClass:
    def __init__(self):
        self.LineWidth=WindowSize.WindowHeight//25
        self.LineWidth2=WindowSize.WindowHeight//10

#This class will remember all of the main variables required by most subroutines so that they don't need to be passed as arguments
class ResizeAttributes:
    def __init__(self):
        self.InitialChoice=""
        self.AllBoxesChecked=""
        self.InitialFrameArray=[]
        self.BackButton2=""
        self.FirstTime=True
        self.YearGroup=""
        self.ClassName=""
        self.TeacherName=""
        self.Selection=""
        self.MainCanvas=""
        self.ModeSelect=""
        self.CentreOfRotation=""
        self.Choice=""
        self.ShapeType=""
        self.ModeSelect2=""
        self.CentreOfRotation2=""
        self.Choice2=""
        self.ShapeType2=""
        Name=""

#This will be used to uniquely identify each window so that certain things will only happen on certain windows
class CurrentWindow:
    def __init__(self):
        self.ActiveWindow=1

#This class will store all of the variables that are needed to display the answer on the canvas apart from the coordinates
class QuestionStuffClass:
    def __init__(self):
        self.Vector=""
        self.ImportantStuff=[]
        self.LineOfReflection=""
        self.X1=""
        self.Y1=""
        self.X2=""
        self.Y2=""
        self.MidPointR=""
        self.MidPointC=""
        self.Quadrant2=""
        self.Colour=""
        self.Rotation=""
        self.ChangeX=""
        self.ChangeY=""

#This class will be used to store the selected student group so that when the user moves through different screens it will not be forgotten
class GroupSelectedClass:
    def __init__(self):
        self.Selection="-Select the Student Group to Load-"
        
#This class is where all of the initial variables are loaded or written to a file        
class Initialisation:
    #The variables that are already stored in a file or that are set to default 
    def SetUpVariables(StudentGroupData):
        #This saves the data from the array as the correct variable names for the program to work properly
        CentreOfRotation=StudentGroupData[3]
        AllWidgets.CentreOfRotation=CentreOfRotation
        Choice=StudentGroupData[4]
        AllWidgets.Choice=Choice
        ModeSelect=StudentGroupData[5]
        AllWidgets.ModeSelect=ModeSelect
        CheckboxXChecked=StudentGroupData[6]
        CheckboxYChecked=StudentGroupData[7]
        CheckboxBothChecked=StudentGroupData[8]
        RotationClockwise=StudentGroupData[9]
        RotationAntiClockwise=StudentGroupData[10]
        Animate=StudentGroupData[11]
        ShapeType=StudentGroupData[12]
        AllWidgets.ShapeType=ShapeType
        AllBoxesChecked=[[RotationClockwise,RotationAntiClockwise],[CheckboxXChecked,CheckboxYChecked,CheckboxBothChecked],[Animate]]
        AllWidgets.AllBoxesChecked=AllBoxesChecked
        #The data is returned so that it can be used in the program later
        return CentreOfRotation, Choice, ModeSelect, AllBoxesChecked, ShapeType

    #This subroutine writes the data to a file so that it can be stored and loaded at a later date
    def WriteVariables(NewFile,StudentGroupData):
        #This loops for the number of items in the array
        for x in range(len(StudentGroupData)):
            #Each item of the array is written to a file, it uses the stepper value to ensure that they are all written
            NewFile.write(str(StudentGroupData[x])+"\n")

#This class is where the variables associated with the check buttons are set
class AdvancedSelectionClass:
    #This routine updates variables so that the checkboxes remember their previous state when the random button is pressed
    def UpdateCheckButtonVariables(AllBoxesChecked):
        CXC= AllBoxesChecked[1][0]
        CYC= AllBoxesChecked[1][1]
        CBC= AllBoxesChecked[1][2]
        RC=AllBoxesChecked[0][0]
        RAC=AllBoxesChecked[0][1]
        Animate=AllBoxesChecked[2][0]
        return CXC, CYC, CBC, RC, RAC, Animate

    #This subroutine sets up the initial variables for the check boxes
    def SetUpCheckButtonVariables(AllBoxesChecked):
        AllBoxesChecked[1][0]=IntVar()
        AllBoxesChecked[1][1]=IntVar()
        AllBoxesChecked[1][2]=IntVar()
        AllBoxesChecked[0][0]=IntVar()
        AllBoxesChecked[0][1]=IntVar()
        AllBoxesChecked[2][0]=IntVar()
        return AllBoxesChecked

    #This routine sets the check boxes to the previous value that they held so that when random is pressed, they do not get reset 
    def SetCheckButtonVariables(AllBoxesChecked,CXC, CYC, CBC,RC, RAC,Animate):
        CheckboxXChecked = AllBoxesChecked[1][0]
        CheckboxYChecked = AllBoxesChecked[1][1]
        CheckboxBothChecked = AllBoxesChecked[1][2]
        CheckboxXChecked.set(CXC)
        CheckboxYChecked.set(CYC)
        CheckboxBothChecked.set(CBC)
        AllBoxesChecked[0][0].set(RC)
        AllBoxesChecked[0][1].set(RAC)
        AllBoxesChecked[2][0].set(Animate)

#This class contains all of the routines that are required to show different types of answer
class RevealAnswers:
    #This routine creates text on the canvas that can be used to display the answer of the question
    def ShowAnswer(Answer,Number,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray):
        #This ensures that the answer has not already been displayed before showing the answer
        if QuestionAnswer.QuestionAnswerShown==False:
            MainCanvas.create_text(MidColumn*CanvasStuff.LineWidth,20*Number,text=Answer, font=("arial",CanvasStuff.LineWidth//2))
            QuestionAnswer.QuestionAnswerShown=True
        
    #This routine generates vectors, they are more difficult to generate because large brackets go around the x and y values
    def ShowVector(IntroAnswer,Answer,Number,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray):
        #This ensures that the answer has not already been displayed before showing the answer
        if QuestionAnswer.QuestionAnswerShown==False:
            #This generates the vector on the canvas
            MainCanvas.create_text((MidColumn//2)*CanvasStuff.LineWidth,20*Number+5,text=IntroAnswer, font=("arial",CanvasStuff.LineWidth//2))
            MainCanvas.create_text((MidColumn+2)*CanvasStuff.LineWidth,20*Number+5,text="(", font=("arial",CanvasStuff.LineWidth))
            MainCanvas.create_text(((MidColumn+2)*CanvasStuff.LineWidth)+20,20*Number+5,text=Answer, font=("arial",CanvasStuff.LineWidth//2))
            MainCanvas.create_text(((MidColumn+2)*CanvasStuff.LineWidth)+40,20*Number+5,text=")", font=("arial",CanvasStuff.LineWidth))
            QuestionAnswer.QuestionAnswerShown=True
            
    #This routine shows the hidden shape on the grid
    def ShowBlueShape(XCoordinates, YCoordinates, Quadrant, MainCanvas, Colour, MidPointR, MidPointC):
        #This ensures that the answer has not already been displayed before showing the answer
        if QuestionAnswer.QuestionAnswerShown==False:
            Colour=Colour1 #blue
            Transformation.CreateShape(XCoordinates, YCoordinates, Quadrant, MainCanvas, Colour, MidPointR, MidPointC)
        
    #This routine shows the centre of rotation on the grid
    def ShowCentreOfRotation(InitialFrameArray,Answer,Number,MainCanvas,ModeSelect, CentreOfRotation, MidPointR, MidPointC ):
        #This ensures that the answer has not already been displayed before showing the answer
        if QuestionAnswer.QuestionAnswerShown==False:
            #Creates centre of rotation
            MainCanvas.create_text(MidPointC*CanvasStuff.LineWidth, MidPointR*CanvasStuff.LineWidth,text="X", fill=Colour6, font=Font(size=InitialButtonDimensions.FontSize, weight="bold"))
            RevealAnswers.ShowAnswer(Answer,Number,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
        
    #This routine draws the line of reflection on the grid
    def DrawReflectionLine(InitialFrameArray,Answer,Number,MainCanvas,ModeSelect, CentreOfRotation,X1, X2, Y1, Y2):
        #This ensures that the answer has not already been displayed before showing the answer
        if QuestionAnswer.QuestionAnswerShown==False:
            #Drawn the line of reflection
            MainCanvas.create_line(X1,Y1,X2,Y2, fill=Colour3, width=2)
            RevealAnswers.ShowAnswer(Answer,Number,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            
        
#This class contains all of the subroutines associated with creating a new shape
class NewShapeInterface:
    
    #This subroutine is used to reset the text for the shape name but only if it is the explanation
    def ClickInEntryBox(self):
        Name=EntryFrameClass2.Name
        
        #This sets the box to be blank if the box contains the placeholder
        if Name.get()=="Enter shape name":
            Name.set("")

    #This subroutine gets the window ready to display the canvas  
    def WelcomeScreen(Selection,ShapeType,AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice):
        GroupSelected.Selection=Selection
        #This allows the screen in use to be identified
        ActiveWindow.ActiveWindow=4
        #This checks whether the user needs help, if they do then a label gets displayed at the bottom of the screen
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can create a new shape\nso that you can make new and\nmore varied transformations\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        SuggestionsAndFeedback.NewSuggestion(root)

        #These arrays are emptied to allow for a new shape to be created
        ShapeToTransformX.xy=[]
        ShapeToTransformY.xy=[]

        #The back button will be removed and remade so that it will take the user back to the welcome window when clicked
        BackButton2.destroy()
        BackButton2 = Button (BottomFrame, text="Back",font=Font(size=InitialButtonDimensions.FontSize), height=InitialButtonDimensions.ButtonHeight//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, command=lambda: AreYouSure(ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back2",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
        BackButton2.pack(side="right", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)

        #This destroys the existing frame that contains everything
        RootFrame1=InitialFrameArray[4]
        RootFrame1.destroy()

        #When the mouse button is clicked while the mouse is over a square will be drawn on the canvas at that position
        CanvasStuff.LineWidth2=WindowSize.WindowHeight//10
        CanvasCreation.config(height=RowNum//4*CanvasStuff.LineWidth2, width=ColumnNum//4*CanvasStuff.LineWidth2)
        CanvasCreation.bind("<Button-1>", NewShapeInterface.CreateSquare)
        
        #This deletes all of the content from the canvas
        CanvasCreation.delete("all")
        
        #This puts the frame on the window
        RootFrame4.pack()
        
        #This creates a frame that will be for the entry box and button to submit the name
        Label(RootFrame4,bg=Colour3, text="Create New Shape", ).grid(column=0, columnspan=2,row=0, pady=10, padx=10)
        EntryFrame=Frame(RootFrame4, bg=Colour3, padx=20, pady=20)
        EntryFrame.grid(column=1, row=1,padx=20, pady=10)
        EntryFrameClass2.EntryFrame=EntryFrame
        EntryFrame2=Frame(EntryFrame, bg=Colour2, pady=20)
        EntryFrame2.grid(column=0,columnspan=2, row=0, pady=20, sticky="ew")
        EntryFrameClass2.EntryFrame2=EntryFrame2
        Label(EntryFrame2, bg=Colour2, text="Enter shape name:", width=15,pady=ButtonDimensions.PaddingY*2,padx=ButtonDimensions.PaddingX*2).grid(column=0, row=0,pady=ButtonDimensions.PaddingY,padx=ButtonDimensions.PaddingX)
        Name=StringVar()
        CreateShapeEntry=Entry(EntryFrame2, textvariable=Name, bg=Colour2, width=20)
        CreateShapeEntry.grid(column=1, row=0,pady=ButtonDimensions.PaddingY,padx=ButtonDimensions.PaddingX*2)
        CreateShapeButton=Button(BottomFrame, text="Create Shape",font=Font(size=InitialButtonDimensions.FontSize), bg=Colour2, width=InitialButtonDimensions.ButtonWidth, height=InitialButtonDimensions.ButtonHeight//2, command=lambda: NewShapeInterface.CreateShape2(ShapeType,AllBoxesChecked,InitialFrameArray,CanvasCreation,Name.get(), EntryFrame,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice))
        CreateShapeButton.pack(pady=InitialButtonDimensions.PaddingY, side="right")
        EntryFrameClass2.CreateShapeButton=CreateShapeButton
        Name.set("Enter shape name")
        EntryFrameClass2.Name=Name
        
        #When the user clicks in the entry box to enter a shape name if it contains the placeholder it will set to blank
        CreateShapeEntry.bind("<Button-1>", NewShapeInterface.ClickInEntryBox)

        #This runs the routine to put the lines on the canvas
        Checkered(CanvasCreation, False, CanvasStuff.LineWidth2)
        
    #This routine creates a square when you click on the canvas
    def CreateSquare(event):
        x1=ShapeToTransformX.xy
        y1=ShapeToTransformY.xy
        #This gets the position of the mouse pointer when you click on the canvas
        x = event.x
        y = event.y
        LineWidth2=CanvasStuff.LineWidth2
        #This uses floor division on x and y by the width of the column and row to get an integer
        y=y//LineWidth2
        x=x//LineWidth2
        #This is to check that the canvas has not been clicked in that position already
        AddThing=True
        if len(x1)==0:
            #If there is nothing in the array already something must be added
            AddThing=True
        else:
            #This looks through the array at an interval of 2 to check if the numbers already exist
            for Count in range(0,len(x1),2):
                if (x1[Count]==x-3 and x1[Count+1]==x-2 and y1[Count]==y-3 and y1[Count+1]==y-2) :
                    #If the numbers have been written already, then they should not be written again, instead they should be removed
                    AddThing=False
                    #This remembers the position to remove from the array
                    Count1=Count
                    #If it is found in the array the loop breaks, this reduces processing
                    break
                else:
                    #If it is not found, then the position must be added to the array
                    AddThing=True
        #If the numbers need to be added to the array they will be added and a square will be drawn on the canvas in the place you clicked
        if AddThing==True:
            CanvasCreation.create_rectangle((x)*LineWidth2,(y)*LineWidth2, ((x)+1)*LineWidth2,((y)+1)*LineWidth2, fill="lightblue", outline="lightgrey")
            y1.append(y-3)
            y1.append(y-2)
            x1.append(x-3)
            x1.append(x-2)
        #If the numbers need removed the position of the coordinates is removed
        else:
            y1.pop(Count1)
            y1.pop(Count1)
            x1.pop(Count1)
            x1.pop(Count1)
            #A square of the colour of the background will be redrawn so that it looks like it has gone
            CanvasCreation.create_rectangle((x)*LineWidth2,(y)*LineWidth2, ((x)+1)*LineWidth2,((y)+1)*LineWidth2, fill="#ce9be8", outline="lightgrey")
        
    #This creates the shape and writes them to a file
    def CreateShape2(ShapeType,AllBoxesChecked,InitialFrameArray,CanvasCreation,Name, EntryFrame,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice):
        #This will be used so that it will raise an exception if the box contains the placeholder
        if Name=="Enter shape name":
            Name=""
            
        #This will be used to do a presence check by raising a zero division error
        try:
            10/len(Name)
            
            #This opens the file and splits each line into a separate element of the array before closing the file
            CheckExistenceFile=open("Shapes/ShapesMade.txt","r")
            ShapesInExistence=CheckExistenceFile.read().split("\n")
            CheckExistenceFile.close()

            #This will attempt to find the shape before creating it to avoid a second shape with the same name from being created
            try:
                print(ShapesInExistence.index(Name))
                #If the shape does exist already a message box will be displayed asking the user to enter a different name
                messagebox.showerror("Small error","Unfortunately a shape with this name already exists")

            #If the shape does not already exist, this exception will run that will set up the shape
            except:
                x1=ShapeToTransformX.xy
                y1=ShapeToTransformY.xy

                try:
                    #This does a presence check on the coordinates of the new shape, if no squares are clicked an exception will be raised
                    10/len(x1)
                    10/len(y1)
                    
                    #This clears the canvas
                    CanvasCreation.delete("all")
                    
                    #This removes the entry frames from the window
                    EntryFrame.destroy()

                    #This opens a file and writes the new shapes to it
                    File=open("Shapes/ShapesMade.txt","a")
                    File.write(Name+"\n")
                    File.close()

                    #This opens the file containing shape details and writes the new details to it
                    ShapeInfoFile=open("Shapes/ShapeInfo2.txt","a")
                    ShapeInfoFile.write(Name+"<>"+str(x1).strip("[]")+"<>"+str(y1).strip("[]")+"\n")
                    ShapeInfoFile.close()
                    
                    #This deletes everything from the arrays
                    del y1[:]
                    del x1[:]

                    #This runs the subroutine to go back to the welcome window
                    CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

                    #This removes the frames and widgets from the window in preparation for the new screen
                    RootFrame4.pack_forget()
                    EntryFrameClass2.CreateShapeButton.destroy()
                    Help.DeleteLabel.destroy()
                    
                except:
                    #If no squares are clicked the user will be asked to click some
                    messagebox.showerror("Small error","You need to create a shape by clicking on a square")

        except:
            #If the user has not entered anything in the shape name box then they will be asked to enter something
            messagebox.showerror("Small error","You must enter something in the shape name box")
       

#This class contains all of the routines that are to do with creating a new student group
class NewStudentGroupInterface:  
    #This subroutine updates the student group file file
    def CreateClass(AllBoxesChecked,InitialFrameArray,Continue2,BackButton2, ClassName, TeacherName, YearGroup,MainCanvas,ModeSelect,CentreOfRotation, Choice):
        #This performs zero division checks on the class name and teacher name boxes to check that they have been filled in
        try:
            10/len(ClassName)
            try:
                10/len(TeacherName)

                #This checks whether the group has already been made
                try:
                    #This opens the file and splits each line into a separate element of an array
                    StudentGroupFile=open("StudentGroups/"+"Classes.txt","r")
                    StudentGroups=StudentGroupFile.read().split("\n")
                    StudentGroupFile.close()
                    #This checks whether the group name is already listed
                    print(StudentGroups.index(ClassName))
                    #This will display a message if it already exists asking the user to enter a different name
                    messagebox.showerror("Small error","Unfortunately the name that you have entered already exists, please rename the student groups")

                #If there is no student group with that name in the file already the exception runs
                except:

                    #This tries to create the new file, if it can't it is due to invalid characters or having too many characters, this will raise an exception
                    try:
                        #Creates a new file with the name of the Student Group
                        ClassFileName=ClassName + ".txt"
                        NewFile=open("StudentGroups/"+ClassFileName, "w")

                        #New filename written to new line in the classes name file
                        ClassFile = open("StudentGroups/"+"Classes.txt", "a")
                        ClassFile.write("\n"+ClassName)
                        ClassFile.close()

                        #The new file is set to default values
                        StudentGroupData=[ClassName, TeacherName, YearGroup, 0, "Translation", 1,0,0,0,0,0,0, "LShape"]
                        Initialisation.WriteVariables(NewFile, StudentGroupData)
                        NewFile.close()

                        #The welcome screen will be displayed
                        CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

                        #This destroys the widgets that are no longer needed
                        Continue2.destroy()
                        Help.DeleteLabel.destroy()

                    #This exception is raised if the file can't be made
                    except:
                        #If the filename is too long this message will be displayed
                        if len(ClassName)>150:
                            messagebox.showerror("Small Error","You have entered an invalid file name, please enter a shorter file name (150 characters or less)")

                        #If the file is not too long then there must be invalid characters
                        else:
                            messagebox.showerror("Small Error","You have entered an invalid file name, please use only letters and numbers")

            #This exception is raised if the teacher name box is left empty
            except:
                messagebox.showerror("Small Error","You must enter something in the Teacher name box")

        #This exception is raised if the student group name box is left empty
        except:
            messagebox.showerror("Small Error","You must enter something in the student group name box")

        
    #This routine sets up the interface for the student group window
    def CreateClassWindow(Selection, AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice):
        GroupSelected.Selection=Selection
        
        #This creates a unique identifier for the screen
        ActiveWindow.ActiveWindow=3

        #If the user has asked for help this label will be displayed to tell them what to do
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can create a new student group\nso that you can save settings for specific\nstudents so that you don't need to remember where you are up to\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel=Label()
            
        SuggestionsAndFeedback.NewSuggestion(root)

        #The widgets that are not needed are removed
        BackButton2.destroy()
        InitialFrameArray[4].destroy()

        #This creates the different frames
        RootFrame2=Frame(root, bg=Colour3)
        InitialFrameArray[5]=RootFrame2
        InputFrame2 = Frame(RootFrame2, bg=Colour3)
        InputFrame2.pack(expand="yes",)
        RootFrame2.pack(fill="both", expand="yes")

        #This creates the input widgets for making a new class
        ClassName = StringVar()
        TeacherName = StringVar()
        YearGroup = StringVar()
        Label(InputFrame2,bg=Colour3, text="Create New Student Group", font=Font(size=20, weight="bold", underline=1)).grid(column=0, row=0, columnspan=2, pady=10, padx=10)
        Label(InputFrame2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize),text="Enter Student Group Name", pady=InitialButtonDimensions.PaddingY).grid(column=0, row=1, pady=10, padx=10)
        Label(InputFrame2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize),text="Enter Teacher Name", pady=InitialButtonDimensions.PaddingY).grid(column=0, row=2, pady=10, padx=10)
        Label(InputFrame2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize),text="Select Year Group", pady=20).grid(column=0, rowspan=2, row=3, pady=10, padx=10)
        ClassNameEntry=Entry(InputFrame2, bg=Colour2, width=InitialButtonDimensions.ButtonWidth,textvariable=ClassName,font=Font(size=22)).grid(column=1, row=1, pady=10, padx=10)
        TeacherNameEntry=Entry(InputFrame2,bg=Colour2, width=InitialButtonDimensions.ButtonWidth, textvariable=TeacherName,font=Font(size=22)).grid(column=1, row=2, pady=10, padx=10)
        YearGroupSelect=Spinbox(InputFrame2,bg=Colour2, width=(InitialButtonDimensions.ButtonWidth//3), values=("Year 7", "Year 8", "Year 9", "Year 10", "Year 11", "Year 12", "Year 13"), textvariable=YearGroup, buttonbackground=Colour2,
                                font=Font(size=62)).grid(column=1, rowspan=2, row=3, pady=10, padx=10)

        #This creates the button widgets
        BottomFrame=InitialFrameArray[3]
        BackButton2 = Button (BottomFrame, text="Back",font=Font(size=InitialButtonDimensions.FontSize), height=InitialButtonDimensions.ButtonHeight//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, command=lambda: AreYouSure(ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
        BackButton2.pack(side="right", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)
        Continue2 = Button(BottomFrame, text="Continue",font=Font(size=InitialButtonDimensions.FontSize),bg=Colour2, width=InitialButtonDimensions.ButtonWidth, height=InitialButtonDimensions.ButtonHeight//2, command=lambda:NewStudentGroupInterface.CreateClass(AllBoxesChecked,InitialFrameArray,Continue2,BackButton2, ClassName.get(), TeacherName.get(), YearGroup.get(),MainCanvas,ModeSelect,CentreOfRotation, Choice))
        Continue2.pack(side="right", pady=InitialButtonDimensions.PaddingY)


#This class contains all of the subroutines associated with deleting a student group
class DeleteStudentInterface:
    #This subroutine actually deletes the group from both the array and the folder
    def DeleteClass(Selection, Classes, Menu2, ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        #This gets the position in the array of the group selected by the user
        Index=Classes.index(Selection)
        #This removes the item at the position in the array
        Classes.pop(Index)
        #This deletes the file from the folder
        os.remove("StudentGroups/"+Selection+".txt")

        #This opens the file containing the groups
        MyFile=open("StudentGroups/Classes.txt", "w")
        #This loops through each element of the array and writes them to the file which overwrites any existing data
        for x in range(len(Classes)):
            MyFile.write(Classes[x]+"\n")
        MyFile.close()
        
        #This destroys widgets that are no longer needed
        Continue2.destroy()
        Menu2.destroy()
        StudentGroupWidgets.DeleteClassTitle.destroy()

        #The welcome screen will be displayed 
        CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

        
    #This subroutine is used to find the student group that the user wants to delete
    def DeleteStudent(Selection, Classes,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        #This checks whether the user needs help, if they do a label will be displayed telling them what to do
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can delete a student group\nso that it does not appear and cannot be used\njust select a shape from the menu then press delete in the bottom right corner", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel=Label()
            
        #This creates a title for the screen to improve user friendliness 
        DeleteClassTitle=Label(root,bg=Colour3, text="Delete an Existing Student Group", font=Font(size=20, weight="bold", underline=1))
        DeleteClassTitle.pack(pady=10, padx=10)
        
        #This creates a drop down menu for the student group selection
        Selection2 = StringVar()
        #The array is reversed so that the newest classes appear at the top
        Classes.reverse()
        Menu2=OptionMenu(root, Selection2, *Classes)
        Menu2.pack(padx=(InitialButtonDimensions.PaddingX)*2, pady=(InitialButtonDimensions.PaddingY)*2, side="top")
        #This changes the appearance of the menu to make it more consistent with the rest of the interface
        Menu2.config(bg=Colour2,highlightbackground=Colour2,font=Font(size=InitialButtonDimensions.FontSize*2))
        Menu2["menu"].config(bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize*2))
        Selection2.set("-Select the Student Group to Delete-")

        Continue2 = Button(BottomFrame, text="Delete",font=Font(size=InitialButtonDimensions.FontSize),bg=Colour2, width=InitialButtonDimensions.ButtonWidth, height=InitialButtonDimensions.ButtonHeight//2, command=lambda:DeleteStudentInterface.ConfirmDeletion(Selection,Selection2.get(),Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
        Continue2.pack(side="right", pady=InitialButtonDimensions.PaddingY)
        StudentGroupWidgets.Continue2=Continue2
        StudentGroupWidgets.DropDown=Menu2
        StudentGroupWidgets.DeleteClassTitle=DeleteClassTitle
        

    #This subroutine will be used to check that the user really does want to delete the group
    def ConfirmDeletion(Selection, Selection2,Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        #If no student group is selected to delete, then a message will be displayed
        if Selection2=="-Select the Student Group to load-":
            messagebox.showerror("Small error","You must select a student group to delete")
            Response=False
        #If a group has been selected, the user will be asked to confirm that they really do want to delete it.
        else:
            Response=messagebox.askyesno("Are you sure", "Do you really want to delete this student group?")

        #This will check that the user is happy to delete the group before deleting it
        if Response==True:
            ActiveWindow.ActiveWindow=1
            #If the group that was previously selected in the drop down menu is selected to delete then the drop down must be set to its default
            if Selection==Selection2:
                GroupSelected.Selection="-Select the Student Group to Load-"

            #This subroutine will delete the class when it runs
            DeleteStudentInterface.DeleteClass(Selection2, Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice)
            Help.DeleteLabel.destroy()

    #This subroutine will get everything ready to delete the student group
    def SetUpDeleteClass(Selection, AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice):
        GroupSelected.Selection=Selection

        #This opens the file and splits each line into a separate element of an array
        MyFile=open("StudentGroups/Classes.txt", "r")
        Classes=MyFile.read().split("\n")
        MyFile.close()

        #This is to remove any files that don't exist/can't be opened
        Deletions=0
        for x in range(0,len(Classes)):
            #As the array is getting shorter this ensures that none are missed and that it is not out of range
            FileName=str(Classes[x-Deletions]) + ".txt"
            try:
                #This attempts to open the files
                MyFile=open("StudentGroups/"+FileName, "r")
                MyFile.close()
            except:
                #This deletes any class names from the list if they could not be opened
                Classes.pop(x-Deletions)
                Deletions+=1

        try:
            #If there are no classes in the array then it will raise a zero division error
            10//len(Classes)
            #If no exception is raised then the unique screen identifier will change
            ActiveWindow.ActiveWindow=6
            SuggestionsAndFeedback.NewSuggestion(root)
            #The back button is removed
            BackButton2.destroy()
            #This frame is destroyed
            InitialFrameArray[4].destroy()

            #This creates the different frames
            RootFrame2=Frame(root, bg=Colour3)
            InitialFrameArray[5]=RootFrame2
            RootFrame2.pack(fill="both", pady=90)

            #This creates the button widgets
            BottomFrame=InitialFrameArray[3]
            BackButton2 = Button (BottomFrame, text="Back",font=Font(size=InitialButtonDimensions.FontSize), height=InitialButtonDimensions.ButtonHeight//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, command=lambda: AreYouSure(ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back3",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
            BackButton2.pack(side="right", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)
            StudentGroupWidgets.Button=BackButton2

            #This brings up the new screen that allows the user to delete shapes
            DeleteStudentInterface.DeleteStudent(Selection,Classes,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice)
        except:
            #If there are no groups then the interface will not be loaded and a message will be displayed
            messagebox.showerror("Small error", "There are no student groups available to delete")
        

#This class contains all of the subroutines that will let the user delete a shape
class DeleteShapeInterface:
    #This subroutine deletes the shape completely
    def ActuallyDeleteShape(Selection, Classes, Menu2, ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        Continue2.destroy()

        #This opens the file and splits each line into separate elements of an array
        MyFile2=open("Shapes/ShapeInfo2.txt", "r")
        ShapeData=MyFile2.read().split("\n")
        MyFile2.close()
        
        #This reverses the classes back to the original order because it needs to align with the data file which has the oldest first
        Classes.reverse()
        #This finds the position where the user selection lies in the array
        Index=Classes.index(Selection)
        #This deletes the position from the data array and the name array so that when they are written back to the files the deleted item will not be
        Classes.pop(Index)
        ShapeData.pop(Index)


        #This overwrites the 2 files in the folder so that the deleted shapes are forgotten
        MyFile=open("Shapes/ShapesMade.txt", "w")
        MyFile2=open("Shapes/ShapeInfo2.txt", "w")
                
        #This checks that once the shape has been deleted that the class has a shape in it to avoid exceptions from occurring
        if len(Classes)>0:
            #This writes each element of both arrays to the files
            for x in range(len(Classes)):
                MyFile.write(Classes[x]+"\n")
                MyFile2.write(ShapeData[x]+"\n")

        #The files are closed
        MyFile.close()
        MyFile2.close()

        #Some widgets that are no longer needed are removed
        Menu2.destroy()
        StudentGroupWidgets.DeleteClassTitle.destroy()

        #The welcome screen is loaded
        CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)
        

    def DeleteShape(Classes,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        #This checks if the user has clicked the help button, if they have then a label will show help
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can delete a shape\nso that it does not appear and cannot be used in the program\njust select a shape from the menu then press delete in the bottom right corner", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel=Label()
            
        
        #This removes any empty entries in the arrays so that the drop down list is not messy
        Deletions=0
        for x in range(0,len(Classes)):
            if Classes[x-Deletions]=="":
                Classes.pop(x-Deletions)
                Deletions+=1
        print(Classes)

        #This creates a title for the screen to make it more user friendly
        DeleteClassTitle=Label(root,bg=Colour3, text="Delete an existing shape", font=Font(size=20, weight="bold", underline=1))
        DeleteClassTitle.pack(pady=10, padx=10)
        
        #This creates a drop down menu for the student group selection
        Selection2 = StringVar()
        Classes.reverse()
        #This changes the appearance of the array so that it looks consistent with the rest of the interface
        Menu2=OptionMenu(root, Selection2, *Classes)
        Menu2.pack(padx=(InitialButtonDimensions.PaddingX)*2, pady=(InitialButtonDimensions.PaddingY)*2)
        Menu2.config(bg=Colour2,highlightbackground=Colour2,font=Font(size=InitialButtonDimensions.FontSize*2))
        Menu2["menu"].config(bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize*2))
        Selection2.set("-Select the shape to delete-")

        Continue2 = Button(BottomFrame, text="Delete",font=Font(size=InitialButtonDimensions.FontSize),bg=Colour2, width=InitialButtonDimensions.ButtonWidth, height=InitialButtonDimensions.ButtonHeight//2, command=lambda:DeleteShapeInterface.ConfirmDeletion(Selection2.get(),Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
        Continue2.pack(side="right", pady=InitialButtonDimensions.PaddingY)
        StudentGroupWidgets.Continue2=Continue2
        StudentGroupWidgets.DropDown=Menu2
        StudentGroupWidgets.DeleteClassTitle=DeleteClassTitle

    #This subroutine is used to check that the user really does want to delete the shape
    def ConfirmDeletion(Selection2,Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,back,BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice):
        #This checks that the user has not selected the LShape as this can't be deleted
        if Selection2=="LShape":
            messagebox.showerror("Small error","LShape can't be deleted")
            Response=False
        #This checks that the user has actually selected a shape
        elif Selection2=="-Select the shape to delete-":
            messagebox.showerror("Small error","You need to select a shape to delete")
            Response=False
        #If the other 2 conditions are not met, then the user must have chosen a valid option, this will display a message box to check that the user really wants to delete the shape
        else:
            Response=messagebox.askyesno("Are you sure", "Do you really want to delete this shape?")

        #If the user says that they do want to delete the shape then the subroutine to delete the shape will be run
        if Response==True:
            ActiveWindow.ActiveWindow=1
            DeleteShapeInterface.ActuallyDeleteShape(Selection2, Classes, Menu2,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice)
            Help.DeleteLabel.destroy()

    #This gets ready to delete the shape
    def SetUpDeleteShape(Selection, ShapeDeleteButton,AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice):
        GroupSelected.Selection=Selection

        #This opens the shapes and splits each line of the file into a separate element in the array
        MyFile=open("Shapes/ShapesMade.txt", "r")
        Classes=MyFile.read().split("\n")
        MyFile.close()

        #This will delete any places in the array that contain blank spaces
        Deletions=0
        for x in range(0,len(Classes)):
            if Classes[x-Deletions]=="":
                Classes.pop(x-Deletions)
                Deletions+=1
        
        try:
            #This will take one away from the length of the array to account for the LShape which can't be deleted
            #If it is 0 then the code below will not be executed and an exception will be raised
            10//(len(Classes)-1)

            #This will change the screen in use to a unique number to identify it
            ActiveWindow.ActiveWindow=5
            
            SuggestionsAndFeedback.NewSuggestion(root)
            
            #The back button is removed
            BackButton2.destroy()
            #This frame is destroyed
            InitialFrameArray[4].destroy()

            #This creates the different frames
            RootFrame2=Frame(root, bg=Colour3)
            InitialFrameArray[5]=RootFrame2
            RootFrame2.pack(fill="both", pady=90)

            #This creates the button widgets
            BottomFrame=InitialFrameArray[3]
            BackButton2 = Button (BottomFrame, text="Back",font=Font(size=InitialButtonDimensions.FontSize), height=InitialButtonDimensions.ButtonHeight//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, command=lambda: AreYouSure(ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"Back3",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice))
            BackButton2.pack(side="right", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)
            StudentGroupWidgets.Button=BackButton2
            DeleteShapeInterface.DeleteShape(Classes,ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,"back",BackButton2, MainCanvas ,ModeSelect, CentreOfRotation, Choice)

        except:
            #If no shapes are available to delete a message will be displayed
            messagebox.showerror("Small error", "There are no shapes available to delete")


#This class contains routines for each of the different transformations
class Transformation:
    #This routine creates coordinates for a rotated shape
    def RotateShape(Coord1, Coord2, XSign, YSign,  XCoords,  YCoords, MidPointC, MidPointR):
        XCoords.append((int(MidPointC)+(int(Coord1)*int(XSign))))
        YCoords.append((int(MidPointR)+(int(Coord2)*int(YSign))))

    #This uses existing coordinates and the quadrant that the new shape is to end up in to create a rotated shape around a given point
    def CreateShape(XCoordinates, YCoordinates, Quadrant, MainCanvas, Colour, MidPointR, MidPointC):
        #This sets the different coordinates
        XCoords=[]
        YCoords=[]
        XCoordinates2=[]
        YCoordinates2=[]

        #These numbers are added to make each question more different
        NumX=RotationClass.RandomNumberX
        NumY=RotationClass.RandomNumberY
            
        #For each coordinate another coordinate must be generated because a second shape is needed
        for x in range(len(XCoordinates)):

            #This adds the number to the coordiantes to make the questions more varied
            XCoordinates2.append(int(XCoordinates[x])+NumX)
            YCoordinates2.append(int(YCoordinates[x])+NumY)

            #The numbers passed into the RotateShape subroutine have an impact on the rotation and where it appears
            if Quadrant==1:
                Transformation.RotateShape(XCoordinates2[x], YCoordinates2[x], 1, -1, XCoords, YCoords, MidPointC, MidPointR)
            elif Quadrant==2:
                Transformation.RotateShape(YCoordinates2[x],XCoordinates2[x], 1, 1, XCoords, YCoords, MidPointC, MidPointR)
            elif Quadrant==3:
                Transformation.RotateShape(XCoordinates2[x], YCoordinates2[x], -1, 1, XCoords, YCoords, MidPointC, MidPointR)
            else:
                Transformation.RotateShape(YCoordinates2[x],XCoordinates2[x], -1, -1, XCoords, YCoords, MidPointC, MidPointR)

        #This draws the shape on the canvas by drawing the squares separately
        for Count2 in range(0,len(XCoordinates2)-1,2):
            MainCanvas.create_rectangle(((XCoords[Count2])*CanvasStuff.LineWidth,(YCoords[Count2])*CanvasStuff.LineWidth),(XCoords[Count2+1])*CanvasStuff.LineWidth,(YCoords[Count2+1])*CanvasStuff.LineWidth,outline=Colour, stipple="gray75",fill=Colour)

    #This subroutine draws the shape for the translations and reflections
    def DrawShape(StippleEffect,MainCanvas, CoordinatesX, CoordinatesY, Colour):
        #This loops through the array at an interval of 2 as there are 2 coordiantes in each array for each square
        for Count4 in range(0,len(CoordinatesX)-1,2):
            #Squares are drawn to create the shape on the canvas
            MainCanvas.create_rectangle((MidColumn+int(CoordinatesX[Count4]))*CanvasStuff.LineWidth,(MidRow-int(CoordinatesY[Count4]))*CanvasStuff.LineWidth,(MidRow+int(CoordinatesX[Count4+1]))*CanvasStuff.LineWidth,(MidColumn-int(CoordinatesY[Count4+1]))*CanvasStuff.LineWidth, fill=Colour,stipple=StippleEffect, outline=Colour)


    #This subroutine will animate the translation when only 1 shape is shown
    def AnimatedTranslation(ImportantStuff,MainCanvas, XCoordinates2, YCoordinates2, Colour1, CentreOfRotation):
        #This checks that the answer has not already been shown
        if QuestionAnswer.QuestionAnswerShown==False:
            QuestionAnswer.QuestionAnswerShown=True
            #The speed depends on the difficulty slider
            Speed=(6-(CentreOfRotation-1))/5

            #This array is used to pass through variables that are required for creating the shape without having to pass them through individually
            Length=ImportantStuff[0]
            XCoordinates=ImportantStuff[1]
            YCoordinates=ImportantStuff[2]
            RanNumX=ImportantStuff[3]
            RanNumY=ImportantStuff[4]
            MainCanvas=ImportantStuff[5]

            #The shadows will be where the shape moves before the final position is displayed
            XShadow=[]
            YShadow=[]

            #This loops through each coordinate
            for Count in range(0,Length):
                #This adds the random number to the shadow in order to vary the question
                XCoordinates[Count]=int(XCoordinates[Count])+RotationClass.RandomNumberX
                YCoordinates[Count]=int(YCoordinates[Count])+RotationClass.RandomNumberY

                #This adds the coordinates to the shadow arrays
                XShadow.append(int(XCoordinates[Count]))
                YShadow.append(int(YCoordinates[Count]))

            #This loops for the magnitude of the X vector
            for Count2 in range(abs(RanNumX)):
                #This loops through each item in the array
                for Count in range(0,Length):
                    #If the number is positive 1 will be added to the coordinate
                    if RanNumX>0:
                        XShadow[Count]+=1

                    #If the number is negative 1 will be subtracted from the coordinate
                    else:
                        XShadow[Count]-=1

                #This will run the subroutine to draw the shadow on the canvas
                Transformation.DrawShape("gray25",MainCanvas, XShadow, YShadow, Colour3)
                #This will draw the initial shape again so that the shadow does not overlap it
                Transformation.DrawShape("gray75",MainCanvas, XCoordinates, YCoordinates, Colour5)

                #This updates the canvas so that the movement will be displayed
                root.update()

                #This will pause briefly so that the animation is visible
                time.sleep(Speed)

                #This will draw a square over the shadow to hide it
                Transformation.DrawShape("gray25",MainCanvas, XShadow, YShadow, "#f0f0f0")

                #This updates the canvas again so that the change is displayed
                root.update()

            #This loops for the magnitude of the Y vector
            for Count3 in range(abs(RanNumY)):
                for Count in range(0,Length):
                    #If the number is positive 1 will be added to the coordinate
                    if RanNumY>0:
                        YShadow[Count]+=1

                    #If the number is negative 1 will be subtracted from the coordinate
                    else:
                        YShadow[Count]-=1

                #This will run the subroutine to draw the shadow on the canvas
                Transformation.DrawShape("gray25",MainCanvas, XShadow, YShadow, Colour3)
                #This will draw the initial shape again so that the shadow does not overlap it
                Transformation.DrawShape("gray75",MainCanvas, XCoordinates, YCoordinates, Colour5)
                
                #This updates the canvas so that the movement will be displayed
                root.update()
                
                #This will pause briefly so that the animation is visible
                time.sleep(Speed)
                
                #This will draw a square over the shadow to hide it
                Transformation.DrawShape("gray25",MainCanvas, XShadow, YShadow, "#f0f0f0")

                #This updates the canvas again so that the change is displayed
                root.update()

            #This draws the final transformation on the canvas in the correct colour
            Transformation.DrawShape("gray75",MainCanvas, XCoordinates2, YCoordinates2, Colour1)
            #This draws the numbers on the canvas again so that they can be seen if the shape overlaps them
            NumbersOnAxis(CanvasStuff.LineWidth, AllWidgets.MainCanvas)

        
    #This subroutine sets up everything required to rotate the shape
    def Rotation(AllBoxesChecked, MainCanvas, CentreOfRotation):
        XCoordinates=ShapeToTransformX.Coordinates
        YCoordinates=ShapeToTransformY.Coordinates

        #This changes where the centre of rotation is
        CreateQuestion.ChangeX=random.randint((CentreOfRotation*-1),CentreOfRotation)
        CreateQuestion.ChangeY=random.randint((CentreOfRotation*-1),CentreOfRotation)
            
        #This changes where the program takes the midpoint so that it is the new centre of rotation
        CreateQuestion.MidPointR = MidRow + (CreateQuestion.ChangeY*-1)
        CreateQuestion.MidPointC = MidColumn +(CreateQuestion.ChangeX)

        #There are 4 quadrants on the grid, the initial shape can be anywhere on this 
        Quadrant1=random.randint(1,4)
        #The other shape must be in a different quadrant
        Quadrant2=Quadrant1

        #The condition is not met so the while loop runs until the quadrants are different
        while Quadrant2==Quadrant1:
            Quadrant2=random.randint(1,4)#Where red is positioned
        CreateQuestion.Quadrant2=Quadrant2

        #The angle of rotation needs to be given an angle so that a question or answer can be generated
        Angle1=Quadrant1*90
        Angle2=Quadrant2*90
        if Quadrant1>Quadrant2:
            Rotation=Angle2+(360-Angle1)
        else:
            Rotation=Angle2-Angle1

        #Mr Price Jones want's to be able to choose which direction the rotations occur (clockwise or anticlockwise)
        RotationDirection=[]
        NoSelection=False

        #There are checkboxes to allow for easy changing of settings
        #The checkboxes can be checked singularly or both giving either clockwise, anticlockwise or both as options
        if AllBoxesChecked[0][0].get() == 1:
            NoSelection=True
            RotationDirection.append("CW")
        if AllBoxesChecked[0][1].get() == 1:
            NoSelection=True
            RotationDirection.append("ACW")

        #If no checkboxes are checked the default is to allow for both clockwise and anticlockwise rotations
        if NoSelection == False:
            RotationDirection=["CW","ACW"]

        #A random direction can be chosen of the options in the array, there are a maximum of 2 options
        CWACW = random.choice(RotationDirection)

        #This will generate a clockwise or anticlockwise rotation or depending on the mode can generate both together
        if CWACW == "ACW" and not AllWidgets.ModeSelect==1:
            Rotation = 360-Rotation
            Rotation = str(Rotation)+ chr(176)  + " anti-clockwise"
        elif not AllWidgets.ModeSelect == 1:
            Rotation = str(Rotation)+ chr(176) + " clockwise"
        else:
            Rotation2 = str(Rotation)+ chr(176) + " clockwise"
            Rotation = 360-Rotation
            Rotation1 = str(Rotation)+ chr(176) + " anti-clockwise"
            Rotation="\nThe rotation is "  + Rotation1 + "/\n" + Rotation2 + " "
        CreateQuestion.Rotation=Rotation
        
        #This draws the original shape
        Colour=Colour5 #red
        Transformation.CreateShape(XCoordinates, YCoordinates, Quadrant1, MainCanvas, Colour, CreateQuestion.MidPointR, CreateQuestion.MidPointC)

        #This changes the colour for when the second shape is drawn to differentiate them
        CreateQuestion.Colour=Colour1 #blue
 
        
    #This subroutine sets everything up to do a reflection
    def Reflection(AllBoxesChecked,CentreOfRotation):
        XCoordinates=ShapeToTransformX.Coordinates
        YCoordinates=ShapeToTransformY.Coordinates    
        #A random number is selected to change the position of the line
        Num = random.randint((CentreOfRotation*-1),CentreOfRotation)
        #Mr Price Jones wanted to be able to choose the line of reflection
        DirectionOptions=[]
        NoSelection=False
        #I have used 3 checkboxes for the 3 different options (reflect in x axis, reflect in y axis, reflect in y=x)
        #If this checkbox is checked then the option for reflection in the x axis is added to the list
        if AllBoxesChecked[1][0].get() == 1:
            NoSelection=True
            DirectionOptions.append("X")
        #If this checkbox is checked then the option for reflection in the y axis is added to the list
        if AllBoxesChecked[1][1].get() == 1:
            NoSelection=True
            DirectionOptions.append("Y")
        #If this checkbox is checked then the option for reflection in the line y=x is added to the list
        if AllBoxesChecked[1][2].get() == 1:
            NoSelection=True
            DirectionOptions.append("Both")

        #If there is no selection then only the x axis is selected as it is the simplest reflection
        if NoSelection == False:
            DirectionOptions.append("X")

        #This picks a random thing from the list which varies depending on the check buttons
        XOrY=random.choice(DirectionOptions)

        #If the random choice is X then 
        if XOrY == "X":
            #This gets the question needed ready
            CreateQuestion.LineOfReflection=("X = " + str(Num))
            
            #This sets the coordinates for the new shape
            for Count in range(0,len(XCoordinates)):
                ShapeToTransformX.Coordinates2.append((int(XCoordinates[Count])*-1)+Num-RotationClass.RandomNumberX)
                ShapeToTransformX.Coordinates3.append(int(XCoordinates[Count])+Num+RotationClass.RandomNumberX)
                ShapeToTransformY.Coordinates2.append(int(YCoordinates[Count])+RotationClass.RandomNumberY)
                ShapeToTransformY.Coordinates3.append(int(YCoordinates[Count])+RotationClass.RandomNumberY)

            #This sets the coordinates for the line of reflection
            CreateQuestion.X1=(MidColumn+Num)*CanvasStuff.LineWidth
            CreateQuestion.Y1=0
            CreateQuestion.X2=CreateQuestion.X1
            CreateQuestion.Y2=RowNum*CanvasStuff.LineWidth

        elif XOrY == "Y":
            #This gets the question needed ready
            CreateQuestion.LineOfReflection=("Y = " + str(Num))

            #This sets the coordiantes for the new shape
            for Count in range(0,len(YCoordinates)):
                ShapeToTransformY.Coordinates2.append(((int(YCoordinates[Count])*-1)+2*Num)-RotationClass.RandomNumberX)
                ShapeToTransformY.Coordinates3.append((int(YCoordinates[Count])+RotationClass.RandomNumberX))
                ShapeToTransformX.Coordinates2.append(int(XCoordinates[Count])+RotationClass.RandomNumberX)
                ShapeToTransformX.Coordinates3.append(int(XCoordinates[Count])+RotationClass.RandomNumberX)
            
            #This sets the coordinates for the line of reflection
            CreateQuestion.X1=0
            CreateQuestion.Y1=(MidRow-Num)*CanvasStuff.LineWidth
            CreateQuestion.X2=RowNum*CanvasStuff.LineWidth
            CreateQuestion.Y2=CreateQuestion.Y1
            
        else:
            #This gets the question needed ready
            if Num*-1 > 0:
                CreateQuestion.LineOfReflection=("Y = -X" + str(Num))
            elif Num*-1<0:
                CreateQuestion.LineOfReflection=("Y = -X +" + str(Num))
            else:
                CreateQuestion.LineOfReflection=("Y = -X")
                
            #This sets the coordinates for the new shape
            for Count in range(0,len(XCoordinates)):
                ShapeToTransformX.Coordinates2.append(-int(YCoordinates[Count])+Num-RotationClass.RandomNumberY+3)
                ShapeToTransformY.Coordinates2.append(-int(XCoordinates[Count])+Num+RotationClass.RandomNumberX-3)
                ShapeToTransformX.Coordinates3.append(int(XCoordinates[Count])-RotationClass.RandomNumberX+3)
                ShapeToTransformY.Coordinates3.append(int(YCoordinates[Count])+RotationClass.RandomNumberY-3)

            #This sets the coordinates for the line of reflection
            CreateQuestion.X1=0
            CreateQuestion.Y1=(0-Num)*CanvasStuff.LineWidth
            CreateQuestion.X2=(ColumnNum)*CanvasStuff.LineWidth
            CreateQuestion.Y2=(RowNum-Num)*CanvasStuff.LineWidth

        
    #This gets ready to do the translation
    def Translation(CentreOfRotation, MainCanvas):
        XCoordinates=ShapeToTransformX.Coordinates
        YCoordinates=ShapeToTransformY.Coordinates
        Length=len(XCoordinates)
        #This sets the X and Y translation vector and is dependent on the slider value
        RanNumX = random.randint((CentreOfRotation*-1),CentreOfRotation)
        RanNumY = random.randint((CentreOfRotation*-1),CentreOfRotation)
        NumX=RotationClass.RandomNumberX
        NumY=RotationClass.RandomNumberY
        #This sets the vector values
        CreateQuestion.Vector=(str(RanNumX) + "\n" + str(RanNumY))
        CreateQuestion.ImportantStuff=[Length, XCoordinates, YCoordinates, RanNumX, RanNumY, MainCanvas]
        #This sets the coordinates for the translation
        for Count in range(0, Length):
            ShapeToTransformX.Coordinates2.append(int(XCoordinates[Count])+RanNumX+NumX)
            ShapeToTransformY.Coordinates2.append(int(YCoordinates[Count])+RanNumY+NumY)
            ShapeToTransformX.Coordinates3.append(int(XCoordinates[Count])+NumX)
            ShapeToTransformY.Coordinates3.append(int(YCoordinates[Count])+NumY)


#This class contains all of the subroutines required to change what happens when the answer button is displayed
class UpdateMainWindow:
    #This changes what the answer button does for rotations
    def Rotation(ModeSelect, MainCanvas, InitialFrameArray, ):
        Quadrant2=CreateQuestion.Quadrant2
        Colour=CreateQuestion.Colour
        MidPointR=CreateQuestion.MidPointR
        MidPointC=CreateQuestion.MidPointC
        Rotation=CreateQuestion.Rotation
        ChangeX=CreateQuestion.ChangeX
        ChangeY=CreateQuestion.ChangeY
        XCoordinates=ShapeToTransformX.Coordinates
        YCoordinates=ShapeToTransformY.Coordinates
        RightFrame=InitialFrameArray[1]
        #There are different modes which require the answer button to do different things
        QuestionAnswer.QuestionAnswerShown=False
        if ModeSelect==1:
            #The blue shape is created, the red one has already been placed
            Transformation.CreateShape(XCoordinates, YCoordinates, Quadrant2, MainCanvas,Colour, MidPointR, MidPointC)
            #This is the question to be displayed but uses the answer subroutine as this works well
            Answer=("State the single transformation from red to blue?")
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #This is the answer to the question, when the answer button is clicked the answer will be displayed on the canvas
            Answer=(str(Rotation)+" around the point ("+str(ChangeX)+","+str(ChangeY)+")")
            QuestionAnswer.QuestionAnswerShown=False
            RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:RevealAnswers.ShowCentreOfRotation(InitialFrameArray,Answer,2,MainCanvas,ModeSelect, CentreOfRotation, MidPointR, MidPointC))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        elif ModeSelect==2:
            #This shows the centre point on the canvas, the blue shape is not shown
            MainCanvas.create_text(MidPointC*CanvasStuff.LineWidth, MidPointR*CanvasStuff.LineWidth,text="X", fill=Colour6, font=Font(size=InitialButtonDimensions.FontSize, weight="bold"))
            #This is the question to be displayed but uses the answer subroutine as this works well
            Answer=("Rotate the red shape "+str(Rotation)+" around the point ("+str(ChangeX)+","+str(ChangeY)+")")
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #When the answer button is pressed it shows the blue shape on the canvas
            QuestionAnswer.QuestionAnswerShown=False
            RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:RevealAnswers.ShowBlueShape(XCoordinates, YCoordinates, Quadrant2, MainCanvas, Colour, MidPointR, MidPointC))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        else:
            #This does everything, it shows the blue shape, the centre of rotation and the question
            Transformation.CreateShape(XCoordinates, YCoordinates, Quadrant2, MainCanvas,Colour, MidPointR, MidPointC)
            MainCanvas.create_text(MidPointC*CanvasStuff.LineWidth, MidPointR*CanvasStuff.LineWidth,text="X", fill=Colour6, font=Font(size=InitialButtonDimensions.FontSize, weight="bold"))
            Answer=("Rotate the red shape "+str(Rotation)+" around the point ("+str(ChangeX)+","+str(ChangeY)+")")
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            
    #This changes what the answer button does for reflections
    def Reflection(ModeSelect, MainCanvas, InitialFrameArray,):
        X1=CreateQuestion.X1
        Y1=CreateQuestion.Y1
        X2=CreateQuestion.X2
        Y2=CreateQuestion.Y2
        LineOfReflection=CreateQuestion.LineOfReflection
        
        RightFrame=InitialFrameArray[1]
        QuestionAnswer.QuestionAnswerShown=False
        if ModeSelect == 1:
            #This is the question to be displayed but uses the answer subroutine as this works well
            Answer=("State the single transformation from red to blue")
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #The initial shape and the new shape are both drawn on the canvas
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1)
            #This is the answer to the question, when the answer button is clicked the answer will be displayed on the canvas
            Answer=LineOfReflection
            QuestionAnswer.QuestionAnswerShown=False
            RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:RevealAnswers.DrawReflectionLine(InitialFrameArray,Answer,2,MainCanvas,ModeSelect, CentreOfRotation,X1, X2, Y1, Y2))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        elif ModeSelect == 2:
            #This is the question to be displayed but uses the answer subroutine as this works well
            Answer="Reflect the red shape in the line" + LineOfReflection
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #This draws the red shape but the blue shape remains hidden
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            #This creates the line of reflection
            MainCanvas.create_line(X1,Y1,X2,Y2, fill=Colour3, width=2)
            #When the answer button is clicked it displays the blue shape on the canvas
            QuestionAnswer.QuestionAnswerShown=False
            RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda: Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        else:
            #This is the question to be displayed but uses the answer subroutine as it works well
            Answer="Reflect the red shape in the line" + LineOfReflection
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #Both shapes are drawn
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1)
            #The line of reflection is drawn
            MainCanvas.create_line(X1,Y1,X2,Y2, fill=Colour3, width=2)

    #This changes what the answer button does for translations
    def Translation(ModeSelect, MainCanvas, InitialFrameArray, ):
        Vector=CreateQuestion.Vector
        ImportantStuff= CreateQuestion.ImportantStuff
        AllBoxesChecked=AllWidgets.AllBoxesChecked
        CentreOfRotation=AllWidgets.CentreOfRotation
        RightFrame=InitialFrameArray[1]
        QuestionAnswer.QuestionAnswerShown=False
        if ModeSelect == 1:
            #This is the question to be displayed but uses the answer subroutine as this works well
            Answer="State the single transformation from red to blue"
            RevealAnswers.ShowAnswer(Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #The answer is set differently as it now uses the showvector routine, there are 2 parts to it
            IntroAnswer="The translation vector is:"
            Answer=(Vector)
            #The 2 shapes are shown
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            #if CentreOfRotation==0:
                #root.update()
                #time.sleep(0.5)
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1)
            #root.update()
            #When the answer button is clicked the vector will be displayed as text on the canvas
            QuestionAnswer.QuestionAnswerShown=False
            RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:RevealAnswers.ShowVector(IntroAnswer,Answer,3,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        elif ModeSelect == 2:
            #The question is set differently as it now uses the showvector routine, there are 2 parts to it
            IntroAnswer="Complete the translation:"
            Answer=(Vector)
            RevealAnswers.ShowVector(IntroAnswer,Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #This draws the initial shape (red shape)
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            #The answer button will display the blue shape when clicked
            Animate=AllBoxesChecked[2][0].get()
            QuestionAnswer.QuestionAnswerShown=False
            #This will animate the translation if the option has been selected
            if Animate==1:
                RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:Transformation.AnimatedTranslation(ImportantStuff,MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1, CentreOfRotation))
            else:
                RevealAnswers.ShowAnswerButton=Button(RightFrame, text="Show Answer",font=Font(size=ButtonDimensions.FontSize), bg=Colour2, cursor=CursorType, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,command=lambda:Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1))
            RevealAnswers.ShowAnswerButton.grid(column=0, row=1, padx=ButtonDimensions.PaddingX//2, pady=ButtonDimensions.PaddingY//2)
        else:
            #The question is set differently as it now uses the showvector routine, there are 2 parts to it
            IntroAnswer="The vector from red to blue is:"
            Answer=(Vector)
            RevealAnswers.ShowVector(IntroAnswer,Answer,1,MainCanvas,ModeSelect, CentreOfRotation,InitialFrameArray)
            #The 2 shapes are shown
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates3, ShapeToTransformY.Coordinates3, Colour5)
            Transformation.DrawShape("gray75",MainCanvas, ShapeToTransformX.Coordinates2, ShapeToTransformY.Coordinates2, Colour1)

#This class contains all of the subroutines that remain that are relevant to the main window but cannot be grouped into more specific categories
class SetUpMainWindow:
    def OpenStudentGroupData(AllBoxesChecked):
        YearGroup=AllWidgets.YearGroup
        ClassName=AllWidgets.ClassName
        TeacherName=AllWidgets.TeacherName
        Selection=AllWidgets.Selection
        ModeSelect=AllWidgets.ModeSelect
        CentreOfRotation=AllWidgets.CentreOfRotation
        Choice=AllWidgets.Choice
        ShapeType=AllWidgets.ShapeType
        #This uses the drop down menu to generate a filename and load a class
        SelectedFile="StudentGroups/"+Selection+".txt"
        #The first time the program is run the initial values must be loaded from the file
        if AllWidgets.FirstTime==True:
            #Once this has started it is no longer the first time that it has been run so is set to false
            AllWidgets.FirstTime=False
            #This reads the selected file into an array
            StudentGroupFile=open(SelectedFile, "r")
            StudentGroupData=StudentGroupFile.read().split("\n")
             
            #A subroutine splits up the array and returns values that are needed
            CentreOfRotation, Choice, ModeSelect, AllBoxesChecked, ShapeType=Initialisation.SetUpVariables(StudentGroupData)

            StudentGroupFile.close()

        #This file is needed to write the data to the file
        File=open(SelectedFile, "w")
        #This array makes it easier to pass everything through the program rather than having to pass individual variables
        StudentGroupData=[ClassName, TeacherName, YearGroup, CentreOfRotation, Choice, ModeSelect, AllBoxesChecked[1][0], AllBoxesChecked[1][1],AllBoxesChecked[1][2],AllBoxesChecked[0][0],AllBoxesChecked[0][1],AllBoxesChecked[2][0] , ShapeType]
        #This writes the new variables to a file
        Initialisation.WriteVariables(File, StudentGroupData)
        #The file is closed
        File.close()
        return StudentGroupData, File

    #This subroutine creates a slider bar in the right frame and sets it to the existing value which is loaded from a file
    def SliderValue(RightFrame,RadioButtonFrame,  CentreOfRotation,Choice):
        #This creates a title for the transformation drop down menu
        Label(RadioButtonFrame, text="Transformation type:",bg=Colour2,font=Font(size=ButtonDimensions.FontSize,weight="bold", underline=1) ).pack()
        Choice2=Choice
        
        #This creates a drop down menu allowing the user to select the type of transformation
        Choice=StringVar()
        ChoiceFrame=Frame(RadioButtonFrame, bg=Colour2)
        ChoiceMenu=OptionMenu(ChoiceFrame, Choice, "Translation","Reflection","Rotation")
        ChoiceMenu.pack(side="left", padx=ButtonDimensions.PaddingX//2)

        #This checks if help is required, if it is then a label will be shown next to the option menu
        if Help.HelpRequired==True:
            Label(ChoiceFrame,font=Font(size=ButtonDimensions.FontSize), width=ButtonDimensions.ButtonWidth,bg=Colour1, text="Choose transformation\nfrom the list").pack(side="right", padx=ButtonDimensions.PaddingX//2)
            ChoiceFrame.pack(fill="x")
        else:
            ChoiceFrame.pack()

        #This changes the style of the menu so that it is consistent with the rest of the program
        ChoiceMenu.config(bg=Colour2,highlightbackground=Colour2,font=Font(size=ButtonDimensions.FontSize))
        ChoiceMenu["menu"].config(bg=Colour2,font=Font(size=ButtonDimensions.FontSize))
        #This sets the value of the drop down menu to the previous value so that it is not reset each time
        Choice.set(Choice2)

        #This creates a title for the difficulty slider
        Label(RadioButtonFrame, text="Difficulty Slider",bg=Colour2,font=Font(size=ButtonDimensions.FontSize,weight="bold", underline=1) ).pack()
        Centre=CentreOfRotation

        #This sets up the difficulty slider's maximum values
        CentreOfRotation=IntVar()
        if MidRow>MidColumn:
            Max=MidColumn-4
        else:
            Max=MidRow-4

        #This creates the difficulty slider
        SliderFrame=Frame(RadioButtonFrame,bg=Colour2)
        PickCentre=Scale(SliderFrame, from_=0, to=Max, orient="horizontal",font=Font(size=ButtonDimensions.FontSize), variable=CentreOfRotation, cursor=CursorType, bg=Colour2, trough=Colour4)
        PickCentre.pack(side="left", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)

        #If the user has pressed the help button a label will be shown next to the slider telling the user what to do
        if Help.HelpRequired==True:
            Label(SliderFrame,font=Font(size=ButtonDimensions.FontSize), width=ButtonDimensions.ButtonWidth, bg=Colour1, text="Set the difficulty\nlevel using the slider").pack(side="right", padx=ButtonDimensions.PaddingX//2)
            SliderFrame.pack(fill="x")
        else:
            SliderFrame.pack()
            
        CentreOfRotation.set(Centre)
        return CentreOfRotation, Choice

    #This subroutine loads the shape selected from the drop down list
    def LoadShapeMainWindow(ShapeType):
        try:
            ShapeToTransformX.ShapeType=ShapeType
            
            #This opens the file containing all of the shapes made and splits each line into a separate array element
            ShapeFile=open("Shapes/ShapesMade.txt", "r")
            Shapes=ShapeFile.read().split("\n")
            ShapeFile.close()

            #This finds the position in the array at which the selected shape resides
            WhichLine=Shapes.index(ShapeType)
            #This gets the line from the shape details file without having to open it saving RAM - Yay!!
            Line = linecache.getline("Shapes/"+"ShapeInfo2.txt",WhichLine+1)
            #This clears the linecache as it would otherwise mess up the file
            linecache.clearcache()

            #This splits the line into parts
            ShapeInfo2=Line.split("<>")
            #The coordinates are split further, there are 2 arrays that need to be split into 2 further arrays to represent coordinates
            x1=ShapeInfo2[1].split(", ")
            y1=ShapeInfo2[2].split(", ")
            #This updates the class which holds the coordinate arrays
            ShapeToTransformX.xy=x1
            ShapeToTransformY.xy=y1

            #This deletes the data from the array
            del ShapeToTransformY.CoordinatesPlaceholder[:]

            #Each item in y1 is multiplied by -1 and the placeholder is updated to represent a different shape
            for Count2 in range(len(y1)):
                ShapeToTransformY.CoordinatesPlaceholder.append(int(y1[Count2])*-1)

            #The placeholder is updated for the new shape
            ShapeToTransformX.CoordinatesPlaceholder=x1

        #If no shape is selected a message box will be displayed
        except:
            messagebox.showerror("Small problem","Please select a shape from the drop down menu")

    #This creates a drop down menu from which a shape can be selected
    def LoadShapeMenu(RadioButtonFrame, Selection, ShapeChoice2):
        #This opens and reads the ShapesMade.txt file and splits it up into arrays
        MyFile=open("Shapes/"+"ShapesMade.txt","r")
        ShapeNames=MyFile.read().split("\n")
        MyFile.close()

        
        try:
            #This tries to find the position of the chosen shape in the array
            WhichLine=ShapeNames.index(ShapeChoice2)
            print(WhichLine)
        except:
            #if the selection is not in the array then it can't load so LShape will be loaded instead
            ShapeChoice2="LShape"
            messagebox.showerror("Small problem","The shape had been deleted, had to switch to LShape")        

        #This gives the shape menu a title
        Label(RadioButtonFrame, text="Select shape",bg=Colour2,font=Font(size=ButtonDimensions.FontSize,weight="bold", underline=1) ).pack()
        
        #This removes any blanks so that they don not appear in the list
        Deletions=0
        for x in range(0,len(ShapeNames)):
            if ShapeNames[x-Deletions]=="":
                ShapeNames.pop(x-Deletions)
                Deletions+=1

        #The drop down menu is made containing all of the shapes in the file
        SelectShape=Frame(RadioButtonFrame, bg=Colour2)
        ShapeChoice=StringVar()
        ShapeNames.reverse()
        ShapeMenu=OptionMenu(SelectShape, ShapeChoice, *ShapeNames)
        ShapeNames.reverse()
        ShapeMenu.pack(side="left")
        #This changes the colour of the drop down menu
        ShapeMenu.config(bg=Colour2,highlightbackground=Colour2,font=Font(size=ButtonDimensions.FontSize))
        ShapeMenu["menu"].config(bg=Colour2,font=Font(size=ButtonDimensions.FontSize))
        #This sets the selection to the previous selection so that it is not reset each time
        ShapeChoice.set(ShapeChoice2)

        #This checks whether the user has requested help, if they have then an explanation label will be shown next to the shape menu
        if Help.HelpRequired==True:
            Label(SelectShape,font=Font(size=ButtonDimensions.FontSize), width=ButtonDimensions.ButtonWidth, bg=Colour1, text="Select the shape from\n the drop down menu").pack(side="right", padx=ButtonDimensions.PaddingX//2)
            SelectShape.pack(fill="x")
        else:
            SelectShape.pack()
            
        Colour=Colour1
        return ShapeChoice

    #This subroutine creates a number of check boxes in the right frame and sets them based on a file
    def RadioButtons(RadioButtonFrame, ModeSelect,Selection):
        #This allows the mode to be set using radio buttons, this is appropriate as only one option can be selected at a time
        Mode=ModeSelect
        ModeSelect=IntVar()

        #This creates a title for the radio buttons
        Label(RadioButtonFrame, text="Select Mode", font=Font(size=ButtonDimensions.FontSize, underline=1, weight="bold"), bg=Colour2).pack()

        #There are 3 radio buttons created, if help is needed subroutines help will be shown when the user hovers
        ShowShape=Radiobutton(RadioButtonFrame,text="Show 2 Shapes",font=Font(size=ButtonDimensions.FontSize),value=1, variable=ModeSelect, indicatoron=0, width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
        ShowShape.pack(fill="x", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)
        if Help.HelpRequired==True:
            CheckButtons.ShowShape=ShowShape
            ShowShape.bind("<Enter>",SetUpMainWindow.ShowShapeEntry)
            ShowShape.bind("<Leave>", SetUpMainWindow.ShowShapeLeave)
        HideShape=Radiobutton(RadioButtonFrame,text="Show 1 Shape",font=Font(size=ButtonDimensions.FontSize), value=2, variable=ModeSelect, indicatoron=0, width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
        HideShape.pack(fill="x", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)
        if Help.HelpRequired==True:
            CheckButtons.HideShape=HideShape
            HideShape.bind("<Enter>",SetUpMainWindow.HideShapeEntry)
            HideShape.bind("<Leave>", SetUpMainWindow.HideShapeLeave)
        Testing=Radiobutton(RadioButtonFrame, text="Show All",font=Font(size=ButtonDimensions.FontSize), value=3, variable=ModeSelect, indicatoron=0, width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
        Testing.pack(fill="x", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)
        if Help.HelpRequired==True:
            CheckButtons.Testing=Testing
            Testing.bind("<Enter>",SetUpMainWindow.TestingEntry)
            Testing.bind("<Leave>", SetUpMainWindow.TestingLeave)

        #The mode is set to the previous value so that it is not reset to default each time as this would cause problems
        ModeSelect.set(Mode)
        return ModeSelect


    #This group of subroutines do similar things but for different widgets
    #The subroutines are paired up
    #one is for when the mouse enters, it changes the colour and text to explain what to do
    #The other changes the widget back to how it looked previously
    
    def CB1Entry(self):
        CheckButtons.CB1.configure(bg=Colour1, text="When clicked the next reflections have the\nchance to be reflected in the line x=k")

    def CB1Leave(self):
        CheckButtons.CB1.configure(bg=Colour2,text="Reflect in X = k")

    def CB2Entry(self):
        CheckButtons.CB2.configure(bg=Colour1, text="When clicked the next reflections have the\nchance to be reflected in the line Y=k")

    def CB2Leave(self):
        CheckButtons.CB2.configure(bg=Colour2,text="Reflect in Y = k")

    def CB3Entry(self):
        CheckButtons.CB3.configure(bg=Colour1, text="When clicked the next reflections have the\nchance to be reflected in the line Y=-X+k")

    def CB3Leave(self):
        CheckButtons.CB3.configure(bg=Colour2,text="Reflect in Y = -X + k")

    def CB4Entry(self):
        CheckButtons.CB4.configure(bg=Colour1, text="When clicked the next reflections have the\nchance to be rotated clockwise")

    def CB4Leave(self):
        CheckButtons.CB4.configure(bg=Colour2,text="Clockwise")

    def CB5Entry(self):
        CheckButtons.CB5.configure(bg=Colour1, text="When clicked the next reflections have the\nchance to be rotated anticlockwise")

    def CB5Leave(self):
        CheckButtons.CB5.configure(bg=Colour2,text="AntiClockwise")
        
    def CB6Entry(self):
        CheckButtons.CB6.configure(bg=Colour1, text="When clicked if the mode selected is show 1\nshape then when the answer is revealed\nmovement will show")

    def CB6Leave(self):
        CheckButtons.CB6.configure(bg=Colour2,text="AntiClockwise")

    def ShowShapeEntry(self):
        CheckButtons.ShowShape.configure(bg=Colour1, text="The next question will show 2 shapes and\nwill ask for either an equation, point or vector")

    def ShowShapeLeave(self):
        CheckButtons.ShowShape.configure(bg=Colour2,text="Show 2 Shapes")

    def HideShapeEntry(self):
        CheckButtons.HideShape.configure(bg=Colour1, text="The next question will show 1 shape, either an equation,\npoint or vector and will ask for the other shape")

    def HideShapeLeave(self):
        CheckButtons.HideShape.configure(bg=Colour2,text="Show 1 Shape")

    def TestingEntry(self):
        CheckButtons.Testing.configure(bg=Colour1, text="The next question will show everything and\nwill not ask a question this is mainly to aid teaching")

    def TestingLeave(self):
        CheckButtons.Testing.configure(bg=Colour2,text="Show All")

    def NewQuestionEntry(self):
        CheckButtons.NewQuestion.configure(bg=Colour1, text="When clicked a\nnew question will\nbe generated")

    def NewQuestionLeave(self):
        CheckButtons.NewQuestion.configure(bg=Colour2,text="New Question")

    def AnswerEntry(self):
        CheckButtons.Answer.configure(bg=Colour1, text="When clicked the\nanswer will\nbe displayed")
        
    def AnswerLeave(self):
        CheckButtons.Answer.configure(bg=Colour2,text="Show Answer")

    def NewStudentGroupEntry(self):
        CheckButtons.NewStudentGroup.configure(bg=Colour1, text="\nWhen clicked a\nwindow will be displayed\nto create a new student group")
        
    def NewStudentGroupLeave(self):
        CheckButtons.NewStudentGroup.configure(bg=Colour2,text="\nCreate New\nStudent Group\n")

    def NewShapeEntry(self):
        CheckButtons.NewShape.configure(bg=Colour1, text="When clicked a new\nwindow will open where you\ncan make your own shapes\nfor a transformation")
        
    def NewShapeLeave(self):
        CheckButtons.NewShape.configure(bg=Colour2,text="\nCreate New\nShape\n")

    def MainWindowEntry(self):
        CheckButtons.MainWindow.configure(bg=Colour1, text="\nWhen clicked the\ntransformations window\nwill open")
        
    def MainWindowLeave(self):
        CheckButtons.MainWindow.configure(bg=Colour2,text="\nAdvance to\nTransformation Questions\n")

    def DeleteShapeEntry(self):
        CheckButtons.DeleteShape.configure(bg=Colour1, text="\nWhen clicked a window\nwill open where you\ncan delete shapes")
        
    def DeleteShapeLeave(self):
        CheckButtons.DeleteShape.configure(bg=Colour2,text="\nDelete a\nShape\n")

    def DeleteGroupEntry(self):
        CheckButtons.DeleteGroup.configure(bg=Colour1, text="\nWhen clicked a new\nwindow will open allowing\nyou to delete student groups")
        
    def DeleteGroupLeave(self):
        CheckButtons.DeleteGroup.configure(bg=Colour2,text="\nDelete a\nStudent Group\n")


    
    #This subroutine only displays the relevant checkboxes to the type of transformation
    def CheckBoxes(AllBoxesChecked, Choice, RightFrame, RadioButtonFrame):
        #This loops through each item in the array and turns them into integers
        for x in range(len(AllBoxesChecked)):
            for y in range(len(AllBoxesChecked[x])):
                AllBoxesChecked[x][y]=int(AllBoxesChecked[x][y])
                
        #These routines set up the initial values for the checkboxes and get them ready to be used
        CXC, CYC, CBC, RC, RAC, Animate = AdvancedSelectionClass.UpdateCheckButtonVariables(AllBoxesChecked)
        AllBoxesChecked=AdvancedSelectionClass.SetUpCheckButtonVariables(AllBoxesChecked)

        #This creates a frame to hold the variables
        CheckButtonFrame=Frame(RadioButtonFrame, bg=Colour2,)
        CheckButtonFrame.pack(fill="x")

        #A title for the relevant transformation is created first
        #Relevant check buttons are then created
        #If the user clicks the help button when they hover over the appropriate check button it will display help
        #When the user's mouse leaves it will return to normal appearance
        if Choice=="Reflection":
            Label(CheckButtonFrame, text="Reflection Options",font=Font(size=ButtonDimensions.FontSize, underline=1,weight="bold"), bg=Colour2).pack()
            CB1=Checkbutton(CheckButtonFrame, text="Reflect in X = k",font=Font(size=ButtonDimensions.FontSize), variable=AllBoxesChecked[1][0],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB1.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB1=CB1
                CB1.bind("<Enter>",SetUpMainWindow.CB1Entry)
                CB1.bind("<Leave>", SetUpMainWindow.CB1Leave)
            CB2=Checkbutton(CheckButtonFrame, text="Reflect in Y = k",font=Font(size=ButtonDimensions.FontSize),variable=AllBoxesChecked[1][1],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB2.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB2=CB2
                CB2.bind("<Enter>",SetUpMainWindow.CB2Entry)
                CB2.bind("<Leave>", SetUpMainWindow.CB2Leave)
            CB3=Checkbutton(CheckButtonFrame, text="Reflect in Y=-X+k",font=Font(size=ButtonDimensions.FontSize),variable=AllBoxesChecked[1][2],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB3.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB3=CB3
                CB3.bind("<Enter>",SetUpMainWindow.CB3Entry)
                CB3.bind("<Leave>", SetUpMainWindow.CB3Leave)
        elif Choice=="Rotation":
            #The clockwise and anti-clockwise options are relevant to rotations
            Label(CheckButtonFrame, text="Rotation Options",font=Font(size=ButtonDimensions.FontSize, underline=1,weight="bold"), bg=Colour2).pack()
            CB4=Checkbutton(CheckButtonFrame, text="Clockwise",font=Font(size=ButtonDimensions.FontSize),variable=AllBoxesChecked[0][0],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB4.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB4=CB4
                CB4.bind("<Enter>",SetUpMainWindow.CB4Entry)
                CB4.bind("<Leave>", SetUpMainWindow.CB4Leave)
            CB5=Checkbutton(CheckButtonFrame, text="Anticlockwise",font=Font(size=ButtonDimensions.FontSize),variable=AllBoxesChecked[0][1],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB5.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB5=CB5
                CB5.bind("<Enter>",SetUpMainWindow.CB5Entry)
                CB5.bind("<Leave>", SetUpMainWindow.CB5Leave)
        else:
            #Option to animate or not
            Label(CheckButtonFrame, text="Translation Options",font=Font(size=ButtonDimensions.FontSize, underline=1,weight="bold"), bg=Colour2).pack()
            CB6=Checkbutton(CheckButtonFrame, text="Animate",font=Font(size=ButtonDimensions.FontSize),variable=AllBoxesChecked[2][0],indicatoron=0,width=ButtonDimensions.ButtonWidth, bg=Colour2, overrelief="groove", cursor=CursorType)
            CB6.pack(padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY, fill="x")
            if Help.HelpRequired==True:
                CheckButtons.CB6=CB6
                CB6.bind("<Enter>",SetUpMainWindow.CB6Entry)
                CB6.bind("<Leave>", SetUpMainWindow.CB6Leave)
                
        #This subroutine sets the checkboxes so that they do not get reset each time the random button is pressed
        AdvancedSelectionClass.SetCheckButtonVariables(AllBoxesChecked,CXC, CYC, CBC,RC,RAC, Animate)
        return AllBoxesChecked

   
#This subroutine is all about feedback and suggestions, is allows the user to press a button to enter comments
class SuggestionsAndFeedback:
    #This subroutine opens the suggestion file and writes the new suggestion to it
    def CreateSuggestion(Suggestions,CheckButtonFrame):
        if ActiveWindow.ActiveWindow==10:
            ActiveWindow.ActiveWindow=2
        file=open("Suggestions/Suggestions.txt","a")
        file.write(str(Suggestions)+"\n")
        SuggestionsAndFeedback.NewSuggestion(CheckButtonFrame)

    #This subroutine is used to close the suggestions box if the user decides not to give feedback
    def CloseSuggestion(Suggestions,CheckButtonFrame):
        SuggestionsAndFeedback.NewSuggestion(CheckButtonFrame)

    #This subroutine destroys the suggestion button and displays the frame in which the suggestions are made
    def UpdateSuggestion(CheckButtonFrame):
        #If the active window is 4 it is the shape creation interface
        if ActiveWindow.ActiveWindow==4:
            EntryFrame=EntryFrameClass2.EntryFrame
            #The frame must be positioned differently using grid due to existing widget positions
            SuggestionsWidgets.SuggestionButtonFrame=Frame(EntryFrame, bg=Colour2, padx=(ButtonDimensions.PaddingX)*2, pady=(ButtonDimensions.PaddingX)*2)
            SuggestionsWidgets.SuggestionButtonFrame.grid(padx=(ButtonDimensions.PaddingX//2), pady=10, column=0, row=1, columnspan=2)

        #If the active window is 1 it is the welcome window
        elif ActiveWindow.ActiveWindow==1:
            SuggestionsWidgets.SuggestionButtonFrame=Frame(SuggestionsWidgets.MiddleFrame, bg=Colour2, padx=(ButtonDimensions.PaddingX)*2, pady=(ButtonDimensions.PaddingX)*2)
            #The frame must be positioned differently using grid due to existing widget positions
            SuggestionsWidgets.SuggestionButtonFrame.grid(column=1, row=2, padx=(ButtonDimensions.PaddingX),)
        else:
            #On every other window the frame can just be packed
            SuggestionsWidgets.SuggestionButtonFrame=Frame(CheckButtonFrame, bg=Colour2, padx=(ButtonDimensions.PaddingX)*2, pady=(ButtonDimensions.PaddingX)*2)
            SuggestionsWidgets.SuggestionButtonFrame.pack(padx=(ButtonDimensions.PaddingX))
        if ActiveWindow.ActiveWindow==2:
            ActiveWindow.ActiveWindow=10
            
        #This creates a multi lined box for text to be entered and 2 buttons within the suggestion button frame
        TextBox=Text(SuggestionsWidgets.SuggestionButtonFrame,width=ButtonDimensions.ButtonWidth*2, bg=Colour2, height=6)
        TextBox.pack()
        TextBox2.TextBox=TextBox
        TextBox.bind("<Button-1>",SuggestionsAndFeedback.TextBoxClicked)
        #This will insert text into the text first line of the check box
        TextBox.insert("1.0","Please submit your feedback")

        #This button runs the subroutine that writes the text in the entry box to a text file
        Button(SuggestionsWidgets.SuggestionButtonFrame,text="Submit", bg=Colour2, height=ButtonDimensions.ButtonHeight, width=ButtonDimensions.ButtonWidth, command=lambda:SuggestionsAndFeedback.CreateSuggestion(TextBox.get('1.0', 'end'),CheckButtonFrame)).pack(pady=20, side="left")
        #This button runs a routine that just hides the box without writing the text
        Button(SuggestionsWidgets.SuggestionButtonFrame,text="Close", bg=Colour2, height=ButtonDimensions.ButtonHeight, width=ButtonDimensions.ButtonWidth, command=lambda:SuggestionsAndFeedback.CloseSuggestion(TextBox.get('1.0', 'end'),CheckButtonFrame)).pack(pady=20, side="right")
        SuggestionsWidgets.MakeSuggestionButton.destroy()

    #This routine will clear the text when the user clicks in the box
    def TextBoxClicked(self):
        TextBox=TextBox2.TextBox
        TextBox.delete("0.1","end")
        
    #This subroutine is where the feedback button is set up and positioned
    def NewSuggestion(CheckButtonFrame):
        BottomFrame=InitialFrameArray[3]
        SuggestionsWidgets.MakeSuggestionButton.destroy()
        SuggestionsWidgets.SuggestionButtonFrame.destroy()

        #This checks if the active screen is the main program
        if ActiveWindow.ActiveWindow==2:
            #This creates a feedback button that can be resized
            SuggestionsWidgets.MakeSuggestionButton=Button(BottomFrame,height=ButtonDimensions.ButtonHeight//2, width=ButtonDimensions.ButtonWidth, bg=Colour2, cursor=CursorType, text="Feedback",font=Font(size=ButtonDimensions.FontSize), command=lambda:(SuggestionsAndFeedback.UpdateSuggestion(CheckButtonFrame)))
            SuggestionsWidgets.MakeSuggestionButton.pack(side="left", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)
        else:
            #This button appears everywhere else and is not influenced by the size of the window
            SuggestionsWidgets.MakeSuggestionButton=Button(BottomFrame,height=InitialButtonDimensions.ButtonHeight//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, cursor=CursorType, text="Feedback",font=Font(size=InitialButtonDimensions.FontSize), command=lambda:(SuggestionsAndFeedback.UpdateSuggestion(CheckButtonFrame)))
            SuggestionsWidgets.MakeSuggestionButton.pack(side="left", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)
        

def NumbersOnAxis(LineWidth, MainCanvas):
     #This puts the numbers on the y axis
        for a in range(1,RowNum//2):
            MainCanvas.create_text((MidColumn*LineWidth)+LineWidth//2, (RowNum//2+a)*LineWidth, text=-a)
            MainCanvas.create_text((MidColumn*LineWidth)+LineWidth//2, (RowNum//2-a)*LineWidth, text=a)
        #This puts numbers on the x axis
        for b in range(1,ColumnNum//2):
            MainCanvas.create_text((ColumnNum//2-b)*LineWidth,(MidRow*LineWidth)+LineWidth//2, text=-b)
            MainCanvas.create_text((ColumnNum//2+b)*LineWidth,(MidRow*LineWidth)+LineWidth//2, text=b)

        #This marks the origin
        MainCanvas.create_text((MidColumn*LineWidth)+LineWidth//2, (RowNum//2)*LineWidth, text=0)
        MainCanvas.create_text( (ColumnNum//2)*LineWidth,(MidRow*LineWidth)+LineWidth//2, text=0)
        
            
#This creates a grid on the canvas, there are 2 situations in which this is used
def Checkered(MainCanvas, FancyGraph, LineWidth):
    if FancyGraph==False:
        ColumnNum2=ColumnNum//4
        RowNum2=RowNum//4
        #This creates a grid on the canvas creation window
        for x in range(0,RowNum2+1):
            MainCanvas.create_line(0,x*LineWidth,ColumnNum2*LineWidth,x*LineWidth,fill="lightgrey")
        for y in range(0,ColumnNum2+1):
            MainCanvas.create_line(y*LineWidth,0,y*LineWidth,RowNum2*LineWidth,fill="lightgrey")
    else:
        RowNum2=RowNum+1
        ColumnNum2=ColumnNum
        #This is needed on the main canvas, the top is left white o that the words show up better
        for x in range(1,RowNum2):
            MainCanvas.create_line(0,x*LineWidth,ColumnNum2*LineWidth,x*LineWidth,fill="lightgrey")
        for y in range(0,ColumnNum2):
            MainCanvas.create_line(y*LineWidth,LineWidth,y*LineWidth,(RowNum2-1)*LineWidth,fill="lightgrey")

    #This checks if the canvas been edited is the main canvas as it needs some additional features
    if FancyGraph==True:
        #This makes the central lines a different colour so that you can see where the axes are
        MainCanvas.create_line(0,MidRow*LineWidth,ColumnNum*LineWidth,MidRow*LineWidth,fill="#ff0040")
        MainCanvas.create_line(MidColumn*LineWidth,LineWidth,MidColumn*LineWidth,RowNum*LineWidth,fill="#ff0040")
        

#This subroutine is to find the real centre and rather than the number used in the difficulty slider
#This avoids it going off the screen
def FindBiggest():
    #New array for sorted coordiantes is created
    SortedXCoordinates=[]
    SortedYCoordinates=[]
    #the numbers are put in the arrays
    for x in range(len(ShapeToTransformX.Coordinates)):
        SortedXCoordinates.append(abs(int(ShapeToTransformX.Coordinates[x])))
        SortedYCoordinates.append(abs(int(ShapeToTransformY.Coordinates[x])))
        
    #The coordinates are sorted in ascending order
    SortedXCoordinates.sort()
    #changes it to descending order
    SortedXCoordinates.reverse()
    #The coordinates are sorted in ascending order
    SortedYCoordinates.sort()
    #changes it to descending order
    SortedYCoordinates.reverse()

    #The biggest number is at position [0]
    #This finds the biggest number in the array
    if SortedXCoordinates[0]>SortedYCoordinates[0]:
        Max=SortedXCoordinates[0]
    else:
        Max=SortedYCoordinates[0]

    #Ths finds the largest number of the 2 that add variety to the questions
    if abs(RotationClass.RandomNumberX)>abs(RotationClass.RandomNumberY):
        Biggest=abs(RotationClass.RandomNumberX)
    else:
        Biggest=abs(RotationClass.RandomNumberY)

    #This calculates the maximum room for manoeuvre
    Max=10-(Max+Biggest+1)
    
    #Prototyping showed that there was a problem that caused reflections to go off the canvas
    if AllWidgets.Choice=="Reflection":
        Max-=2

    #This updates the centre of rotation if needed
    if AllWidgets.CentreOfRotation>Max:
        AllWidgets.CentreOfRotation=Max

#This is where the transformations actually called
def PerformTransformations():
    AllBoxesChecked=AllWidgets.AllBoxesChecked
    InitialFrameArray=AllWidgets.InitialFrameArray

    #This puts checks on the main canvas
    LineWidth=CanvasStuff.LineWidth
    MainCanvas=AllWidgets.MainCanvas
    Checkered(MainCanvas, True, LineWidth)

    #Variables got from classes
    ModeSelect=AllWidgets.ModeSelect
    Choice=AllWidgets.Choice
    ShapeType=AllWidgets.ShapeType
    
    #This resets the coordinates
    ShapeToTransformX.Coordinates2=[]
    ShapeToTransformX.Coordinates3=[]
    ShapeToTransformY.Coordinates2=[]
    ShapeToTransformY.Coordinates3=[]
    
    #This sets the Coordinates to the placeholder values for if they have changed from their default
    ShapeToTransformX.Coordinates=ShapeToTransformX.CoordinatesPlaceholder
    ShapeToTransformY.Coordinates=ShapeToTransformY.CoordinatesPlaceholder

    #This generates random numbers to give the questions more variety
    RotationClass.RandomNumberX=random.randint(-3,3)
    RotationClass.RandomNumberY=random.randint(-3,3)

    #This finds the largest centre of rotation that is actually possible
    FindBiggest()
    CentreOfRotation=AllWidgets.CentreOfRotation

    #This runs the subroutines that perform the transformations
    if Choice=="Rotation":
        Transformation.Rotation(AllBoxesChecked,MainCanvas,CentreOfRotation)        
    elif Choice=="Reflection":
        Transformation.Reflection(AllBoxesChecked,CentreOfRotation)
    else:
        Transformation.Translation(CentreOfRotation,MainCanvas)    


#This subroutine is used to update the interface
def UpdateInterface():
    #This gets variables from classes
    InitialFrameArray=AllWidgets.InitialFrameArray
    MainCanvas=AllWidgets.MainCanvas
    ModeSelect=AllWidgets.ModeSelect
    Choice=AllWidgets.Choice
    ShapeType=AllWidgets.ShapeType

    #This sets the Coordinates to the placeholder values for if they have changed from their default
    ShapeToTransformX.Coordinates=ShapeToTransformX.CoordinatesPlaceholder
    ShapeToTransformY.Coordinates=ShapeToTransformY.CoordinatesPlaceholder

    #This gets the coordinates from the class
    XCoordinates=ShapeToTransformX.Coordinates
    YCoordinates=ShapeToTransformY.Coordinates

    #This looks at the type of transformation and the mode selected so that the answer button does what is expected
    #The questions will also be displayed
    if Choice == "Rotation":
        UpdateMainWindow.Rotation(ModeSelect, MainCanvas,InitialFrameArray)
    elif Choice == "Reflection":
        UpdateMainWindow.Reflection(ModeSelect, MainCanvas, InitialFrameArray)
    else:
        UpdateMainWindow.Translation(ModeSelect, MainCanvas, InitialFrameArray)
    NumbersOnAxis(CanvasStuff.LineWidth, AllWidgets.MainCanvas)

    #If the user has requested help then when they hover over the answer button it will explain what it does, when the mouse leaves
    #it will then change it back to how it looked at first
    if Help.HelpRequired==True:
        CheckButtons.Answer=RevealAnswers.ShowAnswerButton
        RevealAnswers.ShowAnswerButton.bind("<Enter>",SetUpMainWindow.AnswerEntry)
        RevealAnswers.ShowAnswerButton.bind("<Leave>", SetUpMainWindow.AnswerLeave)


#This subroutine calls other routines and sets up
def SetUpWidgets():
    #Get all of the variables from the class
    AllBoxesChecked=AllWidgets.AllBoxesChecked
    BackButton2=AllWidgets.BackButton2

    #The widgets that are not needed anymore are destroyed
    InitialFrameArray=AllWidgets.InitialFrameArray
    LeftFrame=InitialFrameArray[0]
    RightFrame=InitialFrameArray[1]
    AllWidgets.BackButton2.destroy()
    RightFrame.destroy()
    LeftFrame.destroy()
    
    #Set up the frames needed for the main window
    LeftFrame=Frame(root, bg=Colour3)
    LeftFrame.pack(fill="both", expand="yes", side="left")
    RightFrame=Frame(root, bg=Colour2)
    RightFrame.pack(fill="both", side="right")
    AllWidgets.InitialFrameArray[1]=RightFrame
    AllWidgets.InitialFrameArray[0]=LeftFrame
    
    #This deals with the Settings file
    StudentGroupData,File=SetUpMainWindow.OpenStudentGroupData(AllBoxesChecked)
    
    #This creates a frame for the radio button options
    RadioButtonFrame=Frame(RightFrame,bg=Colour2,)
    RadioButtonFrame.grid(column=0, row=3, sticky="ew")

    #This creates the random button, when clicked it will load a new question
    RandomButton=Button(RightFrame, text="New Question",font=Font(size=ButtonDimensions.FontSize), cursor="exchange", bg=Colour2, width=ButtonDimensions.ButtonWidth, height=ButtonDimensions.ButtonHeight,
                        command=lambda:CreateMainWindow("self"))
    RandomButton.grid(column=0, row=0, pady=ButtonDimensions.PaddingY, padx=ButtonDimensions.PaddingX)

    #If the user has asked for help then when hovering over the button help will be displayed, when hover leaves it goes back to normal
    if Help.HelpRequired==True:
        CheckButtons.NewQuestion=RandomButton
        RandomButton.bind("<Enter>",SetUpMainWindow.NewQuestionEntry)
        RandomButton.bind("<Leave>", SetUpMainWindow.NewQuestionLeave)

    #This creates the canvas
    MainCanvas=Canvas(LeftFrame, height=RowNum*CanvasStuff.LineWidth, width=ColumnNum*CanvasStuff.LineWidth, background="white")
    MainCanvas.pack(expand="yes")
    AllWidgets.MainCanvas=MainCanvas
    
    #This allows the user to select how random the centre of rotation to be, from 0 to maximum
    CentreOfRotation, Choice=SetUpMainWindow.SliderValue(RightFrame,RadioButtonFrame, StudentGroupData[3],StudentGroupData[4])
    Selection=AllWidgets.Selection

    #This creates the shape drop down
    ShapeType=SetUpMainWindow.LoadShapeMenu(RadioButtonFrame, Selection, StudentGroupData[12])
    SetUpMainWindow.LoadShapeMainWindow(ShapeType.get())

    #This allows the mode to be set using radio buttons
    ModeSelect=SetUpMainWindow.RadioButtons(RadioButtonFrame, StudentGroupData[5], Selection)

    #This sets up the CheckBoxes allowing for more specific options to be selected
    AllBoxesChecked=[[StudentGroupData[9],StudentGroupData[10]],[StudentGroupData[6],StudentGroupData[7],StudentGroupData[8]],[StudentGroupData[11]]]
    AllBoxesChecked=SetUpMainWindow.CheckBoxes(AllBoxesChecked, StudentGroupData[4], RightFrame, RadioButtonFrame)
    AllWidgets.AllBoxesChecked=AllBoxesChecked

    #This creates a back button so that the user can go back to the welcome window
    BackButton2 = Button (BottomFrame, text="Back",font=Font(size=ButtonDimensions.FontSize), height=ButtonDimensions.ButtonHeight//2, width=ButtonDimensions.ButtonWidth, bg=Colour2,
                          command=lambda: AreYouSure(ShapeType.get(),[[AllBoxesChecked[0][0].get(), AllBoxesChecked[0][1].get()],[AllBoxesChecked[1][0].get(), AllBoxesChecked[1][1].get(), AllBoxesChecked[1][2].get()],[AllBoxesChecked[2][0].get()]],InitialFrameArray,Continue2,"Back",BackButton2, MainCanvas,ModeSelect.get(),CentreOfRotation.get(), Choice.get()))
    BackButton2.pack(side="right", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)

    #This updates the class with new variable values so that they can be accessed without having to be passed as arguments
    AllWidgets.ModeSelect2=ModeSelect
    AllWidgets.CentreOfRotation2=CentreOfRotation
    AllWidgets.Choice2=Choice
    AllWidgets.ShapeType2=ShapeType
    AllWidgets.RandomButton=RandomButton
    AllWidgets.BackButton2=BackButton2



#This subroutine can be called to deal with creating a new question 
def CreateMainWindow(self):
    if ActiveWindow.ActiveWindow==2:
        SuggestionsAndFeedback.NewSuggestion(root)

        #This gets the user's settings selections and saves them to classes
        ModeSelect=AllWidgets.ModeSelect2
        AllWidgets.ModeSelect=ModeSelect.get()
        CentreOfRotation=AllWidgets.CentreOfRotation2
        AllWidgets.CentreOfRotation=CentreOfRotation.get()
        Choice=AllWidgets.Choice2
        Choice=AllWidgets.Choice=Choice.get()
        ShapeType=AllWidgets.ShapeType2
        AllWidgets.ShapeType=ShapeType.get()

        AllBoxesChecked = AllWidgets.AllBoxesChecked
        AllWidgets.AllBoxesChecked=[[AllBoxesChecked[0][0].get(), AllBoxesChecked[0][1].get()],[AllBoxesChecked[1][0].get(), AllBoxesChecked[1][1].get(), AllBoxesChecked[1][2].get()],[AllBoxesChecked[2][0].get()]]

        #These subroutines create the new question in full
        SetUpWidgets()
        PerformTransformations()
        UpdateInterface()


#This subroutine gets the selected group from the drop down menu and opens the student group
def GetSelection(Selection):
    GroupSelected.Selection=Selection
    SuggestionsAndFeedback.NewSuggestion(root)
    try:
        root.wm_title("Transformations for "+Selection)

        #Opens and reads the student group
        StudentGroup="StudentGroups/"+Selection+ ".txt"
        FileToOpen=open(StudentGroup, "r")

        #The individual lines of the read file are loaded into an array
        Contents=FileToOpen.read().split("\n")
        FileToOpen.close()
        RootFrame1=InitialFrameArray[4]
        RootFrame1.destroy()

        #Some variables are set using the data from the file
        AllWidgets.ClassName=Contents[0]
        AllWidgets.TeacherName=Contents[1]
        AllWidgets.YearGroup=Contents[2]
        AllWidgets.CentreOfRotation=Contents[3]
        AllWidgets.Choice=Contents[4]
        AllWidgets.ModeSelect=Contents[5]
        AllWidgets.AllBoxesChecked=[[Contents[9],Contents[10]],[Contents[6],Contents[7],Contents[8]],[Contents[11]]]
        AllWidgets.ShapeType=Contents[12]
        AllWidgets.InitialFrameArray=InitialFrameArray

        #This tries to get the real values of the variables but sometimes this is not possible for example when a new file is opened
        try:
            AllWidgets.AllBoxesChecked=[[AllBoxesChecked[0][0].get(), AllBoxesChecked[0][1].get()],[AllBoxesChecked[1][0].get(), AllBoxesChecked[1][1].get(), AllBoxesChecked[1][2].get()],[AllBoxesChecked[2][0].get()]]
        except:
            AllBoxesChecked=AllWidgets.AllBoxesChecked
            AllWidgets.AllBoxesChecked=AllBoxesChecked
        AllWidgets.Selection=Selection
        ActiveWindow.ActiveWindow=2

        #This creates the widgets needed for the main window so that the main window can be created
        SetUpWidgets()       
    except:
        #If there is a problem and no group is selected from the drop down list, then a message box will be displayed
        messagebox.showerror("Small error","You need to choose a class from the drop down menu")
    CreateMainWindow("Self")
    
#This subroutine asks for confirmation when quitting or using the back button
def AreYouSure(ShapeType,AllBoxesChecked,InitialFrameArray,Continue2,ButtonPress,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice):
    #If the back button is pressed a message box confirmation appears checking that the user really wants to go back
    if ButtonPress=="Back":
        Response=messagebox.askyesno("Please confirm","Do you really want to exit to the options menu?")

        #Only if the user clicks yes does the program exit
        if Response==True:
            ActiveWindow.ActiveWindow=1
            Continue2.destroy()
            CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)
            Help.DeleteLabel.destroy()

    #If the back button is pressed a message box confirmation appears checking that the user really wants to go back
    if ButtonPress=="Back2":
        Response=messagebox.askyesno("Please confirm","Do you really want to exit to the options menu?")

        #Only if the user clicks yes does the program exit
        if Response==True:
            ActiveWindow.ActiveWindow=1
            EntryFrame=EntryFrameClass2.EntryFrame
            EntryFrame.destroy()
            Continue2.destroy()
            CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)
            EntryFrameClass2.CreateShapeButton.destroy()
            Help.DeleteLabel.destroy()

    #If the back button is pressed a message box confirmation appears checking that the user really wants to go back
    if ButtonPress=="Back3":
        Response=messagebox.askyesno("Please confirm","Do you really want to exit to the options menu?")
        #Only if the user clicks yes does the program exit
        if Response==True:
            Help.DeleteLabel.destroy()
            ActiveWindow.ActiveWindow=1
            StudentGroupWidgets.Continue2.destroy()
            StudentGroupWidgets.Button.destroy()
            Menu2=StudentGroupWidgets.DropDown.destroy()
            StudentGroupWidgets.DeleteClassTitle.destroy()
            CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

    #This creates a help label so that it can be destroyed without been displayed
    Help.DeleteLabel=Label()


#This creates the initial interface that the user sees
def CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType):
    SuggestionsAndFeedback.NewSuggestion(root)
    #This removes some frames and widgets that are unnecessary
    RootFrame4.pack_forget()
    BottomFrame=InitialFrameArray[3]
    InitialFrameArray[5].destroy()
    BackButton2.destroy()
    InitialFrameArray[0].destroy()
    InitialFrameArray[1].destroy()

    #This creates a back button but disables it, this means that the interface is consistent
    BackButton2=Button(BottomFrame,text="Back",font=Font(size=InitialButtonDimensions.FontSize), height=(InitialButtonDimensions.ButtonHeight)//2, width=InitialButtonDimensions.ButtonWidth, bg=Colour2, state="disabled")
    BackButton2.pack(side="right", padx=InitialButtonDimensions.PaddingX, pady=InitialButtonDimensions.PaddingY)
    Help.BackButton2=BackButton2
    AllWidgets.BackButton2=BackButton2

    #This opens the StudentGroup file and creates an array with each separate lines
    MyFile=open("StudentGroups/Classes.txt", "r")
    Classes=MyFile.read().split("\n")
    MyFile.close()

    #This deletes the bits that would cause an error in case a file gets deleted
    #The deleted items won't show up in the drop down list as they would cause an error if selected
    Deletions=0
    for x in range(0,len(Classes)):
        #As the array is getting shorter this ensures that none are missed and that it is not out of range
        FileName=str(Classes[x-Deletions]) + ".txt"
        try:
            #This attempts to open the files
            MyFile=open("StudentGroups/"+FileName, "r")
            MyFile.close()
        except:
            #This deletes any class names from the list if they could not be opened
            Classes.pop(x-Deletions)
            Deletions+=1
    RootFrame2.destroy()

    #This creates 3 frames
    BottomFrame=InitialFrameArray[3]
    RootFrame1=Frame(root)
    TopFrame = Frame(RootFrame1, bg=Colour3)
    MiddleFrame = Frame(RootFrame1, bg=Colour3)
    InitialFrameArray[2]=TopFrame
    InitialFrameArray[4]=RootFrame1

    #If after checking the file against the files that exist there are no items remaining a new file will be created
    if len(Classes)==0:
        #A default file is opened
        DefaultFile=open("StudentGroups/"+"Default.txt", "w")
        MyFile=open("StudentGroups/"+"Classes.txt","a")
        MyFile.write("Defaults")
        MyFile.close()
        #Some default values are set and then written to the file
        StudentGroupData=["Default Class", "The best teacher in the world", "Your Year group", 0, "Translation", 1,0,0,0,0,0,0, "LShape"]
        Initialisation.WriteVariables(DefaultFile, StudentGroupData)
        DefaultFile.close()
        Classes.append("Default")
    
    #This positions the frames on the screen
    TopFrame.pack(fill="both", side="top", expand="yes")
    MiddleFrame.pack(fill="both", expand="yes")
    RootFrame1=InitialFrameArray[4]
    RootFrame1.pack()

    #This creates a title for the program
    Label(TopFrame,bg=Colour3, text="Transformation Question Generator", font=Font(size=20, weight="bold", underline=1)).pack(pady=20)
    
    #This creates a drop down menu for the student group selection
    Selection = StringVar()
    Classes.reverse()
    Menu=OptionMenu(MiddleFrame, Selection, *Classes)
    Menu.grid(row=0, column=2, columnspan=2,padx=(InitialButtonDimensions.PaddingX)*2, pady=(InitialButtonDimensions.PaddingY)*2)
    Menu.config(bg=Colour2,highlightbackground=Colour2,font=Font(size=InitialButtonDimensions.FontSize))
    Menu["menu"].config(bg=Colour2,font=Font(size=InitialButtonDimensions.FontSize))
    Selection.set(GroupSelected.Selection)

    GroupSelected.Selection=Selection

    #This imports photos to use for the buttons
    Image1=PhotoImage(file="Images/StudentGroupCreation.gif")
    Image2=PhotoImage(file="Images/ShapeCreation.gif")
    Image3=PhotoImage(file="Images/MainWindow.gif")
    Image5=PhotoImage(file="Images/Deletions.gif")
    Image6=PhotoImage(file="Images/DeleteShape.gif")

    #This creates the buttons in the same way but with a different command
    #Each button runs a different subroutine when clicked so that it takes the user to a different part of the program
    #Each button has an image that is displayed on it so that the user can see what screen they are navigating too easily
    #If the user has clicked the help button when they hover over any of the buttons the appearance will change to display help
    #When the mouse no longer hovers the button the help will disappear and the button will return to its previous appearance
    
    NewStudentGroup=Button(MiddleFrame, image=Image1, compound="top",text = "\nCreate New\nStudent Group\n",font=Font(size=InitialButtonDimensions.FontSize), bg=Colour2, command=lambda:NewStudentGroupInterface.CreateClassWindow(Selection.get(), AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice))
    NewStudentGroup.image=Image1
    NewStudentGroup.grid(column=0, row=1, padx=(InitialButtonDimensions.PaddingX)//2, pady=(InitialButtonDimensions.PaddingY)*2)
    if Help.HelpRequired==True:
        CheckButtons.NewStudentGroup=NewStudentGroup
        NewStudentGroup.bind("<Enter>",SetUpMainWindow.NewStudentGroupEntry)
        NewStudentGroup.bind("<Leave>", SetUpMainWindow.NewStudentGroupLeave)

    CreateNewShape=Button(MiddleFrame,image=Image2, compound="top", text = "\nCreate New\nShape\n",font=Font(size=InitialButtonDimensions.FontSize), bg=Colour2, command=lambda:NewShapeInterface.WelcomeScreen(Selection.get(),ShapeType,AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice))
    CreateNewShape.image=Image2
    CreateNewShape.grid(column=1, row=1, padx=(InitialButtonDimensions.PaddingX)//2, pady=(InitialButtonDimensions.PaddingY)*2)
    if Help.HelpRequired==True:
        CheckButtons.NewShape=CreateNewShape
        CreateNewShape.bind("<Enter>",SetUpMainWindow.NewShapeEntry)
        CreateNewShape.bind("<Leave>", SetUpMainWindow.NewShapeLeave)
        
    Continue = Button (MiddleFrame,image=Image3, compound="top", text="\nAdvance to\nTransformation Questions\n",font=Font(size=InitialButtonDimensions.FontSize+5), bg=Colour2, padx=60, pady=60,command=lambda:GetSelection(Selection.get()))
    Continue.image=Image3
    Continue.grid(column=2, columnspan = 2, rowspan=2, row=1,padx=(InitialButtonDimensions.PaddingX)//2, pady=(InitialButtonDimensions.PaddingY)*2)
    if Help.HelpRequired==True:
        CheckButtons.MainWindow=Continue
        Continue.bind("<Enter>",SetUpMainWindow.MainWindowEntry)
        Continue.bind("<Leave>", SetUpMainWindow.MainWindowLeave)
        
    StudentDeleteButton=Button(MiddleFrame,image=Image5, compound="top", text="\nDelete a\nStudent Group\n", font=Font(size=InitialButtonDimensions.FontSize), bg=Colour2, command=lambda:DeleteStudentInterface.SetUpDeleteClass(Selection.get(), AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice))
    StudentDeleteButton.image=Image5
    StudentDeleteButton.grid(column=0, row=2)
    CheckButtons.DeleteGroup=StudentDeleteButton
    if Help.HelpRequired==True:
        StudentDeleteButton.bind("<Enter>",SetUpMainWindow.DeleteGroupEntry)
        StudentDeleteButton.bind("<Leave>", SetUpMainWindow.DeleteGroupLeave)
        
    ShapeDeleteButton=Button(MiddleFrame,image=Image6, compound="top", text="\nDelete a\nShape\n", font=Font(size=InitialButtonDimensions.FontSize), bg=Colour2, command=lambda:DeleteShapeInterface.SetUpDeleteShape(Selection.get(), ShapeDeleteButton,AllBoxesChecked,InitialFrameArray,BackButton2,MainCanvas,ModeSelect,CentreOfRotation, Choice))
    ShapeDeleteButton.image=Image6
    ShapeDeleteButton.grid(column=1, row=2)
    if Help.HelpRequired==True:
        CheckButtons.DeleteShape=ShapeDeleteButton
        ShapeDeleteButton.bind("<Enter>",SetUpMainWindow.DeleteShapeEntry)
        ShapeDeleteButton.bind("<Leave>", SetUpMainWindow.DeleteShapeLeave)

    SuggestionsWidgets.MiddleFrame=MiddleFrame

#This subroutine is used when the help button is pressed to reload the appropriate window with help
def ToggleHelp(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType):
    #This is used to toggle whether the help is on or off
    if Help.HelpRequired==True:
        Help.HelpRequired=False
        Help.HelpButton.configure(relief="raised")
    else:
        #When help is turned on a messagebox is displayed telling the user how to use it
        messagebox.showinfo("Help","When help is on, hovering over buttons highlights them blue and displays a description.\nYou can knock help off at any time by pressing the help button again")
        Help.HelpRequired=True
        Help.HelpButton.configure(relief="sunken")

    #If the welcome window is in use it will be recreated so that all of the widgets will be set to change what they do when hovered over
    if ActiveWindow.ActiveWindow==1:
        GroupSelected.Selection="-Select the Student Group to Load-"
        RootFrame1=InitialFrameArray[4]
        RootFrame1.destroy()
        Help.BackButton2.destroy()
        CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

    #If the main window is in use it will be recreated so that all of the widgets will be set to change what they do when hovered over
    elif ActiveWindow.ActiveWindow==2:
        CreateMainWindow("self")

    #If this screen is in use a label will be displayed at the bottom of the screen explaining how to use it
    elif ActiveWindow.ActiveWindow==3:
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can create a new student group\nso that you can save settings for specific\nstudents so that you don't need to remember where you are up to\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel.destroy()

    #If this screen is in use a label will be displayed at the bottom of the screen explaining how to use it
    elif ActiveWindow.ActiveWindow==4:
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can create a new shape\nso that you can make new and\nmore varied transformations\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel.destroy()

    #If this screen is in use a label will be displayed at the bottom of the screen explaining how to use it
    elif ActiveWindow.ActiveWindow==5:
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can delete a shape\nso that it does not appear and cannot be used\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel.destroy()

    #If this screen is in use a label will be displayed at the bottom of the screen explaining how to use it
    else:
        if Help.HelpRequired==True:
            Help.DeleteLabel=Label(root,text="\nHere you can delete a student group\nso that it does not appear and cannot be used\n", bg=Colour1)
            Help.DeleteLabel.pack(side="bottom", fill="x", pady=10)
        else:
            Help.DeleteLabel.destroy()



#Main program
#Colours to use
Colour1="#737bf2" #Blue
Colour2="#97ee96" #Green
Colour3="#B785E8" #purple
Colour4="#1ca202" #Dark green
Colour5="#c40b0b" #red
Colour6="#1ca202" #Centre of rotation colour

#This sets up the root window that the whole program is built in
root=Tk()
#This gives the window a title
root.wm_title("Grid")
#This sets the background colour to purple
root.configure(bg=Colour3)
#This maximises the window
root.state("zoomed")
#When the spacebar a new question will be generated
root.bind("<space>", CreateMainWindow)
#This sets the minimum size of the window if it is resized
root.minsize(775,475)
#This prevents the window from automatically resizing
root.pack_propagate(0)

#Creates an L shape with these coordinates
ShapeToTransformX=ShapeSetup([1,2,2,3,2,3,2,3],[])
ShapeToTransformY=ShapeSetup([3,4,1,2,2,3,3,4],[])

#Various frames needed for different screens are set up
RootFrame4=Frame(root, bg=Colour3)
RootFrame1=(root)
RootFrame2=Frame(root)

#This sets up the arrays needed for representing the checkboxes
RotationArray=[1,0]             #[RotateClockwise, RotateAntiClockwise]
ReflectionBoxesArray=[1, 0, 0]  #[CheckboxXChecked, CheckboxYChecked, CheckboxBothChecked]
AnimateArray=[1]                #[Animate]
#This creates a 2D array to hold check button values
AllBoxesChecked=[RotationArray, ReflectionBoxesArray, AnimateArray]

#This sets the type of cursor to be used along with other default choices
CursorType="dotbox"
Choice="Reflection"
ModeSelect=1
CentreOfRotation=0
ShapeType=ShapeToTransformX.ShapeType

#This creates some initial frames that are used in other subroutines
TopFrame=Frame(root, bg=Colour1, height=20)
TopFrame.pack(fill="x")
BottomFrame=Frame(root, bg=Colour1, height=10)
BottomFrame.pack(fill="x",side="bottom")
LeftFrame=Frame(root, bg=Colour3)
RightFrame=Frame(root, bg=Colour1)

#The frames are put into an array to make it easier to pass them through subroutines
InitialFrameArray=[LeftFrame, RightFrame, TopFrame, BottomFrame, RootFrame1, RootFrame2]

#This sets up the class that will hold the window size
WindowSize=SizeOfWindow()
#This updates the window
root.update()
#This gets the window size and saves it in the class
WindowSize.WindowHeight=root.winfo_height()
WindowSize.WindowWidth=root.winfo_width()

#The classes are made ready to use and will be accessible in all subroutines
AllWidgets=ResizeAttributes()
ActiveWindow=CurrentWindow()
TextBox2=TextBoxClass()
CheckButtons=CheckButtonClass()
Help=HelpClass()
StudentGroupWidgets=ThingsToDestroy()
QuestionAnswer=QuestionAnswerClass()

#This will set the variable to true as the program will be running through its first cycle
AllWidgets.FirstTime=True

#The classes are made ready to use and will be accessible in all subroutines
ButtonDimensions=ButtonSizes()
InitialButtonDimensions=ButtonSizes()
CreateQuestion=QuestionStuffClass()
EntryFrameClass2=EntryFrameClass()
GroupSelected=GroupSelectedClass()

#This will be used when the user wants to give feedback
SuggestionsWidgets=SuggestionButtons()

#This creates the help button
Image4=PhotoImage(file="Images/HelpButton.gif")
print("Active",ActiveWindow.ActiveWindow)
Help.HelpButton=Button(BottomFrame, image=Image4, bg=Colour1, cursor=CursorType,font=Font(size=ButtonDimensions.FontSize), command=lambda:ToggleHelp(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType))
Help.HelpButton.image=Image4
Help.HelpButton.pack(side="right", padx=ButtonDimensions.PaddingX, pady=ButtonDimensions.PaddingY)

#Size of the grid is set
CanvasStuff=LineWidthClass()
ColumnNum=10
RowNum=10
LineWidth=CanvasStuff.LineWidth
LineWidth2=100

#This creates the canvas for the user to create shapes on
CanvasCreation=Canvas(RootFrame4, width=(ColumnNum//2)*LineWidth2, height=(RowNum//2)*LineWidth2, bg="#ce9be8")
CanvasCreation.grid(column=0, row=1, pady=25, padx=20)

#Another class is set up
RotationClass=ClassForRotation()

#This means that each side of the axes has the number of rows/columns specified initially
ColumnNum*=2
RowNum*=2

#This represents the middle of the canvas
MidRow=RowNum//2
MidColumn=ColumnNum//2

#This creates the main canvas
MainCanvas=Canvas(LeftFrame, height=RowNum*CanvasStuff.LineWidth, width=ColumnNum*CanvasStuff.LineWidth, background="white")
MainCanvas.pack(expand="yes")

#This creates a back button and a continue button
BackButton2 = Button(root)
Continue2 = Button(root)

#This creates the initial interface
CreateWelcomeWindow(AllBoxesChecked,InitialFrameArray,BackButton2, MainCanvas,ModeSelect,CentreOfRotation, Choice, ShapeType)

#This creates a label placeholder so that it can be destroyed before it is actually used if necessary
Help.DeleteLabel=Label()


#This subroutine will wait for changes of window height and transformation type, when a change occurs it will respond
def ResizeWidgets(Thing):
    AllWidgets.InitialChoice=AllWidgets.Choice2
    #This gets the current height of the window
    WindowSize.InitialWindowHeight=root.winfo_height()
    WindowSize.InitialWindowWidth=root.winfo_width()
    WindowSize.MyVariable=False
    ChangeSize=False
    ChangeInitialChoice=False
    #This keeps looping until the variable is true
    while not WindowSize.MyVariable:
        try:
            #This gets the new window size
            WindowSize.WindowHeight=root.winfo_height()
            WindowSize.WindowWidth=root.winfo_width()
            #This pauses for 0.1 seconds
            time.sleep(0.1)

            #This checks if the current window size is the same as the saved window size
            while (root.winfo_height() != WindowSize.WindowHeight) or (root.winfo_width() != WindowSize.WindowWidth):
                #If different the new sizes will be saved
                WindowSize.WindowHeight=root.winfo_height()
                WindowSize.WindowWidth=root.winfo_width()
                #This means that during the window resizing that if you stop moving for more than 0.1 seconds the size it was then will be done
                time.sleep(0.1)
                #The widget size will then need to be changed
                ChangeSize=True

            #This checks that the user is on the transformation window
            if ActiveWindow.ActiveWindow==2:
                try:
                    #This checks if the transformation type has changed
                    if (AllWidgets.InitialChoice != AllWidgets.Choice2.get()) and ChangeInitialChoice==False:
                        ChangeInitialChoice=True
                except:
                    print()

            #This ensures that no unnecessary things happen
            if ChangeSize==True:
                ChangeInitialChoice=False

            #If the choice has changed this code will be executed
            if ChangeInitialChoice==True:
                AllWidgets.InitialChoice = AllWidgets.Choice2.get()
                ChangeInitialChoice=False
                #This will create a new question 
                CreateMainWindow("self")

            if ChangeSize==True:
                #Once you are happy you have 1 second to release the click otherwise it will resize to the previous size
                time.sleep(1)
                #This gets the new size of the window
                WindowSize.WindowHeight=root.winfo_height()
                WindowSize.WindowWidth=root.winfo_width()
                #The code will only run if the active screen is the transformation screen
                if ActiveWindow.ActiveWindow==2:
                    #This changes the widget sizes
                    ButtonDimensions.ButtonWidth=WindowSize.WindowWidth//50
                    ButtonDimensions.PaddingY=WindowSize.WindowHeight//200
                    ButtonDimensions.ButtonHeight=WindowSize.WindowHeight//150
                    ButtonDimensions.PaddingX=WindowSize.WindowWidth//100
                    #The font size is changed based on the height of the window
                    if WindowSize.WindowWidth//120 > WindowSize.WindowHeight//120:
                        ButtonDimensions.FontSize=WindowSize.WindowHeight//70
                    if WindowSize.WindowHeight>550:
                        ButtonDimensions.FontSize=WindowSize.WindowHeight//100

                    CanvasStuff.LineWidth=WindowSize.WindowHeight//25
                    SuggestionsAndFeedback.NewSuggestion(root)
                    AllWidgets.InitialChoice = AllWidgets.Choice2.get()
                    #This creates all of the widgets on the main window again at a more appropriate size
                    CreateMainWindow("self")
                    ChangeSize=False
        except:
            break

#This will run the subroutine in parallel with the rest of the program
WindowThread = threading.Thread(target=ResizeWidgets, args=("hi",))
WindowThread.start()

root.mainloop()
