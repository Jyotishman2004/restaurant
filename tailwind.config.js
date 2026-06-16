/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./*.html"],
  theme: {
    extend: {
      "colors": {
        "surface-container-highest": "#3d3327",
        "on-primary": "#472a00",
        "surface-container": "#271e13",
        "outline": "#9c8e81",
        "on-primary-fixed-variant": "#643f09",
        "on-primary-container": "#4f2f00",
        "on-background": "#f1e0ce",
        "surface-container-high": "#32281d",
        "primary": "#f3bc7d",
        "on-surface-variant": "#d4c4b5",
        "on-surface": "#f1e0ce",
        "on-error": "#690005",
        "secondary-container": "#484a46",
        "on-secondary-fixed-variant": "#454744",
        "outline-variant": "#50453a",
        "tertiary": "#e8bf91",
        "on-tertiary-container": "#4b310f",
        "inverse-primary": "#7f5620",
        "primary-fixed-dim": "#f3bc7d",
        "background": "#1a1208",
        "surface-container-lowest": "#140d04",
        "surface-bright": "#42372b",
        "surface-tint": "#f3bc7d",
        "on-secondary-fixed": "#1a1c19",
        "surface-variant": "#3d3327",
        "tertiary-fixed": "#ffddb8",
        "secondary-fixed-dim": "#c6c7c2",
        "secondary": "#c6c7c2",
        "tertiary-fixed-dim": "#e8bf91",
        "on-tertiary-fixed-variant": "#5d411d",
        "tertiary-container": "#be996d",
        "inverse-surface": "#f1e0ce",
        "on-primary-fixed": "#2b1700",
        "surface-dim": "#1a1208",
        "surface-container-low": "#231a0f",
        "on-tertiary": "#442b09",
        "on-secondary": "#2f312e",
        "secondary-fixed": "#e3e3de",
        "inverse-on-surface": "#392f23",
        "error-container": "#93000a",
        "primary-fixed": "#ffddb9",
        "primary-container": "#c8965a",
        "on-error-container": "#ffdad6",
        "error": "#ffb4ab",
        "surface": "#1a1208",
        "on-tertiary-fixed": "#2a1700",
        "on-secondary-container": "#b8b9b4"
      },
      "borderRadius": {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "full": "9999px"
      },
      "spacing": {
        "margin-desktop": "64px",
        "unit": "8px",
        "container-max": "1200px",
        "section-gap": "128px",
        "margin-mobile": "24px",
        "gutter": "32px"
      },
      "fontFamily": {
        "label-caps": ["Inter", "sans-serif"],
        "headline-sm": ["EB Garamond", "serif"],
        "body-lg": ["Inter", "sans-serif"],
        "headline-md": ["EB Garamond", "serif"],
        "body-md": ["Inter", "sans-serif"],
        "display-lg-mobile": ["EB Garamond", "serif"],
        "display-lg": ["EB Garamond", "serif"]
      },
      "fontSize": {
        "label-caps": ["12px", { "lineHeight": "16px", "letterSpacing": "0.15em", "fontWeight": "600" }],
        "headline-sm": ["24px", { "lineHeight": "32px", "fontWeight": "400" }],
        "body-lg": ["18px", { "lineHeight": "28px", "letterSpacing": "0.01em", "fontWeight": "300" }],
        "headline-md": ["32px", { "lineHeight": "40px", "fontWeight": "400" }],
        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
        "display-lg-mobile": ["40px", { "lineHeight": "48px", "letterSpacing": "-0.01em", "fontWeight": "500" }],
        "display-lg": ["64px", { "lineHeight": "72px", "letterSpacing": "-0.02em", "fontWeight": "500" }]
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
