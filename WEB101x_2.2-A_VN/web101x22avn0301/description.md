You can add images to your website by using the `img` element, and point to a specific image's URL using the `src` attribute.

An example of this would be:

```html
<img src="https://www.freecatphotoapp.com/your-image.jpg" />
```

Note that `img` elements are self-closing.

All `img` elements **must** have an `alt` attribute. The text inside an `alt` attribute is used for screen readers to improve accessibility and is displayed if the image fails to load.

**Note:** If the image is purely decorative, using an empty `alt` attribute is a best practice.

Ideally the `alt` attribute should not contain special characters unless needed.

Let's add an `alt` attribute to our img example above:

```html
<img
  src="https://www.freecatphotoapp.com/your-image.jpg"
  alt="freeCodeCamp logo"
/>
```

Let's try to add an image to our website:

Within the existing `main` element, insert an `img` element before the existing `p` elements.

Now set the `src` attribute so that it points to the url `https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg`

Finally, don't forget to give your `img` element an `alt` attribute with applicable text.

---

Bạn có thể thêm hình ảnh vào trang web của mình bằng cách sử dụng phần tử `img` và trỏ đến URL của một hình ảnh cụ thể bằng cách sử dụng attribute `src`.

Ví dụ:

```html
<img src="https://www.freecatphotoapp.com/your-image.jpg" />
```

Lưu ý rằng các phần tử `img` có thẻ tự đóng.

Tất cả các phần tử `img` phải có attribute `alt`. Văn bản bên trong attribute `alt` được sử dụng cho trình đọc màn hình cải thiện khả năng tiếp cận và hiển thị diễn giải nếu hình ảnh không được tải.

Lưu ý: Nếu hình ảnh chỉ mang tính chất trang trí, thì cách tốt nhất là sử dụng attribute `alt` trống.

Attribute `alt` không nên chứa các ký tự đặc biệt trừ khi cần thiết.

Hãy thêm một attribute `alt` vào ví dụ img ở trên

```html
<img
  src="https://www.freecatphotoapp.com/your-image.jpg"
  alt="freeCodeCamp logo"
/>
```

Hãy thử thêm một hình ảnh vào trang web

Trong phần tử `main` , hãy chèn một phần tử `img` trước phần tử `p`.

Bây giờ, hãy đặt attribute `src` để nó trỏ đến url `https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg`

Cuối cùng, đừng quên đặt attribute `alt` vào phần tử `img`

```html
<h2>CatPhotoApp</h2>
<main>
  <p>
    Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching
    attack your ankles chase the red dot, hairball run catnip eat the grass
    sniff.
  </p>
  <p>
    Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere
    rip the couch sleep in the sink fluffy fur catnip scratched.
  </p>
</main>
```
