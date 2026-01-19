<html><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neon NFT</title>
  <link rel="stylesheet" href="style.css">
<script id="anydoc-subtitle-inject" src="chrome-extension://pajdgpfjcgcdfkccnbinpalbihedpkfm/public/subtitle/script/inject.js"></script></head>
<body>

<header>
  <div class="logo">NFT ZONE</div>

  <div class="top-buttons">
    <!-- LEFT SIDE PROFILE -->
    <a href="profile.html">Profile</a>

    <!-- RIGHT SIDE WALLET -->
    <a href="wallet.html">Wallet</a>

    <!-- TELEGRAM CHANNEL LINK -->
    <a href="https://t.me/YOUR_CHANNEL" target="_blank">TG@</a>
  </div>
</header>

<div class="grid" id="nftGrid">
  <!-- NFT cards yahan auto load honge -->
<div class="card">
        <img src="https://i.getgems.io/x62IomC4AeL9wwLBhSShdnzDmbS-xcN4tYPRAtTH9fg/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUE3MlVldnJfTUh2ell3U0NISlVLLXVDNmtkLXc4a2J4emhKNDlXSWlHLW82Q0QvNzAxYjJhOTNjODY5NDM2ZQ">
        <h3>Snoop Cigar</h3>
        <div class="price">2.5 TON</div>
      </div><div class="card">
        <img src="https://i.getgems.io/PAdh7nUGX1IQ11M3LkmBWTgyixGkCOMUzjlyfoVSh6M/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUNaNC1oNjVpVGlXRFBSUGNMbFM2M2diY1M0MFlCYWRFRkxBNFctaUlXVVpsZDAvNTFmNzE5YTQ5NWM2NDUwZA">
        <h3>spring basket</h3>
        <div class="price">11 TON</div>
      </div><div class="card">
        <img src="https://i.getgems.io/AEai7oeIAQRDXn0KHU_Ej2KFYrCTOQJ4YtBDMERuc68/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUJJMDdQWGV3OTRZUXo3R3dONzJuUE5HRjZodFNUT0prdVU0S3hfYmpUWnYzMlUvNmFkODVjODZhYWIzNmQxOA">
        <h3>Swiss watch</h3>
        <div class="price">15000 TON</div>
      </div><div class="card">
        <img src="https://i.getgems.io/YUyEYL8GTt_cEkpoN8eeWP4mKecEN52gZjiUpaWRM6M/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUJJajB1Ri1xSUFTcXY2cUl2Y1RpZjJ3S1NkdDRXUWM0bWNvQnl3TnA1R250dUcvZjg3MDE0ZTEwNTQ2ODllMA">
        <h3>instant Ramen </h3>
        <div class="price">4 TON</div>
      </div><div class="card">
        <img src="https://i.getgems.io/VA9GSxoDDkXHAyuBBmDu0fFlJCLYbMFR_uVq2jGArVI/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUR4LVNxUUVoUDlSemZpMmNxZGVoVFZVdlFiQXJzVXoxWDd0LXVsOElpS1pwWWIvZjdmY2U2NWFiN2VkMzc5Ng">
        <h3>Big Year</h3>
        <div class="price">5 TON</div>
      </div><div class="card">
        <img src="https://i.getgems.io/gQliKhRqMp2WZcYt4QR8fJD5a19Uo2ed06ONsaiww8c/rs:fill:500:500:1/g:ce/czM6Ly9nZXRnZW1zLXMzL25mdC1jb250ZW50LWNhY2hlL2ltYWdlcy9FUUEwRXpSWVg1d21fcTQ2X05YOGI3RVlodE9rWGZYZ3NyMDZFVGJvdjFhN1N0WmwvN2RkYWI4YTBjOGRiMGE5NA">
        <h3>Preety Posy</h3>
        <div class="price">29 TON</div>
      </div></div>

<script>
/*
=============================
JSON SETUP
=============================

1. Ek file banao: nfts.json
2. JSON structure:
[
  {
    "NFT_NAME": "Birthday Candle",
    "IMAGE_URL": "https://example.com/candle.png",
    "PRICE_TON": "1.2",
    "NFT_LINK": "http://t.me/nft/BDayCandle-32276"
  },
  {
    "NFT_NAME": "Gift Box",
    "IMAGE_URL": "https://example.com/gift.png",
    "PRICE_TON": "0.5",
    "NFT_LINK": "https://getgems.io/..."
  }
]
3. index.html aur nfts.json same folder me rakho
*/

fetch('nfts.json')
  .then(res => res.json())
  .then(data => {
    const grid = document.getElementById("nftGrid");

    data.forEach(nft => {
      const card = document.createElement("div");
      card.className = "card";
      card.onclick = () => window.open(nft.link, "_blank");

      card.innerHTML = `
        <img src="${nft.image}">
        <h3>${nft.name}</h3>
        <div class="price">${nft.price}</div>
      `;

      grid.appendChild(card);
    });
  })
  .catch(err => console.error("Error loading NFTs JSON:", err));
  </script>
  
  
  </body><wps-translate-entry></wps-translate-entry></html>
