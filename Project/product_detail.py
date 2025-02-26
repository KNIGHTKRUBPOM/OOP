from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
        Style("""
        .product-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 20px;
            padding: 20px;
            max-width: 1200px;
            margin: auto;
        }
        
        .product-card {
            display: flex;
            align-items: center;
            gap: 20px;
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        }

        .product-image {
            width: 250px;
            height: auto;
            object-fit: contain;
        }

        .product-details {
            flex: 1;
        }

        .product-title {
            font-size: 1.5em;
            font-weight: bold;
        }

        .product-price {
            font-size: 1.2em;
            color: #f39c12;
        }

        .product-description {
            font-size: 1em;
            color: #333;
        }
        """),
    )
)

class Product:
    def __init__(self, name, price, description, stock, img):
        self.__name = name
        self.__price = price
        self.__img = img
        self.__description = description
        self.__stock = stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_img(self):
        return self.__img

    def get_description(self):
        return self.__description
    
    def get_stock(self):
        return self.__stock
    
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
product1 = Product("Apple iPhone 13 128GB Midnight", "฿17,200", "iPhone 13 ระบบกล้องคู่ที่ล้ำหน้าที่สุดเท่าที่เคยมีมาบน iPhone พร้อมชิป A15 Bionic ที่เร็วสุดขั้ว, แบตเตอรี่ที่ใช้งานได้นานขึ้น แบบก้าวกระโดดครั้งใหญ่, ดีไซน์ที่ทนทาน, 5G ที่เร็วสุดแรงและจอภาพ Super Retina XDR ที่สว่างยิ่งขึ้น", 5, "PIC\Apple iPhone 13 128GB Midnight.png")
system.add_product(product1)

@rt('/')
def get():
    return Div(
        Div(id="results", cls="product-container", *[
            Div(
                Img(src=product.get_img(), alt=product.get_name(), cls="product-image"),
                Div(
                    H3(product.get_name(), cls="product-title"),
                    P(f"Price : {product.get_price()} THB", cls="product-price"),
                    P(product.get_description(), cls="product-description"),
                    cls="product-details"
                ),
                cls="product-card"
            ) for product in system.get_lst_product()
        ]),
        Div(
            P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"),
            cls="container"
        )
    )

serve()
