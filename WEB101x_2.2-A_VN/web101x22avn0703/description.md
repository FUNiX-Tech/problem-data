The next option for the CSS `position` property is `absolute`, which locks the element in place `relative` to its parent container. Unlike the relative position, this removes the element from the normal flow of the document, so surrounding items ignore it. The CSS offset properties (top or bottom and left or right) are used to adjust the position.

One nuance with absolute positioning is that it will be locked relative to its closest positioned ancestor. If you forget to add a position rule to the parent item, (this is typically done using `position: relative;`), the browser will keep looking up the chain and ultimately default to the `body` tag.

---

Lock the `#searchbar` element to the top-right of its `section` parent by declaring its `position` as `absolute`. Give it `top` and `right` offsets of 50 pixels each.

---

Tùy chọn tiếp theo cho thuộc tính CSS `position` là `absolute`, cố định phần tử liên quan đến vùng chứa mẹ của nó. Không giống như vị trí `relative`, điều này loại bỏ phần tử khỏi normal flow của tài liệu, vì vậy các phần tử xung quanh sẽ bỏ qua nó. Các thuộc tính CSS offset (top, bottom, left hoặc right) được sử dụng để điều chỉnh vị trí.

Khi định vị tuyệt đối, phần tử sẽ được cố định so với phần tử ancestor có vị trí gần nhất . Nếu bạn quên thêm quy tắc position vào phần tử mẹ, (điều này thường được thực hiện bằng cách sử dụng `position: relative;`), trình duyệt sẽ tiếp tục tìm kiếm và mặc định thẻ `body` là phần tử mẹ.

---

Cố định phần tử `#searchbar` nằm góc trên bên phải của phần tử `section` bằng cách khai báo thuộc tính `position` là `absolute`. Chỉ định `top` và `right` là 50 pixel .

```html
<style>
  #searchbar {
  }
  section {
    position: relative;
  }
</style>
<body>
  <h1>Welcome!</h1>
  <section>
    <form id="searchbar">
      <label for="search">Search:</label>
      <input type="search" id="search" name="search" />
      <input type="submit" name="submit" value="Go!" />
    </form>
  </section>
</body>
```
