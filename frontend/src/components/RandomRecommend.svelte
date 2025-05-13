<script>
    import CocktailCard from './CocktailCard.svelte';
    import SkeletonCocktailCard from './SkeletonCocktailCard.svelte';
    import { onMount } from 'svelte';

    let ready = false;
    let error = false;
    let random_recommendation = [];

    onMount(async () => {
        try{
            random_recommendation = await fetch("/api/recommend/random").then(async res => {
                if (res.ok){
                    ready = true;
                    return await res.json();
                }
                error = true;
            });
        }catch(e){
            error = true;
        }
    })
</script>

<!-- 전체 랜덤 추천 시작 -->
<!-- 모바일 랜덤 추천 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="block md:hidden m-5">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">랜덤 추천 레시피</div>
        </div>
        <div class="w-full flex justify-center mb-5">
            <div class="text-xl">이런 칵테일은 어떠세요?</div>
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
            {#each random_recommendation as item}
                <CocktailCard {...item}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}<!-- 모바일 랜덤 추천 끝 -->

<!-- 데스크톱 랜덤 추천 시작 -->
{#if error}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{:else}
<div class="hidden md:block m-20">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">랜덤 추천 레시피</div>
        </div>
        <div class="w-full flex justify-center mb-5">
            <div class="text-xl">이런 칵테일은 어떠세요?</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div class="grid grid-cols-4">
            {#if !ready}
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            {:else}
            {#each random_recommendation as item}
                <CocktailCard {...item}/>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}
<!-- 데스크톱 랜덤 추천 끝 -->
<!-- 전체 랜덤 추천 끝 -->