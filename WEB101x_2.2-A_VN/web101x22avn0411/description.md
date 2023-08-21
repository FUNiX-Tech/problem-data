One cool thing about `id` attributes is that, like classes, you can style them using CSS.

However, an `id` is not reusable and should only be applied to one element. An `id` also has a higher specificity (importance) than a class so if both are applied to the same element and have conflicting styles, the styles of the `id` will be applied.

Here's an example of how you can take your element with the `id` attribute of `cat-photo-element` and give it the background color of green. In your `style` element:

```html
<style>
  #cat-photo-element {
    background-color: green;
  }
</style>
```

Note that inside your `style` element, you always reference classes by putting a `.` in front of their names. You always reference ids by putting a `#` in front of their names.

---

Try giving your form, which now has the `id` attribute of `cat-photo-form`, a green background.

---

Một điều thú vị về attribute `id` là bạn có thể chọn phần tử và tạo style trong CSS, tương tự như các class

Tuy nhiên, `id` không thể sử dụng lại và chỉ nên được áp dụng cho một phần tử. `id` cũng có tính cụ thể (tầm quan trọng) cao hơn một class, vì vậy nếu cả hai class và `id` đều được áp dụng cho cùng một phần tử và xung đột, thì style của `id` sẽ được áp dụng.

Dưới đây là một ví dụ về cách chọn phần tử với attribute `id` là `cat-photo-element` và đặt cho nó màu nền là xanh lục.

Trong phần tử `style` của bạn:

```html
<style>
  #cat-photo-element {
    background-color: green;
  }
</style>
```

Lưu ý rằng bên trong phần tử `style`, chúng ta tham chiếu đến các class bằng cách đặt dấu `.` trước tên của class, tham chiếu `id` bằng cách đặt dấu `#` trước tên của `id`.

---

Hãy thiết lập màu nền cho phần tử `form` với attribute id là `cat-photo-form` màu xanh lá cây.

```html
<link
  href="https://fonts.googleapis.com/css?family=Lobster"
  rel="stylesheet"
  type="text/css"
/>
<style>
  .red-text {
    color: red;
  }

  h2 {
    font-family: Lobster, monospace;
  }

  p {
    font-size: 16px;
    font-family: monospace;
  }

  .thick-green-border {
    border-color: green;
    border-width: 10px;
    border-style: solid;
    border-radius: 50%;
  }

  .smaller-image {
    width: 100px;
  }

  .silver-background {
    background-color: silver;
  }
</style>

<h2 class="red-text">CatPhotoApp</h2>
<main>
  <p class="red-text">Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"
    ><img
      class="smaller-image thick-green-border"
      src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
      alt="A cute orange cat lying on its back."
  /></a>

  <div class="silver-background">
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

  <form
    action="https://freecatphotoapp.com/submit-cat-photo"
    id="cat-photo-form"
  >
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
