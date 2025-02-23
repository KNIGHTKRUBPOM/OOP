from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
            Style("""
                .highlight { color: red; font-weight: bold; }
                .important { background-color: yellow; padding: 2px; }
                .box { border: 2px solid black; padding: 10px; margin-top: 10px; background-color: #f0f0f0; }
            """),
        )
    )

class Product:
    def __init__(self, name, price, img):
        self.__name = name
        self.__price = price
        self.__img = img

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def get_img(self):
        return self.__img
    
class System:
    def __init__(self):
        self.__lst_product = []
    
    def get_lst_product(self):
        return self.__lst_product
    
    def add_product(self, product):
        self.__lst_product.append(product)

    def search(self, name):
        result = []
        for product in self.__lst_product:
            if name.lower() in product.get_name().lower():
                result.append(product)
        return result
            
system = System()
product1 = Product("Apple iPhone 13 128GB Midnight", "฿17,200", "PIC\Apple iPhone 13 128GB Midnight.png")
product2 = Product("Apple iPhone 16e 128GB Black", "฿22,900", "PIC\Apple iPhone 16e 128GB Black.png")
product3 = Product("Apple iPhone 16e 128GB White", "฿22,900", "PIC\Apple iPhone 16e 128GB White.png")
product4 = Product("ร่ม Jisulife FA52 Portal Umbrella Fan Pink", "฿1,190", "PIC\ร่ม Jisulife FA52 Portal Umbrella Fan Pink.png")
product5 = Product("Apple iPhone 16 Pro Max 256GB Desert Titanium", "฿46,400", "PIC\Apple iPhone 16 Pro Max 256GB Desert Titanium.png")
product6 = Product("Apple Watch Series 10 GPS 42mm Rose Gold Aluminium Case with Light Blush Sport Band - S/M", "฿13,300", "PIC\Apple Watch Series 10 GPS 42mm Rose Gold Aluminium Case with Light Blush Sport Band.png")
product7 = Product("Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue", "฿21,900", "PIC\Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue.png")
product8 = Product("สมาร์ทโฟน Samsung Galaxy S25 (12+512) Silver Shadow (5G)", "฿34,900", "PIC\สมาร์ทโฟน Samsung Galaxy S25 (12+512) Silver Shadow (5G).png")

system.add_product(product1)
system.add_product(product2)
system.add_product(product3)
system.add_product(product4)
system.add_product(product5)
system.add_product(product6)
system.add_product(product7)
system.add_product(product8)

@rt('/')
def get():
    return Titled("Search Product",
                Form(Input(id="name", placeholder="Search products...",
                    hx_get="/search", target_id="results", hx_trigger="keyup delay:500ms")),
                Div(id="results", *[Card(
                    Img(src=product.get_img(), alt=product.get_name(), width="200", height="200"),
                    H3(product.get_name()),
                    P(f"Price : {product.get_price()} THB"),
                )for product in system.get_lst_product()]))

@rt('/search')
def get(name: str):
    results = system.search(name)
    if results:
        return Div(*[Card(
            Img(src=product.get_img(), alt=product.get_name(), width="200", height="200"),
            H3(product.get_name()),
            P(f"Price : {product.get_price()} THB"),
        ) for product in results])
    else:
        return Div(P("Products Not Found."))

serve()