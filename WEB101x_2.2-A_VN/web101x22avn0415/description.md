Another way you can represent colors in CSS is by using `RGB` values.

The `RGB` value for black looks like this:

```css
rgb(0, 0, 0)
```

The `RGB` value for white looks like this:

```css
rgb(255, 255, 255)
```

Instead of using six hexadecimal digits like you do with hex code, with `RGB` you specify the brightness of each color with a number between 0 and 255.

If you do the math, the two digits for one color equal 16 times 16, which gives us 256 total values. So `RGB`, which starts counting from zero, has the exact same number of possible values as hex code.

Here's an example of how you'd change the `body` background to orange using its RGB code.

```css
body {
  background-color: rgb(255, 165, 0);
}
```

---

Let's replace the hex code in our `body` element's background color with the RGB value for black: `rgb(0, 0, 0)`

---

Chúng ta sử dụng các giá trị `RGB` để biểu diễn màu sắc trong CSS

Giá trị `RGB` cho màu đen trông như thế này:

```css
rgb(0, 0, 0)
```

Giá trị `RGB` cho màu trắng trông như thế này:

```css
rgb(255, 255, 255)
```

Thay vì sử dụng sáu chữ số thập lục phân như bạn làm với hex code, với RGB, bạn chỉ định độ sáng của từng màu với một số từ 0 đến 255.

Nếu bạn làm phép toán, hai chữ số của một màu bằng 16 nhân 16, cho chúng ta tổng cộng 256 giá trị. Vì vậy giá trị `RGB` bắt đầu đếm từ 0

Đây là một ví dụ về cách bạn thay đổi màu nền của `body` thành màu cam bằng cách sử dụng `RGB` code

```css
body {
  background-color: rgb(255, 165, 0);
}
```

---

Hãy thay thế hex code của màu nền `body` bằng giá trị `RGB` với màu đen:`rgb(0, 0, 0)`

---

```html
<style>
  body {
    background-color: #f00;
  }
</style>
```
