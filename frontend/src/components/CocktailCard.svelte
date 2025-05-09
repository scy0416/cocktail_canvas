<script>
    let { name, image, description, tags } = $props();
</script>

<!-- 카드 시작 -->
<div class="card bg-base-100 m-5 shadow-md">
    <figure>
        <a href="#/"><img src={image}></a>
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