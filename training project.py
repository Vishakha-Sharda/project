# Importing all the modules
from tkinter import *
from tkinter.messagebox import *

# Setting the file location and the localhost IP address for the GUI
host_files = {
    'Windows': r"C:\Windows\System32\drivers\etc\hosts"
}
localhost = '127.0.0.1'

def block(win):
    def block_websites(websites):
        host_file = host_files['Windows']
        sites_to_block = list(websites.split(' , '))

        # First we will make a copy of the websites you want blocked to a text file called 'blocked_websites.txt'
        with open('block_websites.txt', 'r+') as blocked_websites_txt:
            blocked_websites_txt.seek(0, 2)
            for site in sites_to_block:
                blocked_websites_txt.write(site)

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site not in content_in_file:
                    hostfile.write(localhost + '\t' + site + '\n')
                    showinfo('Websites blocked!', message='We have blocked the websites you wanted blocked!')
                else:
                    showinfo('Website Already blocked!', 'A website you entered is already blocked')


    blck_wn = Toplevel(win, background='LightBlue')
    blck_wn.title("Block a website")
    blck_wn.geometry('500x300')

    Label(blck_wn, text='Block websites', background='LightBlue', font=("impact", 28)).place(x=145, y=15)
    Label(blck_wn, text='(Enter the websites separated only by \' , \')', background='LightBlue',
          font=("verdana", 12)).place(x=75, y=100)
    Label(blck_wn, text='Enter the URLs (www.<sitename>.com):', background='LightBlue', font=('verdana', 12)).place(x=80, y=130)

    sites = Text(blck_wn, width=59, height=3)
    sites.place(x=10, y=170)

    submit_btn = Button(blck_wn, text='Submit', bg='MidnightBlue',fg="white",width="10", command=lambda: block_websites(sites.get('1.0',END)))
    submit_btn.place(x=215, y=248)

def unblock(win):
    def unblock_websites(websites_to_unblock):
        host_file = host_files['Windows']
        print(host_file)
        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.readlines()
            print(content_in_file)
            hostfile.seek(0)

            for line in content_in_file:
                if not any(site in line for site in websites_to_unblock):
                    hostfile.write(line)

                hostfile.truncate()

        with open('block_websites.txt', 'r+') as blocked_websites_txt:
            file_content = blocked_websites_txt.readlines()
            blocked_websites_txt.seek(0)

            for line in file_content:
                if not any(site in line for site in websites_to_unblock):
                    blocked_websites_txt.write(line)

                blocked_websites_txt.truncate()


        Label(unblck_wn, text='Website Blocked!', font=("Times", 13), bg='Aquamarine').place()


    # We are now going to get a list of all the blocked websites from the blocked_websites.txt file from its 3rd line
    with open('block_websites.txt', 'r+') as blocked_websites:
        blck_sites = blocked_websites.read().splitlines()[2:]

    unblck_wn = Toplevel(win, background='Aquamarine')
    unblck_wn.title("Block a website")
    unblck_wn.geometry('500x250')
    Label(unblck_wn, text='Unblock websites', background='Aquamarine', font=("Impact", 28)).place(x=125, y=15)
    Label(unblck_wn, text='Select the URLs that you want to unblock:', background='Aquamarine', font=('verdana',
                                                                                                      12)).place(x=75, y=80)

    # Creating a dropdown menu from the textfile to get the sites that are blocked
    blck_sites_strvar = StringVar(unblck_wn)
    blck_sites_strvar.set(blck_sites[0])
    dropdown = OptionMenu(unblck_wn, blck_sites_strvar, *blck_sites)
    dropdown.config(width=35)
    dropdown.place(x=130, y=130)

    submit_btn = Button(unblck_wn, text='Submit', bg='MidnightBlue',fg="white",width=10,command=lambda: unblock_websites(blck_sites_strvar.get()))
    submit_btn.place(x=210, y=180)


# Creating a GUI master window
root = Tk()
root.title(" Website Blocker")
root.geometry('1920x1080')
bg=PhotoImage(file="4578691.png")
label=Label(root,image=bg)
label.place(x=-10,y=0)

frame=Frame(root,bg="bisque")
frame.place(x=250,y=130,width=1000,height=520)

# Creating and setting the locations of all the components of the GUI
Label(root, text=' Website Blocker',bg="bisque",fg="#000000", font=("impact", 50)).place(x=540, y=230)
Label(root, text='Select below what do you want to do?',bg="bisque",fg="gray20", font=("verdana", 14)).place(x=595, y=390)

Button(root, text='Block a Website', font=('verdana', 11),cursor="hand2", bg= "red",width=20,height=2, command=lambda: block(root)).place(x=480, y=480)

Button(root, text='Unblock a Website', font=('verdana', 11), bg="green",cursor="hand2" ,width=20,height=2,command=lambda: unblock(root)).place(x=880, y=480)

root.update()
root.mainloop()