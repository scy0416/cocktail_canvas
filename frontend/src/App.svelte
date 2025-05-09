<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';
  import AIBartender from './routes/AIBartender.svelte';
  import CocktailRecipe from './routes/CocktailRecipe.svelte';
  import NotFound from './routes/NotFound.svelte';
  import { link } from 'svelte-spa-router';

  import Header from './components/Header.svelte';

  const routes = {
    '/': Home,
    '/ai-bartender': AIBartender,
    '/cocktail-recipe': CocktailRecipe,
    '*': NotFound
  };
</script>

<Header />

<Router {routes} />
