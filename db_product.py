import pymysql

def product_menu():            # Product Menu
    print("=====Products Menu====")
    print("======================")
    print("==1) Products List====")
    print("==2) Add Products=====")
    print("==3) Update Products==")
    print("==4) Delete Products==")
    print("=0) Back to Main Menu=")
    print("======================")

conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password',
cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

def products():
    while True:
        product_menu()
        products_option = input("Please Enter a choice! ")
        if products_option == "0":         # back to main menu
            break
        elif products_option == "1":       # list avaialable products
            list_option = input("Looking for Product List(PL)/ Inventory(I) ?")
            if list_option == "PL":
                cur.execute("select * from products")
                products_list = cur.fetchall()
                for product in products_list:
                    print(str(product).strip("{").replace("}","\n"))
            elif list_option == "I":  # monitory of inventory
                cur.execute("select * from inventory")
                inventory_list = cur.fetchall()
                for inventory in inventory_list:
                    print(inventory)
        elif products_option == "2":      # add new products
            new_name = input("Enter New Product's Name! ")
            new_price = float(input ("Enter New Price! "))
            try:
                cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (new_name, new_price))
                conn.commit()
                cur.execute("select * from products")
                products_list = cur.fetchall()
                for product in products_list:
                    print(str(product).strip("{").replace("}","\n"))
            except Exception as e:
                print("Error Found:", e)
        elif products_option == "3":    # update products list
            cur.execute("select * from products")
            products_list = cur.fetchall()
            for product in products_list:
                print(str(product).strip("{").replace("}","\n"))
            product_id = int(input("Enter ID of Respective Products!"))
            new_name = input("Enter New Name of Product! ")
            new_price = float(input("Enter New Price! "))
            if product_id != "":
                if new_name == "" and new_price == "":
                    pass
                elif new_price == "" and new_name != "":
                    cur.execute("UPDATE couriers SET name = %s where id = %s", (new_name, product_id))
                    conn.commit()
                elif new_price != "" and new_name == "":
                    cur.execute("UPDATE couriers SET price = %s where id = %s", (new_price, product_id))
                    conn.commit()
                try:
                    cur.execute("UPDATE products SET name = %s, price = %s where id = %s", (new_name, new_price, product_id))
                    conn.commit()
                    cur.execute("select * from products")
                    products_list = cur.fetchall()
                    for product in products_list:
                        print(str(product).strip("{").replace("}","\n"))
                except Exception as e:
                    print("Error Found:", e)

        elif products_option == "4":   # delete product from product list
            cur.execute("select * from products")
            products_list = cur.fetchall()
            for product in products_list:
                print(str(product).strip("{").replace("}","\n"))
            product_id = int(input("Enter the id of item needs to be deleted! "))
            try:
                cur.execute("DELETE FROM products WHERE id = %s", (product_id))
                conn.commit()
                cur.execute("select * from products")
                products_list = cur.fetchall()
                for product in products_list:
                    print(str(product).strip("{").replace("}","\n"))
            except Exception as e:
                print("Error Found:", e)