from billing import shop

running = True
shop_name = input("enter your shop name")
shopdatabase = shop(shop_name)

print("================================================================================")

print("                       WELCOME TO OUR SHOP MANAGEMENT SERVICE version(1.0.2)")

print("================================================================================")
usertype=int(input("1.for admin access\nany other number for normal user access\n-->"))
previliges="normal"
if usertype==1:
    print("admin previliges will be available after login:")
    flag=False
    while True:
    
        username=input("enter username: ")
        password=input("enter password: ")
        shopdatabase.cursor.execute("select * from admins")
        for i in shopdatabase.cursor.fetchall():
            if username==i[1] and password==i[2]:
                previliges="admin"
                print("admin access granted")
                flag=True
                break
        
        if flag==False:
            ch=int(input("access denied.type 0 for for normal user access and 1 for trying again"))
            if ch==1:
                continue
            else:
                break
        else:
            break
if previliges=="normal":
    print("normal previliges given !")
while running:
    print("choose your service")
    userinp = int(
        input(
            "1. for accessing stocks data\n3. for quiting application\nbelow options for admins only \n2. for using billing service\n4. adding admin\n-->"
        )
    )
    if userinp == 1:

        while True:
            ser1inp = int(
            input(
                """


-----------------------------------------------------------------------------------------------------------------------------------------
#options for chosen service
    1. for seeing all products data 
    6. for back to main menu
    7. for searching products by vram
    8. for searching products according to price
    9. for searching products by gpu_company
    10. for searching products by graphics card manufacturer
    11. for searching products by name
    below options for admins only
    2. for updating price of product
    3. for updating quantity of product
    4. for inserting new product data
    5. for deleting existing product data

--->"""
            ))
        
            if ser1inp== 1:
                shopdatabase.showproductsrecords()
            elif ser1inp== 2 and previliges=="admin":
                id= int(input("enter product id of product whose price is to be altered:"))                    
                shopdatabase.updateprice(id)

            elif ser1inp== 3 and previliges=="admin":
                quantity= int(input("enter product id of product whose price is to be altered:"))
                shopdatabase.updatequantity(quantity)


            elif ser1inp== 4 and previliges=="admin":           
                shopdatabase.insert()
            elif ser1inp==5 and previliges=="admin":
                pr_id= int(input("enter product id of product whose record is to be deleted: "))
                shopdatabase.delete(pr_id)
            elif ser1inp==6:
                print("back to main menu...")
                break
            elif ser1inp== 7:
                vram= int(input("enter vram"))
                shopdatabase.showproductsbyvram(vram)
            elif ser1inp== 8:
                maximum= int(input("enter your maximum price for product"))
                shopdatabase.showproductsbybudget(maximum)
            elif ser1inp== 9:
                gpu= input("enter your GPU")
                shopdatabase.showproductsbygpu_company(gpu)
            elif ser1inp== 10:
                company = input("enter your GPU card manufacturer")
                shopdatabase.showproductsbygpu_company(company)
            elif ser1inp== 11:
                name = input("enter name of product")
                shopdatabase.showproductsrecordsbyname(name)
            else:
                continue

    elif userinp == 2 and previliges=="admin":
        while True:
            ser2inp = int(
            input(
                """


-----------------------------------------------------------------------------------------------------------------------------------------                
#options for chosen service
    1. for seeing all customers data 
    2. for searching customers by name
    3. for searching customers by customer id
    4. for insert new transaction data
    5. for back to main menu
-->"""
            )
        )
            
            if ser2inp== 1:
                shopdatabase.showshoprecords()

            elif ser2inp== 2 :
                cus_name=input("enter customer name: ")
                shopdatabase.searchcustomersbyname(cus_name)

            elif ser2inp== 3 :
                cus_id=int(input("enter customer id: "))
                shopdatabase.searchcustomersbyid(cus_id)

            elif ser2inp== 4 :
                shopdatabase.billing()
            elif ser2inp== 5 :
                print("back to main menu")
                break
            else:
                continue

    

    elif userinp== 4  and previliges=="admin":
        username1=input("enter username: ")
        pas=input("enter password: ")
        shopdatabase.add_admin(username1,pas)
    elif userinp == 3:
        shopdatabase.cursor.close()
        break