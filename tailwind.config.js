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
        'custom-16': '16px',
        'custom-20': '20px',
        'custom-24': '24px',
        'custom-28': '28px',
        'custom-32': '32px',
        'custom-36': '36px',
        'custom-40': '40px',
        'custom-44': '44px',
        'custom-48': '48px',
        'custom-52': '52px',
        'custom-56': '56px',
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
            left: '20%', // Adjust this to move the underline to the right
            bottom: '2.5px',
            height: '3px',
            width: '58%', // Adjust this to change the length of the underline
            backgroundColor: 'currentColor',
            zIndex: '10',
          },
        },
        '.bg-switch-mobile': {
          position: 'relative',
          '&::after': {
            content: '""',
            position: 'absolute',
            backgroundColor: 'rgb(253,255,10)',
            height: '64px',
            width: '64px',
            borderRadius: '9999px',
            zIndex: '-2',
            bottom: 'calc(100% - 45px)',
            left: 'calc(50% - 32px + 2px)',
          },
        },
        '.speech-bubble-text': {
          transform: 'perspective(500px) rotateY(10deg) rotateX(5deg) skew(-20deg, 5deg)',
          transformOrigin: 'left bottom' /* Adjust the origin of transformation if needed */
        },
      };
      addUtilities(newUtilities, ['responsive', 'hover']);
    }),
  ],
}
