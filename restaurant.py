from tkinter import *
import random
import time;
import datetime
import tkinter.messagebox
root=Tk()
root.geometry("1350x750+0+0")
root.title("RESTAURANT MANAGEMENT SYSTEM")
root.configure(background='Silver')
Tops=Frame(root,bg='Silver',bd=10,pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle =Label(Tops,font=('arial',50,'bold'),text="RESTAURANT MANAGEMENT SYSTEM",bd=21,bg='Light Grey',fg='Black',justify=CENTER)
lblTitle.grid(row=0,column=0)
ReceiptCal_F=Frame(root,bg='Light Grey',bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F,bg='Light Grey',bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F,bg='Light Grey',bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F,bg='Light Grey',bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)
MenuFrame=Frame(root,bg='Silver',bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='Light Grey',bd=4)
Cost_F.pack(side=BOTTOM)
Food_F=Frame(MenuFrame,bg='Silver',bd=10)
Food_F.pack(side=TOP)
Food_F=Frame(MenuFrame,bg='Light Grey',bd=10, relief=RIDGE)
Food_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame,bg='Light Grey',bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)
#------variable------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofFood=StringVar()
CostofCakes=StringVar()
ServiceCharge=StringVar()

text_Input=StringVar()
operator=""

E_SnackBreakfast=StringVar()
E_South_Indian=StringVar()
E_Thick_Shakes=StringVar()
E_Hot_Beverges=StringVar()
E_Cold_Drinks=StringVar()
E_Lunch=StringVar()
E_Dinner=StringVar()
E_Non_Veg=StringVar()

E_Angel_food_Cake=StringVar()
E_Butter_Cake=StringVar()
E_Pound_Cake=StringVar()
E_Sponge_Cake=StringVar()
E_Genoise=StringVar()
E_Biscuit_Cake=StringVar()
E_Chocolate_Cake=StringVar()
E_Chiffon_Cake=StringVar()

E_SnackBreakfast.set('0')
E_South_Indian.set('0')
E_Thick_Shakes.set('0')
E_Hot_Beverges.set('0')
E_Cold_Drinks.set('0')
E_Lunch.set('0')
E_Dinner.set('0')
E_Non_Veg.set('0')

E_Angel_food_Cake.set('0')
E_Butter_Cake.set('0')
E_Pound_Cake.set('0')
E_Sponge_Cake.set('0')
E_Genoise.set('0')
E_Biscuit_Cake.set('0')
E_Chocolate_Cake.set('0')
E_Chiffon_Cake.set('0')

DateofOrder.set(time.strftime("%d/%m/%y"))
#---------Func declaration-----
def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return
def Reset():
    PaidTax.set('')
    SubTotal.set('')
    TotalCost.set('')
    CostofFood.set('')
    CostofCakes.set('')
    ServiceCharge.set('')
    txtReceipt.delete('1.0',END)
    E_SnackBreakfast.set('0')
    E_South_Indian.set('0')
    E_Thick_Shakes.set('0')
    E_Hot_Beverges.set('0')
    E_Cold_Drinks.set('0')
    E_Lunch.set('0')
    E_Dinner.set('0')
    E_Non_Veg.set('0')

    E_Angel_food_Cake.set('0')
    E_Butter_Cake.set('0')
    E_Pound_Cake.set('0')
    E_Sponge_Cake.set('0')
    E_Genoise.set('0')
    E_Biscuit_Cake.set('0')
    E_Chocolate_Cake.set('0')
    E_Chiffon_Cake.set('0')

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
    txtSnackBreakfast.configure(state=DISABLED)
    txtSouth_Indian.configure(state=DISABLED)
    txtThick_Shakes.configure(state=DISABLED)
    txtHot_Beverges.configure(state=DISABLED)
    txtCold_Drinks.configure(state=DISABLED)
    txtLunch.configure(state=DISABLED)
    txtDinner.configure(state=DISABLED)
    txtNon_Veg.configure(state=DISABLED)
    txtAngel_food_Cake.configure(state=DISABLED)
    txtButter_Cake.configure(state=DISABLED)
    txtPound_Cake.configure(state=DISABLED)
    txtSponge_Cake.configure(state=DISABLED)
    txtGenoise.configure(state=DISABLED)
    txtBiscuit_Cake.configure(state=DISABLED)
    txtChocolate_Cake.configure(state=DISABLED)
    txtChiffon_Cake.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_SnackBreakfast.get())
    Item2=float(E_South_Indian.get())
    Item3=float(E_Thick_Shakes.get())
    Item4=float(E_Hot_Beverges.get())
    Item5=float(E_Cold_Drinks.get())
    Item6=float(E_Lunch.get())
    Item7=float(E_Dinner.get())
    Item8=float(E_Non_Veg.get())
    Item9=float(E_Angel_food_Cake.get())
    Item10=float(E_Butter_Cake.get())
    Item11=float(E_Pound_Cake.get())
    Item12=float(E_Sponge_Cake.get())
    Item13=float(E_Genoise.get())
    Item14=float(E_Biscuit_Cake.get())
    Item15=float(E_Chocolate_Cake.get())
    Item16=float(E_Chiffon_Cake.get())
    PriceofFood=(Item1*1.5)+(Item2*1.5)+(Item3*1.5)+(Item4*1.5)+(Item5*1.5)+(Item6*1.5)+(Item7*1.5)+(Item8*1.5)
    PriceofCakes=(Item9*2.5)+(Item10*2.5)+(Item11*2.5)+(Item12*2.5)+(Item13*2.5)+(Item14*2.5)+(Item15*2.5)+(Item16*2.5)
    FoodPrice="₹",str('%0.2f'%(PriceofFood))
    CakesPrice="₹",str('%0.2f'%(PriceofCakes))
    CostofFood.set(FoodPrice)
    CostofCakes.set(CakesPrice)
    SC="₹",str('%0.2f'%(1.59))
    ServiceCharge.set(SC)
    SubTotalofItems="₹",str('%0.2f'%(PriceofFood+PriceofCakes+1.59))
    SubTotal.set(SubTotalofItems)
    Tax="₹",str('%.2f'%((PriceofFood +PriceofCakes + 1.59)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofFood + PriceofCakes + 1.59)*0.15)
    TC="₹",str('%.2f'%(PriceofFood + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)

def chkSnackBreakfast():
    if (var1.get()== 1):
        txtSnackBreakfast.configure(state=NORMAL)
        txtSnackBreakfast.focus()
        txtSnackBreakfast.delete('0',END)
        E_SnackBreakfast.set("")
    elif(var1.get()== 0):
        txtSnackBreakfast.configure(state=DISABLED)
        E_SnackBreakfast.set("0")
def chkSouth_Indian():
    if (var2.get()== 1):
        txtSouth_Indian.configure(state=NORMAL)
        txtSouth_Indian.focus()
        txtSouth_Indian.delete('0',END)
        E_South_Indian.set("")
    elif(var2.get()== 0):
        txtSouth_Indian.configure(state=DISABLED)
        E_South_Indian.set("0")
def chkThick_Shakes():
    if (var3.get()== 1):
        txtThick_Shakes.configure(state=NORMAL)
        txtThick_Shakes.focus()
        txtThick_Shakes.delete('0',END)
        E_Thick_Shakes.set("")
    elif(var3.get()== 0):
        txtThick_Shakes.configure(state=DISABLED)
        E_Thick_Shakes.set("0")
def chkHot_Beverges():
    if (var4.get()== 1):
        txtHot_Beverges.configure(state=NORMAL)
        txtHot_Beverges.focus()
        txtHot_Beverges.delete('0',END)
        E_Hot_Beverges.set("")
    elif(var4.get()== 0):
        txtHot_Beverges.configure(state=DISABLED)
        E_Hot_Beverges.set("0")
def chkCold_Drinks():
    if (var5.get()== 1):
        txtCold_Drinks.configure(state=NORMAL)
        txtCold_Drinks.focus()
        txtCold_Drinks.delete('0',END)
        E_Cold_Drinks.set("")
    elif(var5.get()== 0):
        txtCold_Drinks.configure(state=DISABLED)
        E_Cold_Drinks.set("0")
def chkLunch():
    if (var6.get()== 1):
        txtLunch.configure(state=NORMAL)
        txtLunch.focus()
        txtLunch.delete('0',END)
        E_Lunch.set("")
    elif(var6.get()== 0):
        txtLunch.configure(state=DISABLED)
        E_Lunch.set("0")
def chkDinner():
    if (var7.get()== 1):
        txtDinner.configure(state=NORMAL)
        txtDinner.focus()
        txtDinner.delete('0',END)
        E_Dinner.set("")
    elif(var7.get()== 0):
        txtDinner.configure(state=DISABLED)
        E_Dinner.set("0")
def chkNon_Veg():
    if (var8.get()== 1):
        txtNon_Veg.configure(state=NORMAL)
        txtNon_Veg.focus()
        txtNon_Veg.delete('0',END)
        E_Non_Veg.set("")
    elif(var8.get()== 0):
        txtNon_Veg.configure(state=DISABLED)
        E_Non_Veg.set("0")
def chkAngel_food_Cake():
    if (var9.get()== 1):
        txtAngel_food_Cake.configure(state=NORMAL)
        txtAngel_food_Cake.focus()
        txtAngel_food_Cake.delete('0',END)
        E_Angel_food_Cake.set("")
    elif(var9.get()== 0):
        txtAngel_food_Cake.configure(state=DISABLED)
        E_Angel_food_Cake.set("0")
def chkButter_Cake():
    if (var10.get()== 1):
        txtButter_Cake.configure(state=NORMAL)
        txtButter_Cake.focus()
        txtButter_Cake.delete('0',END)
        E_Butter_Cake.set("")
    elif(var10.get()== 0):
        txtButter_Cake.configure(state=DISABLED)
        E_Butter_Cake.set("0")
def chkPound_Cake():
    if (var11.get()== 1):
        txtPound_Cake.configure(state=NORMAL)
        txtPound_Cake.focus()
        txtPound_Cake.delete('0',END)
        E_Pound_Cake.set("")
    elif(var11.get()== 0):
        txtPound_Cake.configure(state=DISABLED)
        E_Pound_Cake.set("0")
def chkSponge_Cake():
    if (var12.get()== 1):
        txtSponge_Cake.configure(state=NORMAL)
        txtSponge_Cake.focus()
        txtSponge_Cake.delete('0',END)
        E_Sponge_Cake.set("")
    elif(var12.get()== 0):
        txtSponge_Cake.configure(state=DISABLED)
        E_Sponge_Cake.set("0")
def chkGenoise():
    if (var13.get()== 1):
        txtGenoise.configure(state=NORMAL)
        txtGenoise.focus()
        txtGenoise.delete('0',END)
        E_Genoise.set("")
    elif(var13.get()== 0):
        txtGenoise.configure(state=DISABLED)
        E_Genoise.set("0")
def chkBiscuit_Cake():
    if (var14.get()== 1):
        txtBiscuit_Cake.configure(state=NORMAL)
        txtBiscuit_Cake.focus()
        txtBiscuit_Cake.delete('0',END)
        E_Biscuit_Cake.set("")
    elif(var14.get()== 0):
        txtBiscuit_Cake.configure(state=DISABLED)
        E_Biscuit_Cake.set("0")
def chkChocolate_Cake():
    if (var15.get()== 1):
        txtChocolate_Cake.configure(state=NORMAL)
        txtChocolate_Cake.focus()
        txtChocolate_Cake.delete('0',END)
        E_Chocolate_Cake.set("")
    elif(var15.get()== 0):
        txtChocolate_Cake.configure(state=DISABLED)
        E_Chocolate_Cake.set("0")
def chkChiffon_Cake():
    if (var16.get()== 1):
        txtChiffon_Cake.configure(state=NORMAL)
        txtChiffon_Cake.focus()
        txtChiffon_Cake.delete('0',END)
        E_Chiffon_Cake.set("")
    elif(var16.get()== 0):
        txtChiffon_Cake.configure(state=DISABLED)
        E_Chiffon_Cake.set("0")
def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10000,60900)
    randomRef=str(x)
    Receipt_Ref.set("BILL"+ randomRef)
    txtReceipt.insert(END,'Receipt Ref:\t\t\t' + Receipt_Ref.get()+'\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Item:\t\t\t' + "Cost of Items\n")
    txtReceipt.insert(END,'SnackBreakfast:\t\t\t' + E_SnackBreakfast.get()+"\n")
    txtReceipt.insert(END,'South_Indian:\t\t\t' + E_South_Indian.get()+"\n")
    txtReceipt.insert(END,'Thick_Shakes:\t\t\t' + E_Thick_Shakes.get()+"\n")
    txtReceipt.insert(END,'Hot_Beverges:\t\t\t' + E_Hot_Beverges.get()+"\n")
    txtReceipt.insert(END,'Cold_Drinks:\t\t\t' + E_Cold_Drinks.get()+"\n")
    txtReceipt.insert(END,'Lunch:\t\t\t' + E_Lunch.get()+"\n")
    txtReceipt.insert(END,'Dinner:\t\t\t' + E_Dinner.get()+"\n")
    txtReceipt.insert(END,'Non_Veg:\t\t\t' + E_Non_Veg.get()+"\n")
    txtReceipt.insert(END,'Angel_food_Cake:\t\t\t' + E_Angel_food_Cake.get()+"\n")
    txtReceipt.insert(END,'Butter_Cake:\t\t\t' + E_Butter_Cake.get()+"\n")
    txtReceipt.insert(END,'Pound_Cake:\t\t\t' + E_Pound_Cake.get()+"\n")
    txtReceipt.insert(END,'Sponge_Cake:\t\t\t' + E_Sponge_Cake.get()+"\n")
    txtReceipt.insert(END,'Genoise:\t\t\t' + E_Genoise.get()+"\n")
    txtReceipt.insert(END,'Biscuit_Cake:\t\t\t' + E_Biscuit_Cake.get()+"\n")
    txtReceipt.insert(END,'Chocolate_Cake:\t\t\t' + E_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,'Chiffon_Cake:\t\t\t' + E_Chiffon_Cake.get()+"\n")
    txtReceipt.insert(END,'Cost of Food:\t\t\t' + CostofFood.get()+'\nTax Paid:\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Cakes:\t\t\t' + CostofCakes.get()+'\nSubTotal:\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t'+str(TotalCost.get()))
#---------FOODS-------
SnackBreakfast=Checkbutton(Food_F,text="Snacks & Breakfast\t",variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkSnackBreakfast).grid(row=0,sticky=W)
South_Indian=Checkbutton(Food_F,text="South Indian",variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkSouth_Indian).grid(row=1,sticky=W)
Thick_Shakes=Checkbutton(Food_F,text="Thick Shakes",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkThick_Shakes).grid(row=2,sticky=W)
Hot_Beverges=Checkbutton(Food_F,text="Hot Beverges",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkHot_Beverges).grid(row=3,sticky=W)
Cold_Drinks=Checkbutton(Food_F,text="Cold Drinks",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkCold_Drinks).grid(row=4,sticky=W)
Lunch=Checkbutton(Food_F,text="Lunch",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkLunch).grid(row=5,sticky=W)
Dinner=Checkbutton(Food_F,text="Dinner",variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkDinner).grid(row=6,sticky=W)
Non_Veg=Checkbutton(Food_F,text="Non Veg",variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkNon_Veg).grid(row=7,sticky=W)
#--------Entry-------
txtSnackBreakfast=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_SnackBreakfast,state=DISABLED)
txtSnackBreakfast.grid(row=0,column=1)
txtSouth_Indian=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_South_Indian)
txtSouth_Indian.grid(row=1,column=1)
txtThick_Shakes=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Thick_Shakes)
txtThick_Shakes.grid(row=2,column=1)
txtHot_Beverges=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Hot_Beverges)
txtHot_Beverges.grid(row=3,column=1)
txtCold_Drinks=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Cold_Drinks)
txtCold_Drinks.grid(row=4,column=1)
txtLunch=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Lunch)
txtLunch.grid(row=5,column=1)
txtDinner=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Dinner)
txtDinner.grid(row=6,column=1)
txtNon_Veg=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Non_Veg)
txtNon_Veg.grid(row=7,column=1)
#--------CAKES------
Angel_food_Cake=Checkbutton(Cake_F,text="Angel food Cake\t",variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkAngel_food_Cake).grid(row=0,sticky=W)
Butter_Cake=Checkbutton(Cake_F,text="Butter Cake",variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkButter_Cake).grid(row=1,sticky=W)
Pound_Cake=Checkbutton(Cake_F,text="Pound Cake",variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkPound_Cake).grid(row=2,sticky=W)
Sponge_Cake=Checkbutton(Cake_F,text="Sponge Cake",variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkSponge_Cake).grid(row=3,sticky=W)
Genoise=Checkbutton(Cake_F,text="Genoise",variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkGenoise).grid(row=4,sticky=W)
Biscuit_Cake=Checkbutton(Cake_F,text="Biscuit Cake",variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkBiscuit_Cake).grid(row=5,sticky=W)
Chocolate_Cake=Checkbutton(Cake_F,text="Chocolate Cake",variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkChocolate_Cake).grid(row=6,sticky=W)
Chiffon_Cake=Checkbutton(Cake_F,text="Chiffon Cake",variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='Light Grey',command=chkChiffon_Cake).grid(row=7,sticky=W)
#--------Entry-------
txtAngel_food_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Angel_food_Cake)
txtAngel_food_Cake.grid(row=0,column=1)
txtButter_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Butter_Cake)
txtButter_Cake.grid(row=1,column=1)
txtPound_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Pound_Cake)
txtPound_Cake.grid(row=2,column=1)
txtSponge_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Sponge_Cake)
txtSponge_Cake.grid(row=3,column=1)
txtGenoise=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Genoise)
txtGenoise.grid(row=4,column=1)
txtBiscuit_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Biscuit_Cake)
txtBiscuit_Cake.grid(row=5,column=1)
txtChocolate_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Chocolate_Cake)
txtChocolate_Cake.grid(row=6,column=1)
txtChiffon_Cake=Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_Chiffon_Cake)
txtChiffon_Cake.grid(row=7,column=1)
#-----Total cost----
lblCostofFood =Label(Cost_F,font=('arial',14,'bold'),text="Cost of Food\t  ",bg='Light Grey',fg='Black')
lblCostofFood.grid(row=0,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=0,column=1)

lblCostofCakes =Label(Cost_F,font=('arial',14,'bold'),text="Cost of Cakes  ",bg='Light Grey',fg='Black')
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=CostofCakes)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge =Label(Cost_F,font=('arial',14,'bold'),text="Service Charge   ",bg='Light Grey',fg='Black')
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
#------Payment info----
lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text="\tPaid Tax\t",bd=7,bg='Light Grey',fg='Black')
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal =Label(Cost_F,font=('arial',14,'bold'),text="\tSub Total",bd=7,bg='Light Grey',fg='Black')
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost =Label(Cost_F,font=('arial',14,'bold'),text="\tTotal Cost",bg='Light Grey',fg='Black',bd=7)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg="white",bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)
#------receipt-----
txtReceipt=Text(Receipt_F,width=46,height=12,bg="white",bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)
#------buttons---
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Total",bg="Light Grey",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Receipt",bg="Light Grey",command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Reset",bg="Light Grey",command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Exit",bg="Light Grey",command= iExit).grid(row=0,column=3)
#---------calculator Display---
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btnClear():
    global operator
    operator=""
    text_Input.set("")
def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

txtDisplay=Entry(Cal_F,width=45,bg="white",bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#------Calculator buttons---
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="7",bg="Light Grey",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="8",bg="Light Grey",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="9",bg="Light Grey",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="+",bg="Light Grey",command=lambda:btnClick('+')).grid(row=2,column=3)
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="4",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="5",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="6",command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="-",bg="Light Grey",command=lambda:btnClick('-')).grid(row=3,column=3)
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="1",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="2",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="3",command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="*",bg="Light Grey",command=lambda:btnClick('*')).grid(row=4,column=3)
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="0",bg="Light Grey",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="C",bg="Light Grey",command=btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="=",bg="Light Grey",command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="/",bg="Light Grey",command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()
