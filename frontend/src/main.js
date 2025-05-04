// src/main.js
import './app.css';        // 반드시 가장 먼저 import
import { mount } from 'svelte';
import App from './App.svelte';

mount(App, { target: document.body });
export default App;
