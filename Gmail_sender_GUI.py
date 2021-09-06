# importing required libs
import smtplib
from tkinter import *
root = Tk()

# Giving Parameters for main dialogue box
root.geometry('750x300')
root.title('Mail Sender')
root.configure(background='black')

# Creating the Email Id part
label = Label(root, text="Email:", font=("Helvetica", 12), bg="black", fg="white")
label.grid(row=2, column=0)

text = Entry(root, width=50)
text.grid(row=2, column=1)


# Creating the password part
label_password = Label(root, text="               Password:        ", font=("Helvetica", 12), bg="black", fg="white")
label_password.grid(row=2, column=2)

text_password = Entry(root, width=50)
text_password.grid(row=2, column=3)

# Creating the subject part
label_subject = Label(root, text="    Subject: ", font=("Helvetica", 12), bg="black", fg="white")
label_subject.grid(row=4, column=0)

text_subject = Entry(root, width=50,)
text_subject.grid(row=4, column=1)

# Creating the body part
label_body = Label(root, text="Body: ", font=("Helvetica", 12), bg="black", fg="white")
label_body.grid(row=4, column=2)

text_body = Entry(root, width=50)
text_body.grid(row=4, column=3)

# Creating the Receivers Id part
label_receivers_mail = Label(root, text="Receivers Email ID: ", font=("Helvetica", 12), bg="black", fg="white")
label_receivers_mail.grid(row=6, column=1)

text_receivers_mail = Entry(root)
text_receivers_mail.grid(row=6, column=2)

# Creating the alginment for the dialogue and titles
label_line = Label(root, text="      ", bg="black", fg="white").grid(row=3, column=2)
label_line_1 = Label(root, text="      ", bg="black", fg="white").grid(row=5, column=2)
label_line_2 = Label(root, text="      ", bg="black", fg="white").grid(row=7, column=2)
label_line_3 = Label(root, text="      ", bg="black", fg="white").grid(row=1, column=2)


def do_it():

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(text.get(), text_password.get())
	print("logged in")

	subject = text_subject.get()
	body = text_body.get()
	message = "Subject:{}\n\n{}".format(subject, body)
	server.sendmail(text.get(), text_receivers_mail.get(), message)
	print("sent successfully")

	server.quit()


# Empting for further use
	text.delete(0, END)
	text_password.delete(0, END)
	text_subject.delete(0, END)
	text_body.delete(0, END)
	text_receivers_mail.delete(0, END)


btn = Button(root, text='Send', command=do_it, font=("Helvetica", 12), width=8, bg='blue').grid(row=8, column=2)
root.mainloop()