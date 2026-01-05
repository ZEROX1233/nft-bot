from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

BOT_TOKEN = "8390566895:AAEgoyjb1f9gTNxIscH_KxI8BZ0xsDTFCPI"
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
    {"id": 11, "name": "Evil Eye", "price": "₹1349" "→" "(14.2 Usdt)", "image": "https://i.postimg.cc/rmjjmK2v/IMG-20260105-164413-822.jpg"},
]

PER_PAGE = 15  # 2 rows × 5 buttons

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