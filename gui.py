from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import ttkbootstrap

# write funcs here

window = Tk()
window.title('Prototype')
window.columnconfigure(0)
window.rowconfigure(0)

font_setting = tkFont.Font(size=16)

main_content_frame = ttk.Frame(window)
img_buttons_frame = ttk.Frame(main_content_frame)

data_disp_frame = ttk.Frame(main_content_frame)

left_button = ttk.Button(img_buttons_frame, text="<-")

img_mesg_lbl_pic = ttk.Label(img_buttons_frame, text="Please select Rover", font=font_setting)
right_button = ttk.Button(img_buttons_frame, text="->")

rovers_frame = ttk.Frame(data_disp_frame)
rovers_label = ttk.Label(rovers_frame, text="Select Rover", font=font_setting)
rovers_dropdown = ttk.Combobox(rovers_frame)
rovers_dropdown['values'] = ('Curiosity','Opportunity','Spirit')
curiosity_dates_label = ttk.Label(rovers_frame, text='Curiosity: Active 2012 - Current')
opportunity_dates_label = ttk.Label(rovers_frame, text='Opportunity: Active 2004 - 2019')
spirit_dates_label = ttk.Label(rovers_frame, text='Spirit: Active 2004 - 2011')

date_frame = ttk.Frame(data_disp_frame)
date_label = ttk.Label(date_frame)
otd_button = ttk.Button(date_frame, text="On This Day")
date_label = ttk.Label(date_frame, text="Date:", font=font_setting)
date_entry_field = ttk.Entry(date_frame)
exec_search_frame = ttk.Frame(data_disp_frame)
exec_search = ttk.Button(exec_search_frame, text="Search!")

# style:
main_content_frame.grid(sticky=(N,W,E,S))
main_content_frame['borderwidth'] = 1
main_content_frame['relief'] = 'solid'
img_buttons_frame.grid(column=0, row=0, sticky=(N,W,S))
img_buttons_frame['borderwidth'] = 1
img_buttons_frame['relief'] = 'solid'
img_buttons_frame.rowconfigure(3, weight=1)
img_buttons_frame.columnconfigure(3, weight=1)

data_disp_frame.grid(column=1, row=0, sticky=(N,E,S))
data_disp_frame['padding'] = 10
data_disp_frame['borderwidth'] = 1
data_disp_frame['relief'] = 'solid'

left_button.grid(column=0, row=1, sticky=(E,W))
img_mesg_lbl_pic.grid(column=1, row=1, sticky=(N,W,E,S))
right_button.grid(column=2, row=1, sticky=(E,W))

rovers_frame.grid(column=0, row=0, sticky=(N,W,E,S))
rovers_frame['padding'] = 15
rovers_frame['borderwidth'] = 1
rovers_frame['relief'] = 'solid'
date_frame.grid(column=0, row=1, sticky=(N,W,E,S))
date_frame['padding'] = 15
date_frame['borderwidth'] = 1
date_frame['relief'] = 'solid'
exec_search_frame.grid(column=0, row=2, sticky=(N,W,E,S))
exec_search_frame['padding'] = 15
exec_search_frame['borderwidth'] = 1
exec_search_frame['relief'] = 'solid'

otd_button.grid(column=0, row=1, sticky=(E,W))
rovers_dropdown.grid(column=0, row=1, sticky=(E,W))
curiosity_dates_label.grid(column=0, row=2, sticky=(E,W))
opportunity_dates_label.grid(column=0, row=3, sticky=(EW))
spirit_dates_label.grid(column=0, row=4, sticky=(E,W))
rovers_label.grid(column=0, row=0, sticky=(E,W))
date_label.grid(column=0, row=2, sticky=(E,W))
date_entry_field.grid(column=0, row=3, sticky=(E,W))
exec_search.grid(column=0, row=0, sticky=(S,E))

main_content_frame.columnconfigure(0)
main_content_frame.rowconfigure(0)

# start main loop
window.mainloop()