The last two challenges used the `flex-direction` property set to `row`. This property can also create a column by vertically stacking the children of a flex container.

---

Add the CSS property `flex-direction` to the `#box-container` element, and give it a value of `column`.

---

Hai thử thách trước sử dụng thuộc tính `flex-direction` được đặt thành `row`. Thuộc tính này cũng có thể tạo cột bằng cách xếp chồng các phần tử con của một flex container theo chiều dọc.

---

Thêm thuộc tính CSS `flex-direction` vào phần tử `#box-container` và đặt cho nó một giá trị là `column`.

```html
<style>
  #box-container {
    display: flex;
    height: 500px;
  }
  #box-1 {
    background-color: dodgerblue;
    width: 50%;
    height: 50%;
  }

  #box-2 {
    background-color: orangered;
    width: 50%;
    height: 50%;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
</div>
```
