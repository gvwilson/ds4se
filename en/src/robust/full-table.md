| Header | Data Type | Description |
|---|---|---|
| `brand` | text | The full brand name. |
| `style` | text | The cut of each pair of jeans (in our analysis, we combined straight and boot-cut styles and skinny and slim styles, but these remain separated here). |
| `menWomen` | text | Whether the jeans were listed as "men's" or "women's". |
| `name` | text | The name of the specific style of measured pair of jeans as indicated by the tag. (e.g., `Fave Super Skinny Jean`). |
| `brandSize` | text | The size of jeans we measured. Each size reflects the sizing for each brand closest to a 32-inch waistband as indicated by the brand's website. |
| `waistSize` | number | The waistband size (in inches) of each measured pair as reported on the brand's website. |
| `fabric` | text | The comma-separated fabric combination as indicated by the tag on the jeans. (e.g., `78% cotton, 20% polyester, 2% spandex`). |
| `price` | number | The price (in US dollars) of each pair of jeans. This number is listed without the dollar sign ($) or any extra 0's (so $39.50 would be written as `39.5`) |
| `maxHeightFront` | number |  The height (in cm) of the front pocket from the top of the highest rivet to the lowest point of the pocket (along the left-hand side or zipper side).|
| `minHeightFront` | number | The height (in cm) of the  front pocket from the top of the highest rivet to the lowest point of the pocket (along the right-hand side or non-zipper side).|
| `rivetHeightFront` | number| The distance (in cm) between the top of the highest rivet to the lowest rivet. |
| `maxWidthFront` | number | The width (in cm) from the widest point of the front pocket. |
| `minWidthFront` | number| The width (in cm) from the highest rivet to the right or non-zipper side of the pocket. |
| `maxHeightBack` | number | The height (in cm) from the deepest point of the back pocket (usually in the pocket's center) to the top of the pocket.|
| `minHeightBack` | number | The height (in cm) from the shallowest point of the back pocket to the top of the pocket. |
| `maxWidthBack` | number | The width of the pocket at the very top (the opening)|
| `minWidthBack` | number | The width of the pocket at its narrowest (just before the pocket tapers to a point).|
