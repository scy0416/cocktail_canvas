// tailwind.config.cjs
module.exports = {
    content: [
      './src/**/*.{html,js,svelte,ts}', 
      './index.html'
    ],
    theme: {
      extend: {}
    },
    plugins: [
      require('daisyui')
    ]
};