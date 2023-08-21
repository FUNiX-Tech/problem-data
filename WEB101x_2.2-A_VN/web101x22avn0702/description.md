The CSS offsets of `top` or `bottom`, and `left` or `right` tell the browser how far to offset an item relative to where it would sit in the normal flow of the document. You're offsetting an element away from a given spot, which moves the element away from the referenced side (effectively, the opposite direction). As you saw in the last challenge, using the `top` offset moved the `h2` downwards. Likewise, using a `left` offset moves an item to the right.

Use CSS offsets to move the `h2` 15 pixels to the right and 10 pixels up.

---

CSS offset bao gồm `top`, `bottom`, `left` hoặc `right` cho trình duyệt biết khoảng cách bù đắp của một phần tử so với vị trí của nó trong normal flow của tài liệu. Bạn đang di chuyển một phần tử ra khỏi một vị trí nhất định, điều này sẽ di chuyển phần tử ra khỏi phía được tham chiếu (theo hướng ngược lại). Như bạn đã thấy trong thử thách trước, việc sử dụng phần `top` đã di chuyển phần `h2` đi xuống. Tương tự như vậy, sử dụng `left` sẽ di chuyển một mục sang bên phải.

---

Sử dụng CSS offset để di chuyển `h2` 15 pixel sang phải và 10 pixel lên trên.

```html
<head>
  <style>
    h2 {
      position: relative;
    }
  </style>
</head>
<body>
  <h1>On Being Well-Positioned</h1>
  <h2>Move me!</h2>
  <p>I still think the h2 is where it normally sits.</p>
</body>
```
