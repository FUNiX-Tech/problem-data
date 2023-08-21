Did you know there are other ways to represent colors in CSS? One of these ways is called hexadecimal code, or hex code for short.

We usually use decimals, or base 10 numbers, which use the symbols 0 to 9 for each digit. Hexadecimals (or hex) are base 16 numbers. This means it uses sixteen distinct symbols. Like decimals, the symbols 0-9 represent the values zero to nine. Then A,B,C,D,E,F represent the values ten to fifteen. Altogether, 0 to F can represent a digit in hexadecimal, giving us 16 total possible values. You can find more information about [hexadecimal numbers here](https://www.freecodecamp.org/news/hexadecimal-number-system/).

In CSS, we can use 6 hexadecimal digits to represent colors, two each for the red (R), green (G), and blue (B) components. For example, `#000000` is black and is also the lowest possible value. You can find more information about the [RGB color system here](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/#whatisthergbcolormodel).

```html
<style>
  body {
    color: #000000;
  }
</style>
```

---

Replace the word `black` in our `body` element's background-color with its hex code representation, `#000000`.

---

Có nhiều cách khác nhau để biểu diễn màu sắc trong CSS. Một trong số đó được gọi là mã thập lục phân, gọi tắt là Hex Code.

Số chúng ta sử dụng hằng ngày là số thập phân , cơ số 10 với các ký hiệu từ 0 đến 9. Hexadecimals (hoặc hex ) là cơ số 16, nó sử dụng 16 ký hiệu riêng biệt. Tương tự số thập phân, nó có các ký hiệu 0-9 đại diện cho các giá trị từ 0 đến 9. Sau đó, A, B, C, D, E, F đại diện cho các giá trị từ mười đến mười lăm. 0 đến F có thể đại diện cho một chữ số trong hệ thập lục phân và nó cho chúng ta tổng số 16 giá trị có thể có. Bạn có thể tìm hiểu thêm thông tin về số thập lục phân tại [đây](https://www.freecodecamp.org/news/hexadecimal-number-system/).

Trong CSS, chúng ta có thể sử dụng 6 chữ số thập lục phân để biểu thị màu sắc, hai số đầu đại diện cho các thành phần màu đỏ (R), hai số tiếp theo là xanh lá cây (G) và hai số cuối là xanh lam (B). Ví dụ, `#000000` là màu đen và cũng là giá trị thấp nhất có thể. Bạn có thể tìm thêm thông tin về hệ màu RGB tại [đây](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/#whatisthergbcolormodel).

```html
<style>
  body {
    color: #000000;
  }
</style>
```

---

Thay thế từ `black` trong màu nền của phần tử `body` bằng hex code `#000000`

```html
<style>
  body {
    background-color: black;
  }
</style>
```
