`grid-gap` is a shorthand property for `grid-row-gap` and `grid-column-gap` from the previous two challenges that's more convenient to use. If `grid-gap` has one value, it will create a gap between all rows and columns. However, if there are two values, it will use the first one to set the gap between the rows and the second value for the columns.

---

Use `grid-gap` to introduce a `10px` gap between the rows and `20px` gap between the columns.

---

`grid-gap` là thuộc tính viết tắt của `grid-row-gap` và `grid-column-gap` từ các lab trước, như vậy sẽ tiện sử dụng hơn. Nếu `grid-gap` có một giá trị, nó sẽ tạo khoảng cách giữa tất cả các hàng và cột. Tuy nhiên, nếu có hai giá trị, nó sẽ sử dụng giá trị đầu tiên để thiết lập khoảng cách giữa các hàng và giá trị thứ hai để thiết lập khoảng cách giữa các cột.

---

Hãy dùng `grid-gap` để thêm khoảng cách `10px` giữa các hàng và khoảng cách `20px` giữa các cột.

```html
<style>
  .d1 {
    background: LightSkyBlue;
  }
  .d2 {
    background: LightSalmon;
  }
  .d3 {
    background: PaleTurquoise;
  }
  .d4 {
    background: LightPink;
  }
  .d5 {
    background: PaleGreen;
  }

  .container {
    font-size: 40px;
    min-height: 300px;
    width: 100%;
    background: LightGray;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    /* Only change code below this line */

    /* Only change code above this line */
  }
</style>
<div class="container">
  <div class="d1">1</div>
  <div class="d2">2</div>
  <div class="d3">3</div>
  <div class="d4">4</div>
  <div class="d5">5</div>
</div>
```
