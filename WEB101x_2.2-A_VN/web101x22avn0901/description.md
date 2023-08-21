This section uses alternating challenge styles to show how to use CSS to position elements in a flexible way. First, a challenge will explain theory, then a practical challenge using a simple tweet component will apply the flexbox concept.

Placing the CSS property `display: flex;` on an element allows you to use other flex properties to build a responsive page.

---

Add the CSS property `display` to `#box-container` and set its value to `flex`.

---

Phần này sử dụng một phương pháp tạo style thay thế khác của CSS để định vị các phần tử một cách linh hoạt. Đầu tiên, một thử thách sẽ giải thích lý thuyết, sau đó một thử thách thực tế sử dụng một thành phần tweet đơn giản sẽ áp dụng khái niệm flexbox.

Việc đặt thuộc tính CSS `display: flex;` trên một phần tử cho phép bạn sử dụng các thuộc tính linh hoạt khác để tạo một responsive page.

---

Thêm thuộc tính `display` vào `#box-container` và đặt giá trị của nó thành `flex`.

```html
<style>
  #box-container {
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
