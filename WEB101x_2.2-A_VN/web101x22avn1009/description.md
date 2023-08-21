In CSS Grid, the content of each item is located in a box which is referred to as a cell. You can align the content's position within its cell horizontally using the `justify-self` property on a grid item. By default, this property has a value of `stretch`, which will make the content fill the whole width of the cell. This CSS Grid property accepts other values as well:

`start`: aligns the content at the left of the cell,

`center`: aligns the content in the center of the cell,

`end`: aligns the content at the right of the cell.

---

Use the `justify-self` property to center the item with the class `item2`.

---

Trong CSS Grid, nội dung của từng item được đặt ở trong một box, coi như một cell. Bạn có thể căn chỉnh vị trí của từng nội dung theo chiều ngang trong cell bằng thuộc tính `justify-self` trên một grid item. Theo mặc định, thuộc tính này có giá trị `stretch`, khiến nội dung sẽ lấp đầy toàn bộ chiều rộng của cell. Thuộc tính CSS Grid này cũng chấp nhận các giá trị khác:

`start`:căn chỉnh nội dung ở phía bên trái cell,

`center`: căn chỉnh nội dung ở giữa cell,

`end`: căn chỉnh nội dung ở phía bên phải cell.

---

Sử dụng thuộc tính `justify-self` để căn giữa item với class `item2`.

```html
<style>
  .item1 {
    background: LightSkyBlue;
  }

  .item2 {
    background: LightSalmon;
    /* Only change code below this line */

    /* Only change code above this line */
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
