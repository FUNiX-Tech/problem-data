In addition to classes, each HTML element can also have an `id` attribute.

There are several benefits to using `id` attributes: You can use an `id` to style a single element and later you'll learn that you can use them to select and modify specific elements with JavaScript.

`id` attributes should be unique. Browsers won't enforce this, but it is a widely agreed upon best practice. So please don't give more than one element the same `id` attribute.

Here's an example of how you give your h2 element the `id` of `cat-photo-app`:

```html
<h2 id="cat-photo-app"></h2>
```

---

Give your `form` element the id `cat-photo-form`.

---

Ngoài các class, mỗi phần tử HTML cũng có thể có một attribute `id`.

Có một số lợi ích khi sử dụng attribute `id`: Bạn có thể gán một `id` vào một phần tử. Sau đó bạn có thể sử dụng chúng để chọn và sửa đổi các phần tử cụ thể bằng JavaScript.

Các attribute `id` phải là duy nhất. Nó không bắt buộc, nhưng đó là một quy ước đã được thống nhất rộng rãi. Vì vậy, vui lòng không cung cấp nhiều hơn một phần tử có cùng attribute `id`.

Dưới đây là một ví dụ về cách bạn gán id `cat-photo-app` cho phần tử `h2`

```html
<h2 id="cat-photo-app"></h2>
```

---

Gán id `cat-photo-form` cho phần tử `form`.

---

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
