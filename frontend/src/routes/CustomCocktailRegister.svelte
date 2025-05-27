<script>
    // 태그 관리
    function addTag(){
        const input = document.getElementById('tagInput');
        const tagList = document.getElementById('tagList');
        if(input.value.trim()){
            const tag = document.createElement('div');
            tag.className = 'badge badge-lg gap-2';
            tag.textContent = input.value;
            const btn = document.createElement('button');
            btn.className = 'btn btn-ghost btn-xs';
            btn.innerHTML = '<i class="fi fi-rr-cross-small"></i>';
            btn.addEventListener('click', () => tag.remove());
            tag.appendChild(btn)
            tagList.appendChild(tag);
            input.value = '';
        }
    }
    // 재료 관리
    function addIngredient(){
        const input = document.getElementById('ingredientInput');
        const ingredientList = document.getElementById('ingredientList');
        const ingredientAmountInput = document.getElementById('ingredientAmountInput');
        if(input.value.trim()){
            const ingredient = document.createElement('div');
            ingredient.className = 'flex items-center gap-2';
            const badge = document.createElement('div');
            badge.className = 'badge badge-lg flex grow';
            badge.textContent = input.value;
            ingredient.appendChild(badge);
            const amount = document.createElement('div');
            amount.className = 'badge badge-lg flex grow';
            amount.textContent = ingredientAmountInput.value;
            ingredient.appendChild(amount);
            const btn = document.createElement('button');
            btn.className = 'btn btn-ghost btn-sm';
            btn.innerHTML = '<i class="fi fi-rr-trash"></i>';
            btn.addEventListener('click', () => ingredient.remove());
            ingredient.appendChild(btn);
            ingredientList.appendChild(ingredient);
            input.value = '';
            ingredientAmountInput.value = '';
        }
    }
    // 레시피 관리
    function addRecipe(){
        const input = document.getElementById('recipeInput');
        const recipeList = document.getElementById('recipeList');
        if(input.value.trim()){
            const recipe = document.createElement('div');
            recipe.className = 'flex items-center gap-2';
            const flex = document.createElement('div');
            flex.className = 'flex-none';
            const upBtn = document.createElement('button');
            upBtn.className = 'btn btn-ghost btn-sm';
            upBtn.innerHTML = '<i class="fi fi-rr-angle-up"></i>';
            upBtn.addEventListener('click', () => moveStep(recipe, -1));
            const downBtn = document.createElement('button');
            downBtn.className = 'btn btn-ghost btn-sm';
            downBtn.innerHTML = '<i class="fi fi-rr-angle-down"></i>';
            downBtn.addEventListener('click', () => moveStep(recipe, 1));
            flex.appendChild(upBtn);
            flex.appendChild(downBtn);
            recipe.appendChild(flex);
            const badge = document.createElement('div');
            badge.className = 'badge badge-lg flex-grow';
            badge.textContent = input.value;
            recipe.appendChild(badge);
            const btn = document.createElement('button');
            btn.className = 'btn btn-ghost btn-sm';
            btn.innerHTML = '<i class="fi fi-rr-trash"></i>';
            btn.addEventListener('click', () => recipe.remove());
            recipe.appendChild(btn);
            recipeList.appendChild(recipe);
            input.value = '';
        }
    }
    // 레시피 단계 이동
    function moveStep(element, direction){
        const list = element.parentElement;
        const index = Array.from(list.children).indexOf(element);
        const newIndex = index + direction;

        if(newIndex >= 0 && newIndex < list.children.length){
            if(direction === 1){
                list.insertBefore(element, list.children[newIndex + 1]);
            } else {
                list.insertBefore(element, list.children[newIndex]);
            }
        }
    }

    function push(url){
        window.location.assign(url);
    }

    let cocktail_name;
    let cocktail_description;
    let cocktail_ingredients;
    let cocktail_ingredient_amounts;
    let cocktail_recipes;
    let cocktail_tags;
    let cocktail_image;
    let cocktail_alcohol;

    async function submit(){
        const ingredientList = document.getElementById('ingredientList');
        const recipeList = document.getElementById('recipeList');
        const tagList = document.getElementById('tagList');

        cocktail_ingredients = [];
        cocktail_ingredient_amounts = [];
        for(let i = 0; i < ingredientList.children.length; i++){
            cocktail_ingredients.push(ingredientList.children[i].children[0].textContent);
            cocktail_ingredient_amounts.push(ingredientList.children[i].children[1].textContent);
        }

        cocktail_recipes = [];
        for(let i = 0; i < recipeList.children.length; i++){
            cocktail_recipes.push(recipeList.children[i].textContent);
        }

        cocktail_tags = [];
        for(let i = 0; i < tagList.children.length; i++){
            cocktail_tags.push(tagList.children[i].textContent);
        }

        if(!cocktail_name || !cocktail_description || !cocktail_ingredients || !cocktail_ingredient_amounts || !cocktail_recipes || !cocktail_tags || !cocktail_image){
            alert("모든 필수 정보를 입력해주세요.");
            return;
        }

        const formData = new FormData();
        formData.append('name', cocktail_name);
        formData.append('description', cocktail_description);
        formData.append('ingredients', cocktail_ingredients);
        formData.append('ingredient_amounts', cocktail_ingredient_amounts);
        formData.append('recipes', cocktail_recipes);
        formData.append('tags', cocktail_tags);
        formData.append('image', cocktail_image.files[0]);
        formData.append('alcohol', cocktail_alcohol);

        const response = await fetch('/api/custom-cocktail/register', {
            method: 'POST',
            body: formData,
        });
        if(response.status === 200){
            push('#/my-page');
        }
        else{
            alert("칵테일 등록에 실패했습니다.");
        }
    }
</script>

<!-- 칵테일 입력 폼 시작 -->
<div class="m-5">
    <h2 class="text-3xl font-bold mb-5">새 칵테일 레시피 작성</h2>

    <!-- 칵테일 이름 입력 시작 -->
    <div class="form-control 2-full mb-5">
        <label class="label">
            <span class="label-text text-lg">칵테일 이름 <span class="text-error">*</span></span>
        </label>
        <input type="text" placeholder="칵테일 이름을 입력하세요" class="input input-bordered w-full" required bind:value={cocktail_name}>
    </div>
    <!-- 칵테일 이름 입력 끝 -->

    <!-- 칵테일 태그 입력 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">태그 <span class="text-error">*</span></span>
        </label>
        <div class="flex gap-2 flex-wrap mb-2" id="tagList">
            <!-- 이 곳에 태그가 추가된다. -->
        </div>
        <div class="join w-full">
            <input type="text" id="tagInput" placeholder="태그를 입력하세요" class="input input-bordered join-item w-full">
            <button class="btn join-item" onclick={() => addTag()}>추가</button>
        </div>
    </div>
    <!-- 칵테일 태그 입력 끝 -->

    <!-- 칵테일 설명 입력 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">설명 <span class="text-error">*</span></span>
        </label>
        <textarea class="textarea textarea-bordered h-24" placeholder="칵테일에 대한 설명을 입력하세요" required bind:value={cocktail_description}></textarea>
    </div>
    <!-- 칵테일 설명 입력 끝 -->

    <!-- 칵테일 도수 입력 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">도수 <span class="text-error">*</span></span>
        </label>
        <input type="number" placeholder="도수를 입력하세요" class="input input-bordered w-full" required bind:value={cocktail_alcohol}>
    </div>
    <!-- 칵테일 도수 입력 끝 -->

    <!-- 칵테일 재료 입력 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">재료 <span class="text-error">*</span></span>
        </label>
        <div class="flex flex-col gap-2 mb-2" id="ingredientList">
            <!-- 이 곳에 재료가 추가된다 -->
        </div>
        <div class="join w-full">
            <input type="text" id="ingredientInput" placeholder="재료를 입력하세요" class="input input-bordered join-item w-full">
            <input type="text" id="ingredientAmountInput" placeholder="재료의 양을 입력하세요" class="input input-bordered join-item w-full">
            <button class="btn join-item" onclick={() => addIngredient()}>추가</button>
        </div>
    </div>
    <!-- 칵테일 재료 입력 끝 -->

    <!-- 칵테일 레시피 입력 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">레시피 <span class="text-error">*</span></span>
        </label>
        <div class="flex flex-col gap-2 mb-2" id="recipeList">
            <!-- 레시피 단계들이 여기에 추가된다. -->
        </div>
        <div class="join w-full">
            <input type="text" id="recipeInput" placeholder="레시피 단계를 입력하세요" class="input input-bordered join-item w-full">
            <button class="btn join-item" onclick={() => addRecipe()}>추가</button>
        </div>
    </div>
    <!-- 칵테일 레시피 입력 끝 -->

    <!-- 칵테일 이미지 업로드 시작 -->
    <div class="form-control w-full mb-5">
        <label class="label">
            <span class="label-text text-lg">이미지 <span class="text-error">*</span></span>
        </label>
        <input type="file" class="input input-bordered" accept="image/*" bind:this={cocktail_image}>
    </div>
    <!-- 칵테일 이미지 업로드 끝 -->

    <!-- 저장 버튼 시작 -->
    <div class="flex justify-end gap-2">
        <button class="btn btn-ghost" onclick={() => push('/#/my-page')}>취소</button>
        <button class="btn btn-primary" onclick={() => submit()}>저장</button>
    </div>
    <!-- 저장 버튼 끝 -->
</div>
<!-- 칵테일 입력 폼 끝 -->