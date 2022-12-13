from database import Database
from prettytable import PrettyTable
import random


class shop(Database):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.cursor.execute(
            "create table if not exists customers (record_id bigint primary key auto_increment,customer_id int, customer_name varchar(40) not null,product_bought varchar(40) not null,quantity integer unsigned not null,dateofpurchasing datetime default now(), total_billings integer unsigned not null,product_id int unsigned not null,foreign key(product_id) references products(product_id))"
        )
        self.prettylist = [
            "record id",
            "customer_id",
            "customer_name",
            "product_bought",
            "quantity",
            "dateofpurchasing",
            "total_billings",
            "product_id",
        ]
    

    def billing(self):
        while True:
            try:
                n = int(input("enter number of products to purchase\enter -1 for going to main menu: "))
                if n==-1:
                    break
                customername = input("enter name of customername: ").lower()
                self.cursor.execute("select * from customers")
                idfouund = False
                idlist = []
                for i in self.cursor.fetchall():
                    if i[2] == customername:
                        customer_id = i[1]
                        idfouund = True
                    idlist.append(i[1])
                if idfouund == False:
                    while True:
                        customer_id = random.randint(0, 40000)
                        if customer_id in idlist:
                            continue
                        else:
                            break
                while n > 0:
                    # customer_id=0

                    productid = int(input("enter product id to purchase\enter -1 for going back: "))
                    if productid==-1:
                        break
                    self.cursor.execute("select * from products")
                    flag = False
                    productname = ""
                    price = 0
                    for i in self.cursor:
                        if i[0] == productid:
                            productname = i[1]
                            price = i[5]
                            print(price, type(price))
                            flag = True
                    if flag:
                        q = int(input("enter quantity of product to purchase: "))
                        actualq=self.cursor.execute("select * from products where product_id={}".format(productid))
                        actualq=self.cursor.fetchone()[2]
                        if actualq<q:
                            print("not enough stock,do this entry again")
                            n+=1
                        else:
                            # customername = input("enter name of customername: ")
                            totalbillings = price * q
                            print(totalbillings)
                            self.cursor.execute(
                                "INSERT INTO customers (customer_id,customer_name,product_bought,quantity,total_billings,product_id) VALUES({},'{}','{}',{},{},{})".format(
                                    customer_id,
                                    customername,
                                    productname,
                                    q,
                                    totalbillings,
                                    productid,
                                )
                            )
                            
                            self.cursor.execute(
                                f"update products set quantity={actualq-q} where product_id={productid}"
                                )
                            

                            self.conn.commit()

                            print("record inserted successfully")

                    else:
                        print("product not found")
                        n += 1
                    n -= 1

            except Exception as e:
                print(e)
                continue
            else:
                break

    def showshoprecords(self):


        self.cursor.execute("select * from customers")
        self.make_database_table(self.prettylist)

    def searchcustomersbyname(self, customername):
        customername = customername.lower()

        self.cursor.execute(
            "select * from customers where customer_name='{}'".format(customername)
        )
        self.make_database_table(self.prettylist)

    def searchcustomersbyid(self, customerid):
        self.cursor.execute(
            "select * from customers where customer_id='{}'".format(customerid)
        )
        self.make_database_table(self.prettylist)

if __name__ =="__main__":
    here = shop("graphics_shop")
    # here.billing()
    here.showshoprecords()
    # here.showproductsrecords()
    here.searchcustomersbyname("utkarsh shAkya")
    here.searchcustomersbyid(16491)
# here.billing()
# +--------------+-------------------------------------------------+------+-----+---------+----------------+
# | Field        | Type                                            | Null | Key | Default | Extra          |
# +--------------+-------------------------------------------------+------+-----+---------+----------------+
# | product_id   | int unsigned                                    | NO   | PRI | NULL    | auto_increment |
# | product_name | varchar(40)                                     | YES  |     | NULL    |                |
# | quantity     | int unsigned                                    | YES  |     | 0       |                |
# | Company      | enum('asus','msi','asrock','gigabyte','inno3d') | NO   |     | NULL    |                |
# | gpu_company  | enum('nvidea','amd')                            | NO   |     | NULL    |                |
# | price        | int unsigned                                    | YES  |     | NULL    |                |
# | vram_gb      | int unsigned                                    | NO   |     | NULL    |                |
# +--------------+-------------------------------------------------+------+-----+---------+----------------+
# 7 rows in set (0.09 sec)
