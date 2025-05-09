<script>
    export let index;
    export let name;
    export let tags;
</script>

<!-- 요소 시작 -->
<li class="list-row">
    <div class="text-4xl tabular-nums">{index}</div>
    <div class="text-4xl list-col-grow uppercase"><a href="#/">{name}</a></div>
    <div class="list-col-wrap">
        {#each tags as tag}
            <span class="badge">{tag}</span>
        {/each}
    </div>
</li>
<!-- 요소 끝 -->