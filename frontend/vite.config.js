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
  ]
});
