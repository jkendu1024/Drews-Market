# Drew's Market – static website

Clean rebuild of drewsmarket.com, replacing the compromised WordPress site.
Content was recovered from the **Jan 14, 2026 Wayback Machine snapshot**, which predates
the first spam post (Mar 30, 2026). Nothing came from the hacked server.

No WordPress, PHP, database or plugins, so there's nothing to exploit. It's plain HTML and CSS.

## Layout
- `build.py`: one file holds all page content, the shared header and footer, hours and contact info
- `style.css`: the styles
- `site/`: the built output that gets deployed
- `site/images/`: the 10 original photos that were archived. Other photos were never saved, so ask the owner for new ones.

## Build
```bash
# site/images/ already holds web-sized copies of the 10 archived photos (fetch-images.sh re-downloads the originals)
python3 build.py          # writes site/
```
To change hours, phone numbers, menus or prices, edit `build.py` and rebuild.

## Deploy (pick one, all free)
- **Cloudflare Pages** or **Netlify**: connect this repo with build command `python3 build.py` and output directory `site`
- **GitHub Pages**: publish `site/` with an Actions workflow

Then point drewsmarket.com DNS at the new host. **Move email first** if it currently runs through the old web host.

## Before launch: owner to confirm
- [ ] Hours. The archive says Mon–Sat 10–6 and Sun 10–4, but the hacked site later listed Sat 9–6 and Sun 9–4.
- [ ] Contact email: drewsmarketspringlake@gmail.com. The old About page also listed drewsitalianmarket@gmail.com.
- [ ] Current prices for the deli sandwiches and catering platters
- [ ] Menu PDFs (catering, sandwich & salad, holiday, cooking instructions). Add them to `site/menus/` and link them from menus.html.
- [ ] Wording of the FAQ, privacy and terms pages
- [ ] Online ordering: dropped for now ("Call to order"). If needed, add a hosted Square or Stripe link.
