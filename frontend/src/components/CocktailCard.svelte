<script>
    let { name, image_url, description, tags, id } = $props();
</script>

<!-- 카드 시작 -->
<div class="card bg-base-100 m-5 shadow-md">
    <figure class="h-45">
        <a href="#/cocktail/{id}"><img src="images/{image_url}"></a>
    </figure>
    <div class="card-body">
        <div>
            {#each tags as tag}
                <span class="badge">{tag}</span>
            {/each}
        </div>
        <h2 class="card-title uppercase">{name}</h2>
        <p>{description}</p>
    </div>
</div>
<!-- 카드 끝 -->