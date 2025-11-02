# WebAssembly Performance Optimizer

**Category:** WebAssembly & High-Performance Computing
**Level:** Advanced
**Auto-trigger:** When user mentions WebAssembly, WASM, performance optimization, or near-native browser performance

---

## Description

Optimizes applications for WebAssembly compilation, including Rust/Go/C++ to WASM compilation, WASM binary size optimization, JavaScript-WASM interop, and browser performance tuning for compute-intensive tasks.

---

## Activation Phrases

- "Compile to WebAssembly"
- "Optimize WASM performance"
- "Set up Rust to WASM"
- "Create WASM module"
- "Optimize WASM binary size"
- "Configure wasm-pack"
- "Set up AssemblyScript"

---

## What This Skill Does

1. **Set up WASM Toolchain**
   - Configure Rust/wasm-pack
   - Set up AssemblyScript
   - Configure Emscripten (C/C++)
   - Set up TinyGo for WASM

2. **Optimize WASM Compilation**
   - Minimize binary size
   - Configure optimization levels
   - Strip unnecessary exports
   - Implement lazy loading

3. **JavaScript Interop**
   - Create efficient bindings
   - Optimize memory management
   - Handle async operations
   - Implement worker threads

4. **Performance Tuning**
   - Benchmark WASM vs JS
   - Profile memory usage
   - Optimize hot paths
   - Configure SIMD

---

## Code Examples

### Example 1: Rust to WebAssembly (Image Processing)

```rust
// lib.rs - Rust WASM module for image processing
use wasm_bindgen::prelude::*;
use web_sys::console;

#[wasm_bindgen]
pub struct ImageProcessor {
    width: u32,
    height: u32,
    data: Vec<u8>,
}

#[wasm_bindgen]
impl ImageProcessor {
    /// Create new image processor
    #[wasm_bindgen(constructor)]
    pub fn new(width: u32, height: u32) -> ImageProcessor {
        console::log_1(&"ImageProcessor initialized".into());

        ImageProcessor {
            width,
            height,
            data: vec![0; (width * height * 4) as usize],
        }
    }

    /// Apply grayscale filter (optimized WASM)
    #[wasm_bindgen]
    pub fn grayscale(&mut self, image_data: &[u8]) -> Vec<u8> {
        let mut result = vec![0u8; image_data.len()];

        for i in (0..image_data.len()).step_by(4) {
            let r = image_data[i] as f32;
            let g = image_data[i + 1] as f32;
            let b = image_data[i + 2] as f32;
            let a = image_data[i + 3];

            // Luminosity method
            let gray = (0.21 * r + 0.72 * g + 0.07 * b) as u8;

            result[i] = gray;
            result[i + 1] = gray;
            result[i + 2] = gray;
            result[i + 3] = a;
        }

        result
    }

    /// Apply blur filter (compute-intensive)
    #[wasm_bindgen]
    pub fn blur(&self, image_data: &[u8], radius: u32) -> Vec<u8> {
        let mut result = image_data.to_vec();
        let width = self.width as i32;
        let height = self.height as i32;

        for y in 0..height {
            for x in 0..width {
                let mut r_sum = 0f32;
                let mut g_sum = 0f32;
                let mut b_sum = 0f32;
                let mut count = 0;

                for dy in -(radius as i32)..=(radius as i32) {
                    for dx in -(radius as i32)..=(radius as i32) {
                        let nx = x + dx;
                        let ny = y + dy;

                        if nx >= 0 && nx < width && ny >= 0 && ny < height {
                            let idx = ((ny * width + nx) * 4) as usize;
                            r_sum += image_data[idx] as f32;
                            g_sum += image_data[idx + 1] as f32;
                            b_sum += image_data[idx + 2] as f32;
                            count += 1;
                        }
                    }
                }

                let idx = ((y * width + x) * 4) as usize;
                result[idx] = (r_sum / count as f32) as u8;
                result[idx + 1] = (g_sum / count as f32) as u8;
                result[idx + 2] = (b_sum / count as f32) as u8;
            }
        }

        result
    }

    /// Edge detection (Sobel operator)
    #[wasm_bindgen]
    pub fn edge_detect(&self, image_data: &[u8]) -> Vec<u8> {
        let width = self.width as i32;
        let height = self.height as i32;
        let mut result = vec![0u8; image_data.len()];

        // Sobel kernels
        let gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]];
        let gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]];

        for y in 1..height - 1 {
            for x in 1..width - 1 {
                let mut sum_x = 0f32;
                let mut sum_y = 0f32;

                for ky in -1..=1 {
                    for kx in -1..=1 {
                        let idx = (((y + ky) * width + (x + kx)) * 4) as usize;
                        let pixel = image_data[idx] as f32;

                        sum_x += pixel * gx[(ky + 1) as usize][(kx + 1) as usize] as f32;
                        sum_y += pixel * gy[(ky + 1) as usize][(kx + 1) as usize] as f32;
                    }
                }

                let magnitude = (sum_x.powi(2) + sum_y.powi(2)).sqrt();
                let edge = magnitude.min(255.0) as u8;

                let idx = ((y * width + x) * 4) as usize;
                result[idx] = edge;
                result[idx + 1] = edge;
                result[idx + 2] = edge;
                result[idx + 3] = 255;
            }
        }

        result
    }
}

// Cargo.toml
/*
[package]
name = "image-processor-wasm"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2"
web-sys = { version = "0.3", features = ["console"] }

[profile.release]
opt-level = "z"     # Optimize for size
lto = true         # Link-time optimization
codegen-units = 1  # Better optimization
panic = "abort"    # Smaller binary
strip = true       # Strip symbols
*/
```

### Example 2: JavaScript WASM Integration

```typescript
// wasm-worker.ts
/**
 * Web Worker for WASM computation
 * Keeps UI thread responsive
 */

let wasmModule: any = null;

// Load WASM module
self.onmessage = async (e) => {
  const { type, payload } = e.data;

  try {
    // Initialize WASM on first use
    if (!wasmModule && type !== 'init') {
      const wasm = await import('./pkg/image_processor_wasm');
      await wasm.default(); // Initialize
      wasmModule = wasm;
    }

    switch (type) {
      case 'init':
        const wasm = await import('./pkg/image_processor_wasm');
        await wasm.default();
        wasmModule = wasm;
        self.postMessage({ type: 'ready' });
        break;

      case 'grayscale':
        const grayscaleResult = processGrayscale(payload);
        self.postMessage({ type: 'result', data: grayscaleResult }, [grayscaleResult.buffer]);
        break;

      case 'blur':
        const blurResult = processBlur(payload);
        self.postMessage({ type: 'result', data: blurResult }, [blurResult.buffer]);
        break;

      case 'edge':
        const edgeResult = processEdgeDetection(payload);
        self.postMessage({ type: 'result', data: edgeResult }, [edgeResult.buffer]);
        break;

      default:
        self.postMessage({ type: 'error', message: `Unknown type: ${type}` });
    }
  } catch (error) {
    self.postMessage({ type: 'error', message: error.message });
  }
};

function processGrayscale(payload: any): Uint8ClampedArray {
  const { imageData, width, height } = payload;
  const processor = new wasmModule.ImageProcessor(width, height);
  const result = processor.grayscale(imageData);
  processor.free(); // Free WASM memory
  return new Uint8ClampedArray(result);
}

function processBlur(payload: any): Uint8ClampedArray {
  const { imageData, width, height, radius } = payload;
  const processor = new wasmModule.ImageProcessor(width, height);
  const result = processor.blur(imageData, radius);
  processor.free();
  return new Uint8ClampedArray(result);
}

function processEdgeDetection(payload: any): Uint8ClampedArray {
  const { imageData, width, height } = payload;
  const processor = new wasmModule.ImageProcessor(width, height);
  const result = processor.edge_detect(imageData);
  processor.free();
  return new Uint8ClampedArray(result);
}
```

```typescript
// wasm-client.ts
/**
 * Client-side WASM usage
 */

class WASMImageProcessor {
  private worker: Worker;
  private ready: boolean = false;

  constructor() {
    this.worker = new Worker(new URL('./wasm-worker.ts', import.meta.url), {
      type: 'module'
    });

    // Initialize worker
    this.worker.postMessage({ type: 'init' });

    this.worker.onmessage = (e) => {
      if (e.data.type === 'ready') {
        this.ready = true;
        console.log('WASM module loaded and ready');
      }
    };
  }

  async processImage(
    imageData: ImageData,
    filter: 'grayscale' | 'blur' | 'edge',
    options?: { radius?: number }
  ): Promise<ImageData> {

    if (!this.ready) {
      throw new Error('WASM module not ready');
    }

    return new Promise((resolve, reject) => {
      this.worker.onmessage = (e) => {
        if (e.data.type === 'result') {
          const result = new ImageData(
            e.data.data,
            imageData.width,
            imageData.height
          );
          resolve(result);
        } else if (e.data.type === 'error') {
          reject(new Error(e.data.message));
        }
      };

      // Transfer imageData buffer for zero-copy
      this.worker.postMessage(
        {
          type: filter,
          payload: {
            imageData: imageData.data,
            width: imageData.width,
            height: imageData.height,
            ...options
          }
        },
        [imageData.data.buffer]
      );
    });
  }

  terminate() {
    this.worker.terminate();
  }
}

// Usage
const processor = new WASMImageProcessor();

// Get image from canvas
const canvas = document.querySelector('canvas')!;
const ctx = canvas.getContext('2d')!;
const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);

// Process with WASM (runs in worker, non-blocking)
const processed = await processor.processImage(imageData, 'grayscale');

// Draw result
ctx.putImageData(processed, 0, 0);
```

---

## Build Configuration

```json
{
  "name": "wasm-app",
  "version": "1.0.0",
  "scripts": {
    "build:wasm": "wasm-pack build --target web --out-dir pkg",
    "build:wasm:release": "wasm-pack build --target web --out-dir pkg --release",
    "optimize": "wasm-opt -Oz -o pkg/optimized_bg.wasm pkg/*_bg.wasm",
    "size": "ls -lh pkg/*.wasm"
  },
  "devDependencies": {
    "wasm-pack": "^0.12.0"
  }
}
```

---

## Best Practices

1. **Minimize Binary Size**
   - Use `opt-level = "z"` in release mode
   - Enable LTO and strip symbols
   - Run wasm-opt for additional optimization

2. **Optimize Memory**
   - Free WASM objects when done
   - Use typed arrays for data transfer
   - Minimize JS-WASM crossings

3. **Use Web Workers**
   - Keep WASM computation off main thread
   - Use transferable objects for zero-copy
   - Initialize WASM once, reuse many times

4. **Profile Performance**
   - Benchmark WASM vs native JS
   - Use browser DevTools for profiling
   - Optimize hot paths first

---

## Common Pitfalls

❌ **Frequent JS-WASM Crossings**
```typescript
for (let i = 0; i < 1000; i++) {
  wasmModule.process(i); // 1000 boundary crossings!
}
```

✅ **Batch Processing**
```typescript
// Process entire array in WASM
wasmModule.processBatch(dataArray);
```

---

**Last Updated:** 2025-11-02
**Version:** 1.0.0
