
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import END, Tk, Canvas, Text, Button, PhotoImage


from deep_translator import GoogleTranslator



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("900x600")
window.configure(bg = "#FFFFFF",)
window.title("Any2Persian | by amirkho.ir")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    367.0,
    600.0,
    fill="#2F63D9",
    outline="")

canvas.create_text(
    25.0,
    42.0,
    anchor="nw",
    text="Anythings To Persian Translator",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 20 * -1),
    
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    183.0,
    496.0,
    image=image_image_1
)

canvas.create_text(
    102.0,
    123.0,
    anchor="nw",
    text="Developed by",
    fill="#FFFFFF",
    font=("RobotoRoman Medium", 18 * -1)
)

canvas.create_text(
    95.0,
    180.0,
    anchor="nw",
    text="www.amirkho.ir",
    fill="#FFFFFF",
    font=("RobotoRoman Medium", 18 * -1),
    
)



entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    642.5,
    155.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#E5E5E5",
    highlightthickness=0,
    font=("RobotoRoman Medium", 15 * -1)
)
entry_1.place(
    x=456.0,
    y=98.0,
    width=373.0,
    height=112.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    642.5,
    478.0,
    image=entry_image_2
)

result = entry_2 = Text(
    bd=0,
    bg="#E5E5E5",
    highlightthickness=0,
    font=("RobotoRoman Medium", 14 * -1),

)

entry_2.place(
    x=456.0,
    y=421.0,
    width=373.0,
    height=112.0
)

canvas.create_text(
    450.0,
    70.0,
    anchor="nw",
    text="Enter text for translate",
    fill="#796D6D",
    font=("RobotoRoman Medium", 16 * -1)
)

canvas.create_text(
    450.0,
    392.0,
    anchor="nw",
    text="Persian Translated Result",
    fill="#796D6D",
    font=("RobotoRoman Medium", 16 * -1),
    
    
)

def gtr():
    result.delete('1.0', END)
    source = str(entry_1.get("1.0","end-1c"))
    trasnlate = GoogleTranslator(target='fa').translate(source)
    result.insert(END, trasnlate)
    result.tag_configure('right', justify='right')
    result.tag_add("right", 1.0, "end")



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gtr(),
    relief="flat"
)
button_1.place(
    x=570.0,
    y=263.0,
    width=146.0,
    height=45.0
)



window.resizable(False, False)
window.mainloop()
