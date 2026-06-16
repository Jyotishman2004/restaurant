---
name: Ember & Grain Aesthetic
colors:
  surface: '#1a1208'
  surface-dim: '#1a1208'
  surface-bright: '#42372b'
  surface-container-lowest: '#140d04'
  surface-container-low: '#231a0f'
  surface-container: '#271e13'
  surface-container-high: '#32281d'
  surface-container-highest: '#3d3327'
  on-surface: '#f1e0ce'
  on-surface-variant: '#d4c4b5'
  inverse-surface: '#f1e0ce'
  inverse-on-surface: '#392f23'
  outline: '#9c8e81'
  outline-variant: '#50453a'
  surface-tint: '#f3bc7d'
  primary: '#f3bc7d'
  on-primary: '#472a00'
  primary-container: '#c8965a'
  on-primary-container: '#4f2f00'
  inverse-primary: '#7f5620'
  secondary: '#c6c7c2'
  on-secondary: '#2f312e'
  secondary-container: '#484a46'
  on-secondary-container: '#b8b9b4'
  tertiary: '#e8bf91'
  on-tertiary: '#442b09'
  tertiary-container: '#be996d'
  on-tertiary-container: '#4b310f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb9'
  primary-fixed-dim: '#f3bc7d'
  on-primary-fixed: '#2b1700'
  on-primary-fixed-variant: '#643f09'
  secondary-fixed: '#e3e3de'
  secondary-fixed-dim: '#c6c7c2'
  on-secondary-fixed: '#1a1c19'
  on-secondary-fixed-variant: '#454744'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#e8bf91'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#5d411d'
  background: '#1a1208'
  on-background: '#f1e0ce'
  surface-variant: '#3d3327'
typography:
  display-lg:
    fontFamily: ebGaramond
    fontSize: 64px
    fontWeight: '500'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: ebGaramond
    fontSize: 40px
    fontWeight: '500'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-sm:
    fontFamily: ebGaramond
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 32px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '300'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 32px
  margin-desktop: 64px
  margin-mobile: 24px
  section-gap: 128px
---

## Brand & Style

The brand personality of this design system is defined by "Quiet Luxury"—an aesthetic that prioritizes quality, heritage, and restraint over ostentation. It targets a discerning audience seeking an immersive, high-end culinary experience. The UI evokes a sense of intimacy and warmth, mirroring the atmosphere of a dimly lit, exclusive dining room.

The design style is a blend of **Minimalism** and **High-Contrast Dark Mode**. It utilizes expansive whitespace (or "dark space") to create a breathing room that signals exclusivity. Visual elements are sparse but intentional, favoring razor-sharp precision and a tactile, editorial layout that feels more like a curated tasting menu than a digital interface.

## Colors

The palette is rooted in the "Midnight Wood" background, a deep, warm black that provides a canvas for the "Spiced Gold" primary accents. 

- **Primary (Spiced Gold):** Used for key calls to action, active states, and decorative flourishes. It represents the "Ember."
- **Secondary (Ivory):** Used for primary body text and high-level headings to ensure maximum legibility against the dark void.
- **Tertiary (Muted Gold):** A desaturated gold used for secondary information and subtle borders.
- **Neutral (Midnight Wood):** The foundational surface color, creating a seamless, immersive dark environment.

## Typography

This design system employs a sophisticated typographic pairing to balance heritage with modern utility. 

**ebGaramond** is the voice of the brand. It is used for all display and headline roles. Large-scale headings should utilize the medium weight with slight negative letter-spacing to create a tight, elegant "editorial" feel. 

**Inter** serves as the functional workhorse. By using it in lighter weights (300-400) for body copy, the UI remains legible and contemporary. The `label-caps` style is essential for navigation items and small UI metadata, using wide letter-spacing to maintain a premium, architectural look.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop to mimic the centered, intentional composition of a printed menu. The layout is anchored by a 12-column grid with generous 32px gutters.

Exclusivity is communicated through "excessive" vertical spacing. Section gaps are intentionally large (128px+) to force the user to slow down and appreciate each piece of content. On mobile, margins remain generous at 24px to ensure content never feels crowded against the edge of the device, maintaining the "gallery" feel even on small screens.

## Elevation & Depth

In a dark, luxury environment, traditional drop shadows are replaced by **Tonal Layers** and **Low-Contrast Outlines**. 

Depth is achieved by subtly shifting the surface color from #1A1208 to a slightly lighter "Charcoal" for elevated containers like cards or menus. Borders are used sparingly; when present, they should be 0.5px or 1px wide in a muted gold with 20-30% opacity. This creates a "glass-like" structure without the blur, focusing on the sharpness of the lines. Subtle, large-radius radial gradients (glows) in Spiced Gold can be used behind key imagery to simulate the warmth of a hearth.

## Shapes

This design system utilizes **Sharp (0)** roundedness. 

Sharp corners convey a sense of precision, architectural rigor, and bespoke tailoring. Buttons, input fields, and image containers should all feature 90-degree angles. This rejection of "bubbly" or "soft" UI elements reinforces the professional, high-end nature of the culinary brand.

## Components

### Buttons
Primary buttons are rectangular with a 1px Spiced Gold border. The label uses `label-caps` typography. Hover states involve a subtle gold fill with ivory text, transitioning smoothly to simulate a lighting effect.

### Cards
Cards for menu items or event showcases feature no background fill or shadows. Instead, they rely on a single 1px bottom border or a very thin surrounding outline. Images within cards should have a slight desaturation to match the brand mood.

### Input Fields
Minimalist underlines are preferred over boxed inputs. The label sits above in `label-caps`, and the active state is indicated by the underline thickening slightly and changing to Spiced Gold.

### Navigation
The navigation is centered and sparse. Links are separated by significant horizontal padding. A "Reservation" CTA is always present, styled as a Ghost Button to remain secondary to the content until needed.

### List Items
Menu lists should utilize "dotted leaders" (periods connecting the item name to the price) to evoke classic fine-dining menu aesthetics, rendered in 30% opacity ivory.