CSS has a property called `width` that controls an element's width. Just like with fonts, we'll use `px` (pixels) to specify the image's width.

For example, if we wanted to create a CSS class called `larger-image` that gave HTML elements a width of 500 pixels, we'd use:

```html
<style>
  .larger-image {
    width: 500px;
  }
</style>
```

---

Create a class called `smaller-image` and use it to resize the image so that it's only 100 pixels wide.

---

CSS có một thuộc tính được gọi là `width` chỉ định chiều rộng của một phần tử. Cũng giống như với phông chữ, chúng ta sẽ sử dụng `px` (pixel) để chỉ định chiều rộng của hình ảnh.

Ví dụ, nếu chúng ta muốn tạo một class CSS có tên `larger-image` và chỉ định chiều rộng phần tử HTML là 500 pixel, chúng ta sẽ sử dụng:

```html
<style>
  .larger-image {
    width: 500px;
  }
</style>
```

---

Tạo một class được gọi `smaller-image` và sử dụng nó để thay đổi kích thước hình ảnh sao cho nó chỉ rộng 100 pixel.

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
</style>

<h2 class="red-text">CatPhotoApp</h2>
<main>
  <p class="red-text">Click here to view more <a href="#">cat photos</a>.</p>

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
