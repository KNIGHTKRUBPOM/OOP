from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
            Style("""
html, body {
    background-color: #ffffff !important; /* บังคับให้เป็นสีขาว */
    color: black; /* ทำให้ข้อความมองเห็นได้ชัดเจน */
}
.container, .product-container {
    background-color: #ffffff !important;
}
body {
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    min-height: 100vh; /* ใช้ความสูงเต็มหน้าจอ */
    display: flex;
    flex-direction: column;
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background-color: #ffffff; /* Header สีขาว */
    color: black;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* เงาเบาๆ */
    position: relative;
}

.header-title {
    font-size: 28px; /* เพิ่มขนาดโลโก้ */
    font-weight: bold;
    color: #f39c12;
}

.header-buttons {
    display: flex;
    gap: 15px;
    align-items: center;
}

.icon {
    width: 30px;  /* ลดขนาดไอคอน */
    height: 30px; /* ลดขนาดไอคอน */
}

.login {
    display: flex;
    align-items: center;
    font-size: 14px;
    cursor: pointer;
}

.login:hover {
    transform: translateY(-3px);
}

.cart:hover {
    transform: translateY(-3px);
}
                           
.login, .cart {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 16px;
    cursor: pointer;
    color: black; /* เปลี่ยนเป็นสีดำ */
}

.search-container {
    display: flex;
    align-items: center;
    width: 800px;  /* ลดขนาดกล่องค้นหา */
    height: 50px;
    background: white;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid #ddd;
}

.search-input {
    flex: 1;
    padding: 10px;
    font-size: 14px;
    border: none;
    outline: none;
    color: black;
    background: transparent;
    text-align: left; /* จัดข้อความไปทางซ้าย */
}

.search-input::placeholder {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: left; /* จัด placeholder ไปทางซ้าย */
}
                  
.search-btn {
    background: transparent;
    border: none;
    padding: auto; /* ปรับขนาดปุ่มให้เล็กลง */
    cursor: pointer;
}
                  
.search-input:focus {
    outline: none;
    box-shadow: none;
    border: none;
}

.product-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
    max-width: 1200px;
    margin: auto;
}

.product-card {
    background-color: #ffffff; /* เปลี่ยนเป็นขาว */
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* ลดเงาให้อ่อนลง */
    text-align: center;
    transition: transform 0.2s;
    cursor: pointer;
}

.product-card:hover {
    transform: translateY(-3px);
}

.product-card img {
    width: 100%;
    height: 200px;
    object-fit: contain;
}

.product-card h3 {
    font-size: 1em;
    margin: 10px 0;
    color: black;
}

.product-card p {
    color: #333; /* เปลี่ยนเป็นสีเทาเข้ม */
    font-weight: bold;
    font-size: 1em;
}
                  
.container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
                  
.footer {
    background-color: #ffffff !important;
    color: black;
    text-align: center;
    padding: 15px 20px;
    font-size: 14px;
    border-top: 1px solid #ddd;
    margin-top: auto; /* ดัน footer ไปอยู่ล่าง */
}

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
product9 = Product("Apple iPhone 16","฿28,700","PIC\9.png")
product10 = Product("Apple iPhone 16 Plus","฿34,400","PIC/Apple iPhone 16 Plus.png")
product11 = Product("Apple iPad mini 7 (A17 Pro) Wi-Fi 8.3 inch","฿17,900","PIC/Apple iPad mini 7.png")
product12 = Product("Apple iPad Air 5 Wi-Fi + Cellular 10.9 inch 2022","฿20,900","PIC/12.png")
product13 = Product("Apple MacBook Pro 14 M4 chip","฿54,900","PIC/13.png")
product14 = Product("Apple iMac 24 M4 chip Nano-texture glass","฿58,900","PIC/14.png")
product15 = Product("หูฟังไร้สาย Apple AirPods 4","฿4,150","PIC/15.png")
product16 = Product("Apple AirPods Max - Purple","฿19,900","PIC/16.png")
product17 = Product("หูฟังไร้สาย Beats Studio Buds Black","฿4,500","PIC/17.png")
product18 = Product("Apple Watch Series 10 (42mm) Aluminium","฿13,300","PIC/18.png")
product19 = Product("Apple Watch Series  9 (45mm) Aluminium","฿12,200","PIC/19.png")
product20 = Product("Apple 20W USB-C Port Power Adapter","฿640","PIC/20.png")
product21 = Product("Apple USB-C to Lightning Cable (1m)","฿750","PIC/21.png")

system.add_product(product1)
system.add_product(product2)
system.add_product(product3)
system.add_product(product4)
system.add_product(product5)
system.add_product(product6)
system.add_product(product7)
system.add_product(product8)
system.add_product(product9)
system.add_product(product10)
system.add_product(product11)
system.add_product(product12)
system.add_product(product13)
system.add_product(product14)
system.add_product(product15)
system.add_product(product16)
system.add_product(product17)
system.add_product(product18)
system.add_product(product19)
system.add_product(product20)
system.add_product(product21)

@rt('/')
def get():
    return Div(
        Div(
            H1("ORANGE", cls="header-title"),  # โลโก้ใหญ่ขึ้น
            Div(
                Form(
                    Div(
                        Input(id="name", placeholder="ค้นหาสินค้าที่ต้องการที่นี่...", 
                              cls="search-input", hx_get="/search", 
                              target_id="results", hx_trigger="keyup delay:500ms"),
                        Button(cls="search-btn"),
                        cls="search-container"
                    )
                ),
            ),
            Div(
                Div(
                    Img(src="https://cdn-icons-png.flaticon.com/128/1077/1077063.png", cls="icon"),
                    Span("เข้าสู่ระบบ", cls="login-text"),
                    cls="login"
                ),
                Img(src="https://cdn-icons-png.flaticon.com/128/5392/5392794.png", cls="icon cart"),
                cls="header-buttons"
            ),
            cls="header-container"
        ),
        Div(id="results", cls="product-container", *[
            Div(
                Img(src=product.get_img(), alt=product.get_name()),
                H3(product.get_name()),
                P(f"Price : {product.get_price()} THB"),
                cls="product-card"
            ) for product in system.get_lst_product()
        ]),Div(
    Div(id="results", cls="product-container"),
    Div(P("© 2025 OrAnGe Store | All Rights Reserved. | 67015105, 67015155, 67015167", cls="footer")),
    cls="container"
)
    )



@rt('/search')
def get(name: str):
    results = system.search(name)
    if results:
        return Div(cls=("product-container"), *[Div(
            Img(src=product.get_img(), alt=product.get_name()),
            H3(product.get_name()),
            P(f"Price : {product.get_price()} THB"),
            cls=("product-card")
        ) for product in results])
    else:
        return Div(P("Products Not Found."))

serve()