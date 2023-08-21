Turn any HTML element into a grid container by setting its `display` property to `grid`. This gives you the ability to use all the other properties associated with CSS Grid.

**Note:** In CSS Grid, the parent element is referred to as the container and its children are called items.

---

Change the display of the div with the `container` class to `grid`.

---

Chuyển bất kỳ phần tử HTML nào thành grid container bằng cách đặt thuộc tính `display` thành `grid`. Điều này cung cấp cho bạn khả năng sử dụng tất cả các thuộc tính khác được liên kết với CSS Grid.

**Lưu ý:** Trong CSS Grid, phần tử mẹ được gọi là container và phần tử con của nó được gọi là item.

---

Thay đổi display của div với class `container` thành `grid`.

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
