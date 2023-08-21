Just as you can align an item horizontally, there's a way to align an item vertically as well. To do this, you use the `align-self` property on an item. This property accepts all of the same values as `justify-self` from the last challenge.

---

Align the item with the class `item3` vertically at the `end`.

---

Nếu đã có thể căn chỉnh item theo chiều ngang thì tất nhiên cũng có thể căn chỉnh theo chiều dọc. Để thực hiện điều này, chúng ta sẽ dùng thuộc tính `align-self`. Thuộc tính này nhận tất cả các giá trị tương tự như `justify-self` từ lab trước.

---

Căn chỉnh item với class `item3` theo chiều dọc ở `end`.

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
    /* Only change code below this line */

    /* Only change code above this line */
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
