<script>
    import Top10Component_desktop from './Top10Component_desktop.svelte';
    import Top10Component_mobile from './Top10Component_mobile.svelte';
    let top10_1 = [
    { name: "ALEXANDER",        tags: ["태그1", "태그2", "태그3"] },
    { name: "AMERICANO",         tags: ["태그1", "태그2", "태그3"] },
    { name: "ANGEL FACE",        tags: ["태그1", "태그2", "태그3"] },
    { name: "AVIATION",          tags: ["태그1", "태그2", "태그3"] },
    { name: "BEE'S KNEES",       tags: ["태그1", "태그2", "태그3"] },
    ];
    let top10_2 = [
    { name: "BELLINI",           tags: ["태그1", "태그2", "태그3"] },
    { name: "BETWEEN THE SHEETS",tags: ["태그1", "태그2", "태그3"] },
    { name: "BLACK RUSSIAN",     tags: ["태그1", "태그2", "태그3"] },
    { name: "BLOODY MARY",       tags: ["태그1", "태그2", "태그3"] },
    { name: "BOULEVARDIER",      tags: ["태그1", "태그2", "태그3"] },
    ];
</script>
<!-- 전체 인기 탑 10 시작 -->
<!-- 모바일 인기 탑 10 시작 -->
<div class="block md:hidden m-5 md:mt-5 md:mb-5 md:ml-100 md:mr-100">
    <!-- 인기 탑 제목 시작 -->
    <div class="w-full flex justify-center mb-5">
        <div class="text-4xl">인기 탑 10 레시피</div>
    </div>
    <!-- 인기 탑 제목 끝 -->

    <div class="w-full flex outline outline-gray-200 outline-2 rounded-box">
        <!-- 인기 탑 왼쪽 시작 -->
        <div class="w-1/2">
            <ul class="bg-base-100">
                {#each top10_1 as item, index}
                    <Top10Component_mobile index={index + 1} {...item}/>
                {/each}
            </ul>
        </div>
        <!-- 인기 탑 왼쪽 끝 -->

        <!-- 인기 탑 오른쪽 시작 -->
        <div class="w-1/2">
            <ul class="bg-base-100">
                {#each top10_2 as item, index}
                    <Top10Component_mobile index={index + 6} {...item}/>
                {/each}
            </ul>
        </div>
        <!-- 인기 탑 오른쪽 끝 -->
    </div>
</div>
<!-- 모바일 인기 탑 10 끝 -->

<!-- 데스크톱 인기 탑 10 시작 -->
<div class="hidden md:block mt-5 ml-50 mr-50">
    <!-- 인기 탑 제목 시작 -->
    <div class="w-full flex justify-center mb-5">
        <div class="text-4xl">인기 TOP 10 레시피</div>
    </div>
    <!-- 인기 탑 제목 끝 -->

    <div class="w-full flex outline outline-gray-200 outline-2 rounded-box">
        <!-- 인기 탑 왼쪽 시작 -->
        <div class="w-1/2">
            <ul class="list bg-base-100">
                {#each top10_1 as item, index}
                    <Top10Component_desktop index={index + 1} {...item}/>
                {/each}
            </ul>
        </div>
        <!-- 인기 탑 왼쪽 끝 -->

        <!-- 인기 탑 오른쪽 시작 -->
        <div class="w-1/2">
            <ul class="list bg-base-100">
                {#each top10_2 as item, index}
                    <Top10Component_desktop index={index + 6} {...item}/>
                {/each}
            </ul>
        </div>
        <!-- 인기 탑 오른쪽 끝 -->
    </div>
</div>
<!-- 데스크톱 인기 탑 10 끝 -->
<!-- 전체 인기 탑 10 끝 -->