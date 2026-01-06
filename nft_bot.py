from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

BOT_TOKEN = "8390566895:AAF2UKnG-8H_r6uURAEjhFQJRjtuLTAOcUc"
ADMIN_ID = 6652220800
UPI_ID = "Vipul9784@axl"
USDT_ADDRESS = "0x6868089d01925faaa66c4dd4597a51dd0578d7f2"
USDT_NETWORK = "BEP20"

# 🔥 NFT DATA
NFTS = [
    {"id": 1, "name": "UFC", "price": "₹2479" "→" "(26.5 Usdt)", "image": "https://i.postimg.cc/C1fXnM5R/photo-2026-01-05-15-00-06.jpg"},
    {"id": 2, "name": "Jolly Chimp", "price": "₹849" "→" "(8.93 Usdt)", "image": "https://i.postimg.cc/fR1m8M5x/IMG_20260105_152201_656.jpg"},
    {"id": 3, "name": "Star Notepad", "price": "₹819" "→" "(8.62 Usdt)", "image": "https://i.postimg.cc/rwD5GDGS/IMG_20260105_152201_594.jpg"},
    {"id": 4, "name": "Jack in the Box", "price": "₹3499" "→" "(36.83 Usdt)", "image": "https://i.postimg.cc/fRVY7V70/IMG_20260105_152201_764.jpg"},
    {"id": 5, "name": "Jelly Bunny", "price": "₹799" "→" "(8.41 Usdt)", "image": "https://i.postimg.cc/dVhGRhRd/IMG_20260105_152202_069.jpg"},
    {"id": 6, "name": "UFC", "price": "₹3899" "→" "(41.04 Usdt)", "image": "https://i.postimg.cc/J46bBNXB/IMG_20260105_152202_159.jpg"},
    {"id": 7, "name": "Tama Gadget", "price": "₹749" "→" "(7.88 Usdt)", "image": "https://i.postimg.cc/Vk2nKz4B/IMG_20260105_152202_153.jpg"},
    {"id": 8, "name": "Ramen", "price": "₹730" "→" "(7.68 Usdt)", "image": "https://i.postimg.cc/sgb7T3KP/IMG_20260105_152202_443.jpg"},
    {"id": 9, "name": "Khabib's Papakha", "price": "₹6999" "→" "(73.67 Usdt)", "image": "https://i.postimg.cc/Gm4vP4Pv/IMG_20260105_152202_367.jpg"},
    {"id": 10, "name": "Restless Jar", "price": "₹799" "→" "(8.41 Usdt)", "image": "https://i.postimg.cc/MpgV9zt7/IMG_20260105_152202_202.jpg"},
    {"id": 11, "name": "Lol Pop", "price": "₹819" "→" "(8.62 Usdt)", "image": "https://i.postimg.cc/TPWWYXwy/IMG_20260105_201434_148.jpg"},
    {"id": 12, "name": "Desk Calender", "price": "₹579" "→" "(6.09 Usdt)", "image": "https://i.postimg.cc/y69bRqMC/IMG_20260105_192904_393.jpg"},
    {"id": 13, "name": "Desk Calender", "price": "₹649" "→" "(6.83 Usdt)", "image": "https://i.postimg.cc/WzMYcrGX/IMG_20260105_192904_256.jpg"},
    {"id": 14, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/8kW0v8q3/IMG_20260105_192904_074.jpg"},
    {"id": 15, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/VvjZPMq4/IMG_20260105_192903_955.jpg"},
    {"id": 16, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/QN5y7L2s/IMG_20260105_192903_909.jpg"},
    {"id": 17, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/VvjZPMqg/IMG_20260105_192904_640.jpg"},
    {"id": 18, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/D0qp3sr1/IMG_20260105_192904_626.jpg"},
    {"id": 19, "name": "Desk Calender", "price": "₹549" "→" "(5.77 Usdt)", "image": "https://i.postimg.cc/gJqGcMPx/IMG-20260105-194844-684.jpg"},
    {"id": 20, "name": "Lol Pop", "price": "₹599" "→" "(6.30 Usdt)", "image": "https://i.postimg.cc/P5P3tPkb/IMG-20260105-200409-655.jpg"},
    {"id": 21, "name": "Lol Pop", "price": "₹669" "→" "(7.04 Usdt)", "image": "https://i.postimg.cc/dtxMmMs2/IMG_20260105_200948_068.jpg"},
    {"id": 22, "name": "Lol Pop", "price": "₹649" "→" "(6.83 Usdt)", "image": "https://i.postimg.cc/28KpFpk7/IMG_20260105_200947_899.jpg"},
    {"id": 23, "name": "Lol Pop", "price": "₹789" "→" "(8.30 Usdt)", "image": "https://i.postimg.cc/qM5fXfJX/IMG_20260105_200947_772.jpg"},
    {"id": 24, "name": "Lol Pop", "price": "₹799" "→" "(8.41 Usdt)", "image": "https://i.postimg.cc/L6bdBd95/IMG_20260105_200947_880.jpg"},
    {"id": 25, "name": "Lol Pop", "price": "₹819" "→" "(8.62 Usdt)", "image": "https://i.postimg.cc/DzbbyKZy/IMG_20260105_201433_638.jpg"},
    {"id": 26, "name": "Candy Cane", "price": "₹759" "→" "(7.98 Usdt)", "image": "https://i.postimg.cc/HLTRvnXk/IMG_20260106_132623_951.jpg"},
    {"id": 27, "name": "Candy Cane", "price": "₹849" "→" "(8.93 Usdt)", "image": "https://i.postimg.cc/43Xq2yVc/IMG_20260106_132624_363.jpg"},
    {"id": 28, "name": "Candy Cane", "price": "₹949" "→" "(9.98 Usdt)", "image": "https://i.postimg.cc/R0vyphK0/IMG_20260106_132624_169.jpg"},
    {"id": 29, "name": "Candy Cane", "price": "₹659" "→" "(6.94 Usdt)", "image": "https://i.postimg.cc/HLTRvnXW/IMG_20260106_132624_057.jpg"},
    {"id": 30, "name": "Candy Cane", "price": "₹845" "→" "(8.90 Usdt)", "image": "https://i.postimg.cc/yN7tpxc3/IMG_20260106_132623_869.jpg"},
    {"id": 31, "name": "Candy Cane", "price": "₹699" "→" "(7.36 Usdt)", "image": "https://i.postimg.cc/jjRm32PJ/IMG_20260106_132624_618.jpg"},
    {"id": 32, "name": "Candy Cane", "price": "₹749" "→" "(7.88 Usdt)", "image": "https://i.postimg.cc/KYmwpjBZ/IMG_20260106_132624_553.jpg"},
    {"id": 33, "name": "Candy Cane", "price": "₹739" "→" "(7.78 Usdt)", "image": "https://i.postimg.cc/Pqd9VJYX/IMG_20260106_132624_531.jpg"},
    {"id": 34, "name": "Candy Cane", "price": "₹729" "→" "(7.68 Usdt)", "image": "https://i.postimg.cc/MGzN3HVH/IMG_20260106_132624_454.jpg"},
    {"id": 35, "name": "Candy Cane", "price": "₹1359" "→" "(14.31 Usdt)", "image": "https://i.postimg.cc/W4sCYzgk/IMG_20260106_132624_419.jpg"},
    {"id": 36, "name": "Candy Cane", "price": "₹1180" "→" "(12.43 Usdt)", "image": "https://i.postimg.cc/Xvnm1qd7/IMG_20260106_132626_667.jpg"},
    {"id": 37, "name": "Candy Cane", "price": "₹794" "→" "(8.36 Usdt)", "image": "https://i.postimg.cc/43Xq2yVs/IMG_20260106_132626_135.jpg"},
    
]

PER_PAGE = 30 # 5 rows × 5 buttons

# 🔹 GRID BUILDER
def build_grid(page):
    start = page * PER_PAGE
    end = start + PER_PAGE
    items = NFTS[start:end]

    buttons = []
    row = []

    for nft in items:
        row.append(
            InlineKeyboardButton(nft["name"], callback_data=f"view_{nft['id']}")
        )
        if len(row) == 5:
            buttons.append(row)
            row = []

    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton("⬅️ Prev", callback_data=f"page_{page-1}"))
    if end < len(NFTS):
        nav.append(InlineKeyboardButton("Next ➡️", callback_data=f"page_{page+1}"))

    if nav:
        buttons.append(nav)

    return InlineKeyboardMarkup(buttons)

# 🔹 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["page"] = 0
    await update.message.reply_text(
        "🛍 *NFT SHOP*\nSelect NFT 👇",
        reply_markup=build_grid(0),
        parse_mode="Markdown"
    )

# 🔹 BUTTON HANDLER
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("page_"):
        page = int(data.split("_")[1])
        context.user_data["page"] = page
        await query.edit_message_reply_markup(reply_markup=build_grid(page))

    elif data.startswith("view_"):
        nft_id = int(data.split("_")[1])
        nft = next(n for n in NFTS if n["id"] == nft_id)
        context.user_data["nft"] = nft

        keyboard = [
            [InlineKeyboardButton("🛒 Buy NFT", callback_data="buy")],
            [InlineKeyboardButton("⬅️ Back to Shop", callback_data="back")]
        ]

        await query.message.reply_photo(
            photo=nft["image"],
            caption=f"🎁 *{nft['name']}*\n💰 Price: {nft['price']}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif data == "back":
        page = context.user_data.get("page", 0)
        await query.message.reply_text(
            "🛍 *NFT SHOP*\nSelect NFT 👇",
            reply_markup=build_grid(page),
            parse_mode="Markdown"
        )

    elif data == "buy":
        nft = context.user_data["nft"]
        await query.message.reply_text(
            f"💳 *Payment Details*\n\n"
            f"NFT: {nft['name']}\n"
            f"💸 Amount: {nft['price']}\n\n"
            f"💰 UPI ID: {UPI_ID}\n\n"
            f"🌐 *USDT ({USDT_NETWORK})*\n"
            f"{USDT_ADDRESS}\n\n"
            f"Payment ke baad screenshot bhejo ✅",
            parse_mode="Markdown"
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📢 New Buy Request\nUser: @{query.from_user.username}\nNFT: {nft['name']}"
        )

    # 🔹 APPROVE / REJECT HANDLER
    elif data.startswith("approve_"):
        user_id = int(data.split("_")[1])
        await context.bot.send_message(
            chat_id=user_id,
            text="✅ Payment approved!\nNFT aapko shortly send kar diya jayega 🎁"
        )
        await query.edit_message_caption(
            caption=query.message.caption + "\n\n✅ *APPROVED*",
            parse_mode="Markdown"
        )

    elif data.startswith("reject_"):
        user_id = int(data.split("_")[1])
        await context.bot.send_message(
            chat_id=user_id,
            text="❌ Payment rejected!\nPlease correct screenshot bhejo."
        )
        await query.edit_message_caption(
            caption=query.message.caption + "\n\n❌ *REJECTED*",
            parse_mode="Markdown"
        )

# 🔹 SCREENSHOT HANDLER
async def handle_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "nft" not in context.user_data:
        return

    nft = context.user_data["nft"]
    user = update.message.from_user

    caption = (
        f"🧾 *Payment Screenshot*\n\n"
        f"👤 User: @{user.username}\n"
        f"🆔 User ID: {user.id}\n"
        f"🎁 NFT: {nft['name']}\n"
        f"💰 Price: {nft['price']}"
    )

    keyboard = [
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user.id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user.id}")
        ]
    ]

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=update.message.photo[-1].file_id,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    await update.message.reply_text(
        "✅ Screenshot received! Admin verification ke baad NFT mil jayega."
    )

# 🔹 APP
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(MessageHandler(filters.PHOTO, handle_screenshot))
app.run_polling()


