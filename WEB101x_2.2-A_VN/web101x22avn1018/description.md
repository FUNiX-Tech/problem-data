The repeat function comes with an option called _auto-fill_. This allows you to automatically insert as many rows or columns of your desired size as possible depending on the size of the container. You can create flexible layouts when combining `auto-fill` with `minmax`, like this:

```css
repeat(auto-fill, minmax(60px, 1fr));
```

When the container changes size, this setup keeps inserting 60px columns and stretching them until it can insert another one. **Note:** If your container can't fit all your items on one row, it will move them down to a new one.

---

In the first grid, use `auto-fill` with `repeat` to fill the grid with columns that have a minimum width of `60px` and maximum of `1fr`. Then resize the preview to see auto-fill in action.

---

Hàm repeat đi kèm với một tùy chọn là _auto-fill_. Điều này cho phép bạn tự động chèn nhiều hàng hoặc cột nhất có thể với kích thước mong muốn tùy thuộc vào kích thước của container. Bạn có thể tạo bố cục linh hoạt khi kết hợp `auto-fill` với `minmax`, như sau:

```css
repeat(auto-fill, minmax(60px, 1fr));
```

Khi container thay đổi kích thước, thiết lập này tiếp tục chèn các cột 60px và kéo dài cho đến khi nó chèn một cột khác. **Lưu ý:** Nếu container của bạn không thể chứa tất cả các item trong một hàng, nó sẽ chuyển chúng xuống một hàng mới.

---

Ở grid đầu tiên, hãy dùng `auto-fill` với `repeat` để điền grid với các cột có chiều rộng tối thiểu là `60px` và tối đa là `1fr`. Sau đó, hãy điều chỉnh kích thước preview để xem auto-fill hoạt động thế nào.

```html
<style>
  .item1 {
    background: LightSkyBlue;
  }
  .item2 {
    background: LightSalmon;
  }
  .item3 {
    background: PaleTurquoise;
  }
  .item4 {
    background: LightPink;
  }
  .item5 {
    background: PaleGreen;
  }

  .container {
    font-size: 40px;
    min-height: 100px;
    width: 100%;
    background: LightGray;
    display: grid;
    /* Only change code below this line */

    grid-template-columns: repeat(3, minmax(60px, 1fr));

    /* Only change code above this line */
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
  }

  .container2 {
    font-size: 40px;
    min-height: 100px;
    width: 100%;
    background: Silver;
    display: grid;
    grid-template-columns: repeat(3, minmax(60px, 1fr));
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
  }
</style>
<div class="container">
  <div class="item1">1</div>
  <div class="item2">2</div>
  <div class="item3">3</div>
  <div class="item4">4</div>
  <div class="item5">5</div>
</div>
<div class="container2">
  <div class="item1">1</div>
  <div class="item2">2</div>
  <div class="item3">3</div>
  <div class="item4">4</div>
  <div class="item5">5</div>
</div>
```
