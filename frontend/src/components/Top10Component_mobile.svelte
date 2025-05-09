<script>
    export let index;
    export let name;
    export let tags;
</script>

<!-- 요소 시작 -->
<li>
    <div>
        <div class="flex m-2">
            <a class="text-xl" href="#/">{index}. {name}</a>
        </div>
        <div class="flex flex-wrap gap-1 m-2">
            {#each tags as tag}
                <span class="badge badge-xs">{tag}</span>
            {/each}
        </div>
    </div>
</li>
<!-- 요소 끝 -->