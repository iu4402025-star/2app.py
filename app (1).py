import streamlit as st
from urllib.parse import quote

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="STYLEHUB | Fashion Store",
    page_icon="👗",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: #f8f6f2;
}
[data-testid="stHeader"] {
    background: transparent;
}
.hero {
    background: linear-gradient(110deg, #171717, #594638);
    padding: 48px 34px;
    border-radius: 18px;
    color: white;
    margin: 12px 0 25px 0;
}
.hero h1 {
    color: white;
    font-size: clamp(30px, 5vw, 52px);
    font-weight: 700;
    margin-bottom: 8px;
}
.hero p {
    color: #eee5dc;
    font-size: 17px;
}
.product-name {
    color: #29231e;
    font-weight: 600;
    min-height: 48px;
}
.product-price {
    color: #9a643c;
    font-size: 19px;
    font-weight: 700;
}
.section-title {
    color: #28221e;
    font-size: 28px;
    font-weight: 700;
    margin: 20px 0 12px 0;
}
div.stButton > button {
    background: #29231e;
    color: white;
    border: 0;
    border-radius: 8px;
    min-height: 42px;
}
div.stButton > button:hover {
    background: #9a643c;
    color: white;
}
[data-testid="stMetric"] {
    background: white;
    padding: 14px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SHOP DETAILS ----------------
SHOP_NAME = "STYLEHUB"
SHOP_PHONE = "923001234567"  # Change this to your WhatsApp number, including country code.

PRODUCTS = [
    {
        "id": 1, "name": "Premium Men's T-Shirt", "category": "Men",
        "price": 1800, "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=700",
        "description": "Comfortable everyday cotton T-shirt."
    },
    {
        "id": 2, "name": "Classic Men's Jacket", "category": "Men",
        "price": 4500, "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=700",
        "description": "A smart jacket for a stylish look."
    },
    {
        "id": 3, "name": "Women's Fashion Dress", "category": "Women",
        "price": 3500, "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=700",
        "description": "An elegant dress for special occasions."
    },
    {
        "id": 4, "name": "Women's Casual Outfit", "category": "Women",
        "price": 2800, "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=700",
        "description": "Relaxed and modern casual fashion."
    },
    {
        "id": 5, "name": "Kids Fashion Outfit", "category": "Kids",
        "price": 1600, "image": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=700",
        "description": "Comfortable clothing for kids."
    },
    {
        "id": 6, "name": "Premium Hoodie", "category": "Men",
        "price": 3200, "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=700",
        "description": "A soft and warm everyday hoodie."
    },
    {
        "id": 7, "name": "Women's Summer Wear", "category": "Women",
        "price": 2400, "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=700",
        "description": "A light outfit for summer days."
    },
    {
        "id": 8, "name": "Kids Casual Wear", "category": "Kids",
        "price": 1900, "image": "https://images.unsplash.com/photo-1503919005314-30d93d07d823?w=700",
        "description": "Trendy and comfortable kids wear."
    },
]

# ---------------- SESSION STATE ----------------
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- HEADER / NAVIGATION ----------------
header_left, header_right = st.columns([3, 1])
with header_left:
    st.markdown(
        f"<h2 style='color:#29231e;margin-bottom:0'>👗 {SHOP_NAME}</h2>"
        "<p style='color:#92765e;margin-top:0'>YOUR STYLE, YOUR IDENTITY</p>",
        unsafe_allow_html=True
    )
with header_right:
    item_count = sum(st.session_state.cart.values())
    st.metric("Items in cart", item_count)

nav1, nav2, nav3, nav4 = st.columns(4)
for col, label, page in [
    (nav1, "🏠 Home", "Home"),
    (nav2, "👕 Shop", "Shop"),
    (nav3, "🛒 My Cart", "Cart"),
    (nav4, "📞 Contact", "Contact"),
]:
    with col:
        if st.button(label, use_container_width=True):
            st.session_state.page = page
            st.rerun()

st.divider()

# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>NEW FASHION COLLECTION</h1>
        <p>Discover your perfect style with our latest clothing collection.</p>
        <h3>STYLE THAT SPEAKS FOR YOU.</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">✨ Featured Collection</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for col, product in zip(cols, PRODUCTS[:4]):
        with col:
            st.image(product["image"], use_container_width=True)
            st.markdown(f'<div class="product-name">{product["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-price">Rs. {product["price"]:,}</div>', unsafe_allow_html=True)
            if st.button("Add to Cart", key=f"home_add_{product['id']}", use_container_width=True):
                pid = product["id"]
                st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
                st.toast("Product added to cart!")
                st.rerun()

    st.markdown("---")
    st.markdown('<div class="section-title">Why Shop With Us?</div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    a.info("📦 **Quality Products**\n\nCarefully selected clothing.")
    b.info("💰 **Affordable Prices**\n\nFashion for every budget.")
    c.info("❤️ **Customer Service**\n\nWe care about your satisfaction.")

# ---------------- SHOP PAGE ----------------
elif st.session_state.page == "Shop":
    st.title("🛍️ Our Clothing Collection")
    st.write("Search and explore our latest fashion products.")

    search_text = st.text_input("🔍 Search products by name")
    category = st.selectbox("Choose a category", ["All", "Men", "Women", "Kids"])

    filtered_products = PRODUCTS
    if category != "All":
        filtered_products = [p for p in filtered_products if p["category"] == category]
    if search_text.strip():
        filtered_products = [
            p for p in filtered_products
            if search_text.lower() in p["name"].lower()
        ]

    if not filtered_products:
        st.warning("No products found. Try another search.")
    else:
        cols = st.columns(4)
        for index, product in enumerate(filtered_products):
            with cols[index % 4]:
                st.image(product["image"], use_container_width=True)
                st.markdown(f'<div class="product-name">{product["name"]}</div>', unsafe_allow_html=True)
                st.caption(product["description"])
                st.markdown(f'<div class="product-price">Rs. {product["price"]:,}</div>', unsafe_allow_html=True)
                if st.button("Add to Cart 🛒", key=f"shop_add_{product['id']}", use_container_width=True):
                    pid = product["id"]
                    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
                    st.toast("Product added to cart!")
                    st.rerun()

# ---------------- CART PAGE ----------------
elif st.session_state.page == "Cart":
    st.title("🛒 Your Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty. Visit the Shop page to add products.")
    else:
        total = 0
        for pid in list(st.session_state.cart.keys()):
            product = next(p for p in PRODUCTS if p["id"] == pid)
            quantity = st.session_state.cart[pid]
            subtotal = product["price"] * quantity
            total += subtotal

            c1, c2, c3 = st.columns([3, 1, 1])
            with c1:
                st.write(f"**{product['name']}**")
                st.caption(f"Rs. {product['price']:,} each")
            with c2:
                new_quantity = st.number_input(
                    "Quantity", min_value=1, max_value=20,
                    value=quantity, key=f"qty_{pid}"
                )
                st.session_state.cart[pid] = int(new_quantity)
            with c3:
                st.write(f"Subtotal: Rs. {subtotal:,}")
                if st.button("Remove", key=f"remove_{pid}"):
                    del st.session_state.cart[pid]
                    st.rerun()
            st.divider()

        # Recalculate after quantity controls
        total = sum(
            next(p for p in PRODUCTS if p["id"] == pid)["price"] * qty
            for pid, qty in st.session_state.cart.items()
        )
        st.subheader(f"Total Amount: Rs. {total:,}")

        st.subheader("Customer Details")
        customer_name = st.text_input("Customer name")
        phone = st.text_input("Phone number")
        address = st.text_area("Delivery address")

        if st.button("Prepare WhatsApp Order", use_container_width=True):
            if not customer_name.strip() or not phone.strip() or not address.strip():
                st.error("Please enter your name, phone number and delivery address.")
            else:
                order_lines = [
                    f"- {next(p for p in PRODUCTS if p['id'] == pid)['name']} x {qty}"
                    for pid, qty in st.session_state.cart.items()
                ]
                message = (
                    f"Hello {SHOP_NAME}! I would like to place an order.\\n"
                    f"Customer: {customer_name}\\nPhone: {phone}\\n"
                    f"Address: {address}\\nProducts:\\n"
                    + "\\n".join(order_lines)
                    + f"\\nTotal: Rs. {total:,}"
                )
                whatsapp_url = f"https://wa.me/{SHOP_PHONE}?text={quote(message)}"
                st.success("Your order message is ready. Open WhatsApp to send it to the shop.")
                st.link_button("Send Order on WhatsApp", whatsapp_url)

# ---------------- CONTACT PAGE ----------------
elif st.session_state.page == "Contact":
    st.title("📞 Contact STYLEHUB")
    st.write("We would love to hear from you!")
    st.markdown("""
    **Business:** STYLEHUB Fashion Store

    **Address:** Add your shop address here.

    **Phone:** +92 300 1234567

    **Email:** stylehub@example.com

    **Opening Hours:** Monday – Saturday
    """)
    st.link_button("Chat on WhatsApp", f"https://wa.me/{SHOP_PHONE}")

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    f"<div style='text-align:center;padding:18px;color:#786b60'>"
    f"<h3>{SHOP_NAME} 👗</h3>Your Fashion Destination"
    f"<p>© 2026 {SHOP_NAME}. All Rights Reserved.</p></div>",
    unsafe_allow_html=True
)
