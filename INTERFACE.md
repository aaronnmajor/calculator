# Calculator Interface Layout

This document describes the visual layout of the GUI calculator.

## Display Area
```
┌─────────────────────────────────────┐
│                               123.45│ ← Main display (large, white on black)
│                          123.45 +  │ ← Operation display (smaller, gray)
└─────────────────────────────────────┘
```

## Button Layout
```
┌────────────────────────────────────────────────────────────────┐
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                               │
│  │  C  │ │ CE  │ │  ⌫  │ │  ÷  │  ← Row 1: Clear functions + divide   │
│  └─────┘ └─────┘ └─────┘ └─────┘                               │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                               │
│  │  7  │ │  8  │ │  9  │ │  ×  │  ← Row 2: Numbers 7-9 + multiply     │
│  └─────┘ └─────┘ └─────┘ └─────┘                               │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                               │
│  │  4  │ │  5  │ │  6  │ │  −  │  ← Row 3: Numbers 4-6 + subtract     │
│  └─────┘ └─────┘ └─────┘ └─────┘                               │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                               │
│  │  1  │ │  2  │ │  3  │ │  +  │  ← Row 4: Numbers 1-3 + add          │
│  └─────┘ └─────┘ └─────┘ └─────┘                               │
│  ┌───────────┐ ┌─────┐ ┌─────┐                                 │
│  │     0     │ │  .  │ │  =  │  ← Row 5: Zero (wide), decimal, equals │
│  └───────────┘ └─────┘ └─────┘                                 │
└────────────────────────────────────────────────────────────────┘
```

## Color Scheme

- **Background**: Dark gray/black theme
- **Display**: Black background with white text for main display, gray for operation
- **Number buttons (0-9, .)**: Gray background (#666666) with white text
- **Operation buttons (+, −, ×, ÷)**: Blue background (#4444ff) with white text
- **Clear buttons (C, CE, ⌫)**: Red/pink background (#ff4444, #ff6666) with white text
- **Equals button (=)**: Green background (#44aa44) with white text

## Features

- **Responsive**: Buttons resize with the window
- **Professional appearance**: Clean, modern design
- **Error handling**: Shows error dialogs for invalid operations
- **Operation preview**: Shows current operation in secondary display
- **Number formatting**: Intelligent formatting to avoid unnecessary decimals

## Window Properties

- **Size**: 400×600 pixels
- **Resizable**: No (fixed size for consistent appearance)
- **Title**: "Calculator"