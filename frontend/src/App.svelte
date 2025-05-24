<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';
  import AIBartender from './routes/AIBartender.svelte';
  import CocktailRecipe from './routes/CocktailRecipe.svelte';
  import NotFound from './routes/NotFound.svelte';
  import MyPage from './routes/MyPage.svelte';
  import IBACocktail from './routes/IBACocktail.svelte';
  import CustomCocktail from './routes/CustomCocktail.svelte';
  import CustomCocktailRegister from './routes/CustomCocktailRegister.svelte';
  import Search from './routes/Search.svelte';
  import { link } from 'svelte-spa-router';
  import { wrap } from 'svelte-spa-router/wrap';
  import { isAuthenticated } from './store.js';
  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';

  import Header from './components/Header.svelte';

  // 이곳에 onMount를 통한 최초 인증하기
  onMount(async () => {
    const response = await fetch('/api/auth/verify', {
      method: 'POST',
    });
    if(response.status === 200){
      isAuthenticated.set(true);
      console.log("인증 성공");
    }
    else{
      isAuthenticated.set(false);
      console.log("인증 실패");
    }
    //const data = await response.json();
  });

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
    '/cocktail/:id': CocktailRecipe,
    '/my-page': wrap({ component: MyPage, conditions: [guardHome] }),
    '/iba-cocktail': IBACocktail,
    '/custom-cocktail': CustomCocktail,
    '/custom-cocktail/register': wrap({ component: CustomCocktailRegister, conditions: [guardHome] }),
    '/search': Search,
    '*': NotFound
  };
</script>

<Header />

<Router {routes} />
