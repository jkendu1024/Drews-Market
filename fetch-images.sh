#!/usr/bin/env bash
# Optional: re-download full-resolution originals from the clean Jan 14, 2026 Wayback snapshot.
# site/images/ already contains web-sized copies of these.
set -euo pipefail
mkdir -p site/images
curl -fsSL -o "site/images/logo-new.png" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2024/05/logo-new.png" && echo "ok  2024/05/logo-new.png" || echo "MISS 2024/05/logo-new.png"
curl -fsSL -o "site/images/image-34.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2021/05/image-34.jpg" && echo "ok  2021/05/image-34.jpg" || echo "MISS 2021/05/image-34.jpg"
curl -fsSL -o "site/images/grilled-reuben-sandwich.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2024/04/grilled-reuben-sandwich.jpg" && echo "ok  2024/04/grilled-reuben-sandwich.jpg" || echo "MISS 2024/04/grilled-reuben-sandwich.jpg"
curl -fsSL -o "site/images/parallax-29.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2021/06/parallax-29.jpg" && echo "ok  2021/06/parallax-29.jpg" || echo "MISS 2021/06/parallax-29.jpg"
curl -fsSL -o "site/images/product-1.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2021/07/product-1.jpg" && echo "ok  2021/07/product-1.jpg" || echo "MISS 2021/07/product-1.jpg"
curl -fsSL -o "site/images/product-2.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2021/07/product-2.jpg" && echo "ok  2021/07/product-2.jpg" || echo "MISS 2021/07/product-2.jpg"
curl -fsSL -o "site/images/product-4.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2021/07/product-4.jpg" && echo "ok  2021/07/product-4.jpg" || echo "MISS 2021/07/product-4.jpg"
curl -fsSL -o "site/images/Boars-Head-Roast-Beef.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2024/04/Boars-Head-Roast-Beef.jpg" && echo "ok  2024/04/Boars-Head-Roast-Beef.jpg" || echo "MISS 2024/04/Boars-Head-Roast-Beef.jpg"
curl -fsSL -o "site/images/Hot-Hero-Chicken-Parmigiana-300x300.jpeg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2024/04/Hot-Hero-Chicken-Parmigiana-300x300.jpeg" && echo "ok  2024/04/Hot-Hero-Chicken-Parmigiana-300x300.jpeg" || echo "MISS 2024/04/Hot-Hero-Chicken-Parmigiana-300x300.jpeg"
curl -fsSL -o "site/images/sea-girt-300x300.jpg" "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/2024/04/sea-girt-300x300.jpg" && echo "ok  2024/04/sea-girt-300x300.jpg" || echo "MISS 2024/04/sea-girt-300x300.jpg"
