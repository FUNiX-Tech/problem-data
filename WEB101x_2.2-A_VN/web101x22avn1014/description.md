The `grid-area` property you learned in the last challenge can be used in another way. If your grid doesn't have an areas template to reference, you can create an area on the fly for an item to be placed like this:

```css
item1 {
  grid-area: 1/1/2/4;
}
```

This is using the line numbers you learned about earlier to define where the area for this item will be. The numbers in the example above represent these values:

```css
grid-area: horizontal line to start at / vertical line to start at / horizontal
  line to end at / vertical line to end at;
```

So the item in the example will consume the rows between lines 1 and 2, and the columns between lines 1 and 4.

---

Using the `grid-area` property, place the element with `item5` class between the third and fourth horizontal lines and between the first and fourth vertical lines.

---

Thuộc tính `grid-area` mà bạn đã thấy có thể dùng theo một cách khác. Nếu grid của bạn không có area template để tham chiếu, bạn có thể tạo nhanh một area để đặt item như sau:

```css
item1 {
  grid-area: 1/1/2/4;
}
```

Điều này sử dụng số dòng mà bạn đã thấy trước đó để xác định vị trí của area cho item này. Các số trong ví dụ trên biểu diễn các giá trị:

```css
grid-area: horizontal line to start at / vertical line to start at / horizontal
  line to end at / vertical line to end at;
```

Vậy item trong ví dụ sẽ sử dụng các cột giữa dòng 1 và hàng 2, các cột giữa dòng 1 và dòng 4

---

Hãy dùng thuộc tính `grid-area` để đặt phần tử có class `item5` giữa hàng ngang số 3 và 4, giữa hàng dọc số 1 và số 4.

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
