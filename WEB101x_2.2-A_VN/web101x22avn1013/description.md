After creating an area template for your grid container, as shown in the previous challenge, you can place an item in your custom area by referencing the name you gave it. To do this, you use the `grid-area` property on an item like this:

```css
.item1 {
  grid-area: header;
}
```

This lets the grid know that you want the `item1` class to go in the area named `header`. In this case, the item will use the entire top row because that whole row is named as the `header` area.

---

Place an element with the `item5` class in the `footer` area using the `grid-area` property.

---

Sau khi tạo một template area cho grid container, bạn có thể đặt item vào custom area bằng cách tham chiếu tên mà bạn đặt cho nó. Để làm điều này, hãy sử dụng thuộc tính `grid-area` trên item như sau:

```css
.item1 {
  grid-area: header;
}
```

Điều này sẽ cho grid biết là bạn muốn class `item1` sẽ tới area có tên là `header`. Trong trường hợp này, item sẽ sử dụng toàn bộ hàng trên cùng vì toàn bộ hàng đó được đặt tên theo `header` area.

---

Hãy đặt một phần tử với class `item5` trong `footer` area sử dụng thuộc tính `grid-area`.

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
    grid-template-areas:
      "header header header"
      "advert content content"
      "footer footer footer";
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
