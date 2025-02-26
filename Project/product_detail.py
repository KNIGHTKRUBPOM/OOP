from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
        Style("""
        html, body {
            background-color: #ffffff !important;
            color: black;
        }
        .container, .product-container {
            background-color: #ffffff !important;
        }
        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
            background-color: #ffffff;
            color: black;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            position: relative;
        }
        .header-title {
            font-size: 28px;
            font-weight: bold;
            color: #f39c12;
        }
        .product-detail-container {
            display: flex;
            gap: 20px;
            max-width: 1000px;
            margin: auto;
            padding: 20px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .product-image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 360px;
            height: 360px;
        }
        .product-image img {
            width: 150px !important;
            height: 150px !important;
            object-fit: cover;
            display: block;
            border-radius: 10px;
        }
        .product-info {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .buy-btn {
            background-color: #f39c12;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
        }
        .footer {
            background-color: #ffffff !important;
            color: black;
            text-align: center;
            padding: 15px 20px;
            font-size: 14px;
            border-top: 1px solid #ddd;
            margin-top: auto;
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
        return [p for p in self.__lst_product if name.lower() in p.get_name().lower()]

system = System()
product1 = Product("Apple iPhone 13 128GB Midnight", "฿17,200", "iPhone 13 ระบบกล้องคู่ที่ล้ำหน้าที่สุดเท่าที่เคยมีมาบน iPhone พร้อมชิป A15 Bionic ที่เร็วสุดขั้ว, แบตเตอรี่ที่ใช้งานได้นานขึ้น แบบก้าวกระโดดครั้งใหญ่, ดีไซน์ที่ทนทาน, 5G ที่เร็วสุดแรงและจอภาพ Super Retina XDR ที่สว่างยิ่งขึ้น", 5, "PIC\Apple iPhone 13 128GB Midnight.png")
system.add_product(product1)

@rt('/')
def get():
    return Div(
        Div(H1("ORANGE", cls="header-title"), cls="header-container"),
        Div(
            Div(
                Div(
                    Img(src=product1.get_img(), alt=product1.get_name(), cls="product-image"),
                    cls="product-image-container"
                ),
                Div(
                    H2(product1.get_name()),
                    P(f"ราคา: {product1.get_price()}"),
                    P(product1.get_description()),
                    Button("ซื้อเลย", cls="buy-btn"),
                    cls="product-info"
                ),
                cls="product-detail-container"
            ),
            cls="container"
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

serve()
