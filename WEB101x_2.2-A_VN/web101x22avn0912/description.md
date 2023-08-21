CSS flexbox has a feature to split a flex container into multiple rows (or columns). By default, a flex container will fit all flex items together. For example, a row will all be on one line.

However, using the `flex-wrap` property tells CSS to wrap items. This means extra items move into a new row or column. The break point of where the wrapping happens depends on the size of the items and the size of the container.

CSS also has options for the direction of the wrap:

- `nowrap`: this is the default setting, and does not wrap items.
- `wrap`: wraps items onto multiple lines from top-to-bottom if they are in rows and left-to-right if they are in columns.
- `wrap-reverse`: wraps items onto multiple lines from bottom-to-top if they are in rows and right-to-left if they are in columns.

---

The current layout has too many boxes for one row. Add the CSS property `flex-wrap` to the `#box-container` element, and give it a value of `wrap`.

---

CSS flexbox có tính năng chia flex container thành nhiều hàng (hoặc cột). Theo mặc định, một flex container sẽ chứa tất cả các flex item. Ví dụ, một hàng sẽ nằm trên một dòng.

Việc sử dụng thuộc tính `flex-wrap` cho phép CSS bọc các item. Điều này có nghĩa là các item bổ sung sẽ chuyển sang một hàng hoặc cột mới. Break point tại nơi bọc các item phụ thuộc vào kích thước của các item và kích thước của container.

CSS cũng có các tùy chọn cho hướng của việc bọc item:

- `nowrap`: đây là cài đặt mặc định và không bao gồm các item.
- `wrap`: bọc các item thành nhiều dòng từ trên xuống dưới nếu chúng ở trong hàng và từ trái sang phải nếu chúng ở trong cột.
- `wrap-reverse`: bọc các item thành nhiều dòng từ dưới lên trên nếu chúng ở trong hàng và từ phải sang trái nếu chúng ở trong cột.

---

Bố cục hiện tại có quá nhiều hộp cho một hàng. Hãy thêm thuộc tính CSS `flex-wrap` vào phần tử `#box-container` và đặt cho nó một giá trị là `wrap`.

---

```html
<style>
  #box-container {
    background: gray;
    display: flex;
    height: 100%;
  }
  #box-1 {
    background-color: dodgerblue;
    width: 25%;
    height: 50%;
  }

  #box-2 {
    background-color: orangered;
    width: 25%;
    height: 50%;
  }
  #box-3 {
    background-color: violet;
    width: 25%;
    height: 50%;
  }
  #box-4 {
    background-color: yellow;
    width: 25%;
    height: 50%;
  }
  #box-5 {
    background-color: green;
    width: 25%;
    height: 50%;
  }
  #box-6 {
    background-color: black;
    width: 25%;
    height: 50%;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
  <div id="box-3"></div>
  <div id="box-4"></div>
  <div id="box-5"></div>
  <div id="box-6"></div>
</div>
```
