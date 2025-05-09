<script>
    let tags = ["태그1", "태그2", "태그3"];
</script>

<!-- 칵테일 이미지, 정보 시작 -->
<div class="ml-5 mr-5 md:ml-50 md:mr-50 flex justify-center">
    <!-- carousel 시작 -->
    <div class="carousel rounded-box w-64 md:w-128">
        <div class="carousel-item w-full">
            <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" alt="칵테일 이미지" class="w-full">
        </div>
        <div class="carousel-item w-full">
            <img src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp" class="w-full">
        </div>
    </div>
    <!-- carousel 끝 -->

    <!-- 칵테일 정보 시작 -->
    <div class="m-5">
        <!-- 칵테일 태그 시작 -->
        <div>
            {#each tags as tag}
                <div class="badge badge-md">{tag}</div>
            {/each}
        </div>
        <!-- 칵테일 태그 끝 -->

        <!-- 칵테일 이름 시작 -->
        <div class="text-4xl m-5">Alexander</div>
        <!-- 칵테일 이름 끝 -->

        <!-- 칵테일 설명 시작 -->
        <div>칵테일 설명</div>
        <!-- 칵테일 설명 끝 -->

        <!-- 도수 정보 시작 -->
        <div>도수: n</div>
        <!-- 도수 정보 끝 -->

        <!-- 느낌 정보 시작 -->
        <div>느낌: 어떠어떠함</div>
        <!-- 느낌 정보 끝 -->
    </div>
    <!-- 칵테일 정보 끝 -->
</div>
<!-- 칵테일 이미지, 정보 끝 -->