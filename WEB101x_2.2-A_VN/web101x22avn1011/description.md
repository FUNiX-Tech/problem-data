Sometimes you want all the items in your CSS Grid to share the same alignment. You can use the previously learned properties and align them individually, or you can align them all at once horizontally by using `justify-items` on your grid container. This property can accept all the same values you learned about in the previous two challenges, the difference being that it will move all the items in our grid to the desired alignment.

---

Use this property to center all our items horizontally.

---

Đôi lúc bạn sẽ muốn tất cả các item trong CSS Grid có căn chỉnh giống nhau. Bạn có thể sử dụng các thuộc tính đã học trước đó và căn chỉnh từng item hoặc căn chỉnh tất cả item cùng một lúc theo chiều ngang bằng `justify-items` trên grid container. Thuộc tính này nhận các giá trị tương tự mà bạn đã thấy ở 2 lab trước, chỉ khác ở chỗ là nó sẽ di chuyển tất cả các item ở grid tới các căn chỉnh mong muốn.

---

Sử dụng thuộc tính này để căn giữa tất cả các item theo chiều ngang.

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
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
    /* Only change code below this line */

    /* Only change code above this line */
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
