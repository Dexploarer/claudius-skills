---
name: file-organizer
description: Organizes files by type into categorized folders. Use when user asks to "organize files", "sort files by type", "clean up this directory", or "categorize these files".
allowed-tools: [Read, Bash, Glob]
---

# File Organizer Skill

Automatically organizes files into folders by type, making directories cleaner and easier to navigate.

## When to Use

This skill activates when the user wants to organize files:
- "Organize files in this directory"
- "Sort these files by type"
- "Clean up my Downloads folder"
- "Categorize files into folders"
- "Organize my project files"

## Instructions

### Step 1: Analyze the Directory

First, scan the target directory to understand what files are present:
- List all files
- Identify file types
- Count files per category
- Note any existing organization

### Step 2: Determine Organization Strategy

**By File Type (Default):**
```
Images/     - .jpg, .png, .gif, .svg, .webp, .ico
Documents/  - .pdf, .doc, .docx, .txt, .md, .rtf
Videos/     - .mp4, .avi, .mov, .mkv, .webm
Audio/      - .mp3, .wav, .flac, .m4a, .ogg
Archives/   - .zip, .tar, .gz, .rar, .7z
Code/       - .js, .py, .java, .cpp, .html, .css
Data/       - .json, .xml, .csv, .yaml, .sql
Executables/ - .exe, .app, .dmg, .deb
Others/     - Everything else
```

**Alternative Strategies:**
- By project (group related files)
- By date (today, this week, this month, older)
- By size (small, medium, large)
- Custom categories

### Step 3: Ask for Confirmation

**IMPORTANT:** Always confirm before moving files!

Show the user:
- What files will be moved
- Where they will go
- How many files in each category

Example:
```
I'll organize 47 files into the following structure:

📁 Images/ (12 files)
   - photo1.jpg, screenshot.png, logo.svg, ...

📁 Documents/ (15 files)
   - report.pdf, notes.txt, readme.md, ...

📁 Videos/ (5 files)
   - tutorial.mp4, demo.mov, ...

📁 Code/ (8 files)
   - script.js, app.py, style.css, ...

📁 Archives/ (3 files)
   - backup.zip, data.tar.gz, ...

📁 Others/ (4 files)
   - unknown.xyz, file.tmp, ...

Proceed with organization? (y/n)
```

Wait for user confirmation before proceeding.

### Step 4: Create Folders and Move Files

Only after confirmation:
1. Create category folders if they don't exist
2. Move files to appropriate folders
3. Handle naming conflicts (don't overwrite)
4. Keep track of what was moved

### Step 5: Report Results

Show what was done:
```
✅ Organization complete!

Moved 47 files:
- 12 images → Images/
- 15 documents → Documents/
- 5 videos → Videos/
- 8 code files → Code/
- 3 archives → Archives/
- 4 others → Others/

Your directory is now organized!
```

## File Type Categories

### Images
```
.jpg, .jpeg, .png, .gif, .svg, .webp, .bmp, .ico, .tiff
```

### Documents
```
.pdf, .doc, .docx, .txt, .md, .rtf, .odt, .pages
```

### Spreadsheets
```
.xlsx, .xls, .csv, .ods, .numbers
```

### Presentations
```
.ppt, .pptx, .key, .odp
```

### Videos
```
.mp4, .avi, .mov, .mkv, .webm, .flv, .wmv, .m4v
```

### Audio
```
.mp3, .wav, .flac, .m4a, .ogg, .wma, .aac
```

### Archives
```
.zip, .tar, .gz, .rar, .7z, .bz2, .xz
```

### Code/Development
```
.js, .ts, .py, .java, .cpp, .c, .h, .cs, .rb, .go, .rs, .php, .swift
```

### Web Files
```
.html, .css, .scss, .sass, .less, .jsx, .tsx, .vue
```

### Data Files
```
.json, .xml, .yaml, .yml, .toml, .ini, .sql, .db
```

### Executables
```
.exe, .app, .dmg, .deb, .rpm, .msi, .sh, .bat
```

## Examples

### Example 1: Basic Organization

**User:** "Organize the files in my Downloads folder"

**Response:**
```
Analyzing Downloads folder...

Found 23 files:
- 8 images (jpg, png)
- 6 PDFs
- 3 zip files
- 4 videos (mp4)
- 2 other files

I'll organize them like this:

📁 Images/ (8 files)
   - vacation-photo.jpg
   - screenshot-2024.png
   - logo-design.png
   [... 5 more]

📁 Documents/ (6 files)
   - invoice-march.pdf
   - book-chapter.pdf
   [... 4 more]

📁 Archives/ (3 files)
   - project-backup.zip
   - photos.zip
   - code-samples.zip

📁 Videos/ (4 files)
   - tutorial.mp4
   - meeting-recording.mp4
   [... 2 more]

📁 Others/ (2 files)
   - data.tmp
   - notes.unknown

Proceed with this organization? (Type 'yes' to confirm)
```

### Example 2: Custom Categories

**User:** "Organize files but put all media (images and videos) together"

**Response:**
```
Analyzing directory with custom categories...

I'll use these categories:
- Media/ (images + videos)
- Documents/ (all documents)
- Code/ (development files)
- Archives/ (compressed files)
- Others/

Found 34 files:

📁 Media/ (15 files)
   Images: photo1.jpg, graphic.png, logo.svg
   Videos: clip.mp4, demo.mov

📁 Documents/ (12 files)
   - report.pdf, notes.txt, readme.md, ...

📁 Code/ (5 files)
   - app.js, styles.css, index.html, ...

📁 Archives/ (2 files)
   - backup.zip, files.tar.gz

Proceed? (yes/no)
```

### Example 3: Handle Conflicts

**User:** "Organize this folder"

**Response:**
```
Analyzing folder...

⚠️  Note: Some folders already exist
- Images/ folder exists with 5 files
- Documents/ folder exists with 3 files

I'll move files without overwriting existing ones.
If a file with the same name exists, I'll rename it:
- photo.jpg → photo-2.jpg (if photo.jpg exists)

Planning to organize 20 new files:

📁 Images/ (7 new files)
   Will be added to existing Images/ folder

📁 Documents/ (8 new files)
   Will be added to existing Documents/ folder

📁 Videos/ (5 new files)
   New folder will be created

Proceed? (yes/no)
```

## Safety Features

### Always Confirm First
Never move files without user approval:
```yaml
Before moving files:
1. Show what will be moved
2. Show where it will go
3. Warn about conflicts
4. Wait for confirmation
```

### Handle Naming Conflicts
If file already exists:
```bash
# Don't overwrite!
# Instead, rename: file.txt → file-2.txt
```

### Preserve File Integrity
- Don't modify file contents
- Keep file permissions
- Maintain timestamps
- Don't corrupt files

### Provide Undo Information
After organizing, note:
```
To undo this organization:
1. Select all files in subdirectories
2. Move them back to parent directory
3. Delete empty folders

Or use: /undo-organization command
```

## Tips

### For Best Results
- Work on one directory at a time
- Back up important files first
- Test with a small folder first
- Review the plan before confirming

### For Custom Organization
Tell the skill your preferences:
- "Put code and web files together"
- "Create a folder for work documents"
- "Keep all media files in one place"

### For Large Directories
- Organize by date first, then by type
- Consider creating subfolders
- May want to organize in stages

## Common Use Cases

### Downloads Folder
```
Organize by type, move old files to archive
```

### Project Directory
```
Organize by function: source/, tests/, docs/, configs/
```

### Media Collection
```
Organize photos by date, videos by type
```

### Work Files
```
Organize by project or client
```

## Bash Commands Used

### List files:
```bash
ls -la
```

### Create folder:
```bash
mkdir -p "FolderName"
```

### Move files:
```bash
mv "source.ext" "Destination/source.ext"
```

### Handle conflicts:
```bash
# Check if file exists before moving
if [ -f "Destination/file.ext" ]; then
  mv "file.ext" "Destination/file-2.ext"
else
  mv "file.ext" "Destination/file.ext"
fi
```

## Edge Cases

### Empty Directory
```
✨ This directory is already clean! No files to organize.
```

### All Files Same Type
```
All 15 files are images. Would you like to:
1. Organize by date
2. Organize by size
3. Leave as is
```

### Hidden Files
```
Found 3 hidden files (.env, .gitignore, .config)
These are typically important config files.
Organize them? (yes/no/skip)
```

### Symbolic Links
```
⚠️  Found 2 symbolic links
Moving these could break links. Recommended action:
- Skip symbolic links
- Leave in original location
```

## Remember

- **Always ask permission**: Never move files without confirmation
- **Show the plan**: User should know exactly what will happen
- **Handle conflicts**: Don't overwrite existing files
- **Be safe**: Preserve file integrity
- **Provide context**: Explain what you're doing and why
- **Make it reversible**: Provide undo instructions
