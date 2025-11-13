# LỘ TRÌNH HỌC HTML5, CSS3 VÀ ES6 TRONG 30 NGÀY

> **Thời lượng:** 30 ngày × 8 tiếng/ngày = 240 giờ
> **Mục tiêu:** Thành thạo HTML5, CSS3 thuần túy (không Bootstrap) và ES6 cơ bản
> **Phương pháp:** Học thực chiến, tập trung vào hiểu bản chất và luyện tập nhiều

---

## TRIẾT LÝ HỌC (Dựa trên kinh nghiệm thực tế)

### Nguyên tắc vàng:
1. **HTML5:** Đọc hết tất cả các tag, hiểu ý nghĩa từng tag → Dựng layout mà không cần CSS nhưng vẫn hiển thị đúng
2. **CSS3:** Đọc toàn bộ properties, chỉ cần biết key và ý nghĩa (không cần nhớ chính xác) → Khi làm thì search lại
3. **Tập trung:** Padding, margin, position là 3 vấn đề chính trong CSS
4. **Thực hành:** Xây dựng layout thuần, không Bootstrap để hiểu rõ bản chất
5. **Responsive:** Sử dụng em, rem cho responsive design

---

## PHÂN BỔ THỜI GIAN

| Giai đoạn | Thời gian | Nội dung | Giờ học |
|-----------|-----------|----------|---------|
| **Tuần 1-2** | Ngày 1-10 | HTML5 Hoàn chỉnh | 80h |
| **Tuần 3-4** | Ngày 11-20 | CSS3 Hoàn chỉnh | 80h |
| **Tuần 5** | Ngày 21-25 | Projects Tổng hợp | 40h |
| **Tuần 6** | Ngày 26-30 | ES6 Cơ bản | 40h |

---

# TUẦN 1-2: HTML5 HOÀN CHỈNH (10 ngày - 80 giờ)

## 📌 Mục tiêu:
- Hiểu rõ TẤT CẢ các tag HTML5
- Có thể dựng layout hoàn chỉnh chỉ bằng HTML (không CSS)
- Hiểu semantic elements và accessibility
- Nắm vững forms, tables, multimedia

---

## NGÀY 1: Nền tảng HTML5 (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 1: Giới thiệu HTML5 (1.5h)
  - HTML5 là gì, lịch sử phát triển
  - Cấu trúc cơ bản của tài liệu HTML5
  - Setup môi trường (VS Code + Live Server)
  - Browser DevTools

- Chương 2: Cấu trúc cơ bản HTML (1.5h)
  - DOCTYPE, html, head, body
  - Meta tags (charset, viewport, description)
  - Thẻ, attributes, comments
  - Nested elements

**💡 Tips:**
- Viết emmet shortcuts: `!` + Tab tạo boilerplate
- Sử dụng W3C Validator ngay từ đầu
- Đọc kỹ từng tag, không cần nhớ hết

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo 5 file HTML cơ bản với cấu trúc khác nhau
2. Viết HTML cho: Personal card, Simple blog post, Product description
3. Validate tất cả files với W3C Validator
4. Thử nghiệm với các meta tags khác nhau

**✅ Checklist:**
- [ ] Tạo được HTML5 boilerplate từ đầu
- [ ] Hiểu rõ tác dụng của từng meta tag
- [ ] Sử dụng comments hiệu quả
- [ ] Validate HTML không lỗi

---

## NGÀY 2: Văn bản và định dạng (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 3: Thẻ văn bản và định dạng (2h)
  - Headings (h1-h6) hierarchy
  - Paragraphs, line breaks
  - Text formatting (strong, em, mark, del, ins, sub, sup)
  - Blockquote, pre, code
  - Lists (ul, ol, dl)

**💡 Tips:**
- Heading hierarchy quan trọng cho SEO
- Đọc kỹ sự khác biệt: strong vs b, em vs i
- Hiểu khi nào dùng ul vs ol vs dl

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo blog post hoàn chỉnh với:
   - Proper heading hierarchy
   - Multiple paragraphs
   - Quotes, code snippets
   - Unordered và ordered lists
2. Tạo documentation page với definition lists
3. Tạo recipe page với ingredients list

**✅ Checklist:**
- [ ] Sử dụng đúng heading hierarchy
- [ ] Phân biệt rõ semantic formatting tags
- [ ] Tạo được nested lists
- [ ] Layout hiển thị rõ ràng chỉ bằng HTML

---

## NGÀY 3: Links và Navigation (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 4: Links và Navigation (2h)
  - Anchor tags (a href)
  - Relative vs absolute URLs
  - Target attribute (_blank, _self)
  - Email links, phone links
  - Anchor links (#)
  - Navigation patterns

**💡 Tips:**
- Luôn dùng relative paths cho internal links
- Hiểu rõ khi nào dùng target="_blank"
- Accessibility: descriptive link text

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo multi-page website (5 pages):
   - Homepage
   - About
   - Services
   - Blog
   - Contact
2. Navigation menu xuất hiện trên mọi page
3. Breadcrumb navigation
4. Anchor links cho table of contents
5. Footer với sitemap

**✅ Checklist:**
- [ ] Navigation hoạt động trên mọi pages
- [ ] Sử dụng đúng relative/absolute paths
- [ ] Anchor links scroll đúng section
- [ ] Email/phone links hoạt động

---

## NGÀY 4: Hình ảnh và Multimedia (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 5: Hình ảnh và Multimedia (2h)
  - Image tag (img, alt, width, height)
  - Figure và figcaption
  - Picture element (responsive images)
  - Audio element
  - Video element
  - Iframe

**💡 Tips:**
- Alt text bắt buộc cho accessibility
- Luôn specify width/height để tránh layout shift
- Hiểu responsive images với picture

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo image gallery với figure/figcaption
2. Responsive images với picture element
3. Video player với controls
4. Audio playlist
5. Embed YouTube video với iframe
6. Image optimization practice

**✅ Checklist:**
- [ ] Mọi images có alt text
- [ ] Sử dụng figure/figcaption đúng cách
- [ ] Responsive images hoạt động
- [ ] Video/audio có controls

---

## NGÀY 5: Tables (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 6: Tables (2h)
  - Table structure (table, tr, td, th)
  - thead, tbody, tfoot
  - colspan, rowspan
  - Caption
  - Accessibility với scope

**💡 Tips:**
- Tables chỉ dùng cho tabular data (không layout!)
- Luôn dùng th cho headers
- Scope attribute quan trọng cho screen readers

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Pricing table (3 tiers comparison)
2. Data table với sorting indicators
3. Schedule/timetable với colspan/rowspan
4. Product comparison table
5. Financial report table với tfoot totals

**✅ Checklist:**
- [ ] Table structure semantic đúng
- [ ] Sử dụng thead/tbody/tfoot
- [ ] colspan/rowspan hoạt động đúng
- [ ] Caption và scope attributes

---

## NGÀY 6: Forms và Input (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 7: Forms và Input (2h)
  - Form structure
  - Input types (text, email, password, number, date, etc.)
  - Textarea, select, datalist
  - Label và for attribute
  - Fieldset và legend
  - HTML5 validation attributes
  - Placeholder vs label

**💡 Tips:**
- Luôn dùng label với for=""
- HTML5 validation trước khi JavaScript
- Understand input types mới của HTML5

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Registration form hoàn chỉnh:
   - Personal info
   - Email validation
   - Password with requirements
   - Date of birth
   - Gender select
   - Terms checkbox
2. Contact form với textarea
3. Survey form với radio/checkbox groups
4. Search form với datalist
5. Login form

**✅ Checklist:**
- [ ] Tất cả inputs có labels
- [ ] HTML5 validation hoạt động
- [ ] Form có fieldset/legend hợp lý
- [ ] Accessibility tốt (keyboard navigation)

---

## NGÀY 7: Semantic Elements (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 8: HTML5 Semantic Elements (2h)
  - header, nav, main, article, section
  - aside, footer
  - time, mark, progress
  - details, summary
  - Khi nào dùng article vs section
  - Semantic HTML benefits (SEO, accessibility)

**💡 Tips:**
- Đọc kỹ sự khác biệt article vs section vs div
- Semantic markup giúp SEO và accessibility
- Screen reader users benefit rất nhiều

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Chuyển đổi div-based layout thành semantic:
   - Blog homepage
   - News website
   - E-commerce page
2. Tạo mới với semantic từ đầu:
   - Magazine article
   - Product landing page
   - Documentation page

**✅ Checklist:**
- [ ] Không còn div soup
- [ ] Sử dụng đúng header/nav/main/footer
- [ ] Article vs section dùng hợp lý
- [ ] Semantic structure rõ ràng

---

## NGÀY 8: HTML5 APIs (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 9: HTML5 APIs (2h)
  - Geolocation API
  - Drag and Drop API
  - Web Workers
  - History API
  - Khi nào sử dụng các APIs

**💡 Tips:**
- APIs này cần JavaScript để hoạt động
- Hiểu concept, implementation sẽ học sau
- Focus vào use cases thực tế

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo HTML structure cho:
   - Drag and drop file upload interface
   - Geolocation-based store locator
   - Multi-step form với history
2. Đọc documentation của từng API
3. Note down use cases thực tế

**✅ Checklist:**
- [ ] Hiểu rõ từng API làm gì
- [ ] Biết khi nào nên sử dụng
- [ ] HTML structure ready cho JavaScript

---

## NGÀY 9: Canvas, SVG, Storage (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 10: Canvas và SVG (1.5h)
  - Canvas element
  - SVG vs Canvas
  - Inline SVG
- Chương 11: Storage và Offline (1.5h)
  - localStorage vs sessionStorage
  - IndexedDB
  - Application Cache
  - Service Workers concept

**💡 Tips:**
- Canvas cho pixel-based graphics
- SVG cho vector graphics
- Storage APIs cần JavaScript

### Buổi chiều (4 giờ)
**🛠️ Thực hành:**
1. Tạo HTML structure cho:
   - Canvas-based drawing app
   - SVG icon library
   - Charts/graphs placeholder
2. Inline SVG icons trong HTML
3. Plan localStorage usage cho projects

**✅ Checklist:**
- [ ] Hiểu Canvas vs SVG
- [ ] Có thể embed SVG inline
- [ ] Understand storage options

---

## NGÀY 10: Best Practices & Tổng hợp (8 giờ)

### Buổi sáng (4 giờ)
**📚 Lý thuyết:**
- Chương 12: Best Practices và Optimization (2h)
  - SEO best practices
  - Accessibility (a11y)
  - Performance optimization
  - Code organization
  - Semantic HTML review
  - Validation và testing

**💡 Tips:**
- Semantic HTML = better SEO
- Accessibility = inclusive design
- Performance = user experience

### Buổi chiều (4 giờ)
**🛠️ Tổng hợp:**
1. **Project: Portfolio Website (chỉ HTML)**
   - Homepage với hero section
   - About page
   - Projects gallery
   - Contact form
   - Blog section
   - Semantic structure hoàn chỉnh
   - Validate tất cả pages
   - Accessibility check

2. **Review:**
   - Đọc lại tất cả notes
   - List ra các tags chưa tự tin
   - Practice lại các tags đó

**✅ Checklist cuối tuần 2:**
- [ ] Nắm vững 100% tags HTML5
- [ ] Có thể tạo layout chỉ bằng HTML
- [ ] Hiểu semantic structure
- [ ] Forms, tables thành thạo
- [ ] Portfolio website hoàn chỉnh (HTML only)

---

# TUẦN 3-4: CSS3 HOÀN CHỈNH (10 ngày - 80 giờ)

## 📌 Mục tiêu:
- Đọc toàn bộ CSS properties, biết key và ý nghĩa
- Thành thạo Padding, Margin, Position
- Tạo layout thuần (không Bootstrap)
- Responsive với em, rem
- Flexbox và Grid thành thạo

---

## NGÀY 11: CSS Fundamentals (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 1: Giới thiệu CSS3 (1.5h)
  - CSS3 là gì, vai trò
  - Cú pháp CSS
  - Cách thêm CSS (inline, internal, external)
  - CSS3 features overview

- Chương 2: Selectors (1.5h)
  - Basic selectors
  - Combinators
  - Pseudo-classes
  - Pseudo-elements
  - Attribute selectors
  - Specificity

**💡 Tips quan trọng:**
- Chỉ cần biết tên properties và tác dụng
- Khi làm thì search lại syntax
- Focus vào hiểu concept, không cần nhớ hết

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Selector Practice:**
   - Style portfolio HTML từ tuần 2
   - Thực hành tất cả loại selectors
   - Specificity wars exercise
   - Pseudo-classes hover, active, focus

2. **Layout cơ bản:**
   - Header with navigation
   - Hero section
   - Footer

**✅ Checklist:**
- [ ] Hiểu rõ selector specificity
- [ ] Sử dụng được pseudo-classes
- [ ] External CSS setup đúng
- [ ] CSS organization tốt

---

## NGÀY 12: Colors & Backgrounds (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 3: Colors và Backgrounds (1.5h)
  - Color values (hex, rgb, rgba, hsl, hsla)
  - Background color
  - Background image
  - Background properties (size, position, repeat)
  - Multiple backgrounds
  - Gradients (linear, radial)

**💡 Tips:**
- RGB vs HSL - khi nào dùng gì
- Gradients cho modern look
- Background-size: cover vs contain

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Color schemes:**
   - Tạo 5 color palettes
   - Apply vào portfolio
   - CSS variables cho colors

2. **Backgrounds:**
   - Hero section với background image
   - Gradient buttons
   - Multiple background layers
   - Pattern backgrounds

**✅ Checklist:**
- [ ] Sử dụng CSS variables cho colors
- [ ] Background images responsive
- [ ] Gradients smooth và đẹp
- [ ] Understand opacity và transparency

---

## NGÀY 13-14: Box Model & Sizing (16 giờ) ⭐ QUAN TRỌNG

### NGÀY 13 - Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 4: Box Model & Sizing (đọc kỹ toàn bộ)
  - Box model traditional vs border-box
  - Width, height
  - Min/max width/height
  - Padding (4 properties quan trọng!)
  - Margin (4 properties quan trọng!)
  - Border
  - Box-sizing

**💡 Tips cực kỳ quan trọng:**
- **LUÔN LUÔN dùng box-sizing: border-box**
- Padding, Margin, Position là 3 vấn đề chính trong CSS
- Margin collapse là điều cần hiểu rõ
- Negative margins cho overlapping effects

### NGÀY 13 - Buổi chiều (5 giờ)
**🛠️ Thực hành - Focus: Padding & Margin:**
1. **Spacing exercises:**
   - Card components với different padding
   - Margin collapse examples
   - Negative margins practice
   - Auto margins cho centering

2. **Layout spacing:**
   - Navigation với proper spacing
   - Content sections spacing
   - Card grids với consistent gaps

**✅ Checklist Ngày 13:**
- [ ] Hiểu rõ box-sizing: border-box
- [ ] Thành thạo padding shorthand
- [ ] Thành thạo margin shorthand
- [ ] Understand margin collapse

---

### NGÀY 14 - Buổi sáng (3 giờ)
**📚 Lý thuyết - Review & Deep dive:**
- Review Box Model
- Border-radius
- Box-shadow
- Overflow
- Aspect-ratio
- Object-fit

**💡 Tips:**
- Box-shadow cho depth
- Border-radius cho modern look
- Object-fit cho responsive images

### NGÀY 14 - Buổi chiều (5 giờ)
**🛠️ Thực hành - Advanced Box Model:**
1. **Component building:**
   - Cards với shadows và rounded corners
   - Buttons với multiple states
   - Image cards với object-fit
   - Modal dialogs

2. **Layout practice:**
   - Pricing table (3 tiers)
   - Product grid
   - Notification cards

**✅ Checklist Ngày 14:**
- [ ] Box-shadow for elevation
- [ ] Border-radius thành thạo
- [ ] Object-fit cho images
- [ ] Overflow handling

---

## NGÀY 15-16: Position (16 giờ) ⭐ QUAN TRỌNG

### NGÀY 15 - Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- **Position properties (đọc rất kỹ):**
  - static (default)
  - relative
  - absolute
  - fixed
  - sticky
- **Z-index**
- **Top, right, bottom, left**

**💡 Tips cực kỳ quan trọng:**
- Position là 1 trong 3 vấn đề chính
- Relative: positioned relative to itself
- Absolute: relative to positioned parent
- Fixed: relative to viewport
- Sticky: hybrid of relative and fixed

### NGÀY 15 - Buổi chiều (5 giờ)
**🛠️ Thực hành - Position basics:**
1. **Position exercises:**
   - Relative positioning practice
   - Absolute positioning trong relative parent
   - Fixed header/footer
   - Sticky sidebar navigation

2. **Real-world examples:**
   - Modal overlay
   - Dropdown menu
   - Tooltip positioning
   - Badge/notification dot

**✅ Checklist Ngày 15:**
- [ ] Hiểu rõ 5 position values
- [ ] Absolute trong relative parent
- [ ] Z-index stacking context
- [ ] Fixed vs sticky

---

### NGÀY 16 - Buổi sáng (3 giờ)
**📚 Lý thuyết - Advanced Positioning:**
- Centering techniques
- Positioning patterns
- Stacking contexts
- Transform with position

**💡 Tips:**
- 5 cách center element
- Position + transform cho perfect centering
- Understand stacking context

### NGÀY 16 - Buổi chiều (5 giờ)
**🛠️ Thực hành - Complex layouts:**
1. **Advanced positioning:**
   - Absolutely positioned navigation
   - Overlapping sections
   - Image captions overlay
   - Fixed sidebar with sticky elements

2. **Complete layouts:**
   - Dashboard với fixed header, sticky sidebar
   - Landing page với multiple sections
   - Portfolio gallery với overlays

**✅ Checklist Ngày 16:**
- [ ] 5 cách centering thành thạo
- [ ] Complex positioning layouts
- [ ] Stacking contexts control
- [ ] Position-based animations ready

---

## NGÀY 17: Typography & Fonts (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 5: Typography và Fonts
  - Font properties
  - Google Fonts
  - Web fonts (@font-face)
  - Font-size units (px, em, rem) ⭐
  - Line-height, letter-spacing
  - Text properties
  - Text shadows

**💡 Tips quan trọng:**
- **rem cho responsive typography**
- Line-height: 1.5-1.6 cho readability
- Google Fonts performance

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Typography system:**
   - Base font-size với rem
   - Typography scale (h1-h6)
   - Paragraph styles
   - Google Fonts integration

2. **Responsive typography:**
   - Fluid typography với clamp()
   - Mobile vs desktop sizes
   - Readable line-lengths

**✅ Checklist:**
- [ ] Typography scale với rem
- [ ] Google Fonts setup
- [ ] Responsive text sizing
- [ ] Line-height optimal

---

## NGÀY 18: Flexbox (8 giờ) ⭐

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 6: Flexbox (đọc kỹ toàn bộ)
  - Display flex
  - Flex direction
  - Justify-content
  - Align-items
  - Flex-wrap
  - Flex-grow, flex-shrink, flex-basis
  - Gap property

**💡 Tips:**
- Flexbox cho 1-dimensional layouts
- justify-content: main axis
- align-items: cross axis
- Flexbox Froggy game để practice

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Flexbox exercises:**
   - Navigation bar
   - Card layouts
   - Centering với flexbox
   - Equal height columns

2. **Real layouts:**
   - Holy Grail layout
   - Pricing table
   - Feature grid
   - Footer with columns

**✅ Checklist:**
- [ ] Flexbox centering thành thạo
- [ ] Navigation với flexbox
- [ ] Card grids responsive
- [ ] Gap property sử dụng

---

## NGÀY 19: Grid Layout (8 giờ) ⭐

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 7: Grid Layout (đọc kỹ toàn bộ)
  - Display grid
  - Grid template columns/rows
  - Grid gap
  - Grid areas
  - Auto-fit vs auto-fill
  - Repeat, minmax

**💡 Tips:**
- Grid cho 2-dimensional layouts
- Auto-fit vs auto-fill cho responsive
- Grid Garden game để practice
- Grid > Flexbox cho complex layouts

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Grid exercises:**
   - Basic grids
   - Responsive grids với auto-fit
   - Grid areas cho layouts
   - Nested grids

2. **Real layouts:**
   - Image gallery
   - Dashboard layout
   - Magazine layout
   - Masonry-style grid

**✅ Checklist:**
- [ ] Grid basics thành thạo
- [ ] Auto-fit responsive grids
- [ ] Grid areas naming
- [ ] Complex grid layouts

---

## NGÀY 20: Animations & Media Queries (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 8-9: Transitions và Animations
  - Transitions
  - Keyframe animations
  - Transform (translate, rotate, scale)
  - Animation properties

- Chương 11: Media Queries & Responsive ⭐
  - Breakpoints
  - Mobile-first approach
  - Responsive units (vw, vh, %, em, rem)
  - Container queries

**💡 Tips:**
- Transition cho subtle effects
- Animations cho attention
- Mobile-first CSS
- Common breakpoints: 576px, 768px, 992px, 1200px

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. **Animations:**
   - Button hover effects
   - Card hover animations
   - Loading spinners
   - Slide-in animations

2. **Responsive design:**
   - Convert all layouts to responsive
   - Mobile navigation
   - Responsive grids
   - Responsive typography

**✅ Checklist Tuần 3-4:**
- [ ] Padding, Margin, Position thành thạo ⭐
- [ ] Flexbox và Grid thành thạo
- [ ] Responsive với em/rem
- [ ] Animations smooth
- [ ] Portfolio hoàn chỉnh với CSS

---

# TUẦN 5: PROJECTS TỔNG HỢP HTML + CSS (5 ngày - 40 giờ)

## 📌 Mục tiêu:
- Áp dụng TẤT CẢ kiến thức HTML5 và CSS3
- Build 5 projects hoàn chỉnh
- Responsive 100%
- Production-ready code

---

## NGÀY 21: Project 1 - Landing Page (8 giờ)

**🎯 Project: Product Landing Page**

### Yêu cầu:
- Header với navigation (fixed/sticky)
- Hero section với CTA
- Features section (Grid 3 columns)
- Pricing table (3 tiers)
- Testimonials slider structure
- Newsletter signup
- Footer với sitemap

### Technical requirements:
- Semantic HTML5
- CSS thuần (NO frameworks)
- Responsive (mobile-first)
- Smooth animations
- Accessibility
- W3C validated

### Thời gian:
- 2h: Planning & wireframe
- 5h: Implementation
- 1h: Testing, refinement, validation

**✅ Deliverables:**
- [ ] Fully responsive
- [ ] All sections complete
- [ ] Validated HTML/CSS
- [ ] Deployed (GitHub Pages/Netlify)

---

## NGÀY 22: Project 2 - Portfolio Website (8 giờ)

**🎯 Project: Personal Portfolio**

### Yêu cầu:
- Homepage với hero
- About section
- Skills visualization
- Projects grid với filters structure
- Contact form
- Resume/CV section
- Blog listing

### Technical requirements:
- Advanced Grid layouts
- Flexbox navigation
- CSS animations
- Responsive images
- Typography scale với rem
- CSS variables cho theming

### Thời gian:
- 1h: Planning
- 6h: Implementation
- 1h: Polish & deploy

**✅ Deliverables:**
- [ ] Portfolio-ready quality
- [ ] Smooth animations
- [ ] Perfect responsive
- [ ] Fast loading

---

## NGÀY 23: Project 3 - E-commerce Page (8 giờ)

**🎯 Project: Product Catalog & Detail Page**

### Yêu cầu:
- Product grid với filters sidebar
- Product cards (image, name, price, rating)
- Product detail page:
  - Image gallery
  - Product info
  - Tabs (description, specs, reviews)
  - Related products
- Shopping cart structure
- Checkout form

### Technical requirements:
- Complex Grid layouts
- Image galleries
- Form validation styling
- Hover effects
- Cards với shadows
- Responsive table

### Thời gian:
- 1h: Planning
- 6h: Development
- 1h: Testing

**✅ Deliverables:**
- [ ] Professional e-commerce look
- [ ] All interactions smooth
- [ ] Mobile checkout easy
- [ ] Forms accessible

---

## NGÀY 24: Project 4 - Dashboard (8 giờ)

**🎯 Project: Admin Dashboard**

### Yêu cầu:
- Sidebar navigation
- Top header với user menu
- Stats cards (4 cards)
- Charts placeholders
- Data table
- Recent activities timeline
- Notifications panel

### Technical requirements:
- Advanced Grid layout
- Sticky sidebar
- Card components
- Table styling
- Responsive (sidebar collapse)
- Dark mode ready structure

### Thời gian:
- 1h: UI planning
- 6h: Implementation
- 1h: Responsive refinement

**✅ Deliverables:**
- [ ] Professional dashboard
- [ ] All components styled
- [ ] Responsive behavior perfect
- [ ] Clean code

---

## NGÀY 25: Project 5 - Blog/Magazine (8 giờ)

**🎯 Project: Magazine-style Blog**

### Yêu cầu:
- Homepage với featured posts
- Grid layout cho articles
- Article detail page:
  - Hero image
  - Typography-focused
  - Table of contents
  - Social sharing
  - Author bio
  - Related posts
- Category pages
- Search results layout
- Archive pages

### Technical requirements:
- Magazine-style grid
- Advanced typography
- Reading-optimized layout
- Lazy-loading structure ready
- SEO-optimized HTML
- Print stylesheet

### Thời gian:
- 1h: Planning
- 5h: Development
- 2h: Typography perfection & testing

**✅ Deliverables:**
- [ ] Beautiful typography
- [ ] Magazine layout
- [ ] SEO perfect
- [ ] Print-friendly

---

## 🎉 Kết thúc Tuần 5:
- 5 production-ready projects
- Portfolio đầy đủ
- HTML/CSS mastery
- Ready cho ES6

---

# TUẦN 6: ES6 CƠ BẢN (5 ngày - 40 giờ)

## 📌 Mục tiêu:
- Học 10 chương ES6 cơ bản nhất
- Có thể viết JavaScript hiện đại
- Tích hợp vào HTML/CSS projects
- Chuẩn bị cho jQuery và frameworks

---

## NGÀY 26: ES6 Foundation (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 1: Giới thiệu ES6
  - ES6 là gì, tại sao quan trọng
  - Browser support
  - Setup environment

- Chương 2: Let, Const, Block Scope
  - var vs let vs const
  - Block scope
  - Temporal dead zone
  - Best practices

**💡 Tips:**
- Luôn dùng const, chỉ dùng let khi cần reassign
- Không còn dùng var
- Block scope vs function scope

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. Refactor code từ var sang let/const
2. Block scope exercises
3. Apply vào HTML forms:
   - Form validation
   - Button interactions
   - Toggle functionality

**✅ Checklist:**
- [ ] Hiểu rõ let/const/var
- [ ] Block scope mastery
- [ ] Apply vào projects

---

## NGÀY 27: Functions & Strings (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 3: Arrow Functions
  - Syntax
  - this binding
  - When to use

- Chương 4: Template Literals
  - String interpolation
  - Multi-line strings
  - Tagged templates

**💡 Tips:**
- Arrow functions cho callbacks
- Template literals cho HTML strings
- this behavior khác biệt

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. Arrow functions exercises
2. Template literals cho dynamic HTML
3. Apply vào projects:
   - Dynamic content rendering
   - HTML string generation
   - Event handlers

**✅ Checklist:**
- [ ] Arrow functions thành thạo
- [ ] Template literals cho HTML
- [ ] Dynamic content rendering

---

## NGÀY 28: Modern Syntax (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 5: Destructuring
  - Array destructuring
  - Object destructuring
  - Function parameters
  - Default values

- Chương 6: Spread & Rest Operators
  - Spread arrays/objects
  - Rest parameters
  - Use cases

**💡 Tips:**
- Destructuring cho clean code
- Spread cho copying/merging
- Rest cho flexible functions

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. Destructuring exercises
2. Spread/rest practice
3. Apply vào projects:
   - Form data handling
   - Array manipulations
   - Function arguments

**✅ Checklist:**
- [ ] Destructuring mastery
- [ ] Spread/rest operators
- [ ] Cleaner code achieved

---

## NGÀY 29: Objects & Async (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 7: Classes
  - Class syntax
  - Constructor
  - Methods
  - Inheritance

- Chương 9: Promises
  - Promise basics
  - then/catch
  - Promise.all
  - Async/await intro

**💡 Tips:**
- Classes cho OOP structure
- Promises cho async operations
- Async/await cleaner syntax

### Buổi chiều (5 giờ)
**🛠️ Thực hành:**
1. Class-based components
2. Promise exercises
3. Apply vào projects:
   - API calls structure
   - Async form submission
   - Loading states

**✅ Checklist:**
- [ ] Classes understanding
- [ ] Promises basics
- [ ] Async operations ready

---

## NGÀY 30: Integration & Review (8 giờ)

### Buổi sáng (3 giờ)
**📚 Lý thuyết:**
- Chương 10: Default Parameters
- Chương 11: Enhanced Object Literals
- Review tất cả ES6 concepts

**💡 Tips:**
- Default params cho functions
- Object shorthand
- Method syntax

### Buổi chiều (5 giờ)
**🛠️ Final Project:**
1. **Interactive Landing Page:**
   - HTML structure
   - CSS styling
   - ES6 JavaScript:
     - Form validation
     - Dynamic content
     - Smooth scrolling
     - Modal interactions
     - API integration structure

2. **Review:**
   - Tất cả projects từ tuần 5
   - Add JavaScript interactions
   - Polish và deploy

**✅ Checklist cuối cùng:**
- [ ] ES6 basics solid
- [ ] Can write modern JavaScript
- [ ] Projects interactive
- [ ] Ready cho jQuery/frameworks

---

# ĐÁNH GIÁ & KIỂM TRA

## Sau 30 ngày, bạn phải:

### ✅ HTML5:
- [ ] Hiểu rõ TẤT CẢ các HTML5 tags
- [ ] Tạo được semantic structure
- [ ] Forms, tables thành thạo
- [ ] Accessibility aware
- [ ] SEO optimization

### ✅ CSS3:
- [ ] **Padding, Margin, Position THÀNH THẠO** ⭐⭐⭐
- [ ] Box model perfect understanding
- [ ] Flexbox và Grid mastery
- [ ] Responsive với em/rem
- [ ] Animations smooth
- [ ] Layout thuần (không Bootstrap)
- [ ] Có thể nhìn design và code ra

### ✅ ES6:
- [ ] Modern JavaScript syntax
- [ ] Can write clean code
- [ ] Async operations basics
- [ ] Ready cho frameworks

### ✅ Projects:
- [ ] 5+ production-ready projects
- [ ] Portfolio website hoàn chỉnh
- [ ] GitHub profile impressive
- [ ] Deployed projects

---

# TIPS QUAN TRỌNG TRONG QUÁ TRÌNH HỌC

## 1. Phương pháp học:
- **Đọc nhiều:** Đọc hết documentation, đọc code người khác
- **Không cần nhớ hết:** Chỉ cần biết tên và ý nghĩa
- **Search khi làm:** Tra cứu syntax khi implement
- **Thực hành nhiều:** 3h lý thuyết = 5h thực hành

## 2. Debugging:
- **Browser DevTools:** F12 là người bạn thân nhất
- **Inspect Element:** Xem cách website khác làm
- **Console log:** Debug JavaScript
- **Validate:** W3C Validator thường xuyên

## 3. Tài nguyên:
- **Documentation:** MDN Web Docs
- **Practice:** Frontend Mentor, CodePen challenges
- **Games:** Flexbox Froggy, Grid Garden
- **Reading:** CSS-Tricks articles

## 4. Padding, Margin, Position - 3 trụ cột:

### Padding:
```css
/* Spacing BÊN TRONG element */
.box {
    padding: 20px;           /* All sides */
    padding: 10px 20px;      /* Vertical Horizontal */
    padding: 10px 15px 20px 25px; /* Top Right Bottom Left */
}
```

### Margin:
```css
/* Spacing BÊN NGOÀI element */
.box {
    margin: 20px;            /* All sides */
    margin: 0 auto;          /* Center horizontally */
    margin: -10px;           /* Negative for overlap */
}
/* Hiểu margin collapse! */
```

### Position:
```css
/* Vị trí của element */
.box {
    position: relative;      /* Relative to itself */
    position: absolute;      /* Relative to positioned parent */
    position: fixed;         /* Relative to viewport */
    position: sticky;        /* Hybrid */
}
/* Luôn nhớ: absolute cần parent có position! */
```

## 5. Responsive thinking:
```css
/* Mobile first approach */
.element {
    /* Mobile styles first */
    width: 100%;
}

@media (min-width: 768px) {
    .element {
        /* Tablet styles */
        width: 50%;
    }
}

@media (min-width: 1200px) {
    .element {
        /* Desktop styles */
        width: 33.333%;
    }
}

/* Use rem for scalability */
html {
    font-size: 16px;
}

h1 {
    font-size: 2rem;  /* 32px, scales with root */
}
```

## 6. Code organization:
```css
/* Structure your CSS */
/* 1. Reset/Variables */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --primary-color: #3498db;
    --spacing: 8px;
}

/* 2. Base styles */
body { }
h1, h2, h3 { }

/* 3. Layout */
.container { }
.grid { }

/* 4. Components */
.button { }
.card { }

/* 5. Utilities */
.text-center { }
.mt-4 { }
```

---

# LỘ TRÌNH HỌC TIẾP SAU 30 NGÀY

## Tuần 7-8: ES6 Advanced
- Modules
- Async/Await deep dive
- Fetch API
- Error handling
- ES6+ features (Map, Set, Symbols, Generators)

## Tuần 9-10: jQuery
- jQuery fundamentals
- DOM manipulation
- AJAX với jQuery
- jQuery plugins
- Custom interactions

## Tuần 11-12: JavaScript Projects
- Interactive UI components
- API integration
- SPA concepts
- Performance optimization

## Tương lai:
- **Frameworks:** React/Vue (sau khi vanilla JS vững)
- **CSS:** SASS/SCSS
- **Tools:** Git, Webpack, NPM
- **Backend:** Node.js basics để hiểu full-stack

---

# KẾT LUẬN

Sau 30 ngày với lộ trình này, bạn sẽ:

1. **Nắm vững nền tảng:** HTML5, CSS3 thuần túy
2. **Tư duy đúng:** Hiểu bản chất, không phụ thuộc Bootstrap
3. **Kỹ năng thực chiến:** Nhìn design, code ra được
4. **Portfolio:** 5+ projects production-ready
5. **JavaScript:** ES6 basics để tiếp tục học framework

**Nhớ:** Không có con đường tắt. 8 giờ/ngày × 30 ngày = 240 giờ là cần thiết để THÀNH THẠO.

**Quan trọng nhất:**
- Padding, Margin, Position - 3 trụ cột CSS
- Làm nhiều, đọc nhiều code người khác
- Không Bootstrap - học thuần để hiểu bản chất
- Responsive từ đầu - mobile-first

Chúc bạn học tốt! 🚀

---

**Version:** 1.0
**Created:** 2025
**License:** Free to use for personal learning
