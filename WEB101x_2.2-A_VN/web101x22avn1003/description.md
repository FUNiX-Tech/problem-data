The grid you created in the last challenge will set the number of rows automatically. To adjust the rows manually, use the `grid-template-rows` property in the same way you used `grid-template-columns` in the previous challenge.

---

Add two rows to the grid that are `50px` tall each.

---

Grid bạn đã tạo trong thử thách trước sẽ tự động đặt số hàng. Để điều chỉnh các hàng theo cách thủ công, hãy sử dụng thuộc tính `grid-template-rows` giống như cách bạn đã sử dụng `grid-template-columns` trong thử thách trước đó.

---

Thêm hai hàng vào grid có chiều cao là `50px` mỗi hàng.

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
    width: 100%;
    background: LightGray;
    display: grid;
    grid-template-columns: 100px 100px 100px;
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
