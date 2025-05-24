<script>
    import SkeletonCocktailCard from '../components/SkeletonCocktailCard.svelte';
    import CocktailCard from '../components/CocktailCard.svelte';
    import { onMount } from 'svelte';
    import { location } from 'svelte-spa-router'; // svelte-spa-router에서 location 가져오기
    import { derived } from 'svelte/store'; // derived store 가져오기
    import { push } from 'svelte-spa-router'; // URL 변경을 위해 push 액션 가져오기

    let search_cocktails = [];
    let ready = false;
    let error;

    ////////
    $: q = new URLSearchParams('?'+window.location.href.split('?')[1]).get('q') || "";
    $: sort = "name-asc";
    async function getSearchCocktails(q, sort){
        const response = await fetch(`/api/search-cocktail?q=${q}&sort=${sort}`);
        search_cocktails = await response.json();
        ready = true;
    }
    $: getSearchCocktails(q, sort);
    ////////
</script>

<!-- 전체 검색된 칵테일 시작 -->
<!-- 모바일 검색된 칵테일 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="block md:hidden m-5">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">검색 결과</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div>
            {#if !ready}
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            {:else}
            {#each search_cocktails as cocktail}
                <CocktailCard {...cocktail}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}<!-- 모바일 검색된 칵테일 끝 -->

<!-- 데스크톱 검색된 칵테일 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="hidden md:block m-20">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">검색 결과</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 정렬 조건 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="rounded-full p-2 shadow-lg flex items-center">
                <div>정렬 기준</div>
                <select class="select" on:change={(e) => sort = e.target.value}>
                    <option value="name-asc" selected>이름순</option>
                    <option value="name-desc">이름역순</option>
                    <option value="alcoholic-asc">알코올 포함순</option>
                    <option value="alcoholic-desc">알코올 미포함순</option>
                </select>
            </div>
        </div>
        <!-- 정렬 조건 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div class="grid grid-cols-4">
            {#if !ready}
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            {:else}
            {#each search_cocktails as cocktail}
                <CocktailCard {...cocktail}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}
<!-- 데스크톱 검색된 칵테일 끝 -->
<!-- 전체 검색된 칵테일 끝 -->