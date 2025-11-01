# Image Optimization Helper - Intermediate Example

A performance-focused skill that optimizes images for web by converting to modern formats (WebP, AVIF), compressing efficiently, and generating responsive sizes.

## What This Example Teaches

- Image optimization techniques and best practices
- Modern image formats (WebP, AVIF) vs legacy (JPEG, PNG)
- Responsive image strategies with srcset
- Build pipeline integration for automated optimization
- Performance measurement and impact analysis
- Framework-specific image handling

## Why Image Optimization Matters

### Performance Impact
- **Images = 50-70% of page weight** on average website
- **LCP (Largest Contentful Paint)** often triggered by images
- **Mobile users** especially affected by large images
- **Core Web Vitals** directly impacted by image performance

### Real-World Impact
```
Before Optimization:
- Hero image: 2.4 MB → Page load: 8-12 seconds on 3G
- Total images: 5.2 MB → Mobile bounce rate: 40%

After Optimization:
- Hero image: 380 KB (84% reduction) → Page load: 2-3 seconds
- Total images: 780 KB (85% reduction) → Mobile bounce rate: 12%
```

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/image-optimizer.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/image-optimizer.md
```

### 2. Install Required Tools

The skill will check for tools and guide installation, but you can install ahead:

**macOS:**
```bash
brew install imagemagick webp

# For Node.js projects (recommended)
npm install -g sharp-cli
```

**Ubuntu/Debian:**
```bash
sudo apt-get install imagemagick webp

# For Node.js projects
npm install -g sharp-cli
```

**Windows:**
```bash
# Using Chocolatey
choco install imagemagick
choco install webp

# Or use npm
npm install -g sharp-cli
```

### 3. Optimize Your Images

```bash
cd your-project
claude

# Then ask:
"Optimize images in the public folder"
"Convert all images to WebP"
"Compress images for web performance"
"Generate responsive image sizes"
```

## Example Usage Scenarios

### Scenario 1: One-Time Optimization

**You:**
```
I have a website with slow loading images. Can you optimize them?
```

**Claude (using image-optimizer skill):**
```
🔍 Analyzing images in your project...

Found 24 images to optimize:
- 15 JPEGs (total: 8.4 MB)
- 7 PNGs (total: 2.1 MB)
- 2 GIFs (total: 540 KB)
Total size: 11.04 MB

Optimization Plan:
✓ Convert to WebP (80% quality)
✓ Compress originals (85% quality)
✓ Generate responsive sizes (320w, 768w, 1920w)
✓ Backup originals to /images/original/

Estimated reduction: ~75-85% (8-9 MB saved)

Required tools: ✓ ImageMagick  ✓ cwebp

Proceed with optimization? (yes/no)
```

**You:** yes

**Claude:**
```
🖼️  Optimizing images...

✅ hero.jpg → hero.webp (2.4 MB → 380 KB, 84% reduction)
✅ product-1.png → product-1.webp (890 KB → 125 KB, 86% reduction)
✅ background.jpg → background.webp (1.6 MB → 240 KB, 85% reduction)
... [21 more images]

📊 Optimization Results:
- Images optimized: 24
- Original size: 11.04 MB
- Optimized size: 1.8 MB
- Reduction: 83.7% (9.24 MB saved)
- Formats: WebP + optimized originals
- Responsive sizes: Created for 15 images

🚀 Performance Impact:
- Expected LCP improvement: 30-50%
- Expected page load improvement: 4-5x on 3G
- Lighthouse score impact: +15 to +25 points

Next Steps:
1. Update HTML to use <picture> elements
2. Implement lazy loading for below-fold images
3. Add images to build pipeline for future automation
4. Test on staging before deploying

Would you like me to generate <picture> elements for your images?
```

### Scenario 2: Automated Build Integration

**You:**
```
How can I automate image optimization in my build process?
```

**Claude (using image-optimizer skill):**
```
I'll set up automated image optimization for your build pipeline.

Detected: Next.js project with Vercel deployment

Setting up:
1. Installing sharp (optimal for Next.js)
2. Configuring next.config.js
3. Creating GitHub Action for optimization
4. Adding npm scripts

[Creates configuration files and scripts]

✅ Setup complete!

Your images will now:
- Automatically optimize during build
- Serve WebP/AVIF on supported browsers
- Generate responsive sizes automatically
- Lazy load by default with Next.js Image component

Example usage in your code:
```jsx
import Image from 'next/image'

<Image
  src="/images/hero.jpg"
  alt="Hero"
  width={1920}
  height={1080}
  priority={true}  // For LCP image
/>
```

Test with: npm run dev
Build with: npm run build
```

### Scenario 3: Responsive Images

**You:**
```
Generate responsive versions of my hero image for different screen sizes
```

**Claude (using image-optimizer skill):**
```
Creating responsive versions of hero.jpg...

Generating sizes:
✅ hero-320.webp (320w) - 45 KB
✅ hero-480.webp (480w) - 72 KB
✅ hero-768.webp (768w) - 145 KB
✅ hero-1024.webp (1024w) - 210 KB
✅ hero-1920.webp (1920w) - 380 KB

Also creating fallback JPEGs:
✅ hero-320.jpg (320w) - 68 KB
✅ hero-768.jpg (768w) - 185 KB
✅ hero-1920.jpg (1920w) - 520 KB

Generated <picture> element for you:
```html
<picture>
  <source
    srcset="
      /images/hero-320.webp 320w,
      /images/hero-480.webp 480w,
      /images/hero-768.webp 768w,
      /images/hero-1024.webp 1024w,
      /images/hero-1920.webp 1920w
    "
    sizes="100vw"
    type="image/webp"
  />
  <source
    srcset="
      /images/hero-320.jpg 320w,
      /images/hero-768.jpg 768w,
      /images/hero-1920.jpg 1920w
    "
    sizes="100vw"
    type="image/jpeg"
  />
  <img
    src="/images/hero-1920.jpg"
    alt="Hero image"
    loading="eager"
    width="1920"
    height="1080"
    fetchpriority="high"
  />
</picture>
```

This ensures:
✓ Right size for each device
✓ WebP for modern browsers
✓ JPEG fallback for older browsers
✓ Fast LCP (loading="eager" + fetchpriority)
```

## What Makes This an Intermediate Example?

### 1. Complex Domain Knowledge

**Image Formats:**
- Understanding lossy vs lossless compression
- Knowing when to use JPEG vs PNG vs WebP vs AVIF
- Alpha channel considerations
- Browser compatibility matrix

**Optimization Techniques:**
- Quality vs size tradeoffs
- Progressive vs baseline JPEG
- Chroma subsampling
- Metadata stripping

### 2. Tool Integration

Multiple external tools:
- ImageMagick for processing
- cwebp/dwebp for WebP
- avifenc for AVIF
- sharp for Node.js optimization
- Build pipeline integration

### 3. Performance Measurement

Understanding web performance:
- Core Web Vitals (LCP, CLS, FID)
- Lighthouse scoring
- Real User Monitoring (RUM)
- Network waterfall analysis

### 4. Framework Awareness

Different approaches for:
- Next.js (next/image)
- Gatsby (gatsby-plugin-image)
- Nuxt (nuxt-img)
- Vue/React vanilla
- Static HTML

### 5. Production Considerations

- Backup strategies
- Rollback plans
- CI/CD integration
- CDN configuration
- Caching strategies
- Git LFS for large files

## Performance Optimization Techniques

### Technique 1: Format Selection

**Decision Tree:**
```
Need transparency?
├─ Yes → WebP (with alpha) or PNG
│   ├─ Modern browsers only? → WebP
│   └─ Legacy support? → PNG with WebP fallback
└─ No → WebP or JPEG
    ├─ Photo? → JPEG/WebP
    └─ Graphics/UI? → WebP

Cutting-edge optimization?
└─ AVIF (20-50% better than WebP)
```

### Technique 2: Quality Settings

**JPEG Quality Guide:**
```
95+ : Unnecessary, huge files
90  : High quality, large files
85  : Sweet spot for photos
80  : Good quality, smaller size ⭐
75  : Acceptable for backgrounds
70  : Noticeable quality loss
<70 : Avoid unless extreme size constraints
```

**WebP Quality Guide:**
```
90+ : Very high quality
80-85 : Sweet spot (recommended) ⭐
75-80 : Good balance
70-75 : Acceptable for non-critical images
<70 : Only for thumbnails
```

### Technique 3: Responsive Strategy

**Breakpoint Selection:**
```
Mobile First Approach:
320w  : Small phones (portrait)
375w  : Standard phones (portrait)
480w  : Phones (landscape) / Small tablets
768w  : Tablets (portrait)
1024w : Tablets (landscape) / Laptop
1366w : Standard laptop
1920w : Full HD desktop
2560w : 2K+ displays
3840w : 4K displays (only if necessary)
```

**sizes Attribute Strategy:**
```html
<!-- Full width image -->
sizes="100vw"

<!-- Half width image -->
sizes="(min-width: 768px) 50vw, 100vw"

<!-- Sidebar layout -->
sizes="(min-width: 1024px) 33vw, (min-width: 768px) 50vw, 100vw"

<!-- Fixed width -->
sizes="(min-width: 768px) 600px, 100vw"
```

### Technique 4: Lazy Loading

**Native Lazy Loading:**
```html
<img src="image.jpg" loading="lazy" alt="..." />
```

**When to use loading="eager":**
- Above-the-fold images
- LCP (Largest Contentful Paint) images
- Logo, navigation elements
- First few images in viewport

**When to use loading="lazy":**
- Below-the-fold images
- Carousel images (except first)
- Gallery images
- Footer images

### Technique 5: Preventing Layout Shift

**Always specify dimensions:**
```html
<!-- ❌ BAD: No dimensions -->
<img src="hero.jpg" alt="Hero" />

<!-- ✅ GOOD: Fixed dimensions -->
<img src="hero.jpg" alt="Hero" width="1920" height="1080" />

<!-- ✅ GOOD: Aspect ratio -->
<img src="hero.jpg" alt="Hero" style="aspect-ratio: 16/9" />
```

**CSS for responsive images:**
```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Prevent layout shift */
img[width][height] {
  aspect-ratio: attr(width) / attr(height);
}
```

## Framework-Specific Examples

### Next.js (Recommended Approach)

```jsx
import Image from 'next/image'

// For static images
import heroImage from '../public/hero.jpg'

export default function Hero() {
  return (
    <>
      {/* LCP image - use priority */}
      <Image
        src={heroImage}
        alt="Hero"
        priority
        placeholder="blur"
        quality={85}
      />

      {/* Below-fold images - lazy load */}
      <Image
        src="/images/product.jpg"
        alt="Product"
        width={800}
        height={600}
        quality={80}
      />
    </>
  )
}
```

**next.config.js:**
```javascript
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    minimumCacheTTL: 60,
    domains: ['your-cdn.com'],
  },
}
```

### Gatsby

```jsx
import { StaticImage, GatsbyImage, getImage } from "gatsby-plugin-image"

export default function Hero({ data }) {
  // Static image (build-time optimization)
  return (
    <>
      <StaticImage
        src="../images/hero.jpg"
        alt="Hero"
        placeholder="blurred"
        layout="fullWidth"
        quality={85}
      />

      {/* Dynamic image from GraphQL */}
      <GatsbyImage
        image={getImage(data.product.image)}
        alt={data.product.name}
      />
    </>
  )
}

export const query = graphql`
  query {
    product {
      image {
        childImageSharp {
          gatsbyImageData(
            width: 800
            placeholder: BLURRED
            formats: [AUTO, WEBP, AVIF]
          )
        }
      }
    }
  }
`
```

### React (Vanilla)

```jsx
function ResponsiveImage({ src, alt, sizes }) {
  return (
    <picture>
      <source
        srcSet={`
          ${src}-320.webp 320w,
          ${src}-768.webp 768w,
          ${src}-1920.webp 1920w
        `}
        sizes={sizes}
        type="image/webp"
      />
      <source
        srcSet={`
          ${src}-320.jpg 320w,
          ${src}-768.jpg 768w,
          ${src}-1920.jpg 1920w
        `}
        sizes={sizes}
        type="image/jpeg"
      />
      <img
        src={`${src}-768.jpg`}
        alt={alt}
        loading="lazy"
        width="768"
        height="432"
      />
    </picture>
  )
}

// Usage
<ResponsiveImage
  src="/images/hero"
  alt="Hero image"
  sizes="100vw"
/>
```

### Vue/Nuxt

```vue
<template>
  <!-- Nuxt Image module -->
  <nuxt-img
    src="/images/hero.jpg"
    alt="Hero"
    width="1920"
    height="1080"
    format="webp"
    quality="85"
    loading="lazy"
    :placeholder="[100, 100, 75, 5]"
  />

  <!-- Or use nuxt-picture for multiple formats -->
  <nuxt-picture
    src="/images/hero.jpg"
    :img-attrs="{
      alt: 'Hero',
      loading: 'lazy'
    }"
  />
</template>

<script setup>
// nuxt.config.ts
export default defineNuxtConfig({
  image: {
    formats: ['webp', 'avif'],
    screens: {
      xs: 320,
      sm: 640,
      md: 768,
      lg: 1024,
      xl: 1280,
      xxl: 1536,
    },
  },
})
</script>
```

## Build Pipeline Integration

### GitHub Actions

```yaml
# .github/workflows/optimize-images.yml
name: Optimize Images

on:
  push:
    paths:
      - 'public/images/**'
      - 'src/assets/images/**'

jobs:
  optimize:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y imagemagick webp
          npm install -g sharp-cli

      - name: Optimize images
        run: |
          # Create optimized directory
          mkdir -p public/images/optimized

          # Optimize with sharp-cli
          sharp -i 'public/images/*.{jpg,png}' \
                -o 'public/images/optimized/{name}-{width}.{format}' \
                --format webp --quality 80 \
                resize 320 768 1920

      - name: Commit optimized images
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "Image Optimizer"
          git add public/images/optimized
          git diff --quiet && git diff --staged --quiet || git commit -m "chore: optimize images"
          git push
```

### npm Scripts

```json
{
  "scripts": {
    "images:optimize": "node scripts/optimize-images.js",
    "images:check": "node scripts/check-image-sizes.js",
    "prebuild": "npm run images:optimize",
    "build": "next build"
  }
}
```

**scripts/optimize-images.js:**
```javascript
const sharp = require('sharp')
const glob = require('glob')
const path = require('path')
const fs = require('fs').promises

async function optimizeImages() {
  const images = glob.sync('public/images/**/*.{jpg,jpeg,png}')

  for (const imagePath of images) {
    const filename = path.basename(imagePath, path.extname(imagePath))
    const dir = path.dirname(imagePath)
    const outputDir = path.join(dir, 'optimized')

    await fs.mkdir(outputDir, { recursive: true })

    const image = sharp(imagePath)
    const metadata = await image.metadata()

    // Generate WebP
    await image
      .webp({ quality: 80 })
      .toFile(path.join(outputDir, `${filename}.webp`))

    // Generate responsive sizes
    const sizes = [320, 768, 1920]
    for (const size of sizes) {
      if (size < metadata.width) {
        await sharp(imagePath)
          .resize(size)
          .webp({ quality: 80 })
          .toFile(path.join(outputDir, `${filename}-${size}.webp`))
      }
    }

    console.log(`✅ Optimized: ${filename}`)
  }
}

optimizeImages().catch(console.error)
```

## Performance Monitoring

### Lighthouse CI

```yaml
# lighthouserc.js
module.exports = {
  ci: {
    collect: {
      numberOfRuns: 3,
      url: ['http://localhost:3000'],
    },
    assert: {
      assertions: {
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-byte-weight': ['error', { maxNumericValue: 1000000 }],
        'uses-webp-images': 'error',
        'uses-responsive-images': 'error',
        'offscreen-images': 'error',
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
}
```

### Web Vitals Monitoring

```javascript
// lib/vitals.js
export function reportWebVitals(metric) {
  // Send to analytics
  if (metric.name === 'LCP') {
    console.log('Largest Contentful Paint:', metric.value)
    // Track LCP element
    console.log('LCP Element:', metric.entries[0]?.element)
  }

  // Send to your analytics service
  window.gtag?.('event', metric.name, {
    value: Math.round(metric.value),
    event_label: metric.id,
    non_interaction: true,
  })
}
```

```jsx
// pages/_app.js
import { reportWebVitals } from '../lib/vitals'

export { reportWebVitals }

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

## Common Issues and Solutions

### Issue 1: Images Too Large After Optimization

**Problem:** Optimized images still > 200 KB

**Solutions:**
```bash
# Lower quality
cwebp -q 70 input.jpg -o output.webp  # Instead of 80

# Resize before optimizing
convert input.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 resized.jpg
cwebp -q 80 resized.jpg -o output.webp

# Try AVIF (better compression)
avifenc --min 20 --max 40 input.jpg output.avif
```

### Issue 2: Quality Loss Visible

**Problem:** Images look pixelated or artifacts visible

**Solutions:**
```bash
# Increase quality
cwebp -q 90 input.jpg -o output.webp

# Use lossless for critical images
cwebp -lossless input.png -o output.webp

# Use higher quality JPEG
convert input.jpg -quality 90 output.jpg
```

### Issue 3: Browser Compatibility

**Problem:** WebP not showing in older browsers

**Solution:** Always provide fallback
```html
<picture>
  <!-- Modern browsers get WebP -->
  <source srcset="image.webp" type="image/webp" />
  <!-- Fallback for older browsers -->
  <img src="image.jpg" alt="..." />
</picture>
```

### Issue 4: Slow Build Times

**Problem:** Image optimization taking too long in build

**Solutions:**
```javascript
// Cache optimized images
const cache = new Map()

async function optimizeWithCache(imagePath) {
  const hash = await getFileHash(imagePath)

  if (cache.has(hash)) {
    return cache.get(hash)
  }

  const optimized = await optimize(imagePath)
  cache.set(hash, optimized)

  return optimized
}

// Or optimize on-demand instead of at build time
// Use Next.js Image Optimization API
// Use Cloudinary/Imgix for dynamic optimization
```

### Issue 5: Layout Shift (CLS)

**Problem:** Images causing layout shift during load

**Solutions:**
```html
<!-- Always specify dimensions -->
<img
  src="image.jpg"
  width="800"
  height="600"
  alt="..."
/>

<!-- Or use aspect ratio -->
<img
  src="image.jpg"
  style="aspect-ratio: 4/3; width: 100%; height: auto;"
  alt="..."
/>
```

```css
/* Reserve space */
.image-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.image-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Advanced Techniques

### Art Direction

Different images for different screen sizes:

```html
<picture>
  <!-- Mobile: Portrait crop -->
  <source
    media="(max-width: 767px)"
    srcset="hero-mobile.webp"
    type="image/webp"
  />

  <!-- Tablet: Landscape crop -->
  <source
    media="(min-width: 768px) and (max-width: 1023px)"
    srcset="hero-tablet.webp"
    type="image/webp"
  />

  <!-- Desktop: Wide crop -->
  <source
    media="(min-width: 1024px)"
    srcset="hero-desktop.webp"
    type="image/webp"
  />

  <!-- Fallback -->
  <img src="hero-desktop.jpg" alt="Hero" />
</picture>
```

### Blur-up Placeholder

Low-quality image placeholder (LQIP):

```javascript
// Generate tiny placeholder
await sharp(input)
  .resize(20, 20, { fit: 'inside' })
  .webp({ quality: 20 })
  .toBuffer()
  .then(data => {
    const base64 = data.toString('base64')
    const placeholder = `data:image/webp;base64,${base64}`
    return placeholder
  })
```

```jsx
function ImageWithPlaceholder({ src, alt, placeholder }) {
  const [loaded, setLoaded] = useState(false)

  return (
    <div className="image-container">
      {/* Placeholder */}
      <img
        src={placeholder}
        alt=""
        className="placeholder"
        style={{ filter: loaded ? 'blur(0)' : 'blur(20px)' }}
      />

      {/* Actual image */}
      <img
        src={src}
        alt={alt}
        onLoad={() => setLoaded(true)}
        style={{ opacity: loaded ? 1 : 0 }}
      />
    </div>
  )
}
```

### Progressive Enhancement

```javascript
// Detect WebP support
function supportsWebP() {
  const canvas = document.createElement('canvas')
  return canvas.toDataURL('image/webp').indexOf('data:image/webp') === 0
}

// Use feature detection
if (supportsWebP()) {
  document.documentElement.classList.add('webp')
}
```

```css
/* Use WebP when supported */
.hero {
  background-image: url('hero.jpg');
}

.webp .hero {
  background-image: url('hero.webp');
}
```

## Best Practices Checklist

Before deploying optimized images:

- [ ] All images optimized (80-85% quality)
- [ ] WebP versions generated
- [ ] Fallback JPEG/PNG provided
- [ ] Responsive sizes created (3+ breakpoints)
- [ ] Dimensions specified (width/height)
- [ ] Lazy loading implemented (below-fold)
- [ ] LCP image uses priority loading
- [ ] `<picture>` elements for hero images
- [ ] Alt text provided for all images
- [ ] Images served from CDN
- [ ] Proper cache headers set
- [ ] Lighthouse score checked (90+)
- [ ] Core Web Vitals monitored
- [ ] Originals backed up
- [ ] Build pipeline automated

## Resources

### Tools
- [sharp](https://sharp.pixelplumbing.com/) - High-performance Node.js image processing
- [ImageMagick](https://imagemagick.org/) - Feature-rich image manipulation
- [Squoosh](https://squoosh.app/) - Google's web-based image optimizer
- [imagemin](https://github.com/imagemin/imagemin) - Image minification for build tools

### Learning
- [web.dev/fast](https://web.dev/fast/) - Web performance best practices
- [MDN: Responsive Images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
- [Addy Osmani: Image Optimization](https://www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/)

### Testing
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Performance auditing
- [WebPageTest](https://www.webpagetest.org/) - Real-world performance testing
- [PageSpeed Insights](https://pagespeed.web.dev/) - Field data + lab data

## Files

- `SKILL.md` - The skill file (copy to `.claude/skills/`)
- `README.md` - This comprehensive documentation

## Related Skills

- **bundle-analyzer** - Optimize JavaScript bundles
- **lighthouse-ci** - Automated performance monitoring
- **lazy-loading-helper** - Implement lazy loading patterns
- **cdn-setup** - Configure CDN for images

---

**Ready to optimize? Your users will thank you for faster page loads!** ⚡
