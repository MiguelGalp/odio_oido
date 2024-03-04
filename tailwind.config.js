/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {},
    fontFamily: {
      sans: ['Geist', 'sans-serif'],
    },
    colors: {
      'orange': '#bc5215',
      'red': '#af312a',
      'gray': '#e1dfd1',
      // ... other custom colors from your CSS
    },
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '992px',
      'xl': '1024px',
      'xxl': '1200px',
      'xxxl': '1400px',
      // ... other custom screen sizes
    },
  },
  plugins: [],
}

