<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';
  import AIBartender from './routes/AIBartender.svelte';
  import CocktailRecipe from './routes/CocktailRecipe.svelte';
  import NotFound from './routes/NotFound.svelte';
  import { link } from 'svelte-spa-router';
  import { wrap } from 'svelte-spa-router/wrap';
  import { isAuthenticated } from './store.js';
  import { push } from 'svelte-spa-router';

  import Header from './components/Header.svelte';

  // 이곳에 onMount를 통한 최초 인증하기

  function guardHome(){
    let auth;
    isAuthenticated.subscribe(v => auth = v)();
    if (!auth){
      push('/');
      //console.log("로그인 필요");
      return false;
    }
    return true;
  }

  const routes = {
    '/': Home,
    '/ai-bartender': wrap({ component: AIBartender, conditions: [guardHome] }),
    '/cocktail-recipe': wrap({ component: CocktailRecipe, conditions: [guardHome] }),
    '*': NotFound
  };
</script>

<Header />

<Router {routes} />
