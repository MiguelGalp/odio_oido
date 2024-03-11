/** @type {import('tailwindcss').Config} */

const plugin = require('tailwindcss/plugin');

module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Geist', 'sans-serif'],
      },
      colors: {
        'orange': '#bc5215',
        'red': '#af312a',
        'gray': '#e1dfd1',
        // ... other custom colors
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
      textUnderlineOffset: {
        '3': '2px',
      },
      fontSize: {
        'custom-20': '20px',
        'custom-24': '24px',
        'custom-28': '28px',
        'custom-32': '32px',
        'custom-36': '36px',
        'custom-44': '44px',
      },
      translate: {
        '-178': '-178px',
      },
    },
  },
  plugins: [
    plugin(function({ addUtilities }) {
      const newUtilities = {
        '.underline-thick': {
          position: 'relative',
          '&::after': {
            content: '""',
            position: 'absolute',
            left: '38%', // Adjust this to move the underline to the right
            bottom: '2.5px',
            height: '2px',
            width: '28%', // Adjust this to change the length of the underline
            backgroundColor: 'currentColor',
          },
        },
      };
      addUtilities(newUtilities, ['responsive', 'hover']);
    }),
  ],
}
