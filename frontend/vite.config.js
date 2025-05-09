// vite.config.js
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    // ① TailwindCSS Vite 플러그인
    tailwindcss(),
    // ② Svelte (기존 사용하셨던 플러그인)
    svelte(),
  ],
  server: {
    host: '0.0.0.0',
    port: 5173,

    proxy: {
      '/api': {
        target: 'http://localhost:8001',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      }
    }
  },
});
