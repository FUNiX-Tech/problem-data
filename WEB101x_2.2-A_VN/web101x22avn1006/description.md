There's another built-in function to use with `grid-template-columns` and `grid-template-rows` called `minmax`. It's used to limit the size of items when the grid container changes size. To do this you need to specify the acceptable size range for your item. Here is an example:

```css
grid-template-columns: 100px minmax(50px, 200px);
```

In the code above, `grid-template-columns` is set to create two columns; the first is 100px wide, and the second has the minimum width of 50px and the maximum width of 200px.

---

Using the `minmax` function, replace the `1fr` in the `repeat` function with a column size that has the minimum width of `90px` and the maximum width of `1fr`, and resize the preview panel to see the effect.

---

Có một hàm tích hợp khác để sử dụng `grid-template-columns` và `grid-template-rows` được gọi `minmax`. Nó được sử dụng để giới hạn kích thước của các item khi grid container thay đổi kích thước. Để làm điều này, bạn cần chỉ định phạm vi kích thước chấp nhận được cho item của bạn. Đây là một ví dụ:

```css
grid-template-columns: 100px minmax(50px, 200px);
```

Trong đoạn code trên, `grid-template-columns` được thiết lập để tạo hai cột; cột đầu tiên có chiều rộng 100px và cột thứ hai có chiều rộng tối thiểu là 50px và chiều rộng tối đa là 200px.

---

Sử dụng hàm `minmax`, thay thế kích thước `1fr` trong hàm `repeat` bằng kích thước cột có chiều rộng tối thiểu `90px` và chiều rộng tối đa `1fr`, và thay đổi kích thước preview panel để xem hiệu ứng.

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
    min-height: 300px;
    width: 100%;
    background: LightGray;
    display: grid;
    /* Only change code below this line */

    grid-template-columns: repeat(3, 1fr);

    /* Only change code above this line */
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
```
