import customtkinter as ctk
imp

app = ctk.CTk()
app.title('ขายเพื่อน sell your friend')
app.geometry('500x500')

label = ctk.CTkLabel(app, text='ชื่อเพื่อนมึงอ่ะ',fg_color='transparent', font=('Aria',30))
label.pack(pady=(20,0))

answer_text = ctk.StringVar()
answer_label = ctk.CTkLabel(app, textvariable=answer_text,fg_color='transparent', font=('Aria',30))
answer_label.pack(pady=(20,0))


entry = ctk.CTkEntry(app, placeholder_text='ใส่ ชื่อ ของเพื่อนมึงตรงนี้ ชื่อพ่อด้วยก็ดี',font=('Aria',20),width=400,)
entry.pack(pady=(15,0))

x = ['kuy','fuck','hellbro']

def button_event():
    user_input = entry.get()
    answer = str(user_input),'',(random.choice(x))
    answer_text.set(answer)
    print(user_input, answer)
    
button = ctk.CTkButton(app, text="-กด ฉัน สิ-", command=button_event)
button.pack(pady=(20,0))

app.mainloop()
