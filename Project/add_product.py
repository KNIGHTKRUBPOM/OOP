from fasthtml.common import *
import os

app, rt = fast_app(
    hdrs=(Style("""
body {
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
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
.search-container {
    display: flex;
    align-items: center;
    width: 800px;
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
}
.search-btn {
    background: #f39c12;
    color: white;
    padding: 10px 15px;
    border-radius: 0 20px 20px 0;
    transition: background 0.3s ease;
}

.search-btn:hover {
    background: #e67e22;
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
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
}
.product-card:hover {
    transform: scale(1.05);
}
.footer {
    background-color: #ffffff;
    color: black;
    text-align: center;
    padding: 15px 20px;
    font-size: 14px;
    border-top: 1px solid #ddd;
    margin-top: auto;
}
button {
    background: #f39c12;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease-in-out;
}
button:hover {
    background: #e67e22;
}
input {
    background-color: white;
    color: black;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 100%;
    max-width: 300px;
    box-sizing: border-box;
    margin: 5px 0;
}
        """),)
)

UPLOAD_DIR = "PIC"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class Product:
    def __init__(self, name, price, description, stock ,img):
        self.__name = name
        self.__price = price
        self.__img = img
        self.__description = description
        self.__stock  = stock

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

system = System()

@rt('/')
def get():
    return Div(
        Div(H1("ORANGE Admin Add", cls="header-title"), cls="header-container"),
        Form(
            Input(id="name", placeholder="ชื่อสินค้า"),
            Input(id="price", placeholder="ราคาสินค้า"),
            Input(id="description", placeholder="รายละเอียดสินค้า"),
            Input(id="quantity", placeholder="จำนวน"),
            Input(type="file", id="img", name="img"),
            Button("Add"),
            hx_post="/add",
            hx_target="#items",
            hx_swap="beforeend",
            enctype="multipart/form-data"
        ),
        Div(id="items", cls="product-container", children=[
            Div(
                Img(src=p.get_img(), alt=p.get_name()),
                H3(p.get_name()),
                P(f"Price : {p.get_price()} THB"),
                cls="product-card"
            ) for p in system.get_lst_product()
        ]),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="footer")
    )

@rt('/add')
def post(name: str, price: str, description:str ,quantity:str ,img: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, img.filename)
    with open(file_path, "wb") as f:
        f.write(img.file.read())
    relative_path = f"{UPLOAD_DIR}/{img.filename}"

    product = Product(name, price, description, description, relative_path)
    system.add_product(product)
    
    return Div(
        Img(src=product.get_img(), alt=product.get_name()),
        H3(product.get_name()),
        P(f"Price : {product.get_price()} THB"),
        cls="product-card"
    )

serve()

