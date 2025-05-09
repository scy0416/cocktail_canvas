<script>
    import CocktailCard from './CocktailCard.svelte';

    let daisy_recommendation = [
    { name: "ALEXANDER", image: "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp", description: "칵테일 설명", tags: ["태그1", "태그2", "태그3"] },
    { name: "AMERICANO", image: "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp", description: "칵테일 설명", tags: ["태그1", "태그2", "태그3"] },
    { name: "ANGEL FACE", image: "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp", description: "칵테일 설명", tags: ["태그1", "태그2", "태그3"] },
    { name: "AVIATION", image: "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp", description: "칵테일 설명", tags: ["태그1", "태그2", "태그3"] },
    ];
</script>

<!-- 전체 오늘의 추천 시작 -->
<!-- 모바일 오늘의 추천 시작 -->
<div class="block md:hidden m-5">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">오늘의 추천 레시피</div>
        </div>
        <div class="w-full flex justify-center mb-5">
            <div class="text-xl">이런 칵테일은 어떠세요?</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div>
            {#each daisy_recommendation as item}
                <CocktailCard {...item}/>
            {/each}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
<!-- 모바일 오늘의 추천 끝 -->

<!-- 데스크톱 오늘의 추천 시작 -->
<div class="hidden md:block m-20">
    <div>
        <!-- 제목 시작 -->
        <div class="w-full flex justify-center mb-5">
            <div class="text-4xl">오늘의 추천 레시피</div>
        </div>
        <div class="w-full flex justify-center mb-5">
            <div class="text-xl">이런 칵테일은 어떠세요?</div>
        </div>
        <!-- 제목 끝 -->

        <!-- 스크롤 가능한 레시피들 시작 -->
        <div class="grid grid-cols-4">
            {#each daisy_recommendation as item}
                <CocktailCard {...item}/>
            {/each}
        </div>
        <!-- 스크롤 가능한 레시피들 끝 -->
    </div>
</div>
<!-- 데스크톱 오늘의 추천 끝 -->
<!-- 전체 오늘의 추천 끝 -->