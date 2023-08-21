Classes are reusable styles that can be added to HTML elements.

Here's an example CSS class declaration:

```html
<style>
  .blue-text {
    color: blue;
  }
</style>
```

You can see that we've created a CSS class called `blue-text` within the `<style>` tag. You can apply a class to an HTML element like this: `<h2 class="blue-text">CatPhotoApp</h2>`. Note that in your CSS `style` element, class names start with a period. In your HTML elements' class attribute, the class name does not include the period.

---

Inside your `style` element, change the `h2` selector to `.red-text` and update the color's value from `blue` to `red`.

Give your `h2` element the `class` attribute with a value of `red-text`.

---

Các class có thể được sử dụng lại nếu chúng được thêm vào các phần tử HTML.

Đây là một khai báo CSS class mẫu:

```html
<style>
  .blue-text {
    color: blue;
  }
</style>
```

Bạn có thể thấy rằng chúng ta đã tạo một class được gọi `blue-text` trong thẻ `<style>`. Bạn có thể áp dụng một class cho một phần tử HTML như sau `<h2 class="blue-text">CatPhotoApp</h2>`. Lưu ý rằng trong CSS, việc chọn phần tử stylebằng tên class bắt đầu bằng dấu chấm. Trong thuộc tính class của các phần tử HTML , tên class không bao gồm dấu chấm.

---

Bên trong phần tử `style`, thay đổi bộ chọn `h2` thành `.red-text` và cập nhật giá trị của màu từ `blue` thành `red`.

Cung cấp cho phần tử `h2` attribute `class` có giá trị là `red-text`.

```html
<style>
  h2 {
    color: blue;
  }
</style>

<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"
    ><img
      src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
      alt="A cute orange cat lying on its back."
  /></a>

  <div>
    <p>Things cats love:</p>
    <ul>
      <li>cat nip</li>
      <li>laser pointers</li>
      <li>lasagna</li>
    </ul>
    <p>Top 3 things cats hate:</p>
    <ol>
      <li>flea treatment</li>
      <li>thunder</li>
      <li>other cats</li>
    </ol>
  </div>

  <form action="https://freecatphotoapp.com/submit-cat-photo">
    <label><input type="radio" name="indoor-outdoor" checked /> Indoor</label>
    <label><input type="radio" name="indoor-outdoor" /> Outdoor</label><br />
    <label><input type="checkbox" name="personality" checked /> Loving</label>
    <label><input type="checkbox" name="personality" /> Lazy</label>
    <label><input type="checkbox" name="personality" /> Energetic</label><br />
    <input type="text" placeholder="cat photo URL" required />
    <button type="submit">Submit</button>
  </form>
</main>
```
