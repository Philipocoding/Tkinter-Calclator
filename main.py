import tkinter
import customtkinter

#------------Calculator Methods---------------#

calculation = ""
answer = ""
def clearResult():
    global calculation
    calculation = ""
    ResultLabel.delete(1.0, "end")
    pass

def DeleteValue():
    global calculation
    if len(calculation) > 0:
        calculation = calculation[:-1]

    ResultLabel.delete(1.0, "end")
    ResultLabel.insert("end", calculation)    



def updateCalculation(value):
    global calculation
    try:
        newCalculation = calculation + str(value)
        calculation = ""
        calculation = newCalculation
        ResultLabel.delete(1.0, "end")
        ResultLabel.insert("end", calculation)   
    except:
        ResultLabel.insert(1.0, "Error")   

def calculateResult():
    global calculation
    global answer
    try:
        answer = str(eval(calculation))
        ResultLabel.delete(1.0, "end")
        ResultLabel.insert("end", answer)   
        calculation = answer
    except:
        ResultLabel.delete(1.0, "end")
        ResultLabel.insert(1.0, "Error")   
    
#-----------------UI setup------------------#
value_x = 354
value_y = 520
button_x = 70
button_y = 70
app = customtkinter.CTk()
app.geometry("450x550")
app.title("Calculator")
app.maxsize(value_x,value_y)
app.minsize(value_x,value_y)

ResultLabel = customtkinter.CTkTextbox(app, height=150, width = value_x, font = ("Arial", 35))
ResultLabel.grid(row = 0, column = 0, columnspan = 4)

#---------------Column_1------------------#
button_7 = customtkinter.CTkButton(app, fg_color=("slate gray"),command = lambda: updateCalculation(7), height = button_y, width = button_x, text = "7",font = ("Arial", 28))
button_7.grid(row = 1,column = 0, padx = 1, pady = 1)

button_4 = customtkinter.CTkButton(app,fg_color=("slate gray"), command = lambda: updateCalculation(4),height = button_y, width = button_x,font = ("Arial", 28), text = "4")
button_4.grid(row = 2,column = 0,padx = 1, pady = 1)

button_1 = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation(1), height = button_y, width = button_x, font = ("Arial", 28), text = "1")
button_1.grid(row = 3,column = 0,padx = 1, pady = 1)

button_0 = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation(0),height = button_y, width = button_x, font = ("Arial", 28), text = "0")
button_0.grid(row = 4,column = 0, padx = 1, pady = 1)
#---------------Column_2------------------#
button_8 = customtkinter.CTkButton(app, fg_color=("slate gray"),command = lambda: updateCalculation(8),height = button_y, width = button_x, font = ("Arial", 28), text = "8")
button_8.grid(row = 1,column = 1, padx = 1, pady = 1)

button_5 = customtkinter.CTkButton(app, fg_color=("slate gray"),command = lambda: updateCalculation(5),height = button_y, width = button_x, text = "5",font = ("Arial", 28))
button_5.grid(row = 2,column = 1,padx = 1, pady = 1)

button_2 = customtkinter.CTkButton(app, fg_color=("slate gray"),command = lambda: updateCalculation(2),height = button_y, width = button_x, text = "2",font = ("Arial", 28))
button_2.grid(row = 3,column = 1,padx = 1, pady = 1)

button_Point = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation("."), height = button_y, width = button_x, text = ".",font = ("Arial", 50))
button_Point.grid(row = 4,column = 1, padx = 1, pady = 1)

#---------------Column_3------------------#
button_9 = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation(9), height = button_y, width = button_x, text = "9",font = ("Arial", 28))
button_9.grid(row = 1,column = 2, padx = 1, pady = 1)

button_6 = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation(6), height = button_y, width = button_x, text = "6",font = ("Arial", 28))
button_6.grid(row = 2,column = 2,padx = 1, pady = 1)

button_3 = customtkinter.CTkButton(app,fg_color=("slate gray"),command = lambda: updateCalculation(3), height = button_y, width = button_x, text = "3",font = ("Arial", 28))
button_3.grid(row = 3,column = 2,padx = 1, pady = 1)

button_Delete = customtkinter.CTkButton(app,fg_color=("slate gray"), command = lambda: DeleteValue(), height = button_y, width = button_x, text = "Del",font = ("Arial", 28))
button_Delete.grid(row = 4,column = 2, padx = 1, pady = 1)

#---------------Column_4------------------#
button_Divide = customtkinter.CTkButton(app, fg_color=("light sea green"), command = lambda: updateCalculation("/"),height = button_y, width = button_x, text = "÷",font = ("Arial", 28))
button_Divide.grid(row = 1,column = 3, padx = 1, pady = 1)

button_Multiply = customtkinter.CTkButton(app, fg_color=("light sea green"), command = lambda: updateCalculation("*"), height = button_y, width = button_x, text = "×",font = ("Arial", 28))
button_Multiply.grid(row = 2,column = 3,padx = 1, pady = 1)

button_Plus = customtkinter.CTkButton(app, fg_color=("light sea green"), command =lambda:  updateCalculation("+"), height = button_y, width = button_x, text = "+",font = ("Arial", 28))
button_Plus.grid(row = 3,column = 3,padx = 1, pady = 1)

buttonMinus = customtkinter.CTkButton(app, fg_color=("light sea green"),command = lambda: updateCalculation("-"), height = button_y, width = button_x, text = "-",font = ("Arial", 28))
buttonMinus.grid(row = 4,column = 3, padx = 1, pady = 1)

#----------------Row 5 added-----------------

button_Left_Bracket = customtkinter.CTkButton(app, fg_color=("slate gray"), command = lambda: updateCalculation("("), height = button_y, width = button_x, text = "(",font = ("Arial", 28))
button_Left_Bracket.grid(row = 5,column = 0,padx = 1, pady = 1)

button_Right_Bracket = customtkinter.CTkButton(app, fg_color=("slate gray"),command = lambda: updateCalculation(")"), height = button_y, width = button_x, text = ")",font = ("Arial", 28))
button_Right_Bracket.grid(row = 5,column = 1,padx = 1, pady = 1)

button_Clear = customtkinter.CTkButton(app, fg_color=("slate gray"), command = lambda: clearResult(), height = button_y, width = button_x, text = "AC",font = ("Arial", 28))
button_Clear.grid(row = 5,column = 2,padx = 1, pady = 1)

button_Equals = customtkinter.CTkButton(app,  fg_color=("dark orange"), command = lambda: calculateResult(), height = button_y, width = button_x, text = "=",font = ("Arial", 28))
button_Equals.grid(row=5, column=3, padx = 1, pady = 1)
app.mainloop()
