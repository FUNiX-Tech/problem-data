Adding `display: flex` to an element turns it into a flex container. This makes it possible to align any children of that element into rows or columns. You do this by adding the `flex-direction` property to the parent item and setting it to row or column. Creating a row will align the children horizontally, and creating a column will align the children vertically.

Other options for `flex-direction` are `row-reverse` and `column-reverse`.

**Note:** The default value for the `flex-direction` property is `row`.

---

Add the CSS property `flex-direction` to the `#box-container` element, and give it a value of `row-reverse`.

---

Việc thêm `display: flex` vào một phần tử, biến nó thành một flex container. Điều này giúp bạn có thể căn chỉnh bất kỳ phần tử con nào của phần tử đó thành các hàng hoặc cột. Bạn thực hiện việc này bằng cách thêm thuộc tính `flex-direction` vào phần tử mẹ và đặt nó thành hàng hoặc cột. Tạo một hàng sẽ căn chỉnh các phần tử con theo chiều ngang, và tạo một cột sẽ căn các phần tử con theo chiều dọc.

Các tùy chọn khác cho `flex-direction`là `row-reverse` và `column-reverse`.

**Lưu ý:** Giá trị mặc định cho thuộc tính `flex-direction` là `row`.

---

Thêm thuộc tính CSS `flex-direction` vào phần tử `#box-container` và đặt cho nó một giá trị là `row-reverse`.

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
