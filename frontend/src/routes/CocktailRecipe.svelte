<script>
    export let params = {};
    let id = params.id;
    import { onMount } from 'svelte';
    import Review from '../components/Review.svelte';
    import { isAuthenticated } from '../store.js';
    import { onDestroy } from 'svelte';

    let cocktail;
    let isAuth;

    const unsubscribe = isAuthenticated.subscribe(v => isAuth = v);
    onDestroy(() => {
        unsubscribe();
    });

    onMount(async () => {
        try{
            const response = await fetch(`/api/cocktail/${id}`);
            cocktail = await response.json();
        }catch(e){
            console.log(e);
        }
    })
</script>

{#if cocktail}
<!-- 칵테일 이미지, 정보 시작 -->
<div class="ml-5 mr-5 md:ml-50 md:mr-50 flex justify-center">
    <!-- carousel 시작 -->
    <div class="carousel rounded-box w-64 md:w-128">
        <div class="carousel-item w-full">
            <img src="images/{cocktail.image_url}" alt="칵테일 이미지" class="w-full">
        </div>
    </div>
    <!-- carousel 끝 -->

    <!-- 칵테일 정보 시작 -->
    <div class="m-5">
        <!-- 칵테일 태그 시작 -->
        <div>
            {#each cocktail.tags as tag}
                <div class="badge badge-md">{tag}</div>
            {/each}
        </div>
        <!-- 칵테일 태그 끝 -->

        <!-- 칵테일 이름 시작 -->
        <div class="text-4xl m-5">{cocktail.name}</div>
        <!-- 칵테일 이름 끝 -->

        <!-- 칵테일 설명 시작 -->
        <div>{cocktail.description}</div>
        <!-- 칵테일 설명 끝 -->

        <!-- 도수 정보 시작 -->
        <div>도수: {cocktail.alcohol}</div>
        <!-- 도수 정보 끝 -->

        <!-- 느낌 정보 시작 -->
        <div>느낌: {cocktail.user_review}</div>
        <!-- 느낌 정보 끝 -->
    </div>
    <!-- 칵테일 정보 끝 -->
</div>
<!-- 칵테일 이미지, 정보 끝 -->

<!-- 칵테일 재료 정보 시작 -->
<div class="m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h1 class="text-3xl">재료</h1>
    <!-- 재료 시작 -->
    {#each cocktail.recipe_ingredients as ingredient}
        <div class="m-5">{ingredient.name}({ingredient.tag}) {ingredient.amount}</div>
    {/each}
    <!-- 재료 끝 -->
</div>
<!-- 칵테일 재료 정보 끝 -->

<!-- 칵테일 레시피 정보 시작 -->
<div class="p-10 pl-20 pr-20 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h1 class="text-3xl">레시피</h1>
    {#each cocktail.recipes as recipe, i}
        <div class="w-full">{i+1}. {recipe}</div>
    {/each}
</div>
<!-- 칵테일 레시피 정보 끝 -->

<!-- 칵테일 평가 시작 -->
<div class="p-10 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h1 class="text-3xl">평가</h1>
    {#each [1, 2, 3] as i}
        <Review />
    {/each}
</div>
<!-- 칵테일 평가 끝 -->

{#if isAuth}
<!-- 평가 등록 인풋 시작 -->
<div class="p-10 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <div class="join w-full">
        <input type="text" placeholder="평가를 입력해주세요." class="input input-sm join-item w-full">
        <button class="btn btn-sm join-item">등록</button>
    </div>
</div>
<!-- 평가 등록 인풋 끝 -->
{/if}
{:else}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{/if}