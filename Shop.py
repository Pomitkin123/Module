class ShopSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product}' added to {self.shop_name}")

    def list_products(self):
        print(f"Products available in {self.shop_name}:")
        if self.products:
            for product in self.products:
                print(product)
        else:
            print("No products available")


if __name__ == "__main__":
    shop1 = ShopSingleton("MyShop")
    shop2 = ShopSingleton("AnotherShop")


    print(f"Shop 1 ID: {id(shop1)}")  
    print(f"Shop 2 ID: {id(shop2)}")  

    shop1.add_product("Product 1")
    shop2.add_product("Product 2")

    shop1.list_products()  
    shop2.list_products() 
