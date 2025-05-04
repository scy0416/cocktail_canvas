<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';
  import About from './routes/About.svelte';
  import DaisyTest from './routes/DaisyTest.svelte';
  import NotFound from './routes/NotFound.svelte';
  import { link } from 'svelte-spa-router';

  const routes = {
    '/': Home,
    '/about': About,
    '/daisytest': DaisyTest,
    '*': NotFound
  };
</script>

<Router {routes} />
