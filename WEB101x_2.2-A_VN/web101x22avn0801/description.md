The next positioning tool does not actually use `position`, but sets the `float` property of an element. Floating elements are removed from the normal flow of a document and pushed to either the `left` or `right` of their containing parent element. It's commonly used with the `width` property to specify how much horizontal space the floated element requires.

---

The given markup would work well as a two-column layout, with the `section` and `aside` elements next to each other. Give the `#left` item a `float` of `left` and the `#right` item a `float` of `right`.

---

Công cụ định vị tiếp theo không thực sự sử dụng `position` mà là thuộc tính `float` của một phần tử. Các phần tử float bị xóa khỏi normal flow của tài liệu và được đẩy sang `left` hoặc `right` của phần tử chứa chúng. Nó thường được sử dụng với thuộc tính `width` để chỉ định lượng không gian ngang mà phần tử float yêu cầu.

---

Nó sẽ hoạt động tốt với một bố cục hai cột, chẳng hạn như các phần tử `section` và `aside` bên cạnh nhau. Chỉ định `float:left;` cho phần tử `#left` và `float:right;` cho phần tử `#right`.

```html
<head>
  <style>
    #left {
      width: 50%;
    }
    #right {
      width: 40%;
    }
    aside,
    section {
      padding: 2px;
      background-color: #ccc;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome!</h1>
  </header>
  <section id="left">
    <h2>Content</h2>
    <p>Good stuff</p>
  </section>
  <aside id="right">
    <h2>Sidebar</h2>
    <p>Links</p>
  </aside>
</body>
```
