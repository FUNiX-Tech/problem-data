Simply creating a grid element doesn't get you very far. You need to define the structure of the grid as well. To add some columns to the grid, use the `grid-template-columns` property on a grid container as demonstrated below:

```css
.container {
  display: grid;
  `grid-template-columns`: 50px 50px;
}
```

This will give your grid two columns that are each 50px wide. The number of parameters given to the `grid-template-columns` property indicates the number of columns in the grid, and the value of each parameter indicates the width of each column.

---

Give the grid container three columns that are each `100px` wide.

---

Việc tạo một phần tử grid chỉ là một khởi đầu. Bạn cần xác định cấu trúc của grid. Để thêm một số cột vào grid, hãy sử dụng thuộc tính `grid-template-columns` trên một grid container được minh họa bên dưới:

```css
.container {
  display: grid;
  grid-template-columns: 50px 50px;
}
```

Điều này sẽ cung cấp cho grid của bạn hai cột có chiều rộng mỗi cột là 50px. Số lượng tham số được cung cấp cho thuộc tính grid-template-columns cho biết số cột trong grid và giá trị của mỗi tham số cho biết chiều rộng của mỗi cột.

---

Tạo một grid container với ba cột có chiều rộng là `100px` mỗi cột.

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
