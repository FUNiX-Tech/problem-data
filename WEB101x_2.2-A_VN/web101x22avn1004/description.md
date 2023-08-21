You can use absolute and relative units like `px` and `em` in CSS Grid to define the size of rows and columns. You can use these as well:

`fr`: sets the column or row to a fraction of the available space,

`auto`: sets the column or row to the width or height of its content automatically,

`%`: adjusts the column or row to the percent width of its container.

Here's the code that generates the output in the preview:

```css
grid-template-columns: auto 50px 10% 2fr 1fr;
```

This snippet creates five columns. The first column is as wide as its content, the second column is 50px, the third column is 10% of its container, and for the last two columns; the remaining space is divided into three sections, two are allocated for the fourth column, and one for the fifth.

---

Make a grid with three columns whose widths are as follows: 1fr, 100px, and 2fr.

---

Bạn có thể sử dụng các đơn vị tuyệt đối và tương đối như `px` và `em` trong CSS Grid để xác định kích thước của hàng và cột. Bạn cũng có thể sử dụng những đơn vị này:

`fr`: đặt cột hoặc hàng thành một phần nhỏ của không gian có sẵn

`auto`: đặt cột hoặc hàng thành chiều rộng hoặc chiều cao tự động theo nội dung

`%`: điều chỉnh cột hoặc hàng theo phần trăm chiều rộng của container

Dưới đây là một ví dụ cụ thể

```css
grid-template-columns: auto 50px 10% 2fr 1fr;
```

Đoạn code này tạo ra năm cột. Cột đầu tiên rộng bằng nội dung của nó, cột thứ hai là 50px, cột thứ ba là 10% vùng chứa của nó và đối với hai cột cuối cùng; không gian còn lại được chia thành ba phần, hai phần được phân bổ cho cột thứ tư và một phần cho cột thứ năm.

---

Tạo lưới có ba cột có chiều rộng như sau: 1fr, 100px và 2fr.

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

    grid-template-columns: auto 50px 10% 2fr 1fr;

    /* Only change code above this line */
    grid-template-rows: 50px 50px;
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
