---
name: image-optimizer
description: Optimizes images for web performance by converting to modern formats, compressing, and generating responsive sizes. Use when user asks to "optimize images", "compress images", "convert to webp", or mentions image performance.
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

# Image Optimization Helper

Optimizes images for web performance using modern formats and compression techniques.

## When to Use

- "Optimize these images"
- "Compress images for web"
- "Convert images to WebP"
- "Reduce image file sizes"
- "Make images load faster"
- "Generate responsive image sizes"

## Instructions

### 1. Analyze Current Images

First, scan for images in the project:

```bash
# Find all images
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \)
```

Present findings:
- Total number of images
- Current formats
- Total size
- Largest images
- Optimization opportunities

### 2. Check for Optimization Tools

Verify available tools:

```bash
# Check for ImageMagick
which convert || echo "ImageMagick not found"

# Check for cwebp (WebP encoder)
which cwebp || echo "cwebp not found"

# Check for sharp-cli (if Node.js project)
which sharp || echo "sharp not found"
```

**If tools missing**, provide installation instructions:

```bash
# macOS
brew install imagemagick webp

# Ubuntu/Debian
apt-get install imagemagick webp

# Node.js projects (recommended)
npm install -g sharp-cli
```

### 3. Create Optimization Plan

Present optimization strategy:

**For WebP Conversion:**
```bash
# Convert JPG/PNG to WebP with 80% quality
cwebp -q 80 input.jpg -o input.webp
```

**For PNG Optimization:**
```bash
# Compress PNG without quality loss
convert input.png -strip -quality 85 output.png
```

**For JPEG Optimization:**
```bash
# Optimize JPEG with progressive loading
convert input.jpg -strip -interlace Plane -quality 85 output.jpg
```

**For Responsive Sizes:**
```bash
# Generate multiple sizes (sharp-cli)
sharp -i input.jpg -o output-{width}.jpg resize 320 480 768 1024 1920
```

### 4. Get User Confirmation

Present plan with:
- Number of images to optimize
- Target formats
- Estimated size reduction
- Whether to keep originals
- Whether to generate responsive sizes

Wait for explicit confirmation before proceeding.

### 5. Execute Optimization

Create organized output structure:

```bash
# Backup originals
mkdir -p images/original
cp images/*.{jpg,png} images/original/

# Create optimized versions
mkdir -p images/optimized
```

Process each image with progress updates.

### 6. Generate Picture Elements (Optional)

For HTML projects, offer to generate `<picture>` elements:

```html
<picture>
  <source
    srcset="image-320.webp 320w,
            image-768.webp 768w,
            image-1920.webp 1920w"
    type="image/webp"
  />
  <source
    srcset="image-320.jpg 320w,
            image-768.jpg 768w,
            image-1920.jpg 1920w"
    type="image/jpeg"
  />
  <img
    src="image-768.jpg"
    alt="Description"
    loading="lazy"
    width="768"
    height="432"
  />
</picture>
```

### 7. Update Configuration Files

**For Next.js projects**, suggest image configuration:

```javascript
// next.config.js
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
}
```

**For Gatsby projects**, suggest gatsby-plugin-image setup.

**For vanilla projects**, suggest lazy loading:

```javascript
// Lazy load images
if ('loading' in HTMLImageElement.prototype) {
  // Browser supports native lazy loading
  document.querySelectorAll('img[loading="lazy"]').forEach(img => {
    img.src = img.dataset.src;
  });
} else {
  // Use IntersectionObserver polyfill
  const images = document.querySelectorAll('img[data-src]');
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        imageObserver.unobserve(img);
      }
    });
  });
  images.forEach(img => imageObserver.observe(img));
}
```

### 8. Report Results

Show final metrics:
- Images optimized: X
- Original size: X MB
- Optimized size: X MB
- Reduction: X% (X MB saved)
- Formats generated: WebP, AVIF, etc.
- Responsive sizes created: 320w, 768w, 1920w

### 9. Suggest Next Steps

Recommend:
- Adding images to .gitignore (originals)
- Setting up build pipeline for automatic optimization
- Implementing lazy loading
- Using CDN for image delivery
- Monitoring performance impact (Lighthouse)

## Optimization Guidelines

### Quality Settings

**JPEG:**
- Photos: 80-85 quality
- UI elements: 90 quality
- Background images: 75 quality

**PNG:**
- Icons: Keep lossless
- Screenshots: 85 quality
- Logos: Keep lossless if transparency needed

**WebP:**
- Photos: 80 quality (excellent compression)
- Graphics: 85 quality
- Transparent images: 90 quality

### Format Selection

**Use WebP when:**
- Browser support is adequate (95%+ as of 2024)
- File size matters most
- Quality/size ratio is important

**Use AVIF when:**
- Cutting-edge optimization needed
- Supporting modern browsers only
- 20-50% better than WebP

**Keep JPEG/PNG when:**
- Legacy browser support required
- As fallback in `<picture>` element
- Tools don't support modern formats

### Responsive Breakpoints

Common breakpoints:
- 320w: Mobile portrait
- 480w: Mobile landscape
- 768w: Tablet
- 1024w: Small desktop
- 1920w: Full HD
- 2560w: Retina displays

### Size Limits

Target sizes:
- Hero images: < 200 KB
- Content images: < 100 KB
- Thumbnails: < 30 KB
- Icons: < 10 KB
- Background images: < 150 KB

## Safety Practices

### Always Backup
```bash
# Create backup before optimization
mkdir -p backups/$(date +%Y%m%d)
cp -r images/ backups/$(date +%Y%m%d)/
```

### Preserve Originals
- Keep original files in separate directory
- Use version control for safety
- Test optimized images before deployment

### Verify Results
- Compare visual quality
- Check file sizes
- Test on different devices
- Validate responsive behavior

### Handle Errors
```bash
# Check if conversion succeeded
if [ $? -eq 0 ]; then
  echo "✅ Optimized successfully"
else
  echo "❌ Optimization failed, keeping original"
fi
```

## Advanced Features

### Batch Processing Script

Offer to create optimization script:

```bash
#!/bin/bash
# optimize-images.sh

set -e

INPUT_DIR=${1:-.}
OUTPUT_DIR="optimized"
QUALITY=80

mkdir -p "$OUTPUT_DIR"

echo "🖼️  Optimizing images in $INPUT_DIR..."

# Process JPEGs
for img in "$INPUT_DIR"/*.{jpg,jpeg,JPG,JPEG}; do
  [ -f "$img" ] || continue
  filename=$(basename "$img" | sed 's/\.[^.]*$//')

  # Original format
  convert "$img" -strip -interlace Plane -quality $QUALITY \
    "$OUTPUT_DIR/${filename}.jpg"

  # WebP format
  cwebp -q $QUALITY "$img" -o "$OUTPUT_DIR/${filename}.webp"

  echo "✅ $filename"
done

# Process PNGs
for img in "$INPUT_DIR"/*.{png,PNG}; do
  [ -f "$img" ] || continue
  filename=$(basename "$img" | sed 's/\.[^.]*$//')

  # Optimize PNG
  convert "$img" -strip -quality 85 "$OUTPUT_DIR/${filename}.png"

  # WebP with alpha
  cwebp -q $QUALITY -lossless "$img" -o "$OUTPUT_DIR/${filename}.webp"

  echo "✅ $filename"
done

echo "🎉 Optimization complete!"
echo "📊 Space saved:"
du -sh "$INPUT_DIR"
du -sh "$OUTPUT_DIR"
```

### Git Integration

Suggest adding to .gitignore:

```gitignore
# Original unoptimized images
images/original/
*-original.jpg
*-original.png

# Large image files
*.jpg filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
```

Or suggest Git LFS for large images:

```bash
# Install Git LFS
git lfs install

# Track large images
git lfs track "*.jpg"
git lfs track "*.png"

# Add to repo
git add .gitattributes
```

### CI/CD Integration

For automated optimization in build pipeline:

**GitHub Actions:**
```yaml
name: Optimize Images

on:
  pull_request:
    paths:
      - 'images/**'

jobs:
  optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Install tools
        run: |
          sudo apt-get install -y imagemagick webp

      - name: Optimize images
        run: |
          chmod +x scripts/optimize-images.sh
          ./scripts/optimize-images.sh images

      - name: Commit optimized images
        run: |
          git config --local user.name "Image Optimizer Bot"
          git add images/optimized
          git commit -m "chore: optimize images"
          git push
```

## Performance Impact

### Lighthouse Metrics

Optimized images improve:
- **LCP (Largest Contentful Paint)**: 20-40% improvement
- **Total Page Size**: 50-70% reduction in image weight
- **Time to Interactive**: Faster due to smaller payloads
- **Performance Score**: +10 to +30 points

### Real-World Examples

**Before optimization:**
- hero-image.jpg: 2.4 MB
- product-1.png: 890 KB
- background.jpg: 1.6 MB
- Total: 4.89 MB

**After optimization:**
- hero-image.webp: 380 KB (84% reduction)
- product-1.webp: 125 KB (86% reduction)
- background.webp: 240 KB (85% reduction)
- Total: 745 KB (85% total reduction)

### Mobile Impact

On 3G connection:
- Before: 12-15 seconds load time
- After: 2-3 seconds load time
- **4-5x faster page loads**

## Best Practices

1. ✅ **Always provide WebP fallback to JPEG/PNG**
2. ✅ **Use lazy loading for below-fold images**
3. ✅ **Specify width and height to prevent layout shift**
4. ✅ **Use responsive images with srcset**
5. ✅ **Compress images during build, not runtime**
6. ✅ **Serve images from CDN when possible**
7. ✅ **Monitor image performance with RUM tools**
8. ✅ **Set appropriate cache headers for images**

## Common Pitfalls

❌ **Over-optimization**: Quality too low (< 70)
❌ **Under-optimization**: Quality too high (> 95)
❌ **No fallbacks**: Only serving WebP without JPEG/PNG
❌ **Wrong format**: Using PNG for photos
❌ **Missing dimensions**: Causing layout shift
❌ **No lazy loading**: Loading all images immediately
❌ **Single size**: Not using responsive images

## Framework-Specific Guidance

### React/Next.js
```jsx
import Image from 'next/image'

<Image
  src="/images/hero.jpg"
  alt="Hero image"
  width={1920}
  height={1080}
  priority  // For LCP images
  placeholder="blur"
/>
```

### Gatsby
```jsx
import { StaticImage } from "gatsby-plugin-image"

<StaticImage
  src="../images/hero.jpg"
  alt="Hero image"
  placeholder="blurred"
  layout="fullWidth"
/>
```

### Vue/Nuxt
```vue
<nuxt-img
  src="/images/hero.jpg"
  alt="Hero image"
  width="1920"
  height="1080"
  format="webp"
  loading="lazy"
/>
```

## Tools Reference

- **ImageMagick**: Swiss army knife for image manipulation
- **cwebp/dwebp**: Google's WebP encoder/decoder
- **avifenc**: AVIF encoder
- **sharp**: Fast Node.js image processing
- **squoosh-cli**: Google's web-based optimizer CLI
- **imagemin**: Node.js image minification
