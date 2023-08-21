The next layout scheme that CSS offers is the `fixed` position, which is a type of absolute positioning that locks an element relative to the browser window. Similar to absolute positioning, it's used with the CSS offset properties and also removes the element from the normal flow of the document. Other items no longer "realize" where it is positioned, which may require some layout adjustments elsewhere.

One key difference between the `fixed` and `absolute` positions is that an element with a fixed position won't move when the user scrolls.

---

The navigation bar in the code is labeled with an id of `navbar`. Change its `position` to `fixed`, and offset it 0 pixels from the `top` and 0 pixels from the `left`. After you have added the code, scroll the preview window to see how the navigation stays in place.

---

Sơ đồ bố cục tiếp theo mà CSS cung cấp là vị trí `fixed`, là một kiểu định vị tuyệt đối với một phần tử liên quan đến cửa sổ trình duyệt. Tương tự như absolute positiioning, nó được sử dụng với các thuộc tính CSS offset và cũng loại bỏ phần tử khỏi normal flow của tài liệu. Khi các phần tử khác không còn "nhận ra" vị trí của nó, điều này có thể yêu cầu một số điều chỉnh bố cục.

Một điểm khác biệt giữa các vị trí `fixed` và `absolute` là một phần tử có vị trí fixed sẽ không di chuyển khi người dùng cuộn trang.

---

Thanh điều hướng trong code được gắn nhãn với một id là `navbar`. Thay đổi giá trị của thuộc tính `position` thành `fixed` và chỉ định khoảng cách là 0 pixel từ `top` và 0 pixel từ `left`. Sau khi bạn đã thêm code, hãy cuộn cửa sổ xem trước để xem thử thanh điều hướng ở vị trí như thế nào.

```html
<style>
  body {
    min-height: 150vh;
  }
  #navbar {
    width: 100%;
    background-color: #767676;
  }
  nav ul {
    margin: 0px;
    padding: 5px 0px 5px 30px;
  }
  nav li {
    display: inline;
    margin-right: 20px;
  }
  a {
    text-decoration: none;
  }
</style>
<body>
  <header>
    <h1>Welcome!</h1>
    <nav id="navbar">
      <ul>
        <li><a href="">Home</a></li>
        <li><a href="">Contact</a></li>
      </ul>
    </nav>
  </header>
  <p>I shift up when the #navbar is fixed to the browser window.</p>
</body>
```
