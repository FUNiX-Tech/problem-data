Up to this point, all the properties that have been discussed are for grid containers. The `grid-column` property is the first one for use on the grid items themselves.

The hypothetical horizontal and vertical lines that create the grid are referred to as lines. These lines are numbered starting with 1 at the top left corner of the grid and move right for columns and down for rows, counting upward.

This is what the lines look like for a 3x3 grid:

![Grid 3x3](https://www.w3schools.com/css/grid_lines.png)

To control the number of columns an item will consume, you can use the `grid-column` property in conjunction with the line numbers you want the item to start and stop at.

Here's an example:

```css
grid-column: 1 / 3;
```

This will make the item start at the first vertical line of the grid on the left and span to the 3rd line of the grid, consuming two columns.

---

Make the item with the class `item5` consume the last two columns of the grid.

---

Cho đến thời điểm này, tất cả các thuộc tính đã được thảo luận đều dành cho các grid container. Thuộc tính `grid-column` là thuộc tính đầu tiên được sử dụng trên chính các grid item.

Các đường ngang và dọc giả định tạo ra lưới được gọi là các line . Các line này được đánh số bắt đầu bằng 1 ở góc trên cùng bên trái của grid và di chuyển sang phải đối với các cột và xuống đối với các hàng.

Đây là một minh họa về các line của một grid 3x3:

![Grid 3x3](https://www.w3schools.com/css/grid_lines.png)

Để chỉ định số cột mà một item sẽ sử dụng, bạn có thể sử dụng thuộc tính `grid-column` kết hợp với số line mà bạn muốn item đó bắt đầu và dừng lại.

Đây là một ví dụ:

```css
grid-column: 1 / 3;
```

Điều này nghĩa là item sẽ bắt đầu ở line đầu tiên của grid từ bên trái và kéo dài đến line thứ 3 của lưới, tổng là hai cột.

---

Chỉ định item có lớp `item5` sẽ sử dụng hai cột cuối cùng của lưới.

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
    /* Only change code below this line */

    /* Only change code above this line */
  }

  .container {
    font-size: 40px;
    min-height: 300px;
    width: 100%;
    background: LightGray;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
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
