<script>
    import SkeletonCocktailCard from '../components/SkeletonCocktailCard.svelte';
    import CocktailCard from '../components/CocktailCard.svelte';
    import { onMount } from 'svelte';

    let custom_cocktails;
    let error;
    let ready;
    let sort;

    onMount(async () => {
        try{
            sort = new URLSearchParams(window.location.search).get("sort") || "name-asc";
            //const response = await fetch(`/api/iba-cocktail?sort=${sort}`);
            //iba_cocktails = await response.json();
            //ready = true;
        }catch(e){
            //error = true;
        }
    })

    async function getCustomCocktails(){
        if(!sort)return;
        const response = await fetch(`/api/custom-cocktail?sort=${sort}`);
        custom_cocktails = await response.json();
        ready = true;
    }

    $: getCustomCocktails(sort);
</script>

<!-- 전체 사용자 칵테일 시작 -->
<!-- 모바일 사용자 칵테일 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="block md:hidden m-5">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">사용자 칵테일</div>
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
            {#each custom_cocktails as cocktail}
                <CocktailCard {...cocktail}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}<!-- 모바일 사용자 칵테일 끝 -->

<!-- 데스크톱 사용자 칵테일 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="hidden md:block m-20">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">사용자 칵테일</div>
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
            {#each custom_cocktails as cocktail}
                <CocktailCard {...cocktail}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}
<!-- 데스크톱 사용자 칵테일 끝 -->
<!-- 전체 사용자 칵테일 끝 -->