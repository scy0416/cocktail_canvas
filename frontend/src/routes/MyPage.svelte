<script>
    import SkeletonCocktailCard from '../components/SkeletonCocktailCard.svelte';
    import CocktailCard from '../components/CocktailCard.svelte';
    import { onMount } from 'svelte';

    let custom_cocktails;
    let error;
    let ready;

    async function getCustomCocktails(){
        const response = await fetch(`/api/user-cocktail`, {
            method: 'POST',
        });
        custom_cocktails = await response.json();
        ready = true;
    }

    async function deleteCocktail(cocktail_id){
        const response = await fetch(`/api/cocktail/delete/${cocktail_id}`, {
            method: 'POST',
        });
        if(response.status === 200){
            custom_cocktails = [];
            ready = false;
            await getCustomCocktails();
        }
    }

    function push(url){
        window.location.assign(url);
    }

    $: getCustomCocktails();
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
            <div class="text-4xl">내가 만든 칵테일</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 칵테일 레시피 등록 버튼 시작 -->
        <button class="btn btn-info w-full" onclick={() => push('/#/custom-cocktail/register')}>칵테일 레시피 등록</button>
        <!-- 칵테일 레시피 등록 버튼 끝 -->

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
                <button class="btn btn-error w-full" onclick={() => deleteCocktail(cocktail.id)}>삭제</button>
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
            <div class="text-4xl">내가 만든 칵테일</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 칵테일 레시피 등록 버튼 시작 -->
        <button class="btn btn-info w-full" onclick={() => push('/#/custom-cocktail/register')}>칵테일 레시피 등록</button>
        <!-- 칵테일 레시피 등록 버튼 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div class="grid grid-cols-4">
            {#if !ready}
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            <SkeletonCocktailCard />
            {:else}
            {#each custom_cocktails as cocktail}
                <div>
                    <CocktailCard {...cocktail}/>
                    <button class="btn btn-error w-full" onclick={() => deleteCocktail(cocktail.id)}>삭제</button>
                </div>
            {/each}
            {/if}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
{/if}
<!-- 데스크톱 사용자 칵테일 끝 -->
<!-- 전체 사용자 칵테일 끝 -->