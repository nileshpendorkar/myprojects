# from logging import root
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
# import db


class Hospital:
    def __init__(self,win):
        self.win=win
        self.win.title("Hospital Management System")
        self.win.geometry("1540x800+0+0")
        self.NamesOfTablet=StringVar()
        self.ReferenceNo=StringVar()
        self.Dose=StringVar()
        self.NoOfTablets=StringVar()
        self.LOT=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.BloodPressure=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientsID=StringVar()
        self.nhsNumber=StringVar()
        self.PatientsName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientsAddress=StringVar()
        # self.dbb=db.dbb
        self.dbb()
        
        lblTital=Label(self.win, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="RED", bg="white", font=("times new roman",50,"bold"))
        lblTital.pack(side=TOP,fill=X)
        
        
        ##### DATA FRAME ########
        DataFrame=Frame(self.win, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)
       
        DFlblL=LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                         font=("arial",12,"bold"),text="Patient Details")
        DFlblL.place(x=0, y=5,width=980,height=350)

        DFlblR=LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                         font=("arial",12,"bold"),text="Prescription")  
        DFlblR.place(x=990, y=5,width=460, height=350)
        
        # -------- BUTTON FRAME ------------
        Buttonframe=Frame(self.win, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)


        # -------- DETAILS FRAME ------------
        Detailsframe=Frame(self.win, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ---------- Data Frame left -------------
        lblNameTablet= Label(DFlblL,text="Names Of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0, column=0)
        Comb_TabletName= ttk.Combobox(DFlblL, state="readonly",textvariable=self.NamesOfTablet, font=("arial",12,"bold"),width=33)
        Comb_TabletName['value']=("nice","corona vaccine","acetaminophane","paracitamol","riboria",
                                  "pentids","folic acid","dolo 650","calpol","metxl trio-50",
                                  "pancil-DSR","Teltrust MT-50","rozerb gold_75")
        Comb_TabletName.current(0)
        Comb_TabletName.grid(row=0, column=1)

        lbl_ref= Label(DFlblL,text="Reference No. :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_ref.grid(row=1, column=0, sticky=W)
        Comb_ref= Entry(DFlblL,textvariable=self.ReferenceNo,font=("arial",12,"bold"),width=35)
        Comb_ref.grid(row=1, column=1)

        lbl_Dose= Label(DFlblL,text="Dose :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Dose.grid(row=2, column=0,sticky=W)
        Comb_Dose= Entry(DFlblL,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        Comb_Dose.grid(row=2, column=1)

        lbl_NoOfTablets= Label(DFlblL,text="No Of Tablets :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_NoOfTablets.grid(row=3, column=0,sticky=W)
        Comb_NoOfTablets= Entry(DFlblL,textvariable=self.NoOfTablets,font=("arial",12,"bold"),width=35)
        Comb_NoOfTablets.grid(row=3, column=1)

        lbl_Lot= Label(DFlblL,text="LOT",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Lot.grid(row=4, column=0,sticky=W)
        Comb_Lot= Entry(DFlblL,textvariable=self.LOT,font=("arial",12,"bold"),width=35)
        Comb_Lot.grid(row=4, column=1)

        lbl_IssueDate= Label(DFlblL,text="Issue Date :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_IssueDate.grid(row=5, column=0,sticky=W)
        Comb__IssueDate= Entry(DFlblL,textvariable=self.IssueDate,font=("arial",12,"bold"),width=35)
        Comb__IssueDate.grid(row=5, column=1)

        lbl_ExpDate= Label(DFlblL,text="Exp Date :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_ExpDate.grid(row=6, column=0, sticky=W)
        Comb__ExpDate= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
        Comb__ExpDate.grid(row=6, column=1)

        lbl_DailyDose= Label(DFlblL,text="Daily Dose :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DailyDose.grid(row=7,column=0, sticky=W)
        Comb__DailyDose= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        Comb__DailyDose.grid(row=7, column=1)

        lbl_SideEffects= Label(DFlblL,text="Side Effects :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_SideEffects.grid(row=8, column=0, sticky=W)
        Comb__SideEffects= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.SideEffects,width=35)
        Comb__SideEffects.grid(row=8, column=1)
        
        lbl_FurtherInfo= Label(DFlblL,text="Further Information :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_FurtherInfo.grid(row=0, column=2, sticky=W)
        Comb__FurtherInfo= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        Comb__FurtherInfo.grid(row=0, column=3)
        
        lbl_BloodPre= Label(DFlblL,text=" Blood Pressure :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_BloodPre.grid(row=1, column=2, sticky=W)
        Comb__BloodPre= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.BloodPressure,width=35)
        Comb__BloodPre.grid(row=1, column=3)
        
        lbl_StorageAdv= Label(DFlblL,text=" Storage Advice:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_StorageAdv.grid(row=2, column=2, sticky=W)
        Comb__StorageAdv= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        Comb__StorageAdv.grid(row=2, column=3)
        
        lbl_Medication= Label(DFlblL,text="Medication :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Medication.grid(row=3, column=2, sticky=W)
        Comb__Medication= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        Comb__Medication.grid(row=3, column=3)
        
        lbl_PatientID= Label(DFlblL,text="Patient ID  :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_PatientID.grid(row=4, column=2, sticky=W)
        Comb__PatientID= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.PatientsID,width=35)
        Comb__PatientID.grid(row=4, column=3)
        
        lbl_NhsNo= Label(DFlblL,text="NHS No. :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_NhsNo.grid(row=5, column=2, sticky=W)
        Comb_NhsNo= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        Comb_NhsNo.grid(row=5, column=3)
        
        lbl_PatientsName= Label(DFlblL,text="Patient Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_PatientsName.grid(row=6, column=2, sticky=W)
        Comb__PatientsName= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.PatientsName,width=35)
        Comb__PatientsName.grid(row=6, column=3)
        
        lbl_DOB= Label(DFlblL,text="Patients DOB :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DOB.grid(row=7, column=2, sticky=W)
        Comb__DOB= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        Comb__DOB.grid(row=7, column=3)
        
        lbl_Address= Label(DFlblL, text="Patients Address :",  font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Address.grid(row=8, column=2, sticky=W)
        Comb__Address= Entry(DFlblL,font=("arial",12,"bold"),textvariable=self.PatientsAddress,width=35)
        Comb__Address.grid(row=8, column=3)
        
        # --------------DFRIGHT------------------
        self.Txt_Prescription = Text(DFlblR, font=("arial",12,"bold"), width=45, height=16, padx=2, pady=6)
        self.Txt_Prescription.grid(row=0, column=0)
        
        # ---------------------BUTTONS---------------
        Btn_Prescription= Button(Buttonframe,text="prescription",command=self.Prescription,bg="green",fg="white",font=("arial",12,"bold"),width=23)
        Btn_Prescription.grid(row=0,column=0)
        
        Btn_Prescription_DAta= Button(Buttonframe,text="prescription Data",bg="green",fg="white",command = self.iPrescription_data, font=("arial",12,"bold"),width=23)
        Btn_Prescription_DAta.grid(row=0,column=1)

        Btn_Update= Button(Buttonframe,text="Update",command=self.Update_Data,bg="green",fg="white",font=("arial",12,"bold"),width=23)
        Btn_Update.grid(row=0,column=2)

        Btn_Delete= Button(Buttonframe,text="Delete",command=self.idelete,bg="green",fg="white",font=("arial",12,"bold"),width=23)
        Btn_Delete.grid(row=0,column=3)

        Btn_Clear= Button(Buttonframe,text="CLear",bg="green",command=self.clear,fg="white",font=("arial",12,"bold"),width=23)
        Btn_Clear.grid(row=0,column=4)

        Btn_Exit= Button(Buttonframe,text="Exit",bg="green",command=self.Ext,fg="white",font=("arial",12,"bold"),width=23)
        Btn_Exit.grid(row=0,column=5)

        # ---------------Table------------
        # SCROLLBAR
        Scrollbar_x= Scrollbar(Detailsframe, orient=HORIZONTAL)
        Scrollbar_y= Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table= ttk.Treeview(Detailsframe,columns=("Names Of Tablet","Reference No. :",
                                    "Dose :","No Of Tablets :","LOT","Issue Date :",
                                    "Exp Date :","Daily Dose :","NHS No. :","Patient Name :","Patients DOB :",
                                    "Patients Address :"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
    
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        
        Scrollbar_x=ttk.Scrollbar(command=self.hospital_table.xview)
        Scrollbar_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Names Of Tablet",text="NamesOfTablet")
        self.hospital_table.heading("Reference No. :",text="Reference No")
        self.hospital_table.heading("Dose :",text="Dose :")
        self.hospital_table.heading("No Of Tablets :",text="No Of Tablets")
        self.hospital_table.heading("LOT",text="LOTT")
        self.hospital_table.heading("Issue Date :",text="Issue Date")
        self.hospital_table.heading("Exp Date :",text="Exp Date")
        self.hospital_table.heading("Daily Dose :",text="Daily Dose")
        self.hospital_table.heading("NHS No. :",text="NHS No.")
        self.hospital_table.heading("Patient Name :",text="Patient Name")
        self.hospital_table.heading("Patients DOB :",text="Patients DOB")
        self.hospital_table.heading("Patients Address :",text="Patients Address")

        self.hospital_table["show"]="headings"
        

        self.hospital_table.column("Names Of Tablet",width=100)
        self.hospital_table.column("Reference No. :",width=100)
        self.hospital_table.column("Dose :",width=100)
        self.hospital_table.column("No Of Tablets :",width=100)
        self.hospital_table.column("LOT",width=100)
        self.hospital_table.column("Issue Date :",width=100)
        self.hospital_table.column("Exp Date :",width=100)
        self.hospital_table.column("Daily Dose :",width=100)
        self.hospital_table.column("NHS No. :",width=100)
        self.hospital_table.column("Patient Name :",width=100)
        self.hospital_table.column("Patients DOB :",width=100)
        self.hospital_table.column("Patients Address :",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()
    



        
    #--------------functionality declaration-----------
    def iPrescription_data(self):

        if (self.NamesOfTablet.get()=="") or (self.ReferenceNo.get()==""):
                messagebox.showerror("Error","all fields are required")
        else:
            
            conn=mysql.connector.connect(host="localhost", username="root", password="nilesh1432",database="new1")
            conn_cursor=conn.cursor()
            # messagebox.showinfo("inside else block","hello")
            # conn_cursor.execute("CREATE TABLE hospital")
            # conn_cursor.execute("CREATE TABLE Hospital (nameoftablet, referenceNo, Dose, NoOfTablets,lot,issuedate,expdate,dailydose,storageadvice,nhs,patname,dob,add)")
            conn_cursor.execute("insert into Hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.NamesOfTablet.get(),self.ReferenceNo.get(),self.Dose.get(),self.NoOfTablets.get(),self.LOT.get(),self.IssueDate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientsName.get(),self.DateOfBirth.get(),self.PatientsAddress.get()))       
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success","record has been inserted successfully")

    def Update_Data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="nilesh1432",database="new1")
        conn_cursor=conn.cursor()
        quryw="update Hospital set referenceNo=%s,nameoftablet=%s,Dose=%s,NoOfTablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storageadvice=%s,nhs=%s,patname=%s,dob=%s where addres=%s"
        vall=(self.ReferenceNo.get(),self.NamesOfTablet.get(),self.Dose.get(),self.NoOfTablets.get(),self.LOT.get(),self.IssueDate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientsName.get(),self.DateOfBirth.get(),self.PatientsAddress.get())
        conn_cursor.execute(quryw, vall)
        conn.commit() 
        conn.close()
        messagebox.showinfo("success","record has been updated successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="nilesh1432",database="new1")
        conn_cursor=conn.cursor()
        conn_cursor.execute("select * from Hospital")       
        rowss=conn_cursor.fetchall()
        if len(rowss)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rowss:
                  self.hospital_table.insert("",END,values=i)
        
            conn.commit()
        else:
            self.hospital_table.delete(*self.hospital_table.get_children())
            self.clear()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        containt=self.hospital_table.item(cursor_row) 
        roww=containt["values"]
        self.NamesOfTablet.set(roww[0])
        self.ReferenceNo.set(roww[1])
        self.Dose.set(roww[2])
        self.NoOfTablets.set(roww[3])
        self.LOT.set(roww[4])
        self.IssueDate.set(roww[5])
        self.ExpDate.set(roww[6])
        self.DailyDose.set(roww[7])
        self.StorageAdvice.set(roww[8])
        self.nhsNumber.set(roww[9])
        self.PatientsName.set(roww[10])
        self.DateOfBirth.set(roww[11])
        self.PatientsAddress.set(roww[12])

    def Prescription(self):
        self.Txt_Prescription.insert(END,"Name of Tablets:\t\t\t"+self.NamesOfTablet.get()+"\n")
        self.Txt_Prescription.insert(END,"Reference No.:\t\t\t"+self.ReferenceNo.get()+"\n")
        self.Txt_Prescription.insert(END,"dose :\t\t\t"+self.Dose.get()+"\n")
        self.Txt_Prescription.insert(END,"Number Of Tablets:\t\t\t"+self.NoOfTablets.get()+"\n")
        self.Txt_Prescription.insert(END,"lot:\t\t\t"+self.LOT.get()+"\n")
        self.Txt_Prescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.Txt_Prescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.Txt_Prescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.Txt_Prescription.insert(END,"Side Effects:\t\t\t"+self.SideEffects.get()+"\n")
        self.Txt_Prescription.insert(END,"Further information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.Txt_Prescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.Txt_Prescription.insert(END,"Driving Using Machine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.Txt_Prescription.insert(END,"Patients ID:\t\t\t"+self.PatientsID.get()+"\n")
        self.Txt_Prescription.insert(END,"NHS No:\t\t\t"+self.nhsNumber.get()+"\n")
        self.Txt_Prescription.insert(END,"Patients Name:\t\t\t"+self.PatientsName.get()+"\n")
        self.Txt_Prescription.insert(END,"Patients DOB:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.Txt_Prescription.insert(END,"Patients Address:\t\t\t"+self.PatientsAddress.get()+"\n")
                                                                                            
    def idelete(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="nilesh1432",database="new1")
        conn_cursor=conn.cursor()
        query="delete from Hospital where referenceNo = %s"                          
        value=(self.ReferenceNo.get(),)
        conn_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("deleted","deleted successfully")

    def clear(self):
        self.NamesOfTablet.set("")
        self.ReferenceNo.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.LOT.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffects.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientsID.set("")
        self.nhsNumber.set("")
        self.PatientsName.set("")
        self.DateOfBirth.set("")
        self.PatientsAddress.set("")
        self.Txt_Prescription.delete("1.0",END) 

    def Ext(self):
        Ext=messagebox.askyesno("Hospital Management System","confirm YOu want to exit?")
        if Ext>0:
           win.destroy()
           return 

    def dbb(self):
        my_db=mysql.connector.connect(host="localhost",username="root",password="nilesh1432")
        db_cur=my_db.cursor()
        db_cur.execute("create database if not exists new1")
        my_db.commit()
        db_cur.execute("create table if not exists new1.Hospital(nameoftablet varchar(45),referenceNo varchar(45),Dose varchar(45),NoOfTablets varchar(45),lot varchar(45),issuedate varchar(45),expdate varchar(45),dailydose varchar(45),storageadvice varchar(45),nhs varchar(45),patname varchar(45),dob varchar(45),addres varchar(45))")
        my_db.commit()
        print('creted')

            
        
         
         
        

win=Tk()
ob=Hospital(win)
win.mainloop()




