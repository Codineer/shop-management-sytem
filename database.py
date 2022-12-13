from prettytable import PrettyTable


class Database:
    def __init__(self, database_name):
        import mysql.connector as m1

        self.var = "w"
        self.conn = m1.connect(host="localhost", user="root", password="utkarsh")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % database_name)
        self.cursor.execute("USE %s" % database_name)
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS products (product_id INTEGER unsigned primary key auto_increment, product_name VARCHAR(50) not null,quantity INTEGER unsigned NOT NULL,Company enum('asus','msi','asrock','gigabyte','inno3d') not null ,gpu_company enum('nvidea','amd') not null,price INTEGER unsigned NOT NULL,vram_gb INTEGER unsigned NOT NULL)"
        )
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins(admin_id integer primary key auto_increment,admin_name VARCHAR(20) unique not null,pas VARCHAR(20) not null)"
        )
        self.producttabletemplate = [
            "product id",
            "product name",
            "quantity",
            "graphics card seller",
            "gpu company",
            "price",
            "vram",
        ]
        try:
            self.cursor.execute(
                "INSERT INTO admins (admin_name,pas) VALUES('admin','1234')"
            )
            self.conn.commit()
        except Exception as e:
            pass
        
    def make_database_table(self,table):
        table = PrettyTable(table)
        for i in self.cursor:
            table.add_row(i)
        print(table)

    def add_admin(self, adminname, password):
        try:
            self.cursor.execute(
                "INSERT INTO admins (admin_name,pas) VALUES('{}','{}')".format(adminname, password)
            )
            self.conn.commit()
        except Exception as e:
            print("something wrong happend.try again,maybe user name taken already")

    def delete(self, id):
        self.cursor.execute("DELETE FROM products where product_id={}".format(id))
        self.conn.commit()

    def insert(self):
        forward = True
        productname = input("enter product name")
        self.cursor.execute(
            "SELECT * FROM products WHERE product_name = '{}'".format(productname)
        )
        for i in self.cursor:
            forward = i
        if forward == True:
            quantity = int(input("enter quantity of product"))
            Company = input(
                "enter company name ('asus','msi','asrock','gigabyte','inno3d')"
            )
            gpu_company = input("enter gpu_company('nvidea','amd')")
            price = input("enter price of product")
            vram = int(input("input vram: "))
        self.cursor.execute(
            "INSERT INTO products(product_name,quantity,Company,gpu_company,price,vram_gb) values('{}',{},'{}','{}',{},{})".format(
                productname, quantity, Company, gpu_company, price, vram
            )
        )
        self.conn.commit()

    def showproductsbyvram(self, vram):
        self.cursor.execute("select * from products where vram_gb = {}".format(vram))
        self.make_database_table(self.producttabletemplate)

    def showproductsbygpu_company(self, gpu):
    
        if gpu not in ["nvidea", "amd"]:
            print("no such gpu company available:")
            return
        self.cursor.execute(
            "select * from products where gpu_company = '{}'".format(gpu)
        )
        self.make_database_table(self.producttabletemplate)

    def showproductsbyseller(self, comp):
        if comp not in ("asus", "msi", "asrock", "gigabyte", "inno3d"):
            print("no such seller available")
            return
        self.cursor.execute("select * from products where Company = '{}'".format(comp))
        self.make_database_table(self.producttabletemplate)

    def showproductsbybudget(self, maximum_price):
        self.cursor.execute(
            "select * from products where price < {}".format(maximum_price)
        )
        self.make_database_table(self.producttabletemplate)

    def showproductsrecords(self):
        self.cursor.execute("select * from products")
        self.make_database_table(self.producttabletemplate)
    def showproductsrecordsbyname(self, name):
        self.cursor.execute("select * from products where LOWER(product_name) = '{}'".format(name.lower()))
        self.make_database_table(self.producttabletemplate)
    def updateprice(self, id):
        price = input("enter price of product")
        self.cursor.execute(
            "UPDATE products SET price={} WHERE product_id={}".format(price, id)
        )
        self.conn.commit()

    def updatequantity(self, id):
        quantity = input("enter quantity of product")
        self.cursor.execute(
            "UPDATE products SET quantity={} WHERE product_id={}".format(quantity, id)
        )
        self.conn.commit()


if __name__ == "__main__":
    db = Database("graphics_shop")
    db.showproductsbybudget(2000000)
    # db.showproductsrecords()
    # db.updateprice(1)
    # db.updatequantity(1)
