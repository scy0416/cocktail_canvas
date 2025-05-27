<script>
    import { isAuthenticated } from '../store.js';
    import { push } from 'svelte-spa-router'; // svelte-spa-router의 push 액션 가져오기
    import { onMount } from 'svelte';

    let searchInput;
    function login(){
        window.location.assign('/api/login/kakao');
    }
    async function logout(){
        const response = await fetch('/api/logout', {
            method: 'POST',
        });
        if(response.status === 200){
            isAuthenticated.set(false);
            console.log("로그아웃 성공");
        }
    }
    // 이 push 함수는 svelte-spa-router의 push를 사용하는 것이 좋습니다.
    // 기존의 window.location.assign('/#/my-page') 대신 push('/my-page')
    // svelte-spa-router는 #/my-page와 같은 hash 기반 라우팅을 자동으로 처리합니다.
    function navigateTo(url){
        push(url);
    }
    function search(){
        const q = searchInput.value;
        //push(`/search?q=${q}`); // window.location.assign 대신 push 사용
        window.location.assign(`#/search?q=${q}`);
        window.location.reload();
    }
    onMount(() => {
        const q = new URLSearchParams('?'+window.location.href.split('?')[1]).get('q') || "";
        if (q){
            searchInput.value = q;
        }
    });
</script>

<!-- 전체 헤더 시작 -->
<!-- 모바일 헤더 시작 -->
<div class="block md:hidden p-5 drawer">
    <input id="header" type="checkbox" class="drawer-toggle">
    <div class="drawer-content relative flex justify-center items-center">
        <label for="header" class="btn btn-square absolute left-0"><i class="fi fi-rr-menu-burger"></i></label>
        <a href="#/" class="text-3xl">칵테일 캔버스<i class="fi fi-rs-martini-glass-citrus"></i></a>
    </div>
    <div class="drawer-side z-50">
        <label for="header" aria-label="close sidebar" class="drawer-overlay"></label>
        <aside class="bg-base-100 min-h-screen w-80">
            <div class="p-4 flex">
                {#if $isAuthenticated}
                <button class="flex-1 btn btn-info" on:click={() => navigateTo('/my-page')}>마이페이지</button>
                <button class="flex-1 btn btn-ghost" on:click={logout}>로그아웃</button>
                {:else}
                <button on:click={login} class="btn" style="background-color: #FEE500; color: #000000; border: none;"><img src="https://developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_medium.png" alt="카카오 로그인" style="height: 18px; margin-right: 8px;">카카오 로그인</button>
                {/if}
            </div>
            <ul class="menu w-full p-4">
                {#if $isAuthenticated}
                <li>
                    <a href="#/ai-bartender" class="link link-hover text-xl text-gray-500">AI 바텐더</a>
                </li>
                {/if}
                <li>
                    <a href="#/iba-cocktail" class="link link-hover text-xl text-gray-500">IBA 공식 칵테일</a>
                </li>
                <li>
                    <a href="#/custom-cocktail" class="link link-hover text-xl text-gray-500">창작 칵테일</a>
                </li>
            </ul>
        </aside>
    </div>
</div>
<!-- 모바일 헤더 끝 -->

<!-- 데스크톱 헤더 시작 -->
<div class="hidden md:flex m-5 flex items-center">
    <!-- 로고 시작 -->
    <h1 class="text-4xl"><a href="#/">칵테일 캔버스<i class="fi fi-rs-martini-glass-citrus"></i></a></h1>
    <!-- 로고 끝 -->
    
    <!-- 네비게이션 시작 -->
    <div>
        {#if $isAuthenticated}
        <a href="#/ai-bartender" class="link link-hover text-xl text-gray-500 ml-10">AI 바텐더</a>
        {/if}
        <a href="#/iba-cocktail" class="link link-hover text-xl text-gray-500 ml-10">IBA 공식 칵테일</a>
        <a href="#/custom-cocktail" class="link link-hover text-xl text-gray-500 ml-10">창작 칵테일</a>
    </div>
    <!-- 네비게이션 끝 -->

    <!-- 로그인, 회원가입 버튼 시작 -->
    <div class="ml-auto">
        {#if $isAuthenticated}
        <button class="btn btn-info" on:click={() => navigateTo('/my-page')}>마이페이지</button>
        <button class="btn btn-ghost" on:click={logout}>로그아웃</button>
        {:else}
        <button on:click={login} class="btn" style="background-color: #FEE500; color: #000000; border: none;"><img src="https://developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_medium.png" alt="카카오 로그인" style="height: 18px; margin-right: 8px;">카카오 로그인</button>
        {/if}
    </div>
    <!-- 로그인, 회원가입 버튼 끝 -->
</div>
<!-- 데스크톱 헤더 끝 -->
<!-- 전체 헤더 끝 -->

<!-- 검색 창 시작 -->
<div class="m-5 shadow-sm">
    <div class="join w-full">
        <input type="text" placeholder="검색어를 입력하세요" class="input input-lg join-item w-full" bind:this={searchInput}>
        <button class="btn btn-lg join-item" on:click={search}><i class="fi fi-rr-search"></i>검색</button>
    </div>
</div>
<!-- 검색 창 끝 -->
