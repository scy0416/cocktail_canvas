<script>
    export let params = {};
    let id = params.id;
    import { onMount } from 'svelte';
    import Review from '../components/Review.svelte';
    import { isAuthenticated } from '../store.js';
    import { onDestroy } from 'svelte';

    let cocktail;
    let isAuth;
    let myReview;
    let reviews;

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
        if(isAuthenticated){
            try{
                const response = await fetch(`/api/cocktail/${id}/review/my`, {method: 'POST'});
                myReview = await response.json();
                updateRating = myReview.rating;
                updateReview = JSON.parse(myReview.review_json).review;
            }catch(e){
                console.log(e);
            }
        }
        try{
            const response = await fetch(`/api/cocktail/${id}/review`);
            reviews = await response.json();
        }catch(e){
            console.log(e);
        }
    })

    let rating;
    let review;

    async function submitReview(){
        if(!rating || !review)return;
        const response = await fetch(`/api/cocktail/${id}/review`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rating,
                review
            })
        });
        if(response.ok){
            rating = null;
            review = null;
            window.location.reload();
        }
    }

    async function deleteReview(){
        const response = await fetch(`/api/cocktail/${id}/review/delete`, {
            method: 'POST'
        });
        if(response.ok){
            myReview = null;
            window.location.reload()
        }
    }

    let updateRating;
    let updateReview;

    async function reviewUpdate(){
        const response = await fetch(`/api/cocktail/${id}/review/update`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rating: updateRating,
                review: updateReview
            })
        })
        if(response.ok){
            window.location.reload();
        }
    }
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

{#if isAuth && !myReview}
<!-- 평가 등록 인풋 시작 -->
<div class="p-10 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h2 class="text-2xl mb-4">평가 등록</h2>

    <!-- 별점 인풋 시작 -->
    <div class="flex items-center mb-4 rounded-full p-2 shadow-lg">
        <span class="mr-2 whitespace-nowrap">별점: </span>
        <input
            type="range"
            min="0"
            max="10"
            step="1"
            bind:value={rating}
            class="range range-xs mr-2"
        />
        <span class="font-bold whitespace-nowrap">{rating}점</span>
    </div>
    <!-- 별점 인풋 끝 -->

    <div class="join w-full">
        <input type="text" placeholder="평가를 입력해주세요." class="input input-sm join-item w-full" bind:value={review}/>
        <button class="btn btn-sm join-item" on:click={submitReview}>등록</button>
    </div>
</div>
<!-- 평가 등록 인풋 끝 -->
{:else if isAuth && myReview}
<!-- 내 평가 시작 -->
<div class="p-10 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h2 class="text-2xl mb-4">내 평가</h2>
    <div class="flex w-full justify-center gap-2">
        <button class="btn btn-error" on:click={deleteReview}>삭제</button>
        <button class="btn btn-info" on:click={reviewUpdate}>수정</button>
    </div>
    <!-- <Review {...myReview}/> -->
    <div class="flex flex-col w-full">
        <!-- 별점 인풋 시작 -->
        <div class="flex items-center justify-center mb-4 rounded-full p-2 shadow-lg">
            <span class="mr-2 whitespace-nowrap">별점: </span>
            <input
                type="range"
                min="0"
                max="10"
                step="1"
                bind:value={updateRating}
                class="range range-xs mr-2"
            />
            <span class="font-bold whitespace-nowrap">{updateRating}점</span>
        </div>
        <!-- 별점 인풋 끝 -->

        <!-- 평가 인풋 시작 -->
        <div class="w-full">
            <textarea placeholder="평가를 입력해주세요." class="input input-sm join-item w-full" bind:value={updateReview}></textarea>
        </div>
        <!-- 평가 인풋 끝 -->
    </div>
</div>
<!-- 내 평가 끝 -->
{:else}
<div role="alert" class="alert alert-error">평가를 찾을 수 없습니다</div>
{/if}
<!-- 칵테일 평가 시작 -->
<div class="p-10 m-5 md:ml-50 md:mr-50 rounded-box shadow-md flex flex-col items-center">
    <h1 class="text-3xl">평가</h1>
    {#each reviews as review}
        <Review {...review}/>
    {/each}
</div>
<!-- 칵테일 평가 끝 -->
{:else}
<div role="alert" class="alert alert-error">정보를 가져오는 중 문제가 발생했습니다</div>
{/if}