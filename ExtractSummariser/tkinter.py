# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:09:06 2021

@author: aj240
"""
import tkinter as tk
import summary_extraction as se
import re
# Function to clear both the text areas 
def clearAll() : 
    # whole content of text area  is deleted  
    text1_field.delete(1.0, tk.END) 
    text2_field.delete(1.0, tk.END) 
    
# summarizer function
def summarize():
    
    #get input from text box
    input_text = text1_field.get("1.0", "end")[:-1]
    input_text=re.sub(r"\s\([A-Z][a-z]+,\s[A-Z][a-z]?\.[^\)]*,\s\d{4}\)", "", input_text)
    output_text = se.summary(input_text)

    text2_field.insert('end -1 chars', output_text)
    
#driver code
if __name__ == "__main__" :
    
    #creating gui window
    root = tk.Tk()
    
    #setting background colour
    root.config(background = "white")
    
    #set configuration of gui window (width and height)
    root.geometry("820x600")
    
    #set the name of tkinter gui window
    root.title("summarizer")
    
    #create welconme label
    tk.headlabel = tk.Label(root, text = "Welcome to text summarizer", fg = "black", bg = 'white')
    
    #create "input text" label
    label1 = tk.Label(root, text = "input text", fg = 'black',bg = 'white')
    
    #create "summary" label
    label2 = tk.Label(root, text = "summary", fg='black',bg = 'white')
    
    #grid method is used for placing
    #the widgets at respective positions in the table like structures
    
    tk.headlabel.grid(row = 0, column = 1)
    
    #padx keyword argument used to set padding along the x axis
    #pady keyword for the same along y axis
    label1.grid(row = 1, column = 0, padx = 10, pady = 10)
    label2.grid(row = 3, column = 0, padx = 10, pady = 10)
    
    #create a text area box for input and display of text
    text1_field= tk.Text(root, height = 12, width = 70, font = "lucida 13",relief=tk.GROOVE)
    text2_field= tk.Text(root, height = 12, width = 70, font = "lucida 13",relief=tk.SUNKEN)
    
    #padx keyword argument used to set padding along x axis
    #pady keyword argument used to set padding along y axis
    text1_field.grid(row = 1, column =1,padx = 10, pady = 10)
    text2_field.grid(row = 3, column =1,padx = 10, pady = 10)
    
    #creating a summary button and attach with summarize function
    button1 = tk.Button(root, text = "summary", bg = 'black', fg = 'white', command = summarize)
    button1.grid(row = 2, column = 1)
    
    #create clear button 
    button2 = tk.Button(root, text = "Clear", bg = "black", fg = "white", command = clearAll)
    button2.grid(row = 4, column = 1)
    root.mainloop()